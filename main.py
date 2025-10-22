import os, time
os.system ("cls")

catalogo_productos = [
    {
        "codigo": "C001",
        "tipo": "cómic",
        "editorial": "DC Comics",
        "genero": "Acción",
        "alineacion": "Héroe",
        "personaje_equipo": "Batman",
        "titulo": "Batman: Año Uno"
    },
    {
        "codigo": "C002",
        "tipo": "cómic",
        "editorial": "Marvel Comics",
        "genero": "Aventura",
        "alineacion": "Héroe",
        "personaje_equipo": "Spider-Man",
        "titulo": "The Amazing Spider-Man #1"
    },
    {
        "codigo": "C003",
        "tipo": "cómic",
        "editorial": "DC Comics",
        "genero": "Fantasía",
        "alineacion": "Héroe",
        "personaje_equipo": "Wonder Woman",
        "titulo": "Wonder Woman: Renacimiento"
    },
    {
        "codigo": "C004",
        "tipo": "cómic",
        "editorial": "Marvel Comics",
        "genero": "Ciencia Ficción",
        "alineacion": "Héroes",
        "personaje_equipo": "Los Vengadores",
        "titulo": "Avengers: La Era de Ultrón"
    },
    {
        "codigo": "M001",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Acción",
        "alineacion": "Héroe",
        "personaje_equipo": "Goku",
        "titulo": "Dragon Ball Vol. 1"
    },
    {
        "codigo": "M002",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Aventura",
        "alineacion": "Héroes",
        "personaje_equipo": "Luffy y Sombrero de Paja",
        "titulo": "One Piece Vol. 1"
    },
    {
        "codigo": "M003",
        "tipo": "manga",
        "editorial": "Kodansha",
        "genero": "Acción",
        "alineacion": "Neutral",
        "personaje_equipo": "Eren Yeager",
        "titulo": "Attack on Titan Vol. 1"
    },
    {
        "codigo": "M004",
        "tipo": "manga",
        "editorial": "Shueisha",
        "genero": "Aventura",
        "alineacion": "Héroe",
        "personaje_equipo": "Naruto Uzumaki",
        "titulo": "Naruto Vol. 1"
    },
    {
        "codigo": "C005",
        "tipo": "cómic",
        "editorial": "Image Comics",
        "genero": "Acción / Fantasía",
        "alineacion": "Anti-héroe",
        "personaje_equipo": "Spawn",
        "titulo": "Spawn #1"
    },
    {
        "codigo": "M005",
        "tipo": "manga",
        "editorial": "VIZ Media",
        "genero": "Acción / Misterio",
        "alineacion": "Neutral",
        "personaje_equipo": "Light Yagami",
        "titulo": "Death Note Vol. 1"
    }

]

def menu():
    print("=== Catálogo de Cómics y Manga ===")
    print("1. Ver el catalogo de productos")
    print("2. Buscar por código y eliminar producto")
    print("3. Actualizar información de un producto")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    return opcion

def mostrar_catalogo():
    print("\n--- Catálogo de Productos ---")
    for producto in catalogo_productos:
        print(f"Código: {producto['codigo']}, Título: {producto['titulo']}, Tipo: {producto['tipo']}, Editorial: {producto['editorial']}, Género: {producto['genero']}, Alineación: {producto['alineacion']}, Personaje/Equipo: {producto['personaje_equipo']}")
    print("-----------------------------\n")
    input("Presione Enter para continuar...")  





    
