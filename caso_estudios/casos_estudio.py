"""
=============================================================
 TECHMART EXPRESS – Sistema de Gestión de Pedidos (Black Friday)
 Programación I: Orientada a Objetos — Semana 13
 Caso de Estudio: Código Base para Estudiantes
=============================================================
 INSTRUCCIONES:
  - Implementa TODOS los métodos marcados con  # TODO
  - NO modifiques los nombres de los métodos ni sus parámetros
  - Puedes agregar métodos auxiliares privados si lo necesitas
  - Ejecuta las pruebas con:  pytest test_tienda_online.py -v
=============================================================
"""

# ─────────────────────────────────────────────
#  CLASE: Producto
# ─────────────────────────────────────────────
class Producto:
    """Representa un artículo disponible en el catálogo de TechMart."""

    def __init__(self, codigo: str, nombre: str, precio: float,
                 stock: int, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio        # precio en Q (quetzales)
        self.stock = stock          # unidades disponibles
        self.categoria = categoria  # "electronico", "ropa", "hogar", "juguete"

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} — Q{self.precio:.2f} (stock: {self.stock})"

    # ── TODO 1 ──────────────────────────────────────────────────────────────
    def aplicar_descuento(self, porcentaje: float) -> float:
        """
        Calcula el precio final después de aplicar un descuento.

        Regla de negocio:
          - El porcentaje debe estar entre 0 y 100 (inclusive).
          - Si está fuera de ese rango, retorna el precio original sin cambios.
          - Retorna el precio con descuento redondeado a 2 decimales.

        Ejemplo:
          producto.precio = 500.0  →  aplicar_descuento(20) → 400.0
        """
        # TODO: implementa la lógica aquí
        if not (0 <= porcentaje <= 100):
            return self.precio
        
        precio_final = self.precio * (1 - porcentaje / 100)
        return round(precio_final, 2)
        
    # ── TODO 2 ──────────────────────────────────────────────────────────────
    def hay_stock(self, cantidad: int) -> bool:
        """
        Verifica si hay suficiente stock para cubrir la cantidad solicitada.

        Retorna True si stock >= cantidad, False en caso contrario.
        """
        # TODO: implementa la lógica aquí
        return self.stock >= cantidad

    # ── TODO 3 ──────────────────────────────────────────────────────────────
    def reducir_stock(self, cantidad: int) -> bool:
        """
        Descuenta 'cantidad' unidades del stock SOLO si hay disponibilidad.

        - Si hay stock suficiente: reduce el stock y retorna True.
        - Si NO hay stock suficiente: NO modifica el stock y retorna False.
        """
        # TODO: implementa la lógica aquí
        if self.hay_stock(cantidad):
            self.stock -= cantidad
            return True
        return False


# ─────────────────────────────────────────────
#  CLASE: Cliente
# ─────────────────────────────────────────────
class Cliente:
    """Representa un cliente registrado en TechMart Express."""

    CATEGORIAS_VALIDAS = ["normal", "vip", "moroso"]

    def __init__(self, id_cliente: str, nombre: str,
                 categoria: str, antiguedad_anios: int, total_compras: float):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.categoria = categoria          # "normal", "vip" o "moroso"
        self.antiguedad_anios = antiguedad_anios
        self.total_compras = total_compras  # total histórico en Q

    def __str__(self):
        return f"Cliente({self.id_cliente}) {self.nombre} [{self.categoria.upper()}]"

    # ── TODO 4 ──────────────────────────────────────────────────────────────
    def es_cliente_preferente(self) -> bool:
        """
        Determina si el cliente califica como preferente.

        Reglas (TODAS deben cumplirse):
          1. categoria == "vip"
          2. antiguedad_anios >= 2
          3. total_compras >= 5000.0

        Retorna True si cumple todas las condiciones, False si no.
        """
        # TODO: implementa la lógica aquí
        return (self.categoria == "vip" and 
                self.antiguedad_anios >= 2 and 
                self.total_compras >= 5000.0)

    # ── TODO 5 ──────────────────────────────────────────────────────────────
    def calcular_descuento_cliente(self) -> float:
        """
        Retorna el porcentaje de descuento al que tiene derecho el cliente.

        Tabla de descuentos:
          - Moroso               →  0 %
          - Normal, < 2 años     →  5 %
          - Normal, >= 2 años    → 10 %
          - VIP, no preferente   → 15 %
          - VIP preferente       → 25 %
        """
        # TODO: implementa la lógica aquí
        if self.categoria == "moroso":
            return 0
        elif self.categoria == "normal":
            return 10 if self.antiguedad_anios >= 2 else 5
        elif self.categoria == "vip":
            return 25 if self.es_cliente_preferente() else 15
        return 0


# ─────────────────────────────────────────────
#  CLASE: Pedido
# ─────────────────────────────────────────────
class Pedido:
    """Representa un pedido realizado por un cliente."""

    ESTADOS_VALIDOS = ["pendiente", "procesando", "enviado", "entregado", "cancelado"]
    REGIONES_VALIDAS = ["ciudad", "interior", "internacional"]

    def __init__(self, id_pedido: str, cliente: Cliente,
                 productos: list, region: str, estado: str = "pendiente"):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = productos  # lista de Producto
        self.region = region        # "ciudad", "interior", "internacional"
        self.estado = estado

    def __str__(self):
        return (f"Pedido({self.id_pedido}) | {self.cliente.nombre} | "
                f"Region: {self.region} | Estado: {self.estado}")

    # ── TODO 6 ──────────────────────────────────────────────────────────────
    def calcular_subtotal(self) -> float:
        """
        Suma el precio de todos los productos del pedido SIN descuentos.
        Retorna el subtotal redondeado a 2 decimales.
        """
        # TODO: implementa la lógica aquí
        subtotal = sum(p.precio for p in self.productos)
        return round(subtotal, 2)
    # ── TODO 7 ──────────────────────────────────────────────────────────────
    def calcular_costo_envio(self) -> float:
        """
        Calcula el costo de envío según la región y el estado del cliente.

        Tabla base de envío:
          - ciudad        →  Q  25.00
          - interior      →  Q  60.00
          - internacional →  Q 150.00

        Modificadores:
          - Si el cliente es VIP preferente → envío GRATIS (Q 0.00)
          - Si el cliente es moroso         → recargo del 50 % sobre la tarifa base
        """
        # TODO: implementa la lógica aquí
        tarifas_base = {
            "ciudad": 25.00,
            "interior": 60.00,
            "internacional": 150.00
        }
        tarifa = tarifas_base.get(self.region, 0.00)

        if self.cliente.es_cliente_preferente():
            return 0.00
        elif self.cliente.categoria == "moroso":
            tarifa *= 1.5

        return round(tarifa, 2)

    # ── TODO 8 ──────────────────────────────────────────────────────────────
    def calcular_impuesto(self) -> float:
        """
        Calcula el IVA (12 %) sobre el subtotal DESPUÉS de aplicar
        el descuento del cliente.

        Pasos:
          1. Obtén el subtotal.
          2. Aplica el descuento del cliente al subtotal.
          3. Calcula el 12 % sobre el monto con descuento.
          4. Retorna el impuesto redondeado a 2 decimales.
        """
        # TODO: implementa la lógica aquí
        subtotal = self.calcular_subtotal()
        porcentaje_desc = self.cliente.calcular_descuento_cliente()
        monto_desc = subtotal * (1 - porcentaje_desc / 100)
        impuesto = monto_desc * 0.12
        return round(impuesto, 2)

    # ── TODO 9 ──────────────────────────────────────────────────────────────
    def calcular_total(self) -> float:
        """
        Retorna el monto total del pedido:
          subtotal − descuento_cliente + impuesto + costo_envio

        Redondeado a 2 decimales.
        """
        # TODO: implementa la lógica aquí
        subtotal = self.calcular_subtotal()
        porcentaje_desc = self.cliente.calcular_descuento_cliente()
        monto_desc = subtotal * (1 - porcentaje_desc / 100)
        impuesto = self.calcular_impuesto()
        envio = self.calcular_costo_envio()

        total = monto_desc + impuesto + envio
        return round(total, 2)

    # ── TODO 10 ─────────────────────────────────────────────────────────────
    def cambiar_estado(self, nuevo_estado: str) -> bool:
        """
        Cambia el estado del pedido siguiendo el flujo permitido:
          pendiente → procesando → enviado → entregado

        Reglas adicionales:
          - Solo se puede cancelar si el estado actual es "pendiente" o "procesando".
          - Si el nuevo_estado no está en ESTADOS_VALIDOS → retorna False sin cambiar.
          - Si el cambio no sigue el flujo válido → retorna False sin cambiar.
          - Si el cambio es permitido → actualiza self.estado y retorna True.
        """
        # TODO: implementa la lógica aquí
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            return False

        # Regla de cancelación
        if nuevo_estado == "cancelado":
            if self.estado in ["pendiente", "procesando"]:
                self.estado = "cancelado"
                return True
            return False

        # Flujo normal
        flujo = {
            "pendiente": "procesando",
            "procesando": "enviado",
            "enviado": "entregado"
        }

        if self.estado in flujo and flujo[self.estado] == nuevo_estado:
            self.estado = nuevo_estado
            return True

        return False


# ─────────────────────────────────────────────
#  CLASE: TechMartSistema
# ─────────────────────────────────────────────
class TechMartSistema:
    """Gestiona la colección completa de pedidos, productos y clientes."""

    def __init__(self):
        self.pedidos: list = []
        self.productos: list = []
        self.clientes: list = []

    def agregar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    # ── TODO 11 ─────────────────────────────────────────────────────────────
    def obtener_pedidos_pendientes(self) -> list:
        """
        Retorna una lista con todos los pedidos cuyo estado sea "pendiente".
        Si no hay ninguno, retorna lista vacía.
        """
        # TODO: implementa la lógica aquí
        return [p for p in self.pedidos if p.estado == "pendiente"]

    # ── TODO 12 ─────────────────────────────────────────────────────────────
    def buscar_pedidos_por_cliente(self, id_cliente: str) -> list:
        """
        Retorna todos los pedidos que pertenezcan al cliente con id_cliente.
        Comparación case-sensitive. Lista vacía si no hay coincidencias.
        """
        # TODO: implementa la lógica aquí
        return [p for p in self.pedidos if p.cliente.id_cliente == id_cliente]

    # ── TODO 13 ─────────────────────────────────────────────────────────────
    def ordenar_pedidos_por_total(self, ascendente: bool = True) -> list:
        """
        Retorna una NUEVA lista de pedidos ordenados por su total calculado.
        - ascendente=True  → de menor a mayor total
        - ascendente=False → de mayor a menor total
        NO modifica self.pedidos.
        """
        # TODO: implementa la lógica aquí
        return sorted(self.pedidos, key=lambda p: p.calcular_total(), reverse=not ascendente)
    
    # ── TODO 14 ─────────────────────────────────────────────────────────────
    def filtrar_clientes_morosos(self) -> list:
        """
        Retorna la lista de clientes cuya categoría sea "moroso".
        """
        # TODO: implementa la lógica aquí
        return [c for c in self.clientes if c.categoria == "moroso"]

    # ── TODO 15 ─────────────────────────────────────────────────────────────
    def calcular_ingresos_totales(self) -> float:
        """
        Suma los totales de TODOS los pedidos que NO estén cancelados.
        Retorna el resultado redondeado a 2 decimales.
        """
        # TODO: implementa la lógica aquí
        total_ingresos = sum(p.calcular_total() for p in self.pedidos if p.estado != "cancelado")
        return round(total_ingresos, 2)

    # ── TODO 16 ─────────────────────────────────────────────────────────────
    def obtener_producto_mas_caro(self) -> Producto:
        """
        Retorna el objeto Producto con el precio más alto.
        Si la lista de productos está vacía, retorna None.
        """
        # TODO: implementa la lógica aquí
        if not self.productos:
            return None
        return max(self.productos, key=lambda p: p.precio)

    
    # ── TODO 17 ─────────────────────────────────────────────────────────────
    def reporte_pedidos_por_region(self) -> dict:
        """
        Genera un diccionario con la cantidad de pedidos por región.

        Ejemplo de resultado:
          {"ciudad": 4, "interior": 2, "internacional": 1}

        Debe incluir las tres regiones aunque la cantidad sea 0.
        """
        # TODO: implementa la lógica aquí
        reporte = {"ciudad": 0, "interior": 0, "internacional": 0}
        for p in self.pedidos:
            if p.region in reporte:
                reporte[p.region] += 1
        return reporte

# ─────────────────────────────────────────────
#  DATOS PRECARGADOS (no modificar)
# ─────────────────────────────────────────────
def cargar_datos_sistema() -> TechMartSistema:
    """Carga los datos de prueba del escenario Black Friday."""
    sistema = TechMartSistema()

    # Productos
    p1 = Producto("PRD-001", "Laptop UltraBook 15", 4500.00, 10, "electronico")
    p2 = Producto("PRD-002", "Audífonos Bluetooth Pro", 350.00, 25, "electronico")
    p3 = Producto("PRD-003", "Silla Ergonómica Mesh", 1200.00, 8, "hogar")
    p4 = Producto("PRD-004", "Camiseta Deportiva XL", 85.00, 50, "ropa")
    p5 = Producto("PRD-005", "Set de Legos Espacial", 450.00, 15, "juguete")
    p6 = Producto("PRD-006", "Monitor 27 pulgadas 4K", 3200.00, 5, "electronico")

    for prod in [p1, p2, p3, p4, p5, p6]:
        sistema.agregar_producto(prod)

    # Clientes
    c1 = Cliente("CLI-001", "María García",    "vip",    3, 12500.00)
    c2 = Cliente("CLI-002", "Juan Pérez",      "normal", 1, 800.00)
    c3 = Cliente("CLI-003", "Ana Rodríguez",   "moroso", 5, 3200.00)
    c4 = Cliente("CLI-004", "Carlos López",    "vip",    2, 5000.00)
    c5 = Cliente("CLI-005", "Lucía Martínez",  "normal", 4, 2000.00)

    for cli in [c1, c2, c3, c4, c5]:
        sistema.agregar_cliente(cli)

    # Pedidos
    ped1 = Pedido("PED-001", c1, [p1, p2],    "ciudad",        "pendiente")
    ped2 = Pedido("PED-002", c2, [p4, p5],    "interior",      "pendiente")
    ped3 = Pedido("PED-003", c3, [p3],         "ciudad",        "procesando")
    ped4 = Pedido("PED-004", c4, [p6, p2],    "internacional", "pendiente")
    ped5 = Pedido("PED-005", c5, [p1, p3, p4], "interior",     "enviado")
    ped6 = Pedido("PED-006", c1, [p5],         "ciudad",        "cancelado")

    for ped in [ped1, ped2, ped3, ped4, ped5, ped6]:
        sistema.agregar_pedido(ped)

    return sistema


if __name__ == "__main__":
    sistema = cargar_datos_sistema()
    print("=== TechMart Express — Sistema cargado ===")
    print(f"Productos registrados : {len(sistema.productos)}")
    print(f"Clientes registrados  : {len(sistema.clientes)}")
    print(f"Pedidos registrados   : {len(sistema.pedidos)}")
    print("\nPedidos pendientes:")
    for ped in (sistema.obtener_pedidos_pendientes() or []):
        print(" ", ped)
        
        
        
