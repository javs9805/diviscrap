from urllib.request import urlopen
from casas.moneda import Moneda
import re
import json
from datetime import datetime
import os

url = "https://www.cambioschaco.com.py/"
casaCambio = "Cambios Chaco"
def openUrlAndGetDecodedHtml(url):
    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")

def findCurrenciesOnDecodedHtml(html):
    index_inicio = html.find('<tbody id="main-exchange-content">')
    index_final = html.find("</tbody>")
    return html[index_inicio:index_final]


def setCleanCurrencies(cuerpo_tabla):
    now = datetime.now()
    current_time = now.strftime("%d%m%Y-%H%M%S")
    monedas = []
    pattern = re.compile(r'<tbody id="main-exchange-content">', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'<td><a href="(.+?)" data-toggle="tooltip" title="See Converter and History"><i class="(.+?)"></i>', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'</a></td>', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'<td class="text-right"> <span class="purchase">', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'</span> <i class="(.+?)Trend estado (.+?)"></i></td>', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'<td class="text-right"> <span class="sale">', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'<tr id="exchange-[\w]+?">(.*?)</tr>',re.DOTALL)
    match_results = pattern.findall(cuerpo_tabla)
    regex = r'\s*([a-zA-Z ]+)\s*([\d.,]+)\s*([\d.,]+)\s*'
    resultados = []
    for string in match_results:
        matches = re.findall(regex, string)[0]
        compra = float(matches[1].replace(".","").replace(",","."))
        venta = float(matches[2].replace(".","").replace(",","."))
        monedas.append(Moneda(matches[0],compra, venta, current_time))
    return monedas

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

def guardarTexto(str):
    f = open(f"sources/prueba{casaCambio.replace(' ','')}.txt","w")
    f.write(str)


def getCambiosChaco():
    html = openUrlAndGetDecodedHtml(url)
    cuerpo_tabla = findCurrenciesOnDecodedHtml(html)
    
    monedas = setCleanCurrencies(cuerpo_tabla)
    json = getCurrenciesAndLog(monedas)
    return json


if __name__ == "__main__":
    print(getCambiosChaco())