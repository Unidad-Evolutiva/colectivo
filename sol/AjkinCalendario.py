from datetime import datetime, timedelta
import pandas as pd

class CalendarioAjkin:
    def __init__(self):
        # Definición corregida de los meses (ordenados según recorrido solar real)
        self.meses = [
            {"num": 0, "es": "-", "en": "-", "normal": 0, "acum_normal": 0, "bisiesto": 0, "acum_bisiesto": 0},
            {"num": 1, "es": "Acuario", "en": "Aquarius", "normal": 28, "acum_normal": 28, "bisiesto": 28, "acum_bisiesto": 28},
            {"num": 2, "es": "Piscis", "en": "Pisces", "normal": 28, "acum_normal": 56, "bisiesto": 28, "acum_bisiesto": 56},
            {"num": 3, "es": "Aries", "en": "Aries", "normal": 28, "acum_normal": 84, "bisiesto": 28, "acum_bisiesto": 84},
            {"num": 4, "es": "Tauro", "en": "Taurus", "normal": 28, "acum_normal": 112, "bisiesto": 28, "acum_bisiesto": 112},
            {"num": 5, "es": "Géminis", "en": "Gemini", "normal": 28, "acum_normal": 140, "bisiesto": 28, "acum_bisiesto": 140},
            {"num": 6, "es": "Cáncer", "en": "Cancer", "normal": 28, "acum_normal": 168, "bisiesto": 28, "acum_bisiesto": 168},
            {"num": 7, "es": "Leo", "en": "Leo", "normal": 28, "acum_normal": 196, "bisiesto": 29, "acum_bisiesto": 197},  # Bisiesto aquí
            {"num": 8, "es": "Virgo", "en": "Virgo", "normal": 29, "acum_normal": 225, "bisiesto": 29, "acum_bisiesto": 226},  # Siempre 29 días
            {"num": 9, "es": "Libra", "en": "Libra", "normal": 28, "acum_normal": 253, "bisiesto": 28, "acum_bisiesto": 254},
            {"num": 10, "es": "Escorpio", "en": "Scorpio", "normal": 28, "acum_normal": 281, "bisiesto": 28, "acum_bisiesto": 282},
            {"num": 11, "es": "Ofiuco", "en": "Ophiuchus", "normal": 28, "acum_normal": 309, "bisiesto": 28, "acum_bisiesto": 310},
            {"num": 12, "es": "Sagitario", "en": "Sagittarius", "normal": 28, "acum_normal": 337, "bisiesto": 28, "acum_bisiesto": 338},
            {"num": 13, "es": "Capricornio", "en": "Capricorn", "normal": 28, "acum_normal": 365, "bisiesto": 28, "acum_bisiesto": 366}
        ]
        
        self.inicio_ajkin = datetime(2012, 12, 22)  # Día 1 Ajk'in
    
    def es_bisiesto(self, año):
        """Determina si un año gregoriano es bisiesto (reglas estándar)"""
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
    
    def convertir_gregoriano_a_ajkin(self, fecha):
        """
        Convierte una fecha gregoriana al Calendario Ajk'in.
        Retorna un diccionario con los datos convertidos.
        """
        if fecha < self.inicio_ajkin:
            return {"error": "Fecha anterior al inicio del calendario Ajk'in (22/12/2012)"}
        
        # Calcular días totales desde el inicio (Día 1 = 22/12/2012)
        delta = fecha - self.inicio_ajkin
        dia_ajkin = delta.days + 1
        
        # Calcular año Ajk'in (cada 365/366 días)
        año_ajkin = 1
        dias_restantes = dia_ajkin
        while True:
            dias_en_año = 366 if self.es_bisiesto(2012 + año_ajkin) else 365
            if dias_restantes <= dias_en_año:
                break
            dias_restantes -= dias_en_año
            año_ajkin += 1
        
        # Determinar si el año actual es bisiesto
        es_bisiesto_ajkin = self.es_bisiesto(2012 + año_ajkin)
        
        # Encontrar mes y día correspondiente
        mes_actual = None
        for mes in self.meses[1:]:  # Saltamos el mes 0
            acumulado = mes["acum_bisiesto"] if es_bisiesto_ajkin else mes["acum_normal"]
            if dias_restantes <= acumulado:
                mes_anterior = self.meses[mes["num"] - 1]
                acum_anterior = mes_anterior["acum_bisiesto"] if es_bisiesto_ajkin else mes_anterior["acum_normal"]
                dia_en_mes = dias_restantes - acum_anterior
                mes_actual = mes
                break
        
        return {
            "fecha_gregoriana": fecha.strftime("%Y-%m-%d"),
            "dia_ajkin": dia_ajkin,
            "año_ajkin": año_ajkin,
            "num_mes": mes_actual["num"],
            "nombre_mes_es": mes_actual["es"],
            "nombre_mes_en": mes_actual["en"],
            "dia_en_mes": dia_en_mes,
            "es_bisiesto": es_bisiesto_ajkin,
            "descripcion_es": f"{dia_en_mes} de {mes_actual['es']} de {año_ajkin}",
            "descripcion_en": f"{dia_en_mes} of {mes_actual['en']} of {año_ajkin}"
        }
    
    def convertir_rango(self, fecha_inicio, fecha_fin):
        """Convierte un rango de fechas gregorianas a Ajk'in y devuelve un DataFrame"""
        fechas = []
        current_date = fecha_inicio
        while current_date <= fecha_fin:
            conversion = self.convertir_gregoriano_a_ajkin(current_date)
            if "error" not in conversion:
                fechas.append(conversion)
            current_date += timedelta(days=1)
        
        return pd.DataFrame(fechas)

# Ejemplo de uso
if __name__ == "__main__":
    calendario = CalendarioAjkin()
    
    # Fechas de prueba
    fechas_ejemplo = [
        datetime(2012, 12, 21),  # Nodo (antes del inicio)
        datetime(2012, 12, 22),  # Día 1 Ajk'in
        datetime(2024, 2, 29),   # Año bisiesto
        datetime(2024, 7, 5),     # 29 Leo (bisiesto)
        datetime(2025, 2, 28),   # Año normal
        datetime(2025, 7, 5)      # 28 Leo (normal)
    ]
    
    # Conversión individual
    print("=== Conversiones individuales ===")
    for fecha in fechas_ejemplo:
        resultado = calendario.convertir_gregoriano_a_ajkin(fecha)
        if "error" in resultado:
            print(f"{fecha.strftime('%Y-%m-%d')}: {resultado['error']}")
        else:
            print(f"{resultado['fecha_gregoriana']} → {resultado['descripcion_es']} (Día Ajk'in {resultado['dia_ajkin']})")
    
    # Conversión de rango (ejemplo: todo 2024)
    print("\n=== Conversión de rango (2024) ===")
    df_2024 = calendario.convertir_rango(datetime(2024, 1, 1), datetime(2024, 12, 31))
    print(df_2024[["fecha_gregoriana", "descripcion_es", "es_bisiesto"]].head())