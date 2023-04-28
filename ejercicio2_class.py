class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota 
 
    def calificacion(self):
        if self.nota > 7:
            print(f'el alumno {self.nombre} a aprobado') 
        else:
            print(f'el alumno {self.nombre} a desaprobado')
            
alumno1 = Alumno("juan", 5)
alumno1.calificacion()

alumno2 = Alumno("CArlos", 7)
alumno2.calificacion()
        