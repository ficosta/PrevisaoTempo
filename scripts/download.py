import requests
from datetime import datetime

cicloList = [0,6,12,18]

def download(data=None, ciclo=0, quantidadeHoras=1, step=1):
    if data == None:
        data = datetime.now().strftime('%Y%m%d')
    if ciclo not in cicloList:
        raise ValueError('Ciclo deve ser 0, 6, 12 ou 18')
    for i in range(0, quantidadeHoras, step):
        print(i)
    urlNoaa="http://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.2019010718/gfs.t18z.pgrb2.0p25.f000"

download()
