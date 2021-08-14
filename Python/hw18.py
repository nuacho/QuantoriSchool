# Написать скрипт, который будет создавать миниатюры фотографий.
# Объем полученого файла должен передаваться как параметр.

import os
from PIL import Image


def resize_image(resize_in_percent):

    # папка с изображениями
    directory = os.getcwd() + '\\pic\\'

    with os.scandir(path=directory) as it:  # сканируем папку с изображениями
        for entry in it:
            # выводим на экран текущее изображение в обработке
            print("file:\t" + entry.name)
            img_obj = Image.open(directory + entry.name)
            percent = 100 / resize_in_percent
            width_size = int(float(img_obj.size[0])/percent)
            height_size = int(float(img_obj.size[1])/percent)

            img_obj = img_obj.resize(
                (width_size, height_size), Image.ANTIALIAS)  # ресайзим
            img_obj.save(directory + entry.name)


resize_image(50)  # размер в процентах от исходного
