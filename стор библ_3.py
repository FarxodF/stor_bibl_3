import requests

url = 'https://ya.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fw.forfun.com%2Ffetch%2F49%2F49437e7fd81b0a33576397b3c48fe949.jpeg&lr=119134&pos=6&rpt=simage&text=картинки'

response = requests.get(url)

if response.status_code == 200:

    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    print("Изображение успешно загружено и сохранено как image.jpg")
else:
    print("Ошибка при загрузке изображения")