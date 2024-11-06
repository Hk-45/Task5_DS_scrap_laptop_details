from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import pandas as pd

if __name__ == '__main__':
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

        page.wait_for_load_state('domcontentloaded')
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(200)
        page.screenshot(full_page=True, path='flip_Laptops.png')

        lapHtml = page.inner_html('body')
        lapPars = HTMLParser(lapHtml)

        mainContainer = lapPars.css('div._75nlfW')
        
        laptopDetails = []

        for Details in mainContainer:
            Title = Details.css('div.KzDlHZ')[0].text()
            specification = Details.css('ul.G4BRas')[0].text()
            Rating = Details.css('div.XQDdHH')[0].text()
            Price = Details.css('div.hl05eU')[0].text()
            Img = Details.css('img.DByuf4')[0].attributes.get('src')

            # titleText = Title[0].text()
            # specText = specification[0].text()
            # ratingText = Rating[0].text()
            # priceText = Price[0].text()
            # imgUrl = Img[0].attributes.get('src')

            Details = {
                'Title': Title,
                'specification':specification,
                'Rating':Rating,
                'Price':Price,
                'ImgUrl':Img
            }
            
            laptopDetails.append(Details)

            print(f'title : {Title}')
            print(f'spec : {specification}')
            print(f'rating : {Rating}')
            print(f'price : {Price}')
            print(f'imgUrl : {Img}')


laptopData = pd.DataFrame(laptopDetails)
laptopData.to_csv('laptopData.csv')


