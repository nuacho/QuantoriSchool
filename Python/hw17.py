from geopy.geocoders import Nominatim
from GPSPhoto import gpsphoto

data = gpsphoto.getGPSData('image17.jpg')
x = data['Latitude']
y = data['Longitude']

# print(data['Latitude'], data['Longitude'])
print(f"{x}, {y}")

with open('maps17.txt', 'w') as f_out:  # пишем координаты в файл
    f_out.write(f"{x}, {y}")
    f_out.close()

coords = []
with open('maps17.txt', 'r') as f_inp:  # берем список координат из файла
    lines = f_inp.readlines()
    # создаем список с кортежами из координат
    for i in range(len(lines)):
        x, y = map(float, lines[i].split(', '))

        coords.append(((x, y)))
    f_inp.close()

    for x, y in coords:  # проходим список по элементам кортежа
        geolocator = Nominatim(user_agent="Quantori")
        # исходные координаты из списка для каждого кортежа
        print('Input data: ', x, y)
        print('Output data:', )
        # используя метод reverse модуля geopy, преобразуем координаты в адрес
        print('Location: ', geolocator.reverse((x, y)))
        print(
            f'Google Maps URL: https://www.google.com/maps/search/?api=1&query={x},{y}')  # создаем ссылку на google maps
