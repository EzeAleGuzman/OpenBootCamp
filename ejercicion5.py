año = int(input('dime el año : '))

def es_bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return (f' El año {año} es bisiesto')
    else:
        return (f' No, {año}  no es bisiesto')
    
print(es_bisiesto(año))

    
