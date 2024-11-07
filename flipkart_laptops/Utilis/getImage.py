import requests as rq

def getImg(img_url = '', img_name = ''):

    imgResp = rq.get(img_url)

    if imgResp.status_code == 200:
        with open(f'{img_name}.png', 'wb') as file:
            file.write(imgResp.content)
        print('img downloaded successfully')
    else: 
        print('something is wrong')