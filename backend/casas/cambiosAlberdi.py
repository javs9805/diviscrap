from urllib.request import urlopen
from casas.moneda import Moneda
import json
from datetime import datetime

url = "https://www.cambiosalberdi.com/"
casaCambio = "cambios Alberdi"

def openUrlAndGetDecodedHtml(url):
    json = "ws/getTablero.json"
    page = urlopen(url+json)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")


def getCambiosAlberdi():
    html = openUrlAndGetDecodedHtml(url)
    resultado = json.loads(html)
    return resultado


if __name__ == "__main__":
    print(getCambiosAlberdi()['villamorra'][0]['id'])