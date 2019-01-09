import requests
import argparse
import sys
from datetime import datetime
import os.path
from bs4 import BeautifulSoup

cicloList = [0,6,12,18]

def listaImagens(url):
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    images = []
    for img in soup.findAll('a'):
        if "tif" in img.get('href'):
            images.append(img.get('href'))
    return images

def download(data=None):
    if data == None:
        ano_mes = datetime.now().strftime('%Y_%m')

    urlCPTEC="http://ftp.cptec.inpe.br/goes/goes16/goes16_web/rgb_nat_true/{}/{:02d}/".format(datetime.now().year,datetime.now().month)
    images = listaImagens(urlCPTEC)
    if not os.path.exists("..\\images\\{}".format(ano_mes)):
            os.makedirs("..\\images\\{}".format(ano_mes))
    for i in images:
        print(i)
        fileName="..\\images\\{}\\{}".format(ano_mes, i)
        if not os.path.isfile(fileName):
            print("Downloading: {}".format(fileName))
            r = requests.get(urlCPTEC + i, allow_redirects=True)
            open(fileName, 'wb').write(r.content)

if __name__ == "__main__":
    download()
