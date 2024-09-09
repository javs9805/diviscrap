from backend.maxicambios import getMaxicambios
from db.database import GestorBaseDeDatos
import json 


if __name__ == "__main__":
    gestor = GestorBaseDeDatos()
    resJson = getMaxicambios()
    res = json.loads(resJson)
    nombreCasa = res["nombre"]
    res = res["monedas"]
    if len(gestor.verificar_si_existe_en("Casa_de_cambios",("nombre",),(nombreCasa,))) == 0:
        gestor.crear_casa_de_cambios(nombreCasa)
        for r in res:
            if len(gestor.verificar_si_existe_en("Casa_de_cambios_Moneda",("nombre",),(r["nombre"],))) == 0:
                gestor.crear_relacion_casa_moneda(nombreCasa,r["nombre"])
            else:
                dato = gestor.verificar_si_existe_en("Casa_de_cambios_Moneda",("nombre",),(r["nombre"],))
                gestor.crear_moneda(r["nombre"],r["compra"],r["venta"],r["timestamp"],dato[0][0])

    else:
        for r in res:
            if len(gestor.verificar_si_existe_en("Casa_de_cambios_Moneda",("nombre",),(r["nombre"],))) == 0:
                gestor.crear_relacion_casa_moneda(nombreCasa,r["nombre"])
            else:
                dato = gestor.verificar_si_existe_en("Casa_de_cambios_Moneda",("nombre",),(r["nombre"],))
                gestor.crear_moneda(r["nombre"],r["compra"],r["venta"],r["timestamp"],dato[0][0])

