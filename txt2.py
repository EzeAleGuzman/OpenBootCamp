import pickle

class vehiculo():
    def __init__(self, marca, color, año):
        self.marca = marca
        self.color = color
        self.año = año

    def getNombre(self):
        return self.marca
        
veh1 = vehiculo("fiat", "rojo", 2010)

f = open("datos.bin", "wb")
pickle.dump(veh1, f)
f.close()
f = open("datos.bin", "rb")
fiat = pickle.load(f)   
f.close()    
print(type(fiat))
print(fiat.getNombre(), "su color es: ", fiat.color, "y su año", fiat.año)