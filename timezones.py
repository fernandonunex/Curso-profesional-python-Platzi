from datetime import datetime
import pytz

bogota_timezone = pytz.timezone('America/Bogota')
#print(type(bogota_timezone))
bogota_date = datetime.now(bogota_timezone)
#print(type(bogota_date))
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))


mexico_timezone = pytz.timezone('America/Mexico_City')
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de México: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))


los_angeles_timezone = pytz.timezone('America/Los_Angeles')
los_angeles_date = datetime.now(los_angeles_timezone)
print("Los Angeles: ", los_angeles_date.strftime("%d/%m/%Y, %H:%M:%S"))