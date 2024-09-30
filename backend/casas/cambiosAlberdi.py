from urllib.request import urlopen
from casas.moneda import Moneda
import json
from datetime import datetime
import os
url = "https://www.cambiosalberdi.com/"
casaCambio = "Cambios Alberdi"

def openUrlAndGetDecodedHtml(url):
    json = "ws/getTablero.json"
    page = urlopen(url+json)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")

def getCurrenciesAndLog(monedas):
    path = os.getcwd()
    f = open(f"{path}\casas\sources\cambiosAlberdi.txt","a")
    now = datetime.now()
    current_time = now.strftime("%d%m%Y-%H%M%S")
    print("Current Time =", current_time)
    jsonMonedas = json.dumps({"time":current_time,"name":casaCambio,"currency":[moneda.to_dict() for moneda in monedas]}, indent = 2)
    f.write(",\n")
    f.write(jsonMonedas)
    return jsonMonedas

def setCleanCurrencies(cuerpo_tabla):
    now = datetime.now()
    current_time = now.strftime("%d%m%Y-%H%M%S")
    match_results = json.loads(cuerpo_tabla)
    match_results = match_results['villamorra']
    monedas = []
    resultados = []
    for moneda in match_results:
        if '->' not in moneda['bcp'] and moneda['bcp'] != '':
            compra = float(moneda['compra'].replace('.','#').replace(',','.').replace('#','.'))
            venta = float(moneda['venta'].replace('.','#').replace(',','.').replace('#','.'))
            monedas.append(Moneda(moneda['id'],compra, venta, current_time))
    return monedas


def getCambiosAlberdi():
    monedasPorSucursal = openUrlAndGetDecodedHtml(url)

    monedas = setCleanCurrencies(monedasPorSucursal)    
    json = getCurrenciesAndLog(monedas)

    return json



if __name__ == "__main__":
    monedas = getCambiosAlberdi()
    print(json)