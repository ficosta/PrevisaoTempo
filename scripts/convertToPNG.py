from PIL import Image
from os import listdir
from os.path import splitext

target_directory = '..\\images\\2019_01\\'
target = '.png'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    if extension not in [target]:
        print("Convertendo: " + filename)
        im = Image.open(target_directory + filename + extension)
        im.save(target_directory + filename + target)
