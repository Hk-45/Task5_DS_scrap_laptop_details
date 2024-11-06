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
            Title = Details.css('div.KzDlHZ')
            specification = Details.css('ul.G4BRas')
            Rating = Details.css('div.XQDdHH')
            Price = Details.css('div.hl05eU')
            Img = Details.css('img.DByuf4')

            titleText = Title[0].text()
            specText = specification[0].text()
            ratingText = Rating[0].text()
            priceText = Price[0].text()
            imgUrl = Img[0].attributes.get('src')

            Details = {
                'Title': titleText,
                'specification':specText,
                'Rating':ratingText,
                'Price':priceText,
                'ImgUrl':imgUrl
            }
            
            laptopDetails.append(Details)

            print(f'title : {titleText}')
            print(f'spec : {specText}')
            print(f'rating : {ratingText}')
            print(f'price : {priceText}')
            print(f'imgUrl : {imgUrl}')


laptopData = pd.DataFrame(laptopDetails)
laptopData.to_csv('laptopData.csv')


