const { chromium } = require('playwright');

(async () => {
  console.log('启动浏览器...');
  const browser = await chromium.launch({ 
    headless: true,
    executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH 
  });
  const page = await browser.newPage();
  
  // 设置 cookies 模拟登录状态
  // 如果用户提供了 cookies，可以在这里设置
  // await page.context().addCookies([...]);
  
  console.log('访问 scys.com 精华帖页面...');
  await page.goto('https://scys.com/?filter=essence');
  await page.waitForLoadState('networkidle');
  
  console.log('页面标题:', await page.title());
  
  // 获取页面内容
  const content = await page.content();
  console.log('页面内容长度:', content.length);
  
  // 获取 body 文本
  const bodyText = await page.evaluate(() => document.body.innerText);
  console.log('Body 文本预览 (前1000字符):');
  console.log(bodyText.substring(0, 1000));
  
  // 检查是否需要登录
  if (bodyText.includes('登录') || bodyText.includes('登录')) {
    console.log('\n⚠️ 检测到登录页面，需要登录凭证才能访问精华帖内容');
    console.log('建议：');
    console.log('1. 在浏览器中手动登录 scys.com');
    console.log('2. 使用 agent-browser state save 保存登录状态');
    console.log('3. 然后使用 agent-browser state load 加载登录状态');
  }
  
  await browser.close();
  console.log('\n浏览器已关闭');
})();
