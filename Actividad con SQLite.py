import sqlite3

DB_NAME = "estudiantes.db"

class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                carrera TEXT NOT NULL,
                promedio REAL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO estudiantes (nombre, carrera, promedio) VALUES (?, ?, ?)",
                (self.nombre, self.carrera, self.promedio)
            )
        print(f"Estudiante '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes")
            filas = cur.fetchall()
            if not filas:
                print("No hay estudiantes registrados.")
                return
            print("\n--- LISTADO DE ESTUDIANTES ---")
            for f in filas:
                print(f"ID: {f['id_estudiante']} | Nombre: {f['nombre']} | Carrera: {f['carrera']} | Promedio: {f['promedio']}")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del estudiante a modificar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes WHERE id_estudiante = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el estudiante.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            promedio = input(f"Nuevo promedio [{fila['promedio']}]: ") or fila['promedio']
            conn.execute("UPDATE estudiantes SET nombre=?, carrera=?, promedio=? WHERE id_estudiante=?",
                         (nombre, carrera, promedio, ide))
        print("Estudiante actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del estudiante a eliminar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("DELETE FROM estudiantes WHERE id_estudiante = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el estudiante.")
            else:
                print("Estudiante eliminado con éxito.")

    @staticmethod
    def promedio_general():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT AVG(promedio) AS prom FROM estudiantes")
            prom = cur.fetchone()["prom"]
            if prom:
                print(f"\nPromedio general: {prom:.2f}")
            else:
                print("No hay datos para calcular el promedio.")

class Curso:
    def __init__(self, nombre, horario, creditos):
        self.nombre = nombre
        self.horario = horario
        self.creditos = creditos

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cursos (
                id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                horario TEXT NOT NULL,
                creditos REAL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO cursos (nombre, horario, creditos) VALUES (?, ?, ?)",
                (self.nombre, self.horario, self.creditos)
            )
        print(f"Curso '{self.nombre}' guardado con éxito.")

    @staticmethod
    def listar():
        with Curso._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos")
            filas = cur.fetchall()
            if not filas:
                print("No hay cursos registrados.")
                return
            print("\n--- LISTADO DE CUROS ---")
            for f in filas:
                print(f"ID: {f['id_curso']} | Nombre: {f['nombre']} | Horario: {f['horario']} | Creditos: {f['creditos']}")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del curos a modificar: ")
        with Curso._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos WHERE id_curso = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el curso.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            horario = input(f"Nuevo horario [{fila['horario']}]: ") or fila['horario']
            creditos = input(f"Nuevos creditos [{fila['creditos']}]: ") or fila['creditos']
            conn.execute("UPDATE cursos SET nombre=?, horario=?, creditos=? WHERE id_curso=?",
                         (nombre, horario, creditos, ide))
        print("Curso actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del curso a eliminar: ")
        with Curso._conn() as conn:
            cur = conn.execute("DELETE FROM cursos WHERE id_curso = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el curso.")
            else:
                print("Curos eliminado con éxito.")






# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\n===== MENÚ DE ESTUDIANTES =====")
        print("1. Ingresar estudiante")
        print("2. Listar estudiantes")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
        print("5. Promedio general")
        print("\n===== CURSOS =====")
        print("6. Ingresar Curos")
        print("7. Listar Curos")
        print("8. Modificar Cursos")
        print("9. Eliminar Cursos")

        print("10. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
            promedio = float(input("Promedio: "))
            e = Estudiante(nombre, carrera, promedio)
            e.guardar()
        elif opcion == "2":
            Estudiante.listar()
        elif opcion == "3":
            Estudiante.modificar()
        elif opcion == "4":
            Estudiante.eliminar()
        elif opcion == "5":
            Estudiante.promedio_general()

        if opcion == "6":
            nombre = input("Nombre: ")
            horario = input("Horario: ")
            creditos = float(input("creditos: "))
            c = Curso(nombre, horario, creditos)
            c.guardar()
        elif opcion == "7":
            Curso.listar()
        elif opcion == "8":
            Curso.modificar()
        elif opcion == "9":
            Curso.eliminar()

        elif opcion == "10":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()