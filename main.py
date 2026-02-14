import db

def pedir_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida. Debe ser un número.")


def mostrar_tareas():
    tareas = db.get_tareas()

    if not tareas:
        print("No hay tareas...")
        return

    for tarea in tareas:
        estado = "[X]" if tarea["hecha"] else "[ ]"
        print(f"{estado} {tarea['id']} - {tarea['texto']}")


db.init_db()

while True:
    opcion = pedir_int(
        "\n--- TO DO LIST ---\n"
        "1) Ver todas las tareas\n"
        "2) Ver tareas pendientes\n"
        "3) Ver tareas hechas\n"
        "4) Agregar tarea\n"
        "5) Marcar tarea como hecha\n"
        "6) Editar tarea\n"
        "7) Eliminar tarea\n"
        "8) Buscar tarea\n"
        "9) Salir\n"
        "Opcion: "
    )

    if opcion is None:
        continue

    if opcion == 1:
        mostrar_tareas(db.get_tareas())

    elif opcion == 2:
        mostrar_tareas(db.get_tareas_pendientes())

    elif opcion == 3:
        mostrar_tareas(db.get_tareas_hechas())

    elif opcion == 4:
        texto = input("Nueva tarea: ")
        if db.agregar_tarea(texto):
            print("Tarea agregada.")
        else:
            print("Texto inválido.")

    elif opcion == 5:
        id = pedir_int("ID de la tarea a marcar como hecha: ")
        if id is not None:
            if db.terminar_tarea(id):
                print("Tarea marcada como hecha.")
            else:
                print("No existe una tarea con ese ID.")

    elif opcion == 6:
        id = pedir_int("ID de la tarea a editar: ")
        if id is not None:
            nuevo_texto = input("Nuevo texto: ")
            if db.editar_tarea(id, nuevo_texto):
                print("Tarea editada.")
            else:
                print("No se pudo editar (ID inexistente o texto inválido).")

    elif opcion == 7:
        id = pedir_int("ID de la tarea a eliminar: ")
        if id is not None:
            if db.eliminar_tarea(id):
                print("Tarea eliminada.")
            else:
                print("No existe una tarea con ese ID.")

    elif opcion == 8:
        palabra = input("Buscar palabra: ")
        resultados = db.buscar_tareas(palabra)
        mostrar_tareas(resultados)

    elif opcion == 9:
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")


