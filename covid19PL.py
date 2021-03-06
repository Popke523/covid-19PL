import json
import urllib.request

req = urllib.request.Request(
    url='https://api.nowywirus.pl/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'}
)
data = urllib.request.urlopen(req).read()
output = json.loads(data)[0]

ilosckoronawirusow = output['cases']
iloscnowa = output['new_cases']
deaths = output['deaths']
deathstoday = output['new_deaths']

print(f'Ilość aktywnych koronawirusów wynosi {ilosckoronawirusow}, przybyło nowych {iloscnowa} koronawirusów w Polsce.')
print(f'Nie żyje już {deaths} osób, dzisiaj zmarło {deathstoday}.')
