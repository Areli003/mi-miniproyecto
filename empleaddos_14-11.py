# Clase padre Empleado con el atributo nombre.
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        pass


#Clase EmpleadoTiempoCompleto, que almacene un salario mensual.
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

#Calcular_pago() en cada clase hija.
    def calcular_pago(self):
        return self.salario_mensual


#Clase EmpleadoPorHora, que almacene horas trabajadas y pago por hora.
class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    #alcular_pago() en cada clase hija.
    def calcular_pago(self):
        return self.horas_trabajadas * self.pago_por_hora


#Un objeto de cada tipo (usando los datos de prueba).
# Ana: Tiempo completo con Q5,000 de salario mensual
emp1 = EmpleadoTiempoCompleto("Ana", 5000)

# Luis: Por hora con 80 horas a Q25 por hora
emp2 = EmpleadoPorHora("Luis", 80, 25)

# 6. Lista y muestra  su nombre y pago mediante un ciclo for.
empleados = [emp1, emp2]

for empleado in empleados:
    print(f"Empleado: {empleado.nombre} - Pago: Q{empleado.calcular_pago():,.2f}")

#¿En qué ´parte del programa se observa el polimofismo?
# El polimorfismo se observa en el ciclo for donde se llama al método calcular_pago() 
# de cada objeto empleado, ya que cada clase hija tiene su propia implementación de este método.










