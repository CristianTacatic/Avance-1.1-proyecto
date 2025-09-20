ef pedir_numero_estudiantes():
    """Pide al usuario la cantidad de estudiantes (mayor que 0)."""
    n = 0
    while n <= 0:
        try:
            n = int(input("¿Cuántos estudiantes? "))
            if n <= 0:
                print("Tiene que ser más que 0")
        except:
            print("¡Pon un número válido!")
    return n


def ingresar_datos(n):
    """Registra los nombres y notas de los estudiantes en listas."""
    nombres = []
    notas = []
    aprobados = 0
    reprobados = 0

    for i in range(n):
        print(f"\n--- Estudiante {i+1} ---")
        nombre = input("Nombre: ")
        nombres.append(nombre)

        nota_valida = False
        while not nota_valida:
            try:
                nota = float(input("Nota (0-100): "))
                if 0 <= nota <= 100:
                    notas.append(nota)
                    nota_valida = True
                    if nota >= 60:
                        aprobados += 1
                    else:
                        reprobados += 1
                else:
                    print("La nota debe estar entre 0 y 100")
            except:
                print("Eso no es un número")
    return nombres, notas, aprobados, reprobados


def mostrar_resumen(n, aprobados, reprobados):
    """Muestra el resumen de estudiantes aprobados y reprobados."""
    print("\n--- RESULTADOS ---")
    print(f"Total: {n}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")


def buscar_estudiante(nombres, notas, aprobados, reprobados):
    """Permite buscar un estudiante y actualizar su nota si es necesario."""
    nombre_buscar = input("\nNombre a buscar: ")
    encontrado = False

    for i in range(len(nombres)):
        if nombres[i] == nombre_buscar:
            print(f"Encontrado: {nombres[i]} - Nota: {notas[i]}")
            estado = "Aprobado" if notas[i] >= 60 else "Reprobado"
            print("Estado:", estado)
            encontrado = True

            cambiar = input("¿Cambiar nota? (si/no): ")
            if cambiar.lower() == "si":
                try:
                    nueva_nota = float(input("Nueva nota: "))
                    if 0 <= nueva_nota <= 100:
                        if notas[i] < 60 and nueva_nota >= 60:
                            aprobados += 1
                            reprobados -= 1
                        elif notas[i] >= 60 and nueva_nota < 60:
                            aprobados -= 1
                            reprobados += 1
                        notas[i] = nueva_nota
                        print("Nota cambiada con éxito")
                    else:
                        print("Nota no válida")
                except:
                    print("Error, ingrese un número")
            break

    if not encontrado:
        print("No se encontró el estudiante")

    return aprobados, reprobados


def mostrar_todos(nombres, notas):
    """Muestra todos los estudiantes con su estado (aprobado/reprobado)."""
    print("\n--- TODOS LOS ESTUDIANTES ---")
    for i in range(len(nombres)):
        estado = "Aprobado" if notas[i] >= 60 else "Reprobado"
        print(f"{nombres[i]}: {notas[i]} - {estado}")


def calcular_promedio(notas):
    """Calcula y muestra el promedio del grupo y su desempeño general."""
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
        print(f"\nPromedio del grupo: {promedio:.2f}")

        if promedio > 80:
            print("Muy bien grupo!")
        elif promedio > 70:
            print("Bien grupo")
        elif promedio >= 60:
            print("Aprobado justo")
        else:
            print("Grupo reprobado")


def main():
    print("SISTEMA DE NOTAS ESCOLAR")
    print("-----------------------")

    n = pedir_numero_estudiantes()
    nombres, notas, aprobados, reprobados = ingresar_datos(n)

    mostrar_resumen(n, aprobados, reprobados)

    buscar = input("\n¿Quieres buscar un estudiante? (si/no): ")
    if buscar.lower() == "si":
        aprobados, reprobados = buscar_estudiante(nombres, notas, aprobados, reprobados)

    mostrar_todos(nombres, notas)
    calcular_promedio(notas)


# Ejecutar programa
if __name__ == "__main__":
    main()
