const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://scys.com/?filter=essence');
  await page.waitForLoadState('networkidle');
  
  const content = await page.content();
  console.log('Page content length:', content.length);
  console.log('Title:', await page.title());
  
  // Try to get some text
  const bodyText = await page.evaluate(() => document.body.innerText);
  console.log('Body text preview:', bodyText.substring(0, 500));
  
  await browser.close();
})();
