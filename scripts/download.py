import requests
import argparse
import sys
from datetime import datetime

cicloList = [0,6,12,18]

def download(data=None, ciclo=0, quantidadeHoras=120, step=3):
    if data == None:
        data = datetime.now().strftime('%Y%m%d')
    if ciclo not in cicloList:
        raise ValueError('Ciclo deve ser 0, 6, 12 ou 18')
    for i in range(0, quantidadeHoras, step):

        urlNoaa="http://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.{}{:02}/gfs.t{:02}z.pgrb2.0p25.f{:03}".format(data, ciclo, ciclo, i)
        fileName=urlNoaa.split('/')[-1]
        print("Downloading: {}".format(fileName))
        r = requests.get(urlNoaa, allow_redirects=True)
        open("../grib/data_{:02}/{}".format(ciclo,fileName), 'wb').write(r.content)

if __name__ == "__main__":
    download()
