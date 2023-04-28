class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        
        
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, Velocidad, Cilindrada):
        super().__init__(color, ruedas, puertas)
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
  
auto = Coche("Negro", 4, 5, "220 km/h", "1.4 litros")
print(f'el auto es color: {auto.color}')
print(f'Tiene {auto.ruedas} ruedas')
print(f'Es de {auto.puertas} puertas')
print(f'con  velocidad max de : {auto.Velocidad}')
print(f'con una cilindrada de {auto.Cilindrada}')