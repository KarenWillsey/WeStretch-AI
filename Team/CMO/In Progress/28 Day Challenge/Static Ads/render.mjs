import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, '../../../../..');
const require = createRequire(path.join(repo, 'Team/CMO/Ready/website-repo/package.json'));
const puppeteer = require('puppeteer-core');
const sharp = require('sharp');
const manifest = JSON.parse(await fs.readFile(path.join(here, 'manifest.json'), 'utf8'));
const stage = path.join(os.tmpdir(), 'westretch-reset-ad-render');
const sourceDir = path.join(here, 'Source');
await fs.mkdir(stage, { recursive: true });
await fs.mkdir(sourceDir, { recursive: true });
const uri = p => pathToFileURL(p).href;
const esc = s => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
const rel = p => path.relative(sourceDir, p).split(path.sep).map(encodeURIComponent).join('/');
const tokens = rel(path.join(repo, 'Team/CMO/In Progress/Brand System/core/tokens.css'));
const logo = rel(path.join(repo, 'Team/CMO/In Progress/App Store Specialist/App Store Image Creation/Knowledge files/02_WeStretch_Logo_Do_Not_Modify.png'));
const font = rel(path.join(here, 'Fonts/WorkSans-Variable.ttf'));
const inter = rel(path.join(here, 'Fonts/Inter-SemiBold.ttf'));

function html(c, height) {
  const vertical = height === 1920;
  const square = height === 1080;
  return `<!doctype html><html><head><meta charset="utf-8"><title>${esc(c.name)}</title>
<link rel="stylesheet" href="${tokens}"><style>
@font-face{font-family:'Work Sans';src:url('${font}');font-weight:100 900}
@font-face{font-family:Inter;src:url('${inter}');font-weight:600}
*{box-sizing:border-box}html,body{margin:0;width:1080px;height:${height}px;overflow:hidden}
body{background:var(--ws-midnight-grey);color:var(--ws-white);font-family:Inter;font-weight:600}
.ad{position:relative;width:1080px;height:${height}px;overflow:hidden}
.logo{position:absolute;left:90px;top:${vertical ? 280 : 90}px;width:300px;height:auto}
.label{position:absolute;left:90px;top:${vertical ? 373 : 185}px;font-size:27px;line-height:34px;letter-spacing:1.6px;color:var(--ws-light-grey)}
.copy{position:absolute;left:90px;top:${vertical ? 440 : square ? 255 : 275}px;width:${vertical ? 900 : 510}px;z-index:2}
h1{margin:0;font-family:'Work Sans';font-weight:700;font-size:${vertical ? (c.id==='r01' ? 118 : c.id==='r03' ? 102 : 91) : c.id==='r01' ? (square ? 82 : 94) : c.id==='r03' ? (square ? 74 : 83) : (square ? 65 : 78)}px;line-height:1.04;letter-spacing:-2.5px}
.support{margin:32px 0 0;font-size:${vertical ? 43 : 40}px;line-height:1.25;letter-spacing:-.8px;max-width:${vertical ? 850 : 495}px;color:var(--ws-light-grey)}
.photo{position:absolute;left:${vertical ? 0 : 625}px;top:${vertical ? 1150 : square ? 210 : 245}px;width:${vertical ? 1080 : 455}px;height:${vertical ? 770 : square ? 640 : 850}px;overflow:hidden}
.photo img{width:100%;height:100%;object-fit:cover;object-position:${vertical ? c.verticalPosition : 'center center'}}
${!vertical && c.id === 'r02' ? '.photo img{object-position:65% center}' : ''}
.cta{position:absolute;left:90px;top:${vertical ? 1030 : square ? 888 : 1150}px;width:900px;height:104px;border-radius:52px;display:flex;align-items:center;justify-content:center;background:var(--ws-cta-fill);color:white;font-size:40px;line-height:1;letter-spacing:.2px;z-index:3}
</style></head><body><main class="ad"><img class="logo essential" src="${logo}" alt="WeStretch"><div class="label essential">${manifest.campaign}</div><div class="copy"><h1 class="essential">${esc(c.headline)}</h1><p class="support essential">${esc(c.support)}</p></div><div class="photo"><img src="${rel(path.join(repo, c.photo))}" alt="${esc(c.name)}"></div><div class="cta essential">${manifest.cta}</div></main></body></html>`;
}

const browser = await puppeteer.launch({
  executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
  headless: true,
  args: ['--allow-file-access-from-files', '--disable-gpu', '--hide-scrollbars'],
});
const checks = [];
const thumbs = [];
try {
  const page = await browser.newPage();
  for (const [row, c] of manifest.concepts.entries()) {
    for (const [col, height] of [1080, 1350, 1920].entries()) {
      const name = `reset-${c.id}-v01-1080x${height}`;
      const source = path.join(sourceDir, `${name}.html`);
      await fs.writeFile(source, html(c, height));
      await page.setViewport({width:1080,height,deviceScaleFactor:1});
      await page.goto(uri(source));
      await page.evaluate(async () => {await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));});
      const check = await page.evaluate(() => ({
        fonts: {display:document.fonts.check('700 70px "Work Sans"'),ui:document.fonts.check('600 40px Inter')},
        text:[...document.querySelectorAll('.essential')].map(e=>{const r=e.getBoundingClientRect();return {text:e.textContent||e.alt,x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom};}),
      }));
      const copyBottom = Math.max(...check.text.filter(t=>!t.text.includes('JOIN THE')).map(t=>t.bottom));
      const ctaTop = check.text.at(-1).y;
      if(copyBottom + 20 > ctaTop) throw new Error(`${name}: text crowds CTA (${copyBottom} > ${ctaTop})`);
      if(height===1920 && check.text.some(t=>t.x<90 || t.right>990 || t.y<280 || t.bottom>1200)) throw new Error(`${name}: vertical safety boundary violated`);
      if(height===1080 && check.text.some(t=>t.x<87 || t.right>993 || t.y<87 || t.bottom>993)) throw new Error(`${name}: square inset violated`);
      await page.screenshot({path:path.join(stage,`${name}.png`)});
      const thumb = await sharp(path.join(stage,`${name}.png`)).resize({width:360}).png().toBuffer();
      thumbs.push({input:thumb,left:col*390+20,top:row*700+55});
      checks.push({name,width:1080,height,...check});
    }
  }
} finally {await browser.close();}
const labels = manifest.concepts.flatMap((c,row)=>['1080 x 1080','1080 x 1350','1080 x 1920'].map((size,col)=>`<text x="${col*390+20}" y="${row*700+35}" font-family="Arial" font-size="19" fill="#1f1f1f">${c.id.toUpperCase()} / ${size}</text>`)).join('');
thumbs.push({input:Buffer.from(`<svg width="1170" height="2100" xmlns="http://www.w3.org/2000/svg">${labels}</svg>`),left:0,top:0});
await sharp({create:{width:1170,height:2100,channels:3,background:'#e4e4e4'}}).composite(thumbs).png().toFile(path.join(stage,'contact-sheet.png'));
await fs.writeFile(path.join(stage,'layout-checks.json'),JSON.stringify(checks,null,2));
console.log(JSON.stringify({stage,count:checks.length,checks:'Fonts, copy spacing, square inset and vertical text safe box passed.'}));
