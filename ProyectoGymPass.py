import datetime
import json  # <Importamos la librería para manejar archivos
class Socio:
    def __init__(self, dni, nombre, tipo_membresia, cuota_al_dia=True, actividades_inscriptas=None):
        self.dni = dni
        self.nombre = nombre
        self.tipo_membresia = tipo_membresia
        self.cuota_al_dia = cuota_al_dia
        # Si no le pasamos actividades, empieza con una lista vacía
        self.actividades_inscriptas = actividades_inscriptas if actividades_inscriptas else []

    def __str__(self):
        estado = "Al día" if self.cuota_al_dia else "Deudor"
        return f"DNI: {self.dni} | {self.nombre} | Pase: {self.tipo_membresia.upper()} | Estado: {estado}"

class Gimnasio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.socios = {}       
        self.asistencias = []        
        self.membresias = {
            "basico": ["musculacion"],
            "platino": ["musculacion", "spinning"],
            "pase libre": ["musculacion", "spinning", "crossfit"]
        }
        self.cupos_actividades = {
            "musculacion": 50,
            "spinning": 2,      
            "crossfit": 20
        }
        # Al crear el gimnasio, intentamos cargar los datos guardados automáticamente
        self.cargar_datos_desde_bloc()
    #FUNCIÓN: GUARDAR EN BLOC DE NOTAS
    def guardar_datos_en_bloc(self):
        # Convertimos nuestro diccionario de objetos Socio en un diccionario de texto común
        datos_a_guardar = {}
        for dni, socio in self.socios.items():
            datos_a_guardar[dni] = {
                "nombre": socio.nombre,
                "tipo_membresia": socio.tipo_membresia,
                "cuota_al_dia": socio.cuota_al_dia,
                "actividades_inscriptas": socio.actividades_inscriptas
                }
                # Abrimos (o creamos) el archivo 'base_datos.txt' y escribimos el JSON estructurado
        with open("base_datos.txt", "w", encoding="utf-8") as archivo:
            json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)
        print("\n[Data] Datos guardados en 'base_datos.txt'.")
    # --- NUEVA FUNCIÓN: CARGAR DESDE BLOC DE NOTAS ---
    def cargar_datos_desde_bloc(self):
        try:
            # Intentamos abrir el archivo de texto
            with open("base_datos.txt", "r", encoding="utf-8") as archivo:
                datos_cargados = json.load(archivo)
                                # Reconstruimos los objetos Socio a partir del texto del archivo
                for dni, datos in datos_cargados.items():
                    nuevo_socio = Socio(
                        dni=dni,
                        nombre=datos["nombre"],
                        tipo_membresia=datos["tipo_membresia"],
                        cuota_al_dia=datos["cuota_al_dia"],
                        actividades_inscriptas=datos["actividades_inscriptas"]
                    )
                    self.socios[dni] = nuevo_socio
            print("\n[Data] ¡Datos cargados con éxito desde el Bloc de Notas!")
        except FileNotFoundError:
            # Si el archivo no existe todavía (primera vez que corre), no pasa nada
            print("\n[Data] No se encontró un archivo previo. Iniciando base de datos vacía.")

    # --- GESTIÓN DE SOCIOS (Modificados para guardar al terminar) ---
    def registrar_socio(self, dni, nombre, tipo_membresia):
        if dni in self.socios:
            print(f"\n[!] El socio con DNI {dni} ya existe.")
            return
        if tipo_membresia.lower() not in self.membresias:
            print(f"\n[!] La membresía '{tipo_membresia}' no existe.")
            return
        self.socios[dni] = Socio(dni, nombre, tipo_membresia.lower())
        print(f"\n[✓] Socio {nombre} registrado con éxito.")
        self.guardar_datos_en_bloc() # <--- Guardamos el cambio

    def registrar_pago(self, dni):
        if dni in self.socios:
            self.socios[dni].cuota_al_dia = True
            print(f"\n[✓] Pago acreditado para {self.socios[dni].nombre}.")
            self.guardar_datos_en_bloc() # <--- Guardamos el cambio
        else:
            print("\n[!] Socio no encontrado.")

    def marcar_deudor(self, dni):
        if dni in self.socios:
            self.socios[dni].cuota_al_dia = False
            print(f"\n[!] {self.socios[dni].nombre} ha sido marcado como DEUDOR.")
            self.guardar_datos_en_bloc() # <--- Guardamos el cambio
        else:
            print("\n[!] Socio no encontrado.")

    def inscribir_a_actividad(self, dni, actividad):
        socio = self.socios.get(dni)
        actividad = actividad.lower()
        if not socio or actividad not in self.cupos_actividades or not socio.cuota_al_dia:
            print("\n[!] Error en la inscripción. Verifique datos o estado de deuda.")
            return
        if actividad in socio.actividades_inscriptas:
            print(f"\n[!] El socio ya está inscrito en {actividad}.")
            return
        socio.actividades_inscriptas.append(actividad)
        print(f"\n[✓] ¡Inscripción exitosa de {socio.nombre} a {actividad}!")
        self.guardar_datos_en_bloc() #Guardamos el cambio

    def registrar_asistencia(self, dni, actividad):
        socio = self.socios.get(dni)
        actividad = actividad.lower()
        if not socio or not socio.cuota_al_dia or actividad not in socio.actividades_inscriptas:
            print("\n[X] ACCESO DENEGADO.")
            return
        hoy = datetime.date.today()
        self.asistencias.append((hoy, dni, actividad))
        print(f"\n[✓] ACCESO PERMITIDO para {socio.nombre}.")

    def mostrar_estadisticas(self):
        print(f"\n====== ESTADÍSTICAS ======")
        print(f"Total de socios: {len(self.socios)}")

    def listar_socios(self):
        if not self.socios:
            print("\nNo hay socios en el sistema.")
            return
        print("\n--- LISTADO GENERAL DE SOCIOS ---")
        for s in self.socios.values():
            print(s)
