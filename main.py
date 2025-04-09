print("¡Bienvenido al gestor de tareas que me costo mucho hacer!");


print("¿Qué quieres hacer?")
print("1. Agregar tarea")
print("2. Ver tareas")
opcion = input("Escribe 1 o 2: ")

if opcion == "1":
    with open("tareas.txt", "a") as archivo:
        tarea = input("Escribe una nueva tarea: ")
        archivo.write(tarea + "\n")
        print("Tarea guardada.")
elif opcion == "2":
    print("\nTus tareas:")
    with open("tareas.txt", "r") as archivo:
        print(archivo.read())
else:
    print("Opción no válida.")
