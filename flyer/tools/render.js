// usage: node render2.js <dir> <html> <outPrefix> <scale>
const {chromium} = require('playwright');
const path = require('path');
(async () => {
  const [dir, html, prefix, scaleArg] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({deviceScaleFactor: Number(scaleArg || 1)});
  await p.goto('file://' + path.join(dir, html), {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const pages = await p.$$('.page');
  const names = ['表面', '裏面'];
  for (let i = 0; i < pages.length; i++) {
    await pages[i].screenshot({path: path.join(dir, prefix + '-' + names[i] + '.png')});
  }
  console.log(await p.evaluate(() => [...document.querySelectorAll('.page')].map(pg => {
    const r = pg.getBoundingClientRect();
    return [...pg.children].map(c => Math.round(c.getBoundingClientRect().bottom - r.bottom)).join(',');
  })));
  await p.emulateMedia({media: 'print'});
  await p.pdf({path: path.join(dir, prefix + '.pdf'), preferCSSPageSize: true, printBackground: true});
  await b.close();
})();
