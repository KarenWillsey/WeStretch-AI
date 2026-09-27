import { readdir, readFile, stat, lstat, readlink, symlink, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

/**
 * Makes every skill in this repo invokable as a slash command, and proves it.
 *
 * Claude Code only auto-discovers skills at `.claude/skills/<name>/SKILL.md`.
 * The real files live in two other places on purpose:
 *
 *   .agents/skills/<name>/     vendored third-party packages (cross-agent standard path)
 *   Team/<ROLE>/**            skills owned by one officer, kept beside that officer's work
 *
 * So `.claude/skills/<name>` is a Windows directory junction pointing at the
 * real folder. Junctions are local filesystem state, not git objects, which
 * means a fresh clone has none of them and none of these skills work until
 * this script is run:
 *
 *   node scripts/sync-skill-links.mjs          create anything missing, report
 *   node scripts/sync-skill-links.mjs --check  report only, exit 1 if wrong
 *
 * It is idempotent. Run it after adding a skill anywhere, after installing a
 * skill package, and after cloning.
 *
 * The link name is the skill's own `name:` from its SKILL.md frontmatter,
 * never its folder name, because that is the name Claude Code matches on. Two
 * skills sharing a name is therefore a hard error, not a warning: the second
 * one silently shadows the first.
 */

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const claudeDir = path.join(rootDir, ".claude", "skills");
const teamDir = path.join(rootDir, "Team");
const gitignorePath = path.join(rootDir, ".gitignore");

const checkOnly = process.argv.includes("--check");

/**
 * Submodules carry their own harness config and their own `.claude/skills`.
 * Hoisting their skills into this repo's namespace would both duplicate them
 * and break the moment the submodule moves.
 */
const SKIP = new Set(["node_modules", ".git", "dist", "website-repo", "Westretch-UX"]);

const frontmatterName = async (skillFile) => {
  const text = await readFile(skillFile, "utf8");
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return null;
  const name = match[1].match(/^name:\s*(.+?)\s*$/m);
  return name ? name[1] : null;
};

/** Every SKILL.md under a directory, at any depth. */
async function findSkills(dir) {
  const found = [];
  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return found;
  }
  for (const entry of entries) {
    if (entry.isDirectory()) {
      if (SKIP.has(entry.name)) continue;
      found.push(...(await findSkills(path.join(dir, entry.name))));
    } else if (entry.name === "SKILL.md") {
      found.push(path.join(dir, entry.name));
    }
  }
  return found;
}

const problems = [];
const wanted = new Map(); // link name -> { target, source, file }

for (const [label, dir] of [
  ["vendored", path.join(rootDir, ".agents", "skills")],
  ["team", teamDir],
]) {
  for (const file of await findSkills(dir)) {
    const folder = path.dirname(file);
    const name = await frontmatterName(file);
    if (!name) {
      problems.push(`No \`name:\` in frontmatter: ${path.relative(rootDir, file)}`);
      continue;
    }
    const existing = wanted.get(name);
    if (existing) {
      problems.push(
        `Two skills are both named "${name}", so one silently shadows the other:\n` +
          `    ${path.relative(rootDir, existing.file)}\n` +
          `    ${path.relative(rootDir, file)}`,
      );
      continue;
    }
    wanted.set(name, { target: folder, source: label, file });
  }
}

const existingEntries = await readdir(claudeDir, { withFileTypes: true }).catch(() => []);
const existing = new Map();
for (const entry of existingEntries) {
  const full = path.join(claudeDir, entry.name);
  const info = await lstat(full);
  const link = info.isSymbolicLink() ? await readlink(full).catch(() => null) : null;
  existing.set(entry.name, { full, link });
}

const created = [];
const alreadyRight = [];
const native = [];

for (const [name, { target }] of wanted) {
  const found = existing.get(name);
  if (found) {
    if (found.link && path.resolve(found.link) === path.resolve(target)) alreadyRight.push(name);
    else if (found.link) problems.push(`.claude/skills/${name} points at ${found.link}, not ${path.relative(rootDir, target)}`);
    else problems.push(`.claude/skills/${name} is a real folder, but a skill of that name also lives at ${path.relative(rootDir, target)}`);
    continue;
  }
  if (checkOnly) {
    problems.push(`Missing junction: .claude/skills/${name} -> ${path.relative(rootDir, target)}`);
    continue;
  }
  await symlink(target, path.join(claudeDir, name), "junction");
  created.push(name);
}

// A .claude/skills entry with no skill behind it is a skill this repo owns
// outright. Those are fine and are left alone; they are only listed so the
// count adds up and nothing looks unaccounted for.
for (const [name, { link }] of existing) {
  if (!wanted.has(name) && !link) native.push(name);
  else if (!wanted.has(name) && link) problems.push(`.claude/skills/${name} is a junction to ${link}, which is no longer a skill. Delete it.`);
}

// The junctions must never be committed; only the real folders behind them are.
if (!checkOnly) {
  const gitignore = await readFile(gitignorePath, "utf8");
  const marker = "# Third-party skill junctions";
  const head = gitignore.slice(0, gitignore.indexOf(marker));
  const rest = gitignore.slice(gitignore.indexOf(marker));
  const afterBlock = rest.split(/\r?\n/).filter((line) => !line.startsWith("/.claude/skills/"));
  const headerEnd = afterBlock.findIndex((line, i) => i > 0 && line.trim() === "");
  const header = afterBlock.slice(0, headerEnd === -1 ? 1 : headerEnd);
  const tail = afterBlock.slice(headerEnd === -1 ? 1 : headerEnd);
  const lines = [...wanted.keys()].sort().map((name) => `/.claude/skills/${name}/`);
  await writeFile(gitignorePath, head + [...header, ...lines, ...tail].join("\n"), "utf8");
}

const rel = (p) => path.relative(rootDir, p).replace(/\\/g, "/");
const bySource = (label) => [...wanted.values()].filter((entry) => entry.source === label).length;

console.log(`Skills found: ${wanted.size} (${bySource("vendored")} vendored, ${bySource("team")} under Team/)`);
console.log(`Junctions already correct: ${alreadyRight.length}`);
console.log(`Junctions created now: ${created.length}${created.length ? " -> " + created.join(", ") : ""}`);
console.log(`Skills this repo owns directly in .claude/skills: ${native.length}`);
console.log(`Total invokable: ${wanted.size + native.length}`);

if (problems.length) {
  console.log(`\n${problems.length} problem${problems.length === 1 ? "" : "s"}:`);
  problems.forEach((p) => console.log(`  - ${p}`));
  process.exit(1);
}
console.log("\nEvery skill in this repo is reachable from .claude/skills.");
