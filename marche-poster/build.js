// node build.js  ->  A2 PDF（矢印 右・左・上）とプレビューPNGを書き出す
const { chromium } = require('playwright');
const path = require('path');
const names = { right: '右', left: '左', up: '上' };
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1587, height: 2245 } });
  for (const d of Object.keys(names)) {
    await p.goto('file://' + path.resolve(__dirname, 'poster.html') + '?dir=' + d);
    await p.waitForSelector('body[data-ready="1"]');
    await p.waitForTimeout(300);
    await p.pdf({ path: `マルシェ動線ポスター_A2_矢印${names[d]}.pdf`, width: '420mm', height: '594mm', printBackground: true });
    await p.screenshot({ path: `preview_${d}.png` });
  }
  await b.close();
})();
