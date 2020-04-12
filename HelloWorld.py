# print("Hello World !")
import requests
from bs4 import BeautifulSoup

url = 'http://www.yyetss.com/'
strhtml = requests.get(url)
# print (strhtml.text)

soup = BeautifulSoup(strhtml.text, 'lxml')
filmName = soup.select('body > div.container > div > div > a > p:nth-child(1)')
print (filmName)

filmImg = soup.select('body > div.container > div > div > a.imgbox > img')
print (filmImg)

filmDate = soup.select('body > div.container > div > div > a > p:nth-child(2)')
print (filmDate)

print(len(filmName),len(filmImg),len(filmDate))

for index in range(len(filmImg)):
    result = {
        'film_name': filmName[index].text,
        'film_img': filmImg[index]['src'],
        'film_date': filmDate[index].text
    }
    print (result)
