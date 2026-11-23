class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca,
        self.modelo = modelo,
        self. año = anio,
        self.kilometraje = 0
        
    def conducir(self, kilometros):
        if kilometros <=0:
            print("Los kilometros deben ser mayores a 0")
            return 
        self.kilometraje += kilometros
        
    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.anio})"     
    
    def costo_mantemiento(self):
        return 100.04
    
    #####################################clases Hijas
class Carro(Vehiculo):
     def __init__(self, marca, modelo, anio, puertas):
            super().__init__(marca, modelo, anio)
            self.puertas = puertas
            
     def descripcion(self):
        return super().descripcion() + f" - {self.puertas} puertas"
    
class Moto(Vehiculo):
    
     def ___init__(self, marca, modelo, anio, capacidad_tonelada):
        super().__init__(marca, modelo, anio)
        self.capacidad_tonelada = capacidad_tonelada
        
     def descripcion(self):
        return super().descripcion() + f" - {self.cilindraje} cc"
    
     def costo_mantenimiento (self):
        return 50.02
    
    ####################
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_tonelada):
                super().__init__(marca, modelo, anio)
                self.capacidad_tonelada = capacidad_tonelada

    def descripcion(self):
        return super().descripcion() + f" - {self.capacidad_tonelada} toneladas"

    def costo_mantenimiento(self): #override: depende de la carga
        return 100.00 + 50 * self.capacacidad_tonelada
    
#----Programa Principal-----#
if __name__ == '__main__':
    flota = [
        Carro("Toyota", "Corolla", 2000, 4),
        Moto("Honda", "CBR500R", 2021, 0.5),
        Camion("Volvo", "FH16", 2019, 10),
    ]
    
    for v in flota:
        v.conducir(120)
        print(v.descripcion)
        print (" km: ", v.kilometraje, " | Mantenimiento: Q. " , v.costo_mantenimiento())
        print("-----------------------------")
        print("Kilometraje total de la flota: ", sum(v.kilometraje for v in flota))
        print("Carro es Moto? ", isinstance)
        print("Total mantenimiento de la flota: Q. ", sum(v.costo_mantenimiento() for v in flota))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    