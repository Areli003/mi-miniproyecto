class Moto(Vehículo):
     
    def __init__(self, marca, modelo, anio, cilindraje):
        super().__init__(marca, modelo, anio)
        self.cilindraje = cilindraje
        
    def descripcion(self):
        return super().descripcion() + f" - {self.cilindraje} cc"
    
    def costo_mantenimiento(self):
        return 50.02
    
    flota = [
        Carro("Toyota"),
        Moto("Honda"),
        Camion()
    ]