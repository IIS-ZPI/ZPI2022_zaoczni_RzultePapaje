import requests


def data_import():
    url = 'http://api.nbp.pl/api/exchangerates/tables/A/2002-01-02/2002-03-02'
    resp = requests.get(url=url)
    for x in resp.json():
        print(x)


if __name__ == '__main__':
    data_import()
