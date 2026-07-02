INICIO

    // 1. DEFINIR VARIABLES GLOBALES (Nuestra memoria de datos)
    socios = Lista vacía  // Guardará {dni, nombre, membresia, cuota_al_dia, asistencias}
    actividades = Lista con ["Spinning", "Crossfit", "Musculación"]
    concurrencia_total = 0 // Contador para estadísticas

    // 2. FUNCIÓN: VALIDAR MENÚ PRINCIPAL
    PROCESO menu_principal()
        REPETIR
            MOSTRAR "--- GIMNASIO - MENÚ ---"
            MOSTRAR "1. Registrar Socio"
            MOSTRAR "2. Controlar Cuota"
            MOSTRAR "3. Inscribir a Actividad"
            MOSTRAR "4. Registrar Asistencia"
            MOSTRAR "5. Ver Estadísticas"
            MOSTRAR "6. Salir"
            LEER opcion

            SI opcion == "1" ENTONCES registrar_socio()
            SINO SI opcion == "2" ENTONCES controlar_cuota()
            SINO SI opcion == "3" ENTONCES inscribir_actividad()
            SINO SI opcion == "4" ENTONCES registrar_asistencia()
            SINO SI opcion == "5" ENTONCES ver_estadisticas()
            SINO SI opcion == "6" ENTONCES MOSTRAR "Cerrando sistema..."
            SINO MOSTRAR "Opción inválida, intente de nuevo."
        HASTA QUE opcion == "6"
    FIN PROCESO

    // 3. FUNCIÓN: REGISTRAR SOCIO (Con validaciones)
    PROCESO registrar_socio()
        MOSTRAR "Ingrese el DNI del nuevo socio:"
        REPETIR
            LEER dni_ingresado
            SI dni_ingresado NO es un número ENTONCES
                MOSTRAR "Error. El DNI debe contener solo números. Intente de nuevo:"
        HASTA QUE dni_ingresado sea un número válido

        // Validar que no exista
        SI buscar_socio_por_dni(dni_ingresado) YA EXISTE ENTONCES
            MOSTRAR "Este socio ya está registrado."
            RETORNAR
        FIN SI

        MOSTRAR "Ingrese Nombre y Apellido:"
        LEER nombre_ingresado

        MOSTRAR "Seleccione Membresía (1. Estándar / 2. VIP / 3. Promo):"
        LEER tipo_promo

        // Creamos el registro del socio y lo guardamos
        nuevo_socio = {
            dni: dni_ingresado,
            nombre: nombre_ingresado,
            membresia: tipo_promo,
            cuota_al_dia: VERDADERO, // Arranca al día
            asistencias: 0
        }
        AGREGAR nuevo_socio A LA LISTA socios
        MOSTRAR "Socio registrado con éxito."
    FIN PROCESO

    // 4. FUNCIÓN: REGISTRAR ASISTENCIA
    PROCESO registrar_asistencia()
        MOSTRAR "Ingrese el DNI del socio:"
        LEER dni_ingresado
        
        socio_encontrado = buscar_socio_por_dni(dni_ingresado)

        SI socio_encontrado NO EXISTE ENTONCES
            MOSTRAR "Socio no encontrado."
        SINO SI socio_encontrado.cuota_al_dia == FALSO ENTONCES
            MOSTRAR "Acceso denegado: El socio tiene deuda."
        SINO
            MOSTRAR "Acceso permitido. ¡Buen entrenamiento, " + socio_encontrado.nombre + "!"
            socio_encontrado.asistencias = socio_encontrado.asistencias + 1
            concurrencia_total = concurrencia_total + 1
        FIN SI
    FIN PROCESO

    // 5. FUNCIÓN: VER ESTADÍSTICAS
    PROCESO ver_estadisticas()
        MOSTRAR "--- ESTADÍSTICAS GENERALES ---"
        MOSTRAR "Cantidad total de socios registrados: " + CONTAR(socios)
        MOSTRAR "Accesos totales al gimnasio hoy: " + concurrencia_total
    FIN PROCESO

    // 6. FUNCIÓN AUXILIAR (Para buscar socios)
    PROCESO buscar_socio_por_dni(dni_a_buscar)
        PARA CADA socio EN socios HACER
            SI socio.dni == dni_a_buscar ENTONCES
                RETORNAR socio // Deuelve los datos del socio si lo encuentra
            FIN SI
        FIN PARA
        RETORNAR NADA // Si recorrió todo y no estaba
    FIN PROCESO

    // --- EL PROGRAMA ARRANCA ACÁ ---
    menu_principal()

FIN