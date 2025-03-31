biblioteca = []
usuarios = {}

def agregar_libro(titulo, autor, genero, copias):
    libro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'copias_disponibles': copias,
        'copias_totales': copias
    }
    biblioteca.append(libro)
    print(f"Libro '{titulo}' agregado correctamente")


def buscar_libros(**criterios):
    resultados = []
    for libro in biblioteca:
        encontrado = True
        for clave, valor in criterios.items():
            if clave in libro and libro[clave].lower() != valor.lower():
                encontrado = False
                break
        if encontrado:
            resultados.append(libro)

    if not resultados:
        print("No se encontraron libros")
    return resultados


def generar_libros_disponibles():
    for libro in biblioteca:
        if libro['copias_disponibles'] > 0:
            yield libro


def mostrar_libros_disponibles():
    print("\n--- Libros Disponibles ---")
    disponibles = list(generar_libros_disponibles())
    if not disponibles:
        print("No hay libros disponibles en este momento.")
    else:
        for i, libro in enumerate(disponibles, 1):
            print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['genero']})")
            print(f"   Copias disponibles: {libro['copias_disponibles']}/{libro['copias_totales']}")


def prestar_libro(usuario_id, titulo):
    if usuario_id not in usuarios:
        usuarios[usuario_id] = {'libros_prestados': []}

    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            if libro['copias_disponibles'] > 0:
                libro['copias_disponibles'] -= 1
                usuarios[usuario_id]['libros_prestados'].append(libro['titulo'])
                print(f"Libro '{libro['titulo']}' prestado a usuario {usuario_id}.")
                return
            else:
                print(f"No hay copias disponibles de '{libro['titulo']}'.")
                return
    print(f"Libro '{titulo}' no encontrado en la biblioteca.")


def devolver_libro(usuario_id, titulo):
    if usuario_id not in usuarios:
        print(f"Usuario {usuario_id} no encontrado.")
        return

    if titulo not in usuarios[usuario_id]['libros_prestados']:
        print(f"El usuario {usuario_id} no tiene el libro")
        return

    for libro in biblioteca:
        if libro['titulo'].lower() == titulo.lower():
            libro['copias_disponibles'] += 1
            usuarios[usuario_id]['libros_prestados'].remove(titulo)
            print(f"Libro '{titulo}' devuelto correctamente.")
            return

    print(f"Libro '{titulo}' no encontrado.")

if __name__ == "__main__":
    agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 5)
    agregar_libro("1984", "George Orwell", "Ciencia ficción", 3)
    agregar_libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", 7)
    agregar_libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 4)
    while True:
        print("1. Agregar libro")
        print("2. Buscar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Mostrar libros disponibles")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                titulo = input("Título del libro: ")
                autor = input("Autor del libro: ")
                genero = input("Género del libro: ")
                copias = int(input("Número de copias: "))
                agregar_libro(titulo, autor, genero, copias)
            case 2:
                print("\nBuscar por:")
                print("1. Título")
                print("2. Autor")
                print("3. Género")
                busqueda = int(input("Seleccione cómo desea buscar: "))
                match busqueda:
                    case 1:
                        titulo = input("Título a buscar: ")
                        resultados = buscar_libros(titulo=titulo)
                    case 2:
                        autor = input("Autor a buscar: ")
                        resultados = buscar_libros(autor=autor)
                    case 3:
                        genero = input("Género a buscar: ")
                        resultados = buscar_libros(genero=genero)
                    case _:
                        print("Opcion no valida")

                if resultados:
                    print("\n--- Resultados de la búsqueda ---")
                    for i, libro in enumerate(resultados, 1):
                        print(f"{i}. {libro['titulo']} - {libro['autor']} ({libro['genero']})")
                        print(f"   Disponibles: {libro['copias_disponibles']}/{libro['copias_totales']}")

            case 3:
                usuario_id = input("usuario:5 ")
                titulo = input("Título del libro a prestar: ")
                prestar_libro(usuario_id, titulo)

            case 4:
                usuario_id = input("ID del usuario: ")
                titulo = input("Título del libro a devolver: ")
                devolver_libro(usuario_id, titulo)
            case 5:
                mostrar_libros_disponibles()

            case 6:
                print("Saliendo")
                break

            case _:
                print("Opción no válida.")

