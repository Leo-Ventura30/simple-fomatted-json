from urllib.request import urlopen
import json

response = urlopen(
    "http://vimeo.com/api/v2/video/57733101.json").read().decode("utf8")


data = json.loads(response)[0]

print('Título: ', data['title'])
print('URL: ', data['url'])
print('Duração: ', data['duration'])
print('Número de Visualizações: ', data['stats_number_of_plays'])
