import requests
import argparse
import sys
from datetime import datetime
import os.path

cicloList = [0,6,12,18]

def download(data=None, ciclo=0, quantidadeHoras=24, step=1):
    if data == None:
        data = datetime.now().strftime('%Y%m%d')
    if ciclo not in cicloList:
        raise ValueError('Ciclo deve ser 0, 6, 12 ou 18')
    for i in range(0, quantidadeHoras, step):
        urlNoaa="http://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.{}{:02}/gfs.t{:02}z.pgrb2.0p25.f{:03}".format(data, ciclo, ciclo, i)
        fileName="..\\grib\\{}_{:02}\\{}".format(data, ciclo, urlNoaa.split('/')[-1])
        if not os.path.isfile(fileName):
            print("Downloading: {}".format(fileName))
            r = requests.get(urlNoaa, allow_redirects=True)
            open(fileName, 'wb').write(r.content)

if __name__ == "__main__":
    download()
