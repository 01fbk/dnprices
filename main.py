import bs4
import requests
import json

URL = "https://api.exchangeratesapi.io/latest?base=USD&symbols=EUR,GBP"

r = requests.get(url=URL)
data = r.json()

euro = data['rates']['EUR']
pound = data['rates']['GBP']
api_time = data['date']


def dynadot():
    dyna_page = requests.get('https://www.dynadot.com/domain/tlds.html?price_level=0')
    html = bs4.BeautifulSoup(dyna_page.text, 'html.parser')

    tab = html.find(name='div', id='St_Data_Info')
    for row in tab.find_all('p', class_='tld-content'):
        tld = row.find('a').text
        dynadot_usd = float(row.find('span', class_='span-register-price').text.strip()[1:])
        dynadot_euro = float(dynadot_usd) * euro
        dynadot_pounds = float(dynadot_usd) * pound

        dynadot_json = {
            "tld": tld,
            "prices": [
                {"USD": dynadot_usd},
                {"EUR": ("%.2f" % dynadot_euro)},
                {"GBP": ("%.2f" % dynadot_pounds)}
            ]
        }

        y = json.dumps(dynadot_json)
        print(y)


def main():
    dynadot()


if __name__ == '__main__':
    main()