#Menu Del Programa 
def menu():
    gym = Gimnasio("Serpiente-Gym") 
    while True:
        print("\n" + "="*35)
        print(f"  SISTEMA CON BLOC DE NOTAS: {gym.nombre.upper()}")
        print("="*35)
        print("1. Registrar nuevo Socio")
        print("2. Registrar pago de cuota / Marcar deuda")
        print("3. Inscribir socio a una Actividad")
        print("4. Control de Acceso (Marcar Asistencia)")
        print("5. Ver panel de Estadísticas")
        print("6. Listar todos los socios")
        print("7. Salir")
        opcion = input("\nSeleccione una opción (1-7): ").strip()
        if opcion == "1":
            dni = input("DNI del socio: ").strip()
            nombre = input("Nombre y Apellido: ").strip()
            tipo_m = input("Seleccione pase (Basico / Platino / Pase Libre): ").strip()
            if dni and nombre and tipo_m:
                gym.registrar_socio(dni, nombre, tipo_m)
        elif opcion == "2":
            dni = input("DNI del socio: ").strip()
            print("1. Registrar Pago\n2. Registrar Deuda")
            sub_op = input("Opción: ").strip()
            if sub_op == "1":
                gym.registrar_pago(dni)
            elif sub_op == "2":
                gym.marcar_deudor(dni)
        elif opcion == "3":
            dni = input("DNI del socio: ").strip()
            act = input("Nombre de la actividad: ").strip()
            gym.inscribir_a_actividad(dni, act)
        elif opcion == "4":
            dni = input("Ingrese DNI: ").strip()
            act = input("¿A qué actividad ingresa?: ").strip()
            gym.registrar_asistencia(dni, act)
        elif opcion == "5":
            gym.mostrar_estadisticas()
        elif opcion == "6":
            gym.listar_socios()
        elif opcion == "7":
            print(f"\n¡Sistema cerrado! Datos a salvo.")
            break
        else:
            print("\n[!] Opción no válida.")

if __name__ == "__main__":
    menu()