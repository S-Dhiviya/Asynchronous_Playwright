import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_google_title_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.google.com")
        await page.wait_for_load_state("load")
        title = await page.title()
        assert "Google" in title
        await browser.close()



# pip install pytest pytest-asyncio playwright
# playwright install