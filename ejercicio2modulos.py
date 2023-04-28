import time

hora_actual = time.localtime().tm_hour

if hora_actual >= 19:
    print(f'son las {hora_actual} es hora de irse')
else:
    horas_restantes = 19 - hora_actual
    minutos_restantes = horas_restantes - time.localtime().tm_min 
    print(f'todavia faltan {horas_restantes} horas y {minutos_restantes} minutos para irnos')
