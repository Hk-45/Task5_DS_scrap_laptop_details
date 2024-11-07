from Utilis.getLaptop import getCont
from Utilis.getImage import getImg
import pandas as pd
import os

flipUrl = 'https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

img_folder = 'laptopImage'

if not os.path.exists(img_folder):
    os.makedirs(img_folder)

if __name__ == '__main__':
    flipParser = getCont(siteUrl=flipUrl, waitNetwork= True, waitDoc=True, showBrowser=False)

    mainContainer = flipParser.css('div._75nlfW')

    laptops = []
    for details in mainContainer:
        title =  details.css_first('div.KzDlHZ').text()
        info = details.css_first('ul.G4BRas').text()
        rating =  details.css_first('div.XQDdHH').text()
        price =  details.css_first('div.Nx9bqj._4b5DiR').text()
        originalPrice = details.css_first('div.yRaY8j.ZYYwLA').text()
        discount = details.css_first('div.UkUFwK').text()
        imgUrl =  details.css_first('img.DByuf4').attributes.get('src')
        titleName = title.split('-')[0].split(' ')

        imgPath = os.path.join(img_folder, f'{titleName}.jpg')
        # img_path = os.path.join(img_folder, f"{titleName}.jpg")
        # getImg(img_url=imgUrl, img_name=img_path) 

        getImg(img_url=imgUrl, img_name = imgPath) 

        detailsDict = {
            'title': title,
            'info': info,
            'rating':rating,
            'price': price,
            'originalPrice': originalPrice,
            'discount': discount,
            'imgUrl': imgUrl
        }

        laptops.append(detailsDict)
        
        print('title :',title)
        print('info :',info)
        print('rating :',rating)
        print('price :',price)
        print('OriginalPrice :',originalPrice)
        print('Discount:',discount)
        print('img :',imgUrl)

    laptopData = pd.DataFrame(laptops)
    laptopData.to_csv('laptopData.csv')