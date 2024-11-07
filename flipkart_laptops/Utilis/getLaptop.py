from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def getCont(siteUrl, waitDoc = False, waitNetwork = False, showBrowser = False, screenShotName = '' ):
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=showBrowser)
        page = browser.new_page()
        page.goto(siteUrl)

        if waitNetwork:
           page.wait_for_load_state('networkidle') 

        if waitDoc:
            page.wait_for_load_state('domcontentloaded')

        page.wait_for_timeout(1000)

        if screenShotName != '':
            page.screenshot(full_page=True, path=f'{screenShotName}.png')

        getHtml = page.inner_html('body')

        return HTMLParser(getHtml)