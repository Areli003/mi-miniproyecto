# Catálogo de mascotas para adopción responsable
# Incluye búsqueda, favoritos, estados, reporte y opción para agregar mascotas.

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from pathlib import Path
import math


# ABSTRACCIÓN:
# Esta clase reúne lo que todas las mascotas tienen en común.
class Mascota:
    def __init__(self, nombre, edad, descripcion, imagen, estado="Disponible"):
        # ENCAPSULAMIENTO:
        # Los atributos privados empiezan con doble guion bajo.
        self.__nombre = nombre
        self.__edad = edad
        self.__descripcion = descripcion
        self.__imagen = imagen
        self.__estado = estado

    # Métodos para consultar los datos privados.
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_descripcion(self):
        return self.__descripcion

    def obtener_imagen(self):
        return self.__imagen

    def obtener_estado(self):
        return self.__estado

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def presentarse(self):
        return f"Hola, soy {self.__nombre} y busco un hogar."


# HERENCIA: Perro hereda de Mascota.
class Perro(Mascota):
    def __init__(self, nombre, edad, descripcion, imagen, tamano,
                 estado="Disponible"):
        super().__init__(nombre, edad, descripcion, imagen, estado)
        self.__tamano = tamano

    # POLIMORFISMO: el perro tiene su propia presentación.
    def presentarse(self):
        return (
            f"¡Guau! Soy {self.obtener_nombre()}, "
            f"un perro de tamaño {self.__tamano}."
        )


# HERENCIA: Gato también hereda de Mascota.
class Gato(Mascota):
    def __init__(self, nombre, edad, descripcion, imagen, color,
                 estado="Disponible"):
        super().__init__(nombre, edad, descripcion, imagen, estado)
        self.__color = color

    # POLIMORFISMO: el gato se presenta de manera diferente.
    def presentarse(self):
        return (
            f"¡Miau! Soy {self.obtener_nombre()}, "
            f"un gato de color {self.__color}."
        )


# Carpeta que contiene las fotos.
carpeta_imagenes = Path(__file__).parent / "imagenes"

# Mascotas iniciales del catálogo.
mascotas = [
    Perro("Luna", 2, "Cariñosa y le gusta jugar.",
          carpeta_imagenes / "luna.png", "mediano"),
    Gato("Milo", 1, "Tranquilo y curioso.",
         carpeta_imagenes / "milo.png", "gris"),
    Perro("Max", 4, "Le gusta caminar y convivir con personas.",
          carpeta_imagenes / "max.png", "grande"),
    Gato("Nina", 3, "Independiente y tranquila.",
         carpeta_imagenes / "nina.png", "blanco"),
]

favoritas = []


# Carga una imagen PNG o GIF y la reduce si es muy grande.
def cargar_imagen(ruta, ancho_maximo=180, alto_maximo=120):
    if ruta is None or not ruta.exists():
        return None

    try:
        foto = tk.PhotoImage(file=str(ruta))
        factor_ancho = math.ceil(foto.width() / ancho_maximo)
        factor_alto = math.ceil(foto.height() / alto_maximo)
        factor = max(1, factor_ancho, factor_alto)
        return foto.subsample(factor, factor)
    except tk.TclError:
        return None


# Crea la ventana principal.
ventana = tk.Tk()
ventana.title("Catálogo de mascotas para adopción")
ventana.geometry("900x760")

tk.Label(
    ventana,
    text="Catálogo de mascotas para adopción",
    font=("Arial", 18, "bold")
).pack(pady=8)

tk.Label(
    ventana,
    text="Adoptar implica compromiso, tiempo y cuidados."
).pack(pady=3)

# Aquí aparecerán las tarjetas de las mascotas.
marco_catalogo = tk.Frame(ventana)
marco_catalogo.pack(pady=8)


def mostrar_detalles(mascota):
    """Abre una ventana con la información de una mascota."""
    detalle = tk.Toplevel(ventana)
    detalle.title("Detalles de " + mascota.obtener_nombre())
    detalle.geometry("370x460")

    foto = cargar_imagen(
        mascota.obtener_imagen(), ancho_maximo=280, alto_maximo=210
    )

    if foto is not None:
        etiqueta_foto = tk.Label(detalle, image=foto)
        etiqueta_foto.image = foto
        etiqueta_foto.pack(pady=8)
    else:
        tk.Label(detalle, text="Foto no encontrada").pack(pady=25)

    tk.Label(
        detalle,
        text=mascota.obtener_nombre(),
        font=("Arial", 18, "bold")
    ).pack(pady=4)

    tk.Label(detalle, text=f"Edad: {mascota.obtener_edad()} años").pack()
    tk.Label(detalle, text=f"Estado: {mascota.obtener_estado()}").pack()

    tk.Label(
        detalle,
        text=mascota.obtener_descripcion(),
        wraplength=330
    ).pack(pady=7)

    tk.Label(
        detalle,
        text=mascota.presentarse(),
        wraplength=330
    ).pack(pady=7)


def marcar_favorita(mascota):
    """Agrega o quita una mascota de la lista de favoritas."""
    if mascota in favoritas:
        favoritas.remove(mascota)
        mensaje = "Se quitó de favoritas."
    else:
        favoritas.append(mascota)
        mensaje = "Se agregó a favoritas."

    messagebox.showinfo("Favoritos", mensaje)
    mostrar_catalogo()


def mostrar_catalogo(lista=None):
    """Muestra las mascotas recibidas; si no recibe lista, muestra todas."""
    if lista is None:
        lista = mascotas

    # Borra las tarjetas anteriores antes de mostrar la nueva lista.
    for tarjeta in marco_catalogo.winfo_children():
        tarjeta.destroy()

    if len(lista) == 0:
        tk.Label(
            marco_catalogo,
            text="No hay mascotas para mostrar."
        ).pack(pady=20)
        return

    # CICLO WHILE: recorre la lista y crea una tarjeta por mascota.
    indice = 0
    while indice < len(lista):
        mascota = lista[indice]
        fila = indice // 3
        columna = indice % 3

        tarjeta = tk.Frame(marco_catalogo, padx=12, pady=8)
        tarjeta.grid(row=fila, column=columna, padx=10, pady=8)

        foto = cargar_imagen(mascota.obtener_imagen())

        if foto is not None:
            etiqueta_foto = tk.Label(tarjeta, image=foto)
            etiqueta_foto.image = foto
            etiqueta_foto.pack()
        else:
            tk.Label(
                tarjeta,
                text="Foto no encontrada",
                width=22,
                height=5
            ).pack()

        tk.Label(
            tarjeta,
            text=f"{mascota.obtener_nombre()} ({type(mascota).__name__})",
            font=("Arial", 12, "bold")
        ).pack(pady=3)

        tk.Label(
            tarjeta,
            text=f"Estado: {mascota.obtener_estado()}"
        ).pack(pady=2)

        tk.Button(
            tarjeta,
            text="Ver detalles",
            command=lambda animal=mascota: mostrar_detalles(animal)
        ).pack(pady=2)

        if mascota in favoritas:
            texto_favorito = "Quitar de favoritos"
        else:
            texto_favorito = "Agregar a favoritos"

        tk.Button(
            tarjeta,
            text=texto_favorito,
            command=lambda animal=mascota: marcar_favorita(animal)
        ).pack(pady=2)

        indice += 1


def buscar_por_nombre():
    """Busca mascotas cuyo nombre coincida con el texto escrito."""
    nombre = simpledialog.askstring(
        "Buscar mascota",
        "Escribe el nombre que quieres buscar:"
    )

    if nombre is None:
        return

    nombre = nombre.strip().casefold()
    resultados = []

    # CICLO WHILE: revisa los nombres del catálogo.
    indice = 0
    while indice < len(mascotas):
        if nombre in mascotas[indice].obtener_nombre().casefold():
            resultados.append(mascotas[indice])
        indice += 1

    mostrar_catalogo(resultados)


def mostrar_favoritas():
    """Muestra únicamente las mascotas favoritas."""
    mostrar_catalogo(favoritas)


def buscar_mascota_por_nombre(nombre):
    """Encuentra una mascota usando su nombre."""
    nombre = nombre.strip().casefold()

    for mascota in mascotas:
        if mascota.obtener_nombre().casefold() == nombre:
            return mascota

    return None


def agregar_a_favoritos():
    """Pide un nombre y agrega esa mascota a favoritas."""
    nombre = simpledialog.askstring(
        "Agregar a favoritos",
        "Escribe el nombre de la mascota:"
    )

    if nombre is None:
        return

    mascota = buscar_mascota_por_nombre(nombre)

    if mascota is None:
        messagebox.showerror("Error", "No se encontró esa mascota.")
    elif mascota in favoritas:
        messagebox.showinfo("Favoritos", "Ya está en favoritas.")
    else:
        favoritas.append(mascota)
        messagebox.showinfo("Favoritos", "Se agregó a favoritas.")
        mostrar_catalogo()


def cambiar_estado_adopcion():
    """Permite cambiar el estado de adopción de una mascota."""
    nombre = simpledialog.askstring(
        "Cambiar estado",
        "Escribe el nombre de la mascota:"
    )

    if nombre is None:
        return

    mascota = buscar_mascota_por_nombre(nombre)

    if mascota is None:
        messagebox.showerror("Error", "No se encontró esa mascota.")
        return

    estado = simpledialog.askstring(
        "Nuevo estado",
        "Escribe: Disponible, En proceso o Adoptada"
    )

    if estado is None:
        return

    estados_validos = ["Disponible", "En proceso", "Adoptada"]
    estado_encontrado = None

    for opcion in estados_validos:
        if estado.strip().casefold() == opcion.casefold():
            estado_encontrado = opcion

    if estado_encontrado is None:
        messagebox.showerror(
            "Estado no válido",
            "Usa Disponible, En proceso o Adoptada."
        )
        return

    mascota.cambiar_estado(estado_encontrado)
    messagebox.showinfo("Estado", "Se actualizó el estado.")
    mostrar_catalogo()


def agregar_mascota():
    """Pide los datos necesarios y agrega una mascota al catálogo."""
    tipo = simpledialog.askstring(
        "Agregar mascota",
        "¿Es perro o gato? Escribe Perro o Gato:"
    )

    if tipo is None:
        return

    tipo = tipo.strip().casefold()

    if tipo not in ["perro", "gato"]:
        messagebox.showerror("Error", "Escribe Perro o Gato.")
        return

    nombre = simpledialog.askstring("Agregar mascota", "Nombre:")
    if not nombre:
        return

    edad_texto = simpledialog.askstring("Agregar mascota", "Edad en años:")
    try:
        edad = int(edad_texto)
        if edad < 0:
            raise ValueError
    except (ValueError, TypeError):
        messagebox.showerror("Error", "La edad debe ser un número válido.")
        return

    descripcion = simpledialog.askstring(
        "Agregar mascota", "Descripción:"
    )
    if not descripcion:
        descripcion = "Sin descripción."

    # La foto es opcional. Elige una imagen PNG o GIF.
    ruta = filedialog.askopenfilename(
        title="Elige una foto (opcional)",
        filetypes=[("Imágenes PNG o GIF", "*.png *.gif")]
    )

    imagen = Path(ruta) if ruta else None

    if tipo == "perro":
        tamano = simpledialog.askstring(
            "Agregar perro", "Tamaño (pequeño, mediano o grande):"
        )
        if not tamano:
            tamano = "no especificado"

        nueva_mascota = Perro(
            nombre, edad, descripcion, imagen, tamano
        )
    else:
        color = simpledialog.askstring("Agregar gato", "Color:")
        if not color:
            color = "no especificado"

        nueva_mascota = Gato(
            nombre, edad, descripcion, imagen, color
        )

    mascotas.append(nueva_mascota)
    messagebox.showinfo("Catálogo", "La mascota fue agregada.")
    mostrar_catalogo()


def ver_reporte():
    """Cuenta mascotas por tipo, estado y cantidad de favoritas."""
    cantidad_perros = 0
    cantidad_gatos = 0
    disponibles = 0
    en_proceso = 0
    adoptadas = 0

    # CICLO WHILE: cuenta los datos del catálogo.
    indice = 0
    while indice < len(mascotas):
        mascota = mascotas[indice]

        if isinstance(mascota, Perro):
            cantidad_perros += 1
        elif isinstance(mascota, Gato):
            cantidad_gatos += 1

        if mascota.obtener_estado() == "Disponible":
            disponibles += 1
        elif mascota.obtener_estado() == "En proceso":
            en_proceso += 1
        elif mascota.obtener_estado() == "Adoptada":
            adoptadas += 1

        indice += 1

    texto = (
        f"Total de mascotas: {len(mascotas)}\n"
        f"Perros: {cantidad_perros}\n"
        f"Gatos: {cantidad_gatos}\n"
        f"Favoritas: {len(favoritas)}\n\n"
        f"Disponibles: {disponibles}\n"
        f"En proceso: {en_proceso}\n"
        f"Adoptadas: {adoptadas}"
    )

    messagebox.showinfo("Reporte del catálogo", texto)


# Opciones del programa, organizadas en dos filas.
marco_opciones = tk.Frame(ventana)
marco_opciones.pack(pady=8)

tk.Button(
    marco_opciones,
    text="1. Mostrar mascotas",
    command=mostrar_catalogo,
    width=19
).grid(row=0, column=0, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="2. Buscar mascota",
    command=buscar_por_nombre,
    width=19
).grid(row=0, column=1, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="3. Agregar a favoritos",
    command=agregar_a_favoritos,
    width=19
).grid(row=0, column=2, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="4. Mostrar favoritos",
    command=mostrar_favoritas,
    width=19
).grid(row=0, column=3, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="5. Cambiar estado",
    command=cambiar_estado_adopcion,
    width=19
).grid(row=1, column=0, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="6. Agregar mascota",
    command=agregar_mascota,
    width=19
).grid(row=1, column=1, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="7. Ver reporte",
    command=ver_reporte,
    width=19
).grid(row=1, column=2, padx=4, pady=4)

tk.Button(
    marco_opciones,
    text="0. Salir",
    command=ventana.destroy,
    width=19
).grid(row=1, column=3, padx=4, pady=4)


# Muestra el catálogo al iniciar.
mostrar_catalogo()

# Mantiene abierta la ventana y responde a los clics.
ventana.mainloop()