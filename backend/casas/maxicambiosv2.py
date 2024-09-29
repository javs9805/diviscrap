from urllib.request import urlopen
from moneda import Moneda
import re
import json
from datetime import datetime

url = "https://www.maxicambios.com.py/"
casaCambio = "Maxicambios"

def guardarTexto(str):
    f = open(f"sources/prueba{casaCambio.replace(' ','')}.txt","w")
    f.write(str)

def openUrlAndGetDecodedHtml(url):
    page = urlopen(url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")

def findCurrenciesOnDecodedHtml(html):
    index_inicio = html.find("<tbody>")
    index_final = html.find("</tbody>")
    return html[index_inicio:index_final]


def setCleanCurrencies(cuerpo_tabla):
    monedas = []
    cuerpo_tabla = cuerpo_tabla.replace("<td>","").replace("</td>","").replace(" ","")
    pattern = re.compile(r'<imgsrc=".*?">', re.DOTALL)
    cuerpo_tabla = re.sub(pattern, '', cuerpo_tabla)
    pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
    match_results = pattern.findall(cuerpo_tabla)
    for i,m in enumerate(match_results):
        match_results[i] = m.strip().split("\n")
    for m in match_results:
        monedas.append(Moneda(m[0],float(m[2]),float(m[3])))
    return monedas

def getCurrenciesAndLog(monedas):
    f = open("../sources/maxicambios.txt","a")
    now = datetime.now()
    current_time = now.strftime("%d%m%Y-%H%M%S")
    print("Current Time =", current_time)
    jsonMonedas = json.dumps({"time":current_time,"name":"Maxicambios","currency":[moneda.to_dict() for moneda in monedas]}, indent = 2)
    f.write(",\n")
    f.write(jsonMonedas)
    return jsonMonedas

def getMaxicambios():
    html = openUrlAndGetDecodedHtml(url)
    cuerpo_tabla = findCurrenciesOnDecodedHtml(html)
    guardarTexto(html)
    #monedas = setCleanCurrencies(cuerpo_tabla)
    #json = getCurrenciesAndLog(monedas)
    #return json


if __name__ == "__main__":
    print(getMaxicambios())