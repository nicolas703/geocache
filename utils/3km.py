import math

# # quiero cambiar esto S 33° 24.920' W 070° 35.370' a decimal

# def dms2str(string):
#     # S 33° 24.920' W 070° 35.370'
#     # 33 + 24.920/60
#     # 70 + 35.370/60

#     string = string.replace('° ', '°')
#     string = string.replace('\'', '')
#     coorx, longitude, coory, latitude = string.split(' ')
#     #funcion if en una linea
#     x = '-' if coorx.upper() == 'S'  else "+"
#     y = '-' if coory.upper() == 'W'  else "+"
#     return x,longitude,y,latitude

# def dms2dec(string):
#     x,longitude,y,latitude = dms2str(string)
#     long_hora, long_min = longitude.split('°')
#     lat_hora, lat_min = latitude.split('°')
#     long_min = float(long_min)/60
#     lat_min = float(lat_min)/60
#     return x, int(long_hora) + long_min, y, int(lat_hora) + lat_min

# def dec2dms(coor):
#     minute,grade = math.modf(coor)
#     minute = float(minute * 60)
#     return f'{int(grade)}° {minute:.3f}\''


# def calc_limit(coor,dist):
#     x, longi, y, lat = coor
#     R = 6371.0
#     lat_rad = math.radians(lat)
#     delta_lat = dist/R * (180/math.pi)
#     delta_long = dist/(R * math.cos(lat_rad)) * (180/math.pi)
#     lat_min = dec2dms(lat - delta_lat)
#     lat_max = dec2dms(lat + delta_lat)
#     long_min = dec2dms(longi - delta_long)
#     long_max = dec2dms(longi + delta_long)
#     min_km = f'{x}{long_min} {y}{lat_min}'
#     max_km = f'{x}{long_max} {y}{lat_max}'
#     return (min_km,max_km)


# coordenate = input("Ingrese las coordenadas: ")

# print(calc_limit(dms2dec(coordenate),3))


# Convertir coordenadas DMS a decimal
def dms2str(string):
    # S 33° 24.920' W 070° 35.370'
    string = string.replace('° ', '°')
    string = string.replace('\'', '')
    coorx, longitude, coory, latitude = string.split(' ')
    x = '-' if coorx.upper() == 'S'  else "+"
    y = '-' if coory.upper() == 'W'  else "+"
    return x, longitude, y, latitude

def dms2dec(string):
    x, longitude, y, latitude = dms2str(string)
    long_hora, long_min = longitude.split('°')
    lat_hora, lat_min = latitude.split('°')
    long_min = float(long_min) / 60
    lat_min = float(lat_min) / 60
    return float(x + str(int(long_hora) + long_min)), float(y + str(int(lat_hora) + lat_min))

def dec2dms(coor):
    minute, grade = math.modf(coor)
    minute = abs(minute * 60)
    return f'{int(grade)}° {minute:.3f}\''

def calc_limit(string, dist):
    longi, lat = dms2dec(string)
    R = 6371.0
    delta_lat = dist / R * (180 / math.pi)
    delta_long = dist / (R * math.cos(math.radians(lat))) * (180 / math.pi)
    
    lat_min = dec2dms(lat - delta_lat)
    lat_max = dec2dms(lat + delta_lat)
    long_min = dec2dms(longi - delta_long)
    long_max = dec2dms(longi + delta_long)
    
    return (f'{long_min} {lat_min}', f'{long_max} {lat_max}')

coordenate = input("Ingrese las coordenadas: ")
print(calc_limit(coordenate, 3))