

image fondo_inicio = "main_01.jpg"

# name of the character.

define m = Character("Marina Lee", color="#dfcdd6")
define b = Character("Capt. Bob Williams", color="#546ace")
define l = Character("Laura Esteban", color="#d4373f")
define y = Character("[nombre_personaje] [[Tú]", color="#1d7c3a")
define c = Character("Charles Grey", color="#363131")
define e = Character("Erika Smith", color="#363131")
define t = Character("Tomás Greenson", color="#363131")
define i = Character("Ingrid Sversson", color="#363131")


#define el player id
default player_id = ""
define player_name = ""
define player_lastname = ""
define player_ids = ["Jugador1", "jugador2", "Jugador3"]  # Lista de IDs válidos para android
default input_id = ""  # Variable para almacenar el ID ingresado por el jugador

# Define images position
transform left:
    xalign 0.15
    yalign 1.25
transform right:
    xalign 0.85 
    yalign 1.25  
transform center:
    xalign 0.5 
    yalign 1.25  
transform leftgr:
    xalign 0.10
    yalign -0.25 
transform rightgr:
    xalign 0.90 
    yalign -0.25  
transform Stuff_1:
    xalign 0.95 
    yalign 1
transform moveinleft:
    xalign -1.0
    ypos posicion_pop_up_y
    linear 1.0 xalign posicion_pop_up_x

# Variables de genero
default genero = "Femenino"
default e = "a"
default le = "la"

# Define the scaled background image
image bg inicio = im.Scale("main_01.jpg", config.screen_width, config.screen_height)
image bg beach storm = im.Scale("bg beach storm.jpg", config.screen_width, config.screen_height)
image bg beach storm1 = im.Scale("bg beach storm parte1.jpg", config.screen_width, config.screen_height)
image bg jungle1 1 = im.Scale("bg jungle parte1_1.jpg", config.screen_width, config.screen_height)
image bg jungle1 blood = im.Scale("bg jungle parte1_2.jpg", config.screen_width, config.screen_height)
image bg jungle1 blood zoom = im.Scale("bg jungle parte1_2_zoom.jpg", config.screen_width, config.screen_height)
image bg jungle claro = im.Scale("bg jungle parte1_3_a.jpg", config.screen_width, config.screen_height)
image bg jungle herida = im.Scale("bg jungle parte1_herida.jpg", config.screen_width, config.screen_height)
image bg jungle herida zoom = im.Scale("bg jungle parte1_herida_zoom.jpg", config.screen_width, config.screen_height)
image bg jungle herida cargar = im.Scale("bg jungle parte1_herida_cargar.jpg", config.screen_width, config.screen_height)
image bg jungle cave = im.Scale("bg jungle cave.jpg", config.screen_width, config.screen_height)
image bg jungle hut = im.Scale("bg jungle hut.jpg", config.screen_width, config.screen_height)
image bg jungle hill = im.Scale("bg jungle hill.jpg", config.screen_width, config.screen_height)
image bg beach storm 2 = im.Scale("bg beach storm 2.jpg", config.screen_width, config.screen_height)
image bg jungle explore 1 = im.Scale("bg jungle explore 1.jpg", config.screen_width, config.screen_height)
image bg jungle trail = im.Scale("bg jungle trail.jpg", config.screen_width, config.screen_height)
image bg jungle fruit = im.Scale("bg jungle fruit.jpg", config.screen_width, config.screen_height)
image bg jungle clearing  = im.Scale("bg jungle clearing.jpg", config.screen_width, config.screen_height)
image bg jungle night stars  = im.Scale("bg jungle night stars.jpg", config.screen_width, config.screen_height)

image bg comic 1 = im.Scale("comic_1.jpg", config.screen_width, config.screen_height)

# Define the character image
image marina hablando = "Marina_hablando.png"
image marina gr hablando = "Marina_hablando_gr.png"
image marina preocupada = "Marina_preocupada.png"
image marina gr preocupada = "Marina_preocupada_gr.png"
image marina sonriendo = "Marina_sonriendo.png"
image marina gr sonriendo = "Marina_sonriendo_gr.png"
image marina triste ="Marina_triste.png"
image marina gr triste ="Marina_triste_gr.png"

image bob saludando sucio = "Bob_saludando_sonriente.png"
image bob gr serio sucio = "Bob_parado_serio_gr.png"
image bob parado serio = "Bob_parado_serio.png"
image bob parado enojado = "Bob_parado_enojado.png"
image bob gr parado enojado = "Bob_parado_enojado_gr.png"
image bob gr parado hablando = "Bob_parado_hablando_gr.png"
image bob parado hablando = "Bob_parado_hablando.png"
image bob pensando = "Bob_pensando.png"
image bob gr pensando = "Bob_pensando_gr.png"

image laura gr seria = "Laura_parada_seria_gr.png"
image laura gr enojada = "Laura_discutiendo_gr.png"
image laura seria = "Laura_parada_seria.png"
image laura enojada = "Laura_discutiendo.png"
image laura hablando = "Laura_hablando.png"
image laura gr hablando = "Laura_hablando_gr.png"
image laura sonriendo = "Laura_parada_sonriendo.png"
image laura gr sonriendo = "Laura_parada_sonriendo_gr.png"


image bote = "bote_icon.png"
image caja = "caja_icon.png"
image bidon lleno = "bidon_lleno_icon.png"
image bidon 3 = "bidon_3_icon.png"
image bidon 2 = "bidon_2_icon.png"
image bidon 1 = "bidon_1_icon.png"
image bidon vacio = "bidon_vacio_icon.png"

image ingrid cargando = im.Scale("ingrid cargando.png", config.screen_width, config.screen_height)
image ingrid icon = "ingrid_icon.png"

# Define las imagenes para el sistema de stats
image sed_rojo = "rojo.png"
image sed_amarillo = "amarillo.png"
image sed_verde = "verde.png"
image hambre_rojo = "rojo.png"
image hambre_amarillo = "amarillo.png"
image hambre_verde = "verde.png"
image cansancio_rojo = "rojo.png"
image cansancio_amarillo = "amarillo.png"
image cansancio_verde = "verde.png"
image cansancio_icon = "cansancio_icon.png"
image hambre_icon = "hambre_icon.png"
image sed_icon = "sed_icon.png"

# Define the game starting variables ###################################################################

#define relacion inicial con NPCs
default marina = 0
default bob = 0
default laura = 0
default ingrid = 0
default charles = 0
default erika = 0
default tomas = 0

# define contador de desiciones de cada capitulo
default desicion_intro = 0
default desicion_contador = [0,0,0,0]
default desicion_1 = 0
default desicion_2 = 0
default desicion_3 = 0

# define recursos iniciales
default agua = 0
default comida = 0

#define posicion del pop up sobre las opciones de menu (default, alta o superior)
default choice_position = "default"

#define variables de arcos narrativos
default loopInvestigar = 0
default reporte_senderoOculto = False
default reporte_intro_status = ""
default reporte_grupo = False
default reporte_grupo_separado = False
default verSangre = False
default volverLaura = False
default refugio = ""
default palitos = 0
default bob_salva = False
default search_west = False
default search_south = False
default search_north = False
default reporte_regresar_busqueda = False
default reporte_prueba = "hola"
default reporte_prueba_2 = 10
default reporte_cargar_ingrid_jungla = False
default reporte_cargar_ingrid_jungla2 = False
default reporte_cargar_ingrid_jungla3 = False
default reporte_descansar_jungla = False
default reporte_comer_frutas_hasta_no_hambre = False
default reporte_comer_algunas_frutas = False
default reporte_ayudar_ingrid = False
default reporte_ayudar_ingrid2 = False
default reporte_p1_investigarConsulta = ""
default reporte_ignorar_sangre = False
default reporte_ignorar_sangre2 = False
default reporte_ignorar_sangre3 = False
default reporte_cuidar_ingrid = False
default reporte_cuidar_ingrid2 = False
default reporte_herido_miente = False
default reporte_herido_abandona = False
default reporte_herido_abandona2 = False
default reporte_herido_abandona3 = False
default reporte_herido_abandona4 = False
default reporte_acusa_marina = False
default reporte_wellness_m = False # Para saber que todavía no hablamos con Marina en el fogón al final del día.
default reporte_wellness_b = False # Para saber que todavía no hablamos con Bob en el fogón al final del día.
default reporte_wellness_l = False # Para saber que todavía no hablamos con Laura en el fogón al final del día.
default reporte_reproche_bob = False
default reporte_no_acompaña_responsable = False
default reporte_no_acompaña_egoista = False
default reporte_acompaña = False
default reporte_mentir_salvataje = False
default reporte_retener_salvataje = False
default reporte_acaparar_salvataje = False
default reporte_compartir_salvataje = False
default reporte_busqueda_lidera = False
default reporte_búsqueda_sigue = False
default reporte_búsqueda_separado = False
default reporte_consulta_grupo = False
default reporte_consulta_grupo_m = False
default reporte_consulta_grupo_b = False
default reporte_seguir_sangre = False
default reporte_seguir_sangre2 = False
default reporte_seguir_sangre3 = False
default reporte_no_buscar_ingrid = False
default reporte_buscar_ingrid = False
default reporte_reconoce_esfuerzo = False
default reporte_repudia_esfuerzo = False
default reporte_admite_no_saber = False
default reporte_objetar_bob = False
default reporte_callar_laura = False
default reporte_orden_en_el_claro = False
default reporte_tranquilizar_laura = False
default reporte_fue_a_colina = False
default reporte_fue_a_playa = False
default reporte_fue_con_marina = False
default reporte_fue_con_bob = False
default reporte_fue_solo = False
default reporte_esfuerzo_adicional = False
default reporte_investigar_cabaña = False
default reporte_buscar_mejor_refugio = False
default reporte_oculta_recursos = False
default reporte_celebra_recursos = False
default reporte_refugio_cueva = False
default reporte_refugio_cabaña = False
default reporte_refugio_claro = False
default reporte_recursos_responsable = False
default reporte_recursos_irresponsable = False
default reporte_recursos_resignacion = False
default reporte_recursos_resignacion2 = False
default reporte_recursos_redobla_esfuerzo = False
default reporte_recursos_redobla_esfuerzo2 = False
default reporte_racionar_agua = False
default reporte_acaparar_agua = False
default reporte_reconsidera_racionar_agua_m = False
default reporte_acaparar_agua_chicana_m = False
default reporte_reconsidera_racionar_agua_l = False
default reporte_acaparar_agua_laura = False
default reporte_acusa_adulacion_marina = False
default reporte_agua_ingrid_bm = False
default reporte_agua_ingrid_y = False
default reporte_agua_ingrid_l = False
default reporte_agua_ingrid_chicana_m = False
default reporte_agua_ingrid_decepcion_m = False
default reporte_agua_ingrid_oportunidad = False
default reporte_discusion_bob_confiar = False
default reporte_discusion_bob_objetar = False
default reporte_discusion_bob_concordia = False
default reporte_discusion_bob_sugerencia = False
default reporte_discusion_bob_inapto = False
default reporte_discusion_bob_reprochar = False
default reporte_discusion_bob_desconfiar = False
default reporte_discusion_bob_votacion = False
default reporte_comida_bob_lidera = False
default reporte_comida_marina_util = False
default reporte_comida_marina_acata = False
default reporte_comida_marina_inutil = False
default reporte_comida_liderazgo = False
default reporte_comida_pereza = False
default reporte_comida_optimizar = False
default reporte_comida_chicana_l = False
default reporte_comida_azar = False
default reporte_comida_bob_permanece = False
default reporte_comida_descansar = False
default reporte_liderazgo_rechazar = False
default reporte_liderazgo_abogar = False
default reporte_liderazgo_desconfiar = False
default reporte_liderazgo_aceptar = False
default reporte_campamento_descansar = False
default reporte_campamento_explorar = False
default reporte_campamento_cuidar = False
default reporte_lleva_fruta = False
default reporte_descanso_reconoce = False
default reporte_descanso_miente = False
default reporte_descanso_cero = False
default reporte_p3_final_optimista = False
default reporte_p3_final_pesimista = False
default reporte_p3_recuperar = False
default reporte_encontrar_agua_comida = False
default reporte_ignorar_sangre_seguir = False
default reporte_ignorar_sangre_volver = False
default reporte_ignorar_sangre2_volver = False
default reporte_ignorar_sangre2_seguir = False
default reporte_marina_laura_exploran = False
default reporte_senderoOculto_grupo = False
default reporte_dormir_mas = False
default reporte_despertar_ingrid = False
default bebio = False
default comio = False
default despierta_antes = False
default todos_despiertos = False
default bob_se_queda = False
default marina_se_queda = False
default laura_se_queda = False

default relaciones_cap1_bob = 99
default relaciones_cap1_marina = 99
default relaciones_cap2_bob = 99
default relaciones_cap2_marina = 99
default relaciones_cap2_laura = 99
default relaciones_cap3_bob = 99
default relaciones_cap3_marina = 99
default relaciones_cap3_laura = 99
default relaciones_cap4_bob = 99
default relaciones_cap4_marina = 99
default relaciones_cap4_laura = 99

#define inventario inicial
default stuff_caja_grande = False
default stuff_bidon_agua = False
default stuff_bote = False

#define variables de stats
default sed = 1
default hambre = 1
default cansancio = 1
default posicion_inicial_x = 0.01
default posicion_inicial_y = 0.1
default separacion_x = 0.05
default ancho_stat = 200  # Ancho fijo para cada stat
default setproxy = 0
default separacion_pop_up_x = 0.15
default separacion_pop_up_y = 0.03
default posicion_pop_up_x = posicion_inicial_x + separacion_pop_up_x
default posicion_pop_up_y = posicion_inicial_y + separacion_pop_up_y
default verde = "#0c700c"
default rojo = "#a50606"

# Define stuff buttons starting variables
default stuff_button_1 = "none"

# Define la variable de la imagen
default boton_imagen = "none_icon.png"


# funcion para actualizar la imagen del bidon segun la cantidad de agua del jugador
init python:
    def actualizar_boton_imagen():
        global boton_imagen
        if agua == 10:
            boton_imagen = "bidon_lleno_icon.png"
        elif 7 <= agua <= 9:
            boton_imagen = "bidon_3_icon.png"
        elif 4 <= agua <= 6:
            boton_imagen = "bidon_2_icon.png"
        elif 1 <= agua <= 3:
            boton_imagen = "bidon_1_icon.png"
        elif agua == 0:
            boton_imagen = "bidon_vacio_icon.png"

init python:
    cycles = 1  # Número de ciclos
    wait_time = 0.1  # Tiempo de espera en segundos

    def alternate_stat(variable_name, new_value):
        current_value = globals()[variable_name]
        current_image = f"{variable_name}_{get_color(current_value)}"
        new_image = f"{variable_name}_{get_color(new_value)}"

        for i in range(cycles):
            # Alternar entre la imagen actual y la nueva imagen
            #renpy.hide_screen("combined_ui")
            # renpy.pause(0.01)
            #globals()[variable_name] = current_value
            #renpy.show_screen("combined_ui")
            #renpy.pause(wait_time)
            #renpy.hide_screen("combined_ui")
            # renpy.pause(0.01)
            globals()[variable_name] = new_value
            renpy.show_screen("combined_ui")
            renpy.pause(wait_time)
        
        # Actualizar la variable al nuevo valor final
        globals()[variable_name] = new_value
        renpy.hide_screen("combined_ui")
        renpy.pause(0.01)
        renpy.show_screen("combined_ui")
        return globals()[variable_name]

    def get_color(value):
        if value == 1:
            return "rojo"
        elif value == 2:
            return "amarillo"
        elif value == 3:
            return "verde"
        return "amarillo"

# funcion para mostrar pop up cuando cambia variable de stat
init python:
    def show_variable_changed_popup(info, color="#FFFFFF"):
        renpy.show_screen("variable_changed_popup", info=info, color=color)

init python:
    # Function to ensure the stat value is within the range 1 to 3 and apply the pulse effect
    def update_stat(stat, value):
        if stat == "sed":
            global sed
            sed = max(1, min(value, 3))
        elif stat == "hambre":
            global hambre
            hambre = max(1, min(value, 3))
        elif stat == "cansancio":
            global cansancio
            cansancio = max(1, min(value, 3))
        
        # Refresh the UI to apply the pulse effect
        renpy.hide_screen("combined_ui")
        renpy.show_screen("combined_ui")

# Inicializar listas para cada decisión
# define tipos de desiciones inicial
default empático_mas = [0, 0, 0, 0]
default empatico_menos = [0, 0, 0, 0]
default honestidad_mas = [0, 0, 0, 0]
default honestidad_menos = [0, 0, 0, 0]
default integridad_mas = [0, 0, 0, 0]
default integridad_menos = [0, 0, 0, 0]
default responsabilidad_mas = [0, 0, 0, 0]
default responsabilidad_menos = [0, 0, 0, 0]
default compromiso_mas = [0, 0, 0, 0]
default compromiso_menos = [0, 0, 0, 0]
default colaboración_mas = [0, 0, 0, 0]
default colaboración_menos = [0, 0, 0, 0]

# lista de desiciones
# Calcular el total de decisiones una vez
default lista_decisiones_intro = ["empático_mas", "empatico_menos", "honestidad_mas", "honestidad_menos", "integridad_mas", "integridad_menos", "responsabilidad_mas", "responsabilidad_menos", "compromiso_mas", "compromiso_menos", "colaboración_mas", "colaboración_menos"]

# Inicializar variable para el capítulo actual
default capitulo_actual = 0

#Calcular status de relaciony desiciones y armar lista
init python:
    def calcular_status(valor):
        if valor > 2:
            return "confianza"
        elif valor == 2:
            return "amistosa"
        elif valor == 1:
            return "cordial"
        elif valor == 0:
            return "neutral"
        elif valor == -1:
            return "fria"
        elif valor == -2:
            return "tensa"
        elif valor < -2:
            return "hostil"
        else:
            return "desconocido"

    def generar_lista_popup(titulo, variables, decisiones=None, es_relacion=False):
        contenido = [titulo]
        if decisiones is not None:
            decision_text = "decisión" if decisiones == 1 else "decisiones"
            contenido.append(f"En este capítulo has tomado {decisiones} {decision_text}")
            for var in variables:
                valor = eval(var)
                if isinstance(valor, list):
                    valor = valor[capitulo_actual]
                if valor > 0:
                    contenido.append(f"{var.capitalize()}:  {valor}")
        else:
            for var in variables:
                valor = eval(var)
                if not es_relacion and isinstance(valor, list):
                    valor = valor[capitulo_actual]
                status = calcular_status(valor)
                contenido.append(f"{var.capitalize()}:  {status}")
        return contenido

    def calcular_decisiones_intro(lista_decisiones):
        decisiones_intro = 0
        for var in lista_decisiones:
            decisiones_intro += eval(var)[capitulo_actual]
            desicion_contador[capitulo_actual] += eval(var)[capitulo_actual]
            print(f"{var}: {eval(var)[capitulo_actual]}")  # Imprimir el valor de cada variable para depuración
        print(f"Total de decisiones: {decisiones_intro}")  # Imprimir el total de decisiones para depuración
        return decisiones_intro

# logica para mandar el reporte a un form
init python:
    import requests

    def enviar_reporte(player_id):
        # 🟢 Obtener todas las variables con "reporte_" dinámicamente
        reporte_variables = []
        for var in renpy.store.__dict__:  
            if var.startswith("reporte_"):  
                reporte_variables.append(f"{var}={renpy.store.__dict__[var]}")  # Guarda nombre y valor

        # 🟢 Obtener todas las variables con "relaciones_" dinámicamente
        relaciones_variables = []
        for var in renpy.store.__dict__:  
            if var.startswith("relaciones_"):  
                relaciones_variables.append(f"{var}={renpy.store.__dict__[var]}")  # Guarda nombre y valor

        # 🟢 Convertir el reporte y relaciones a formato texto
        reporte_texto = ", ".join(reporte_variables)  # Une todas las variables en un string
        relaciones_texto = ", ".join(relaciones_variables)  # Une todas las variables en un string

        # 🟢 ID del formulario en Google Forms
        formulario_id = "1FAIpQLSejCRSpb3Ouw7_ewVP0rViiV01hBriPuX9Da6btTMRgMA24Aw"

        # 🟢 URL de envío automática
        url = f"https://docs.google.com/forms/d/e/{formulario_id}/formResponse"

        # 🟢 Datos a enviar con el reporte completo
        datos = {
            "entry.243862175": player_id,  # ID del jugador
            "entry.1095225020": reporte_texto,  # Todas las variables concatenadas con "reporte_"
            "entry.469138304": relaciones_texto  # Todas las variables concatenadas con "relaciones_"
        }

        # 🟢 Enviar los datos con una solicitud POST
        try:
            respuesta = requests.post(url, data=datos)
            if respuesta.status_code == 200:
                print("✔️ Reporte enviado correctamente con todas las variables.")
            else:
                print(f"❌ Error al enviar el reporte. Código: {respuesta.status_code}")
        except Exception as e:
            print(f"❌ Error en la solicitud: {str(e)}")

############################################   ###############################################################################################################
############################################   ###############################################################################################################
## Aca comienza la PARTE 1 #################   ###############################################################################################################
############################################   ###############################################################################################################
label pedir_id:
    if renpy.android:  # Solo mostrar en Android
        while True:  # Se repite hasta que el ID sea válido
            show screen pedir_id_screen
            $ resultado = ui.interact()

            if resultado:
                #$ input_id = renpy.get_screen_variable("input_id")  # Obtener el ID ingresado
                
                if input_id in player_ids:
                    $ player_id = input_id  # Asignar el ID válido
                    
                    "ID válido registrado: [player_id]."
                    hide screen pedir_id_screen
                    
                    jump start_game  # Sale del label si el ID es válido
                
                else:
                    "ID inválido. Intenta nuevamente."

            else:
                "Debes ingresar un ID válido."

label start:
    #$ quick_menu = False  # Oculta el menú
    # Inicializar el capítulo actual
    $ capitulo_actual = 0

    # Estado de los stats al inicio
    $ sed = 2
    $ hambre = 3
    $ cansancio = 2
    
    $ posicion_inicial_x = 0.05
    $ posicion_inicial_y = 0.15
    $ separacion_x = 0.15

    scene bg inicio at truecenter
    with Dissolve(.5)

    if renpy.android:  # Si el juego está en Android, pedir ID
        call pedir_id
    else:
        jump start_game

label start_game:

    # Define una función para mostrar el pop-up y pedir el nombre del personaje  ############################
    # Muestra un cuadro de entrada para que el jugador introduzca el nombre
    $ nombre_personaje = renpy.input("¿Cuál es el nombre de tu personaje?")

    # Elimina los espacios en blanco alrededor del nombre
    $ nombre_personaje = nombre_personaje.strip()

    # Verifica si el jugador ha introducido un nombre
    if nombre_personaje == "":
        # Si no se introduce un nombre, usa un nombre por defecto
        $ nombre_personaje = "Margot"
    
    # Muestra un menú para seleccionar el género
    $ choice_position = "default"

    menu:
        "Selecciona cómo quieres que se refieran a tu personaje:"
        "Masculino":
            $ genero = "Masculino"
            $ e = "o"
            $ le = "el"
        "Femenino":
            $ genero = "Femenino"
            $ le = "la"
            $ e = "a"
    jump comic

label comic:
    scene bg comic 1 at truecenter
    $ persistent.first_time = True
    with Dissolve(1)

    call screen custom_button
    jump start_continue


label start_continue:

    scene bg beach storm1 at truecenter
    with Dissolve(.5)

    show screen combined_ui

    show marina hablando at right
    with Dissolve(.5)

    # prueba de enviar reporte
    #$ enviar_reporte(player_id)


    m "No puedo creer... que llegamos... a la costa... ¡Nos hemos salvado, [nombre_personaje]! ¿Estás muy cansad[e]?"

    y "(recuperando el aliento)"

    # $ update_stat("hambre", hambre - 1)
    # $ show_variable_changed_popup("El hambre ha aumentado", rojo)

    show marina gr preocupada at leftgr
    with Dissolve(.5)

    m "No podemos ser los únicos, ¿verdad? Deberíamos buscar mas sobrevivientes."

    $ choice_position = "default" # default alta superior

    menu:
        "Sí, tiene que haber más. Vamos a buscarles.":

            show marina hablando at left
            with Dissolve(.5)
            m "Recorramos la playa, no pueden estar muy lejos."
            jump playa_intro

        "Espera, no podemos arriesgarnos a que las olas se lleven las cosas que hay en la orilla. Tenemos que salvar lo que se pueda.":
            show marina hablando at left
            with Dissolve(.5)
            m "Las cosas no me importan, alguien puede precisar ayuda."

            jump stay_intro

label playa_intro:

    scene bg beach storm 2 at truecenter
    with Dissolve(.5)
    $ desicion_intro += 1
    $ reporte_acompaña = True
    $ marina += 1 

    #$ colaboración_mas[capitulo_actual] += 1
    #$ empatico_mas[capítulo_actual] += 1
    $ reporte_intro_status = "gente"

    m "Allá parece haber alguien, vamos a ver si está bien."
   
    hide marina gr preocupada
    with Dissolve(.5)

    b "¡Aquí! ¡Por aquí! "
    
    show bob saludando sucio at right
    with Dissolve(.5)

    b "Me alegra que ustedes también lo hayan logrado. Esta es la peor tormenta que he visto en toda mi carrera como capitán."
    
    $ choice_position = "default" # default alta superior
    menu:
        "Estamos recorriendo la orilla, pero eres la primera persona con la que nos cruzamos.":
            b "No se preocupen, ya he visto huellas de otros sobrevivientes en la playa. Vamos a buscarlos."

            jump buscar_mas

        "¡No vengas con excusas, tormenta o no tú eras el responsable del barco! ¡Este desastre es tu culpa!":
            $ bob -= 1
            $ desicion_intro += 1
            $ reporte_reproche_bob = True
            #$ empatico_menos[capitulo_actual] +=1
            show bob gr parado enojado at rightgr 
            with Dissolve(.5) 
            b "En el mar hay peligros contra los que ni siquiera el mejor capitán puede hacer mucho. Nada podía prepararnos para esa tormenta."
            show bob gr serio sucio at rightgr 
            with Dissolve(.5) 
            b  "Yo no seré el mejor capitán, pero pueden contar conmigo. Ahora es mi deber encargarme de encontrar más sobrevivientes."

            jump buscar_mas

label buscar_mas:
    show marina hablando at left
    with Dissolve(.5)
    m "Vamos a buscar a los demás sobrevivientes."
    show marina preocupada
    with Dissolve(.5)
    m "No podemos dejar a nadie atrás."
    hide marina
    with Dissolve(.5)
    hide bob
    with Dissolve(.5)
    jump intro_final
   

label stay_intro:
    $ reporte_intro_status = "cosas"
    hide marina gr preocupada
    with Dissolve(.5)
    $ desicion_intro += 1
    $ marina -= 1
    "{i}Parece que Marina lo tomó a mal.{/i}"

    $ choice_position = "alta" # default alta superior
    menu:
        "{i}Lamento que no entienda que nuestra supervivencia depende de que recuperemos todo lo posible antes de que las olas se lo lleven.{/i}":
            $ desicion_intro += 1
            $ reporte_no_acompaña_responsable = True
            #$ colaboración_menos[capitulo_actual] += 1
            #$ responsabilidad_mas[capitulo_actual] += 1
            jump stay_savestuff
        "{i}¡Por fin se marchó! Para sobrevivir debo recuperar lo que se pueda. Ya veremos cuando pasen unos dias...{/i}":
            $ desicion_intro += 1
            $ reporte_no_acompaña_egoista = True
            #$ integridad_menos[capitulo_actual] += 1
            jump stay_savestuff

label stay_savestuff:
    scene bg beach storm at truecenter
    with Dissolve(.5)

    "{i}Hay muchas cosas y la marea ya esta subiendo. Tendré que elegir rápido que voy a salvar.{/i}"

    $ choice_position = "default" # default alta superior
    menu:
        "BOTE SALVAVIDAS":  
            jump bote
        "CAJA DE MADERA CERRADA":
            jump caja
        "BIDÓN DE AGUA LLENO":
            jump bidon

label bote:
    $ stuff_bote = True
    #show bote at Stuff_1
    $ boton_imagen = "bote_icon.png"
    show screen top_right_button(boton_imagen)
    $ stuff_button_1 = "bote"
    jump intro_ending

label caja:
    $ stuff_caja_grande = True
    # show caja at Stuff_1
    $ boton_imagen = "caja_icon.png"
    show screen top_right_button(boton_imagen)
    $ stuff_button_1 = "caja"
    jump intro_ending

label bidon:
    $ stuff_bidon_agua = True
    $ agua += 10 
    #show bidon lleno at Stuff_1
    $ boton_imagen = "bidon_lleno_icon.png"
    show screen top_right_button(boton_imagen)
    $ stuff_button_1 = "bidon"
    jump beber_bidon
    
label beber_bidon:
    if sed < 3:
        $ choice_position = "default" # default alta superior
        menu:
            "{i}Deberia beber algo de agua, estoy con la garganta seca.{/i}":
                pause 0.5
                y "Glup.... glup... glup..."
                pause 0.5
                $  agua -= 4
                # Llamar a la función para actualizar la imagen del botón
                $ actualizar_boton_imagen()
                $ update_stat("sed", sed + 1)
                $ show_variable_changed_popup("La sed ha disminuido", verde)
                # Ocultar y volver a mostrar la pantalla para actualizar la imagen
                hide screen combined_ui
                show screen combined_ui
                jump beber_bidon

            "{i}Mejor reservar el agua. Quizás sea muy difícil conseguir agua potable en la isla.{/i}":
                if capitulo_actual == 0:
                    jump intro_ending
                if capitulo_actual == 3:
                    jump refugio_init_sed
    else: 
        $ choice_position = "default" # default alta superior
        menu:
            "{i}Mejor reservar el agua. Quizás sea muy difícil conseguir agua potable en la isla.{/i}":
                if capitulo_actual == 0:
                    jump intro_ending
                if capitulo_actual == 3:
                    jump refugio_init_sed
            "{i}No tengo sed ahora. Aún hay mucho por hacer.{/i}":
                if capitulo_actual == 0:
                    jump intro_ending
                if capitulo_actual == 3:
                    jump refugio_init_sed

    jump intro_ending

label intro_ending:
    "{i}¡Listo! Ahora debo pensar mis siguientes pasos...{/i}"
    jump intro_final

label botonObjetos:
    if stuff_button_1 == "bote": 
        "{i}Aún no es momento de usar el bote.{/i}"
    if stuff_button_1 == "caja": 
        "{i}Aún no es momento de usar la caja.{/i}"
    if stuff_button_1 == "bidon": 
        "{i}Aún no es momento de usar el bidón.{/i}"
    elif stuff_button_1 == "none": 
        "No tengo ningún objeto para usar aquí"
    return 
    
label intro_final:
    pause 0.5
    # Generar contenido para los pop-ups de relaciones
    if reporte_intro_status == "cosas":
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina"], es_relacion=True)
        $ relaciones_cap1_bob = 99
        $ relaciones_cap1_marina = marina
    else:
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob"], es_relacion=True)
        $ relaciones_cap1_bob = bob
        $ relaciones_cap1_marina = marina
    
    # Calcular el total de decisiones y obtener la lista de variables específicas para la introducción
    $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
    
    # Generar contenido para los pop-ups de decisiones
    $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

    "Este es el resúmen de tu intro."
    # Mostrar los pop-ups
    show screen relaciones_popup(contenido=relaciones_contenido)
    show screen decisiones_popup(contenido=decisiones_contenido)

    "{size=-15}Las decisiones pueden afectar la relación con los demás supervivientes. Sin ser inherentemente buenas o malas las decisiones tienen consecuencias.{/size}"
    
    
    "Aquí termina la introducción. En el siguiente capítulo tus decisiones definirán el destino de los supervivientes. ¿Preparad[e] para descubrir los secretos de la isla?"
    # Ocultar los pop-ups con dissolve
    hide screen relaciones_popup with dissolve
    hide screen decisiones_popup with dissolve

    $ choice_position = "default" # default alta superior
    menu:
        "CONTINUAR":
            jump parte_1start
        "VOLVER A VER EL RESÚMEN":
            jump intro_final
############################################   ######   #########################################################################################################
############################################   ######   #########################################################################################################
## Aca comienza la PARTE 2 #################   ######   #########################################################################################################
############################################   ######   #########################################################################################################
label parte_1start:
    # Inicializar el capítulo actual
    $ capitulo_actual = 1

    if reporte_intro_status == "cosas":
        jump p1desicion
    if reporte_intro_status == "gente":
        jump p1supervivientes

label p1desicion:
    $ choice_position = "default" # default alta superior
    menu:
        "Avanzar por la playa buscando más cosas o supervivientes.":
            jump p1supervivientes
        "Investigar el interior de la isla por comida o refugio.":
            jump p1islaInvestigar
    
label p1supervivientes:
    show bg beach storm1 at truecenter
    with Dissolve(.5)
    if ((reporte_intro_status == "cosas" and reporte_grupo_separado == True) or (reporte_intro_status == "gente" and reporte_grupo_separado == True)):
        y "Mmmm... quizás debí quedarme con Marina y Bob."
        $ choice_position = "default" # default alta superior
        menu:
            "Seguir las huellas y alcanzar a Marina y Bob.":
                $ verSangre = False
                jump p1herido_volver
            "Mejor sigo explorando la isla por mi cuenta.":
                jump p1islaInvestigar
    show bob saludando sucio at left
    with Dissolve(.5)
    b "Marina, por aquí hay unas huellas, se meten en la isla..."
    if reporte_intro_status == "cosas":
        b "¡Hola [nombre_personaje]! ¡Qué alegría que estés bien!"
        b "¡Marina, aquí está el otro superviviente del que me hablaste!"
        show marina gr preocupada at rightgr
        with Dissolve(.5)
        m "¿Así que al final apareces? Aún no puedo creer que hayas preferido quedarte juntando cosas antes que ayudar a los demás."
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        b "Marina, ¡por favor! Tal vez logró encontrar algo útil."

        b "Vamos a necesitar todos los recursos posibles hasta que llegue la ayuda o encontremos la manera salir vivos de aquí."
    
        if stuff_bidon_agua == True:
            $ tengo = "Tengo un bidón con agua."
        if stuff_bote == True:
            $ tengo = "Tengo un bote salvavidas."
        if stuff_caja_grande == True:
            $ tengo = "Tengo una caja grande de madera."
        if stuff_bidon_agua == True:
            $ encontre = "Encontré un bidón con agua."
        if stuff_bote == True:
            $ encontre = "Encontré un bote salvavidas."
        if stuff_caja_grande == True:
            $ encontre = "Encontré una caja grande de madera."

        $ choice_position = "default" # default alta superior
        menu:
            "No he logrado recuperar nada, todo se lo llevó el mar.":
                $ desicion_intro += 1
                $ reporte_mentir_salvataje = True
                $ bob -= 1
                b "¿Todo? Que pena que te hayas quedado atrás para eso y no lograras recuperar nada."
            "Logré rescatar algo, pero hasta que las cosas no estén más claras permanecerá en un lugar seguro.":
                $ desicion_intro += 1
                $ reporte_retener_salvataje = True
                b "Vamos a necesitar confiar en los demás, pero entiendo que todos estamos un poco en shock aún."
                b "Tan solo saber que contamos con eso que guardaste, cuando lo necesitemos, me deja más tranquilo."
            "[tengo] Pero yo lo encontré asi que es para mi.":
                $ desicion_intro += 1
                $ reporte_acaparar_salvataje = True
                $ bob -= 1
                $ marina -= 1
                b "Una actitud que no comparto. Espero que pronto veas que en esto estamos juntos."
            "[encontre] Nos va a ayudar a salir adelante.":
                $ desicion_intro += 1
                $ reporte_compartir_salvataje = True
                $ bob += 1
                $ marina += 1
                b "¡Qué buena noticia! Nos vendrá muy bien."

                m "Después de todo, fue buena idea que te quedaras en la playa mientras yo buscaba más supervivientes."

                m "Buen trabajo, [nombre_personaje]. Discúlpame por enojarme contigo."
    else:
        show marina gr sonriendo at rightgr
        with Dissolve(.5)
        m "¡Eso significa que hay más supervivientes!" 
        hide marina
        with Dissolve(.5)
    jump p1_grupoPlaya

label p1_grupoPlaya:
    show bg beach storm1 at truecenter
    with Dissolve(.5)
    show bob gr parado hablando at leftgr
    with Dissolve(.5)
    b "Hay que hallar a los demás antes que oscurezca, sigamos las huellas al interior de la isla." 

    $ choice_position = "default" # default alta superior
    menu:
        "¡Vamos! No hay tiempo que perder. ¡Síganme!":
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            $ desicion_intro += 1
            $ reporte_busqueda_lidera = True
            $ compromiso_mas[capitulo_actual] += 1
            $ reporte_grupo = True
            jump p1islaInvestigarLead
        "Lidere usted la búsqueda, capitán.":
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            $ desicion_intro += 1
            $ reporte_búsqueda_sigue = True
            $ colaboración_mas[capitulo_actual] += 1
            $ reporte_grupo = True
            jump p1islaInvestigarLead
        "Mejor sigo por mi cuenta, adiós.":
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            $ desicion_intro += 1
            $ reporte_búsqueda_separado = True
            $ colaboración_menos[capitulo_actual] += 1
            $ reporte_grupo = True
            $ reporte_grupo_separado = True 
            jump p1islaInvestigar

label p1islaInvestigar:
    show bg jungle1 1 at truecenter
    with Dissolve(.5)
    y "La jungla esta muy densa, no parece que haya pasado nadie por aquí. Además la lluvia ha hecho un barrial."
    if loopInvestigar == 0:
        $ update_stat("hambre", hambre - 1)
        $ show_variable_changed_popup("El hambre ha aumentado", rojo)
        $ loopInvestigar += 1 
    else: 
        y "Ya he pasado por acá, al menos este lugar ya me es familiar."
        $ loopInvestigar += 1 
    
    if reporte_senderoOculto== True:
        $ choice_position = "alta" # default alta superior
    else:
        $ choice_position = "default" # default alta superior
    menu:
        "{i}Debería regresar, me estoy agotando y no quiero pasar la noche a oscuras en medio de esta jungla.{/i}":
            jump p1regresoJungla
        "{i}Debo apurar el paso, hay que aprovechar la luz que aún queda para encontrar comida o refugio.{/i}":
            jump p1continuarJungla
        "{i}Aqui hay otro pasaje, podría investigar a donde me lleva.{/i}" if (loopInvestigar > 2 and reporte_senderoOculto == False):
            $ reporte_senderoOculto_grupo = True
            jump p1encuentroJungla
        "{i}Aquí está el sendero oculto para ir al claro con Laura.{/i}" if reporte_senderoOculto == True:
            $ volverLaura = True
            jump p1encuentroJungla

label p1regresoJungla:
    if reporte_intro_status == "cosas":
        scene bg beach storm at truecenter
        with Dissolve(.5)
        jump p1desicion
    if reporte_intro_status == "gente":
        scene bg beach storm 2 at truecenter
        with Dissolve(.5)
        jump p1supervivientes

label p1continuarJungla:
    show bg jungle1 blood at truecenter
    with Dissolve(.3)
    pause(1.0)
    y "Hay algo raro en esas hojas, ¿será alguna serpiente?"
    
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Podría ser alguna fruta o algo comestible, me acercaré con cuidado.{/i}" if volverLaura == False:
            jump p1rastroSangre
        
        "{i}Quizás sea alguna pista de Ingrid, tengo que ver más de cerca.{/i}" if volverLaura == True:
            jump p1rastroSangre

        "{i}No estoy para correr riesgos, volveré sobre mis pasos.{/i}":
            if ((reporte_intro_status == "cosas" and reporte_grupo == False) or reporte_grupo_separado == True):
                jump p1islaInvestigar
            else:
                jump p1islaInvestigarLead

        "{i}Debería consultar con Bob y Marina, es peligroso y deberíamos estar todos de acuerdo.{/i}" if ((reporte_intro_status == "gente" and reporte_grupo_separado == False) or (reporte_grupo == True and reporte_grupo_separado == False)):
            $ desicion_intro += 1
            $ reporte_consulta_grupo = True
            jump p1islaInvestigarConsulta

                
label p1rastroSangre:
    show bg jungle1 blood zoom at truecenter
    with Dissolve(0.3)

    y "¡¿Eso es... sangre?! ¡Y está fresca! Parece haber más hacia el interior de la selva."
    $ verSangre = True

    $ choice_position = "superior" # default alta superior
    menu:
        "{i}Voy a seguir el rastro de sangre, alguien parece necesitar ayuda.{i}" if volverLaura == False:
            $ desicion_intro += 1
            $ reporte_seguir_sangre = True
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            jump p1herido
        
        "{i}Voy a seguir el rastro de sangre, si es Ingrid puede necesitar ayuda.{i}" if volverLaura == True:
            $ desicion_intro += 1
            $ reporte_seguir_sangre = True
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            jump p1herido

        "{i}Donde hay sangre hay problemas, mejor seguir adelante.{i}":
            $ desicion_intro += 1
            $ integridad_menos[capitulo_actual] += 1
            $ reporte_ignorar_sangre = True
            $ reporte_ignorar_sangre_seguir = True
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)

            jump p1encuentroJungla
            
        "{i}Esto se puso complicado, mejor volver atrás.{i}":
            $ desicion_intro += 1
            $ compromiso_menos[capitulo_actual] += 1
            $ reporte_ignorar_sangre = True
            $ reporte_ignorar_sangre_volver = True
            jump p1islaInvestigar           

label p1encuentroJungla:
    show bg jungle claro at truecenter
    with Dissolve(.5)

    show laura seria at right
    with Dissolve(.5)
    if volverLaura == True:
        l "¿Hás encontrado a Ingrid?"
        y "No, he dado varias vueltas pero no he visto nada."
        #### ACÁ SE PUEDE ESTAR DICIENDO LA PURA VERDAD, LA VERDAD A MEDIAS, O SE PUEDE ESTAR MINTIENDO, DEPENDIENDO DESDE DÓNDE SE LLEGÓ. TENERLO EN CUENTA PARA REGISTRO ###
        jump p1_EsperarClaro

    l "¡[nombre_personaje]! ¡Me alegra que también hayas logrado llegar a la costa!"
    $ volverLaura = True
    l "¿Hás visto a Ingrid? Ella fué hace rato a buscar algunas frutas y plantas."

    $ choice_position = "superior" # default alta superior
    menu:
        "Para nada, no la vi. Quizás se cruzó con Marina, ella llegó a la playa también pero nos separamos para investigar." if (reporte_intro_status == "cosas" or reporte_grupo == False or reporte_senderoOculto == False):
            $ desicion_intro += 1
            $ reporte_herido_miente = True
            jump p1_EsperarClaro
        
        "Para nada, no la vi. Me metí por un sendero medio oculto y no me crucé con ella." if reporte_senderoOculto == True:
            l "Estoy preocupada, hace tiempo que no sé nada de ella."
            menu:
                "Estoy muy cansad[e], Ingrid tendrá que arreglarse sola.":
                    y "No te preocupes, seguramente ella vuelva pronto."
                    $ desicion_intro += 1
                    $ reporte_no_buscar_ingrid = True
                    jump p1_EsperarClaro
                "Fue difícil llegar hasta aquí, quizás Ingrid necesite ayuda.":
                    y "Espera aquí por si vuelve, voy a recorrer un poco por si la encuentro."
                    $ desicion_intro += 1
                    $ reporte_buscar_ingrid = True
                    $ laura += 1  
                    hide laura
                    with Dissolve(.5)
                    jump p1continuarJungla

        "Me pareció ver unas huellas pero no las seguí asi que no sé si eran de ella." if reporte_senderoOculto == False:
            $ desicion_intro += 1
            $ reporte_herido_miente = True
            jump p1_BuscarIngrid

        "Vi unas manchas de sangre de camino acá, pero no quise arriesgarme a investigar." if reporte_senderoOculto == False:
            $ desicion_intro += 1
            $ reporte_herido_miente = False
            $ laura -= 1  
            jump p1_BuscarIngrid

label p1_BuscarIngrid:
    show laura gr enojada at rightgr
    with Dissolve(0.5)

    l "¡Podía haber un superviviente en problemas! Ya veo la clase de compañía con la que me tocó sufrir este calvario."

    l "Yo voy a buscarla, quizás necesita ayuda. Supongo que puedes quedarte aquí por si regresa."

    hide laura 
    with Dissolve(0.5) 
    
    if reporte_grupo_separado == False:
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        b "Yo voy contigo."
        hide bob
        with Dissolve(0.5)
        show marina gr preocupada at rightgr
        with Dissolve(.5)
        m "Yo también voy. Espéranos aquí, [nombre_personaje]"
        hide marina
        with Dissolve(0.5)

    jump p1_rlauraBobIngrid

label p1_rlauraBobIngrid:

    "Recorres el pequeño claro donde Laura e Ingrid han juntado algunas ramas. No parece que se pueda hacer un refugio en este lugar."
    "Un rato después entran al claro Laura, seguida de Bob y Marina. Entre los tres cargan a Ingrid. Parece herida."

    y "¿Está bien? ¿Dónde la encontraron?"
    show laura gr enojada at rightgr
    with Dissolve(0.5)

    l "¿Ahora te preocupa? La encontré tirada en el suelo."
    $ boton_imagen_character = "ingrid_icon_sangre.png"
    show screen character_top_right_button(boton_imagen_character)
    with Dissolve(0.5)

    l "Por suerte Marina y Bob me ayudaron. Si no fuera por ellos, Ingrid podría haber muerto."

    show bob gr serio sucio at leftgr
    with Dissolve(0.5)
    b "Conozco de primeros auxilios, ya no pierde sangre. Necesita descanso y cuidados."
    $ boton_imagen_character = "ingrid_icon_firstaid.png"
    show screen character_top_right_button(boton_imagen_character)
    with Dissolve(0.5)

    l "Hay algunas cosas que no me cierran, tengo muchas preguntas..."

    $ choice_position = "default" # default alta superior
    menu:
        "Mejor ahora pensemos como salir adelante, ya habrá tiempo.":
            jump p1_resumen
        "Yo también tengo algunas cosas que decir cuando llegue el momento.":
            jump p1_resumen
        "Ingrid no se va a curar si seguimos perdiendo el tiempo hablando. Precisa refugio, agua y comida.":
            jump p1_resumen


label p1_EsperarClaro:
    show laura gr seria at rightgr
    with Dissolve(0.5)

    l "Supongo que deberíamos esperar un poco a que regrese."
    jump p1_bob_salva

label p1islaInvestigarLead:
    show bg jungle1 1 at truecenter
    with Dissolve(.5)

    y "La jungla está muy densa, no parece que haya pasado nadie por acá. Además la lluvia ha hecho un barrial."
    
    if loopInvestigar == 0:
        $ update_stat("hambre", hambre - 1)
        $ show_variable_changed_popup("El hambre ha aumentado", rojo)
        $ loopInvestigar += 1 
    else: 
        y "Ya hemos pasado por acá, al menos este lugar ya me es familiar." 
        $ loopInvestigar += 1 
    menu:
        "Deberíamos regresar, me estoy agotando y no quiero pasar la noche a oscuras en medio de esta jungla.":
            jump p1_grupoPlaya
        "Debemos apurar el paso, hay que aprovechar la luz que aún queda para encontrar a los demás.":
            jump p1continuarJungla
        "Por aquí hay otro sendero, podríamos investigar a dónde lleva." if loopInvestigar > 2:

            jump p1regresoJunglaGrupo

label p1islaInvestigarConsulta:
    y "Marina! ... ¡Bob!"
    show marina sonriendo at right
    with Dissolve(.5)
    pause(0.5)
    show bob saludando sucio  at left
    with Dissolve(.5)
    b "¿Qué sucede, [nombre_personaje]?"
    y "Hay algo raro en esas hojas. ¿Les parece que investiguemos o volvemos atras?"
    y "Puede ser comida, algún animal peligroso, es difícil de saber desde aquí."
    show marina gr preocupada at rightgr
    with Dissolve(.5)
    m "Si puede ser peligroso mejor volver atrás, creo."
    show bob gr pensando at leftgr
    with Dissolve(.5)
    b "¿Y si es comida? ¿O algún rastro de los demás? Volver no es una opción."

    $ choice_position = "default" # default alta superior
    menu:
        "Marina tiene razón, hay que usar la cabeza y ser cuidadosos. Volvamos y busquemos otro camino.":
            $ reporte_p1_investigarConsulta == "Marina"
            $ marina += 1
            $ bob -= 1
            $ desicion_intro += 1
            $ reporte_consulta_grupo_m = True
            hide bob
            hide marina
            jump p1regresoJunglaGrupo
        "Bob tiene razón, con miedo no vamos a salir adelante. Veamos que hay entre esas hojas.":
            $ reporte_p1_investigarConsulta == "Bob"
            $ bob += 1
            $ marina -= 1
            $ desicion_intro += 1
            $ reporte_consulta_grupo_b = True
            hide bob
            hide marina
            jump p1rastroSangreGrupo

label p1rastroSangreGrupo:
    show bg jungle1 blood zoom at truecenter
    with Dissolve(0.3)

    y "¡¿Eso es... sangre?! ¡Y está fresca! Parece haber más hacia el interior de la selva."
    $ verSangre = True

    $ choice_position = "alta" # default alta superior
    menu:
        "Debemos seguir el rastro de sangre, alguien parece necesitar ayuda.":
            $ desicion_intro += 1
            $ reporte_seguir_sangre2 = True
            show marina gr preocupada at rightgr
            with Dissolve(0.5)
            m "De acuerdo. Pero vayamos con cuidado."
            hide bob
            with Dissolve(0.5)
            hide marina
            with Dissolve(0.5)
            jump p1herido
        
        "Donde hay sangre hay problemas, mejor seguir adelante.":
            $ desicion_intro += 1
            $ reporte_ignorar_sangre2_seguir = True
            $ bob -= 1
            $ marina -= 1
            $ reporte_grupo_separado = True

            show bob gr serio sucio at rightgr
            with Dissolve(0.5)
            b "Tu sigue si quieres, si hay alguien herido es mi deber ayudar."
            show marina gr preocupada at leftgr
            with Dissolve(0.5)
            m "Yo voy contigo Bob, tal vez necesites ayuda."
            hide bob
            with Dissolve(0.5)
            hide marina
            with Dissolve(0.5)
            jump p1encuentroJungla
            
        "Esto se puso complicado, mejor volver atrás.":
            show bob gr serio sucio at rightgr
            with Dissolve(0.5)
            b "Tu sigue si quieres, si hay alguien herido es mi deber ayudar."
            show marina gr preocupada at leftgr
            with Dissolve(0.5)
            m "Yo voy contigo Bob, tal vez necesites ayuda."
            $ desicion_intro += 1
            $ reporte_ignorar_sangre2_volver = True
            $ reporte_grupo_separado = True
            hide bob
            with Dissolve(0.5)
            hide marina
            with Dissolve(0.5)
            jump p1islaplayasolo

label p1herido:
    show bg jungle herida  at truecenter
    with Dissolve(0.5)

    y "¡Allí! ¿Estará viva?"
    show bg jungle herida zoom  at truecenter
    y "¡Si! Está viva, pero inconsciente y malherida. Tiene un golpe muy feo en la cabeza."
    if (reporte_grupo == False or reporte_grupo_separado == True):
        jump herida_desicion
    else:
        show bob parado hablando at left
        with Dissolve(.5)
        b "¿Esta herida? Dejame revisarla, puedo darle primeros auxilios."
        pause(1.0)
        $ boton_imagen_character = "ingrid_icon_firstaid.png"
        show screen character_top_right_button(boton_imagen_character)

        show bob gr serio sucio  at leftgr
        with Dissolve(.5)
        b "Por ahora debería ser suficiente, el sangrado se ha detenido."
        pause(1.0)
        show bob gr pensando at leftgr
        with Dissolve(.5)
        b "Pero aún esta delicada, necesita agua y refugio."
        show marina gr hablando at rightgr
        with Dissolve(0.5)
        m "Hay que buscar en el interior de la isla algún refugio y comida."
        b "Entre los tres podemos cargar con ella. ¡Vamos!"
        hide bob
        with Dissolve(.5)
        hide marina
        with Dissolve(.5)
        jump p1_claro_grupo_ingrid

label herida_desicion:
    $ boton_imagen_character = "ingrid_icon_sangre.png"
    show screen character_top_right_button(boton_imagen_character)
    with Dissolve(0.5)
    if volverLaura == False:
        $ choice_position = "superior" # default alta superior
        menu:
            "{i}¿Qué hago? No soy doctor y lo único que puedo hacer es cargarla hasta la playa y buscar a alguien que pueda ayudarme.{/i}":
                jump herida_playa
            "{i}¡Qué problema! Estoy muy cansad[e]. Cargarla sería el fin para l[e]s dos.{/i}":
                jump herida_abandonar
            "{i}¡No voy a dejarla aquí. La puedo cargar y avanzar con ella más al interior de la isla.{/i}":
                jump herida_cargar
    else:
        $ choice_position = "default" # default alta superior
        menu: 
            "{i}¡Qué problema! Estoy muy cansad[e]. Cargarla sería el fin para l[e]s dos.{/i}":
                jump herida_abandonar
            "{i}¡No voy a dejarla aquí. La puedo cargar y llevarla al claro con Laura.{/i}":
                jump herida_cargar

label herida_playa:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Marina y yo quizás podamos ayudarla. Es la manera de darle mas posibilidades de sobrevivir.{/i}":
            $ desicion_intro += 1
            $ reporte_cargar_ingrid_jungla = True
            $ boton_imagen_character = "ingrid_icon_sangre.png"
            show screen character_top_right_button(boton_imagen_character)
            jump descion_playa
        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump herida_desicion

label herida_abandonar:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Aún no encontré ni comida ni refugio. Debería resolver como sobrevivir antes de ayudar a otros.{/i}" if volverLaura == False:
            $ desicion_intro += 1
            $ reporte_herido_abandona = True
            jump abandonar_ingrid
        "{i}No creo poder llegar con ella al claro con Laura, debería dejarla aquí.{/i}"if volverLaura == True:
            $ reporte_herido_abandona = True
            $ desicion_intro += 1
            jump abandonar_ingrid
        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump herida_desicion

label herida_cargar:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Espero encontrar refugio y algo de alimento o quizás no sobreviva ningun[e] de los dos.{/i}" if volverLaura == False:
            #show ingrid at boton personaje
            $ boton_imagen_character = "ingrid_icon_sangre.png"
            show screen character_top_right_button(boton_imagen_character)
            $ desicion_intro += 1
            $ reporte_cargar_ingrid_jungla2 = True
            jump p1_cargar_jungla
        
        "{i}Espero poder cargar con ella de vuelta al claro con Laura o quizás no sobreviva ningun[e] de l[e]s dos.{/i}" if volverLaura == True:
            #show ingrid at boton personaje
            $ boton_imagen_character = "ingrid_icon_sangre.png"
            show screen character_top_right_button(boton_imagen_character)
            $ desicion_intro += 1
            $ reporte_cargar_ingrid_jungla2 = True
            jump p1_cargar_jungla

        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump herida_desicion

label abandonar_ingrid:
    $ renpy.hide_screen("character_top_right_button")
    $ renpy.with_statement(Dissolve(1.0))
    if volverLaura == False:
        y "{i}Debo encontrar refugio y comida, luego veré de volver por ella.{/i}"
    else:
        y "{i}Mejor hago de cuenta que no la encontré, luego veré de volver por ella.{/i}"
    $ desicion_intro += 1
    $ reporte_herido_abandona2 = True 
    jump p1encuentroJungla

label descion_playa:
    scene bg beach storm at truecenter
    with Dissolve(.5)
    $ boton_imagen_character = "ingrid_icon_sangre.png"
    show screen character_top_right_button(boton_imagen_character)
    # show ingrid cargando at truecenter
    # with Dissolve(0.5)

    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)

    y "{i}Volver hasta la playa ha sido muy difícil cargando con ella.{/i}"
    jump p1_playa_ingrid

label p1_playa_ingrid:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}No puedo seguir cargando con ella. No reacciona y me estoy quedando sin fuerzas.{/i}":
            jump playa_abandonar
        "{i}Un esfuerzo más, no me voy a rendir ahora. Tenemos que salvarnos los dos.{/i}":
            jump playa_cargar

label playa_abandonar:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Nunca debí haberme arriesgado, la voy a dejar aqui.{/i}":
            $ desicion_intro += 1
            $ reporte_herido_abandona3 = True
            jump ingrig_abandonada_playa
        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump p1_playa_ingrid

label ingrig_abandonada_playa:
    $ renpy.hide_screen("character_top_right_button")
    $ renpy.with_statement(Dissolve(1.0))

    y "{i}Debo volver a meterme al interior de la isla, tengo que encontrar refugio y alimento.{/i}"
    y "{i}Mejor buscar otro camino esta vez.{/i}"
    jump p1encuentroJungla


label playa_cargar:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}No sé si me darán las fuerzas para encontrar ayuda pero no la voy a dejar aca.{/i}":
            $ desicion_intro += 1
            $ reporte_ayudar_ingrid = True
            jump p1_ingrid_marina
        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump p1_playa_ingrid

label p1_ingrid_marina:
    show bg beach storm1 at truecenter
    with Dissolve(.5)
    show marina preocupada at right
    with Dissolve(.5)

    m "¿Está muy herida? ¿Que le pasó? Traeré ayuda."
    
    m "¡Capitán Bob! ¡Estos supervivientes necesitan ayuda! ¡Ven pronto!" 
    show bob gr serio sucio  at leftgr
    with Dissolve(.5)
    b "¿Están herid[e]s?"
    b "Tu pareces estar bien."
    b "Déjame revisarla a ella, puedo darle primeros auxilios."
    pause(1.0)
    $ boton_imagen_character = "ingrid_icon_firstaid.png"
    show screen character_top_right_button(boton_imagen_character)
    b "Por ahora debería ser suficiente, el sangrado se ha detenido, pero está delicada."
    pause(1.0)
    m "Necesita agua y refugio." 
    if reporte_grupo == False:
        b "[nombre_personaje], me alegra que tú estés bien."
        show marina gr preocupada at rightgr
        m "Definitivamente te juzqué mal por haberte quedado juntando cosas en lugar de buscar sobrevivientes."
        $ marina += 1
    y "Lo importante ahora es buscar en el interior de la isla algún refugio y comida."
    y "Entre los tres podemos cargar con ella."

    hide bob
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    jump p1_claro_grupo_ingrid

label p1_cargar_jungla:
    show bg jungle herida cargar at truecenter
    with Dissolve(0.5)
    $ boton_imagen_character = "ingrid_icon_sangre.png"
    show screen character_top_right_button(boton_imagen_character)
    # show ingrid cargando at truecenter
    # with Dissolve(0.5)

    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)

    y "{i}La selva está cada vez mas densa y la cabeza me da vueltas. Estoy agotad[e].{/i}"
    jump p1_cargar_desicion

label p1_cargar_desicion:
    show bg jungle herida cargar at truecenter
    with Dissolve(0.5)
    #show ingrid cargando at truecenter
    #with Dissolve(0.5)
    $ choice_position = "default" # default alta superior
    menu:
        "{i}No puedo seguir cargado con ella. No reacciona y me estoy quedando sin fuerzas.{/i}":
            jump cargando_abandonar
        "{i}Un esfuerzo más, no me voy a rendir ahora. Tenemos que salvarnos los dos.{/i}":
            jump cargando_cargar

label cargando_abandonar:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Nunca debí haberme arriesgado, la voy a dejar aquí.{/i}":
            $ desicion_intro += 1
            $ reporte_herido_abandona4 = True
            $ renpy.hide_screen("character_top_right_button")
            $ renpy.with_statement(Dissolve(1.0))
            y "{i}Tengo que encontrar refugio y alimento.{/i}"
            y "{i}Luego veré si puedo volver por ella.{/i}"
            jump p1encuentroJungla
        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump p1_cargar_desicion

label cargando_cargar:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}No sé si me darán las fuerzas para encontrar comida y refugio pero no la voy a dejar acá.{/i}"if volverLaura == False:
            $ desicion_intro += 1
            $ reporte_cargar_ingrid_jungla3 = True
            jump p1_herida_salvada
        "{i}No sé si me darán las fuerzas para regresar al claro con Laura pero no la voy a dejar acá.{/i}"if volverLaura == True:
            $ desicion_intro += 1
            $ reporte_cargar_ingrid_jungla3 = True
            jump p1_herida_salvada
        "{i}No sé si será la mejor alternativa, debería considerar de nuevo mis opciones.{/i}":
            jump p1_cargar_desicion


label p1_bob_salva:
    show laura seria at left
    with Dissolve(.5)

    y "¿Han podido reunir algunas cosas como para armar un refugio?"
    l "Solo unas pocas ramas y algunas hierbas aromáticas."

    $ choice_position = "default" # default alta superior
    menu:
        "Algo es algo. Desde aquí podemos ir buscando un mejor lugar.":
            $ desicion_intro += 1
            $ reporte_reconoce_esfuerzo = True
            $ laura += 1
        "Aquí no vale la pena armar nada, juntar ramas en este lugar es tiempo perdido.":
            $ desicion_intro += 1
            $ reporte_repudia_esfuerzo = True
            $ laura -= 1
    "Se escucha ruido de ramas quebrarse y entra Bob con Ingrid en brazos. Parece estar herida."
    y "¿Qué pasó? ¿Está muy malherida?"

    show bob gr serio sucio at rightgr
    with Dissolve(.5)

    $ bob_salva = True
    b "La encontré en el suelo inconciente y con una herida en la cabeza. Le hice primeros auxilios y paré el sangrado."
    $ boton_imagen_character = "ingrid_icon_firstaid.png"
    show screen character_top_right_button(boton_imagen_character)
    $ renpy.with_statement(Dissolve(1.0))
    b "Ahora necesita descanso y cuidado."

    jump p1_resumen


label p1regresoJunglaGrupo:
    show bg jungle claro at truecenter
    with Dissolve(.5)

    show laura seria at right
    with Dissolve(.5)

    l "¡Más supervivientes, qué alegría!"

    l "Creí que sería Ingrid de regreso, ella fue a buscar algunas frutas y plantas. ¿La han visto?"
    
    if reporte_senderoOculto_grupo == True:
        y "No la hemos visto, encontramos un sendero bastante oculto que nos trajo aquí."
        show bob gr serio sucio at leftgr
        b "Yo voy a buscarla, esperen aquí así no terminamos todos perdidos."
        hide bob
        with Dissolve(.5)
        jump p1_bob_salva
    else:
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        b "Vimos algo raro de camino aqui pero ellos no quisieron explorar."

        $ choice_position = "default" # default alta superior
        menu:
            "Responsabilizar a Marina.":
                y "La que no quiso explorar fue Marina."
                $ desicion_intro += 1
                $ marina -= 1
                $ reporte_acusa_marina = True
                jump p1_BuscarIngrid
            "Reafiimar la desición.":
                y "No sabemos si era Ingrid, podía tratarse de la presa herida de algún depredador."
                $ desicion_intro += 1
                $ reporte_admite_no_saber = True
                jump p1_BuscarIngrid

            "Poner a Bob en su lugar.":
                y "El momento para insistir ya pasó Bob. La decisión fue tomada en grupo."
                y "No es justo que nos culpes a Marina y a mi."
                $ desicion_intro += 1
                $ reporte_objetar_bob = True
                $ bob -= 1  
                jump p1_BuscarIngrid

label p1_herida_salvada:
    show bg jungle claro at truecenter
    with Dissolve(.5)

    show laura seria at right
    with Dissolve(.5)

    if volverLaura == True:
        l "¿Ingrid? ¿Está muy herida?"
        y "La encontré en el suelo, inconsciente. Tiene una herida en la cabeza y está sangrando. La traje para aquí tan pronto como pude."
        l "La salvaste al ir a buscarla, habría muerto sola en la jungla."
        $ desicion_intro += 1
        $ reporte_ayudar_ingrid2 = True
        $ laura += 2
        y "Veamos si podemos detener el sangrado. Yo no sé mucho de primeros auxilios."
    else:
        l "¡[nombre_personaje]!¿Ingrid? ¿Qué le pasó?"
        y "La encontre en el suelo, inconsciente. Tiene una herida en la cabeza y está sangrando. La traje para aqui tan pronto como pude."
        l "Estaba muy preocupada por ella, se fué a buscar frutas hace rato."
        l "Qué suerte que lograste llegar a la costa. No sabíamos si alguien más lo habia logrado."
        y "Me alegra que ustedes dos se hayan salvado también. Vi a Marina en la playa más temprano, ella está bien también."
        $ desicion_intro += 1
        $ reporte_ayudar_ingrid2 = True
        $ laura += 1
        y "Veamos si podemos detener el sangrado. Yo no sé mucho de primeros auxilios."
    "Bob entra de pronto al claro, avanzando entre los arbustos con dificultad."
    b "Pero yo si, déjenme ayudar."
    show bob gr serio sucio at leftgr
    with Dissolve(.5)
    b "Permítanme ver sus heridas."
    if reporte_grupo == True:
        b "Veo que irte solo fué una buena idea al final de cuentas. Ingrid ha tenido mucha suerte de que la encontraras"
    else: 
        y "¿Capitán Bob? Que suerte que estés aquí. ¿Hás visto otros supervivientes?"
        b "Me encontré con Marina, ella me dijo que te había visto. Viene un poco más atrás."
        b "¡Qué suerte que hayas llegado tu también a la costa!"
    hide laura
    with Dissolve(.5)
    b "Ha parado el sangrado, ahora necesita descanso y cuidados."
    $ boton_imagen_character = "ingrid_icon_firstaid.png"
    show screen character_top_right_button(boton_imagen_character)
    $ renpy.with_statement(Dissolve(1.0))

    hide bob
    with Dissolve(.5)

    show marina preocupada at right
    with Dissolve(.5)
    m "Qué suerte que Bob sabe de primeros auxilios, espero que pueda salvar a Ingrid."

    show laura seria at left
    with Dissolve(.5)
    l "Si no fuera por [nombre_personaje], ni si quiera habría tenido la chance de intentarlo.."

    show marina gr preocupada at rightgr
    if reporte_intro_status == "cosas":
        m "Definitivamente te juzgué mal por preocuparte más por las cosas en la playa que por los supervivientes."
        $ marina += 1
    else:
        m "Parece que hás estado en el lugar correcto, en el momento justo."
    show laura gr enojada at leftgr
    with Dissolve(.5)
    l "Sin su ayuda Ingrid seguramente hubiera muerto en la jungla."
    $ marina += 1
    m "No debí juzgarte, [nombre_personaje]. Discúlpame."

    jump p1_resumen

label p1islaplayasolo:
    hide bob
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    show bg beach storm1 at truecenter
    with Dissolve(.5)
    pause (1)
    y "{i}Debo encontrar refugio, no puedo quedarme aquí en la playa.{/i}"
    jump p1playasolo_volver

label p1playasolo_volver:
    $ choice_position = "default" # default alta superior
    menu:
        "{i}Debería volver sobre mis pasos. Es más fácil ir por un lugar conocido.{/i}":
            jump p1rastroSangreVolver
        "{i}Mejor buscar otro camino al interior de la isla, quizás encuentre algo útil.{/i}":
            jump p1encuentroJungla

label p1rastroSangreVolver:
    show bg jungle1 blood zoom at truecenter
    with Dissolve(0.3)

    y "{i}Aquí esta la mancha de sangre que vimos con Marina y Bob.{/i}"

    $ choice_position = "default" # default alta superior
    menu:
        "{i}Debería tratar de alcanzar y ayudar a Bob y Marina.{/i}":
            $ desicion_intro += 1
            $ reporte_seguir_sangre3 = True
            jump p1herido_volver
        
        "{i}Donde hay sangre hay problemas, mejor seguir adelante.{/i}":
            $ desicion_intro += 1
            $ reporte_ignorar_sangre3 = True
            $ reporte_grupo_separado = True
            jump p1encuentroJungla

label p1herido_volver:
    show bg jungle herida cargar at truecenter
    with Dissolve(0.5)
    show marina preocupada at right
    with Dissolve(.5)
    show bob saludando sucio  at left
    with Dissolve(.5)

    y "¡Bob! ¡Marina! Voy con ustedes, quizás pueda ayudar."
    $ bob += 1
    $ marina += 1
    $ reporte_grupo_separado = False

    m "Qué bueno que cambiaras de opinión. ¡Vamos!"
    if verSangre == False:
        show bob serio gr sucio at leftgr
        b "Encontramos un rastro de sangre, lo estamos siguiendo."
        show marina gr preocupada at rightgr
        m "Tal vez sea de algún otro superviviente. Apuesto a que necesita ayuda."
        y "Sigamos el rastro entonces. ¡Vamos!"
        hide bob
        with Dissolve(0.5)
        hide marina
        with Dissolve(0.5)

    jump p1_herido_grupo

label p1_herido_grupo:
    hide marina
    hide bob
    show bg jungle herida  at truecenter
    with Dissolve(0.5)
    y "¡Allí está! ¿Estará viva?"
    show bg jungle herida zoom  at truecenter
    y "¡Si! Está viva, pero inconciente y malherida. Tiene un golpe muy feo en la cabeza."
    show bob gr serio sucio  at leftgr
    with Dissolve(.5)
    b "¿Está herida? Déjame revisarla, puedo darle primeros auxilios."
    pause(1.0)
    $ boton_imagen_character = "ingrid_icon_firstaid.png"
    show screen character_top_right_button(boton_imagen_character)
    b "Por ahora debería ser suficiente, el sangrado se ha detenido."
    pause(1.0)
    b "Pero aún esta delicada, necesita agua y refugio."
    y "Sigamos avanzando, la podemos llevar entre los tres."
    hide bob
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    jump p1_claro_grupo_ingrid

label p1_claro_grupo_ingrid:
    show bg jungle claro at truecenter
    with Dissolve(.5)

    show laura sonriendo at right
    with Dissolve(.5)

    l "¡Bob! ¡[nombre_personaje]! ¡Marina! ¡Qué alegría verlos!" 
    show laura hablando at right
    with Dissolve(.5)
    l "¿Ingrid? ¿Está herida?"

    l "Se fué hace un rato a buscar frutas y plantas. ¿Qué le pasó? ¿Dónde la encontraron?"

    $ choice_position = "default" # default alta superior
    menu:
        "Estoy muy cansad[e] como para aguantar este interrogatorio. Ojalá se callara.":
            y "Las preguntas deben esperar, ¿no ves que Ingrid necesita ayuda? Bob, Marina, recostémosla aquí."
            $ desicion_intro += 1
            $ reporte_callar_laura = True
            $ laura -= 1  
            show laura gr enojada at rightgr
            with Dissolve(0.5)
            l "Solo estoy preocupada, podrías mostrar más empatía tu también, ¿no?"
            y "Ahora no, luego podremos conversar."
            hide laura 
            with Dissolve(0.5)
            hide bob
            with Dissolve(0.5)
            hide marina
            with Dissolve(0.5)
            jump p1_resumen

        "Tratemos de ver que recursos tenemos y que Ingrid esté en un lugar donde pueda recuperarse.":
            y "Ingrid esta bien, al menos por ahora. Ayúdame a recostarla. ¿Tenemos agua o comida? ¿Se pudo salvar algo?"
            $ desicion_intro += 1
            $ reporte_orden_en_el_claro = True
            hide laura 
            with Dissolve(0.5)
            hide bob
            with Dissolve(0.5)
            hide marina
            with Dissolve(0.5)
            jump p1_resumen

        "Laura está muy preocupada, debería tranquilizarla para que pueda ayudar a organizarnos.":
            y "Laura, mírame. Ingrid estará bien. La encontramos inconsciente, hace poco, no muy lejos de aquí. ¿Puédes ayudarnos?"
            $ laura += 1
            $ desicion_intro += 1
            $ reporte_tranquilizar_laura = True
            hide laura 
            with Dissolve(0.5)
            hide bob
            with Dissolve(0.5)
            hide marina
            with Dissolve(0.5)      
            jump p1_resumen
    
    label p1_resumen:
        hide laura 
        with Dissolve(0.5)
        hide bob
        with Dissolve(0.5)
        hide marina
        with Dissolve(0.5)
        "Unos cuantos supervivientes se han logrado reunir en un claro en el interior de la isla."
        "Luego de dejar a Ingrid en un lugar cómodo y repasar como llegó cada uno hasta allí, es claro que carecen prácticamente de todo."
        "Hay muchas preguntas pendientes y algunas miradas de reproche o suspicacia, pero para todos encontrar refugio y comida parece ser lo más urgente."
        "Laura va a cuidar de Ingrid mientras los demás buscan algun lugar seguro donde pasar la noche."
        jump final




label final:
    hide bob
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)

    pause 1.5
    # Generar contenido para los pop-ups de relaciones
    $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura"], es_relacion=True)
    $ relaciones_cap2_bob = bob
    $ relaciones_cap2_marina = marina
    $ relaciones_cap2_laura = laura
    
    # Calcular el total de decisiones y obtener la lista de variables específicas para la introducción
    $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
    
    # Generar contenido para los pop-ups de decisiones
    $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

    # Mostrar los pop-ups
    show screen relaciones_popup(contenido=relaciones_contenido)
    show screen decisiones_popup(contenido=decisiones_contenido)
    
    "Aquí termina el capitulo, pero la historia aún tiene grandes desafíos y muchas decisiones de las que depende la superviviencia del grupo."
    # Ocultar los pop-ups con dissolve
    hide screen relaciones_popup with dissolve
    hide screen decisiones_popup with dissolve
    $ choice_position = "default" # default alta superior
    menu:
        "CONTINUAR":
            jump chapter_3_start
        "VOLVER A VER EL RESÚMEN":
            jump final
############################################   #######   ########   ################################################################################################
############################################   #######   ########   ################################################################################################
## Aca comienza la PARTE 3 #################   #######   ########   ################################################################################################
############################################   #######   ########   ################################################################################################

label chapter_3_start:
    # Inicializar el capítulo actual
    $ capitulo_actual = 2
    $ compartido = False
    scene bg jungle claro at truecenter
    with Dissolve(.5)

    "La tormenta finalmente ha pasado, pero la isla sigue siendo peligrosa. El grupo necesita encontrar refugio y recursos para sobrevivir."

    show marina triste at right
    with Dissolve(.5)

    m "Necesitamos encontrar un lugar seguro para quedarnos. La tormenta podría regresar y no podemos quedarnos a la intemperie."

    show bob parado serio at left
    with Dissolve(.5)

    b "De acuerdo. Vamos a dividirnos y buscar un refugio adecuado. Nos reuniremos aquí en una hora."

    jump choose_partner

label choose_partner:

    $ choice_position = "default" # default alta superior
    menu:
        "Buscar en la parte norte de la isla con Marina.":
            y "Marina, exploramos l[e]s dos? Es más seguro."
            $ desicion_intro += 1
            $ reporte_fue_con_marina = True
            if marina >= 0:
                $ colaboración_mas[capitulo_actual] += 1
                $ marina += 1
                jump check_marina
            else:
                m "Prefiero que no vayamos junt[e]s."
                hide marina
                with Dissolve(.5)
                jump choose_partner_no_marina

        "Buscar en la parte sur de la isla con Bob.":
            y "¿Qué te parece si exploramos los dos?"
            $ desicion_intro += 1
            $ reporte_fue_con_bob = True
            if bob >= 0:
                $ bob += 1
                $ colaboración_mas[capitulo_actual] += 1
                jump check_bob
            else:
                b "Prefiero ir solo."
                hide bob
                with Dissolve(.5)
                jump choose_partner_no_bob

        "Buscar en la parte oeste de la isla sol[e].":
            y "Iré sol[e]. Veré que encuentro por mi lado."
            $ desicion_intro += 1
            $ reporte_fue_solo = True
            $ colaboración_menos[capitulo_actual] += 1
            jump search_west

label choose_partner_no_marina:
    menu:
        "Buscar en la parte sur de la isla con Bob.":
            y "¿Qué te parece si exploramos los dos?"
            $ desicion_intro += 1
            $ reporte_fue_con_bob = True
            if bob >= 0:
                $ bob += 1                
                $ colaboración_mas[capitulo_actual] += 1
                jump check_bob
            else:
                b "Prefiero que no vayamos juntos."
                hide bob
                with Dissolve(.5)
                jump search_solo

        "Buscar en la parte oeste de la isla sol[e].":
            y "Iré sol[e]. Veré que encuentro por mi lado."
            $ desicion_intro += 1
            $ reporte_fue_solo = True
            $ colaboración_menos[capitulo_actual] += 1
            jump search_west

label choose_partner_no_bob:
    $ choice_position = "default" # default alta superior
    menu:
        "Buscar en la parte norte de la isla con Marina.":
            y "Marina, exploramos l[e]s dos? Es más seguro."
            $ desicion_intro += 1
            $ reporte_fue_con_marina = True
            if marina >= 0:
                $ colaboración_mas[capitulo_actual] += 1
                $ marina += 1
                jump check_marina
            else:
                m "Prefiero que no vayamos juntos."
                hide marina
                with Dissolve(.5)
                jump search_solo

        "Buscar en la parte oeste de la isla sol[e].":
            y "Iré sol[e]. Veré que encuentro por mi lado."
            $ desicion_intro += 1
            $ reporte_fue_solo = True
            $ colaboración_menos[capitulo_actual] += 1
            jump search_west

label search_solo:
    $ choice_position = "default" # default alta superior
    menu:
        "Buscar en la parte oeste de la isla sol[e].":
            y "Iré sol[e] entonces. Puedo investigar perfectamente por mi cuenta."
            jump search_west

label check_marina:
    if marina < 0:
        m "Prefiero que no vayamos juntos. Disculpa, mejor voy sola."
        hide marina
        with Dissolve(.5)
        jump choose_partner_no_marina
    else:
        jump search_north

label check_bob:
    if bob < 0:
        b "Creo que no funcionamos muy bien juntos. Mejor voy por mi cuenta."
        hide bob
        with Dissolve(.5)
        jump choose_partner_no_bob
    else:
        jump search_south

label search_north:
    scene bg jungle1 1 at truecenter
    with Dissolve(.5)

    show marina hablando at right
    with Dissolve(.5)
    $ search_north = True 
    m "La parte norte de la isla parece densa. Podríamos encontrar una cueva o algún refugio natural."

    "Tú y Marina avanzan a través de la espesa vegetación buscando un refugio."

    $ choice_position = "default" # default alta superior
    menu:
        "Seguir buscando a pesar del terreno difícil.":
            y "Vamos Marina, los demás también cuentan con nosotros. Sigamos aunque la zona sea difícil."
            if cansancio < 3:
                $ update_stat("cansancio", cansancio - 1)
                $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
                hide screen combined_ui
                show screen combined_ui
            $ desicion_intro += 1
            $ reporte_esfuerzo_adicional = True
            $ compromiso_mas[capitulo_actual] += 1
            jump find_cave

        "Sugerir regresar al punto de encuentro.":
            y "Mejor volvamos, nos estamos agotando y los otros quizás hayan encontrado algo"
            $ desicion_intro += 1
            $ honestidad_mas[capitulo_actual] += 1
            $ reporte_regresar_busqueda = True
            jump return_meeting_point

label find_cave:
    scene bg jungle cave at truecenter
    with Dissolve(.5)

    "Tú y Marina encuentran una pequeña cueva escondida detrás de unos arbustos. Parece que podría proporcionar un buen refugio."

    m "Esto parece prometedor. Deberíamos traer a los demás aquí."

    jump return_meeting_point

label search_south:
    scene bg jungle1 1 at truecenter
    with Dissolve(.5)

    show bob pensando at left
    with Dissolve(.5)
    $ search_south = True

    b "La parte sur de la isla podría tener algunas estructuras antiguas o ruinas. Vamos a revisar."

    "Tú y Bob avanzan con cautela, buscando un refugio."

    $ choice_position = "default" # default alta superior
    menu:
        "Investigar una vieja cabaña abandonada.":
            y "Esta cabaña está bastante ruinosa, pero es una opción segura. Veamos como está por dentro y volvamos."
            $ desicion_intro += 1
            $ reporte_investigar_cabaña = True
            $ responsabilidad_mas[capitulo_actual] += 1
            $ bob += 1
            jump find_hut

        "Seguir buscando una mejor opción.":
            y "La cabaña no se va a ir de aquí, busquemos un poco más por si escontramos algo mejor."
            $ desicion_intro += 1
            $ reporte_buscar_mejor_refugio = True
            $ colaboración_mas[capitulo_actual] += 1
            jump find_better_shelter

label find_hut:
    scene bg jungle hut at truecenter
    with Dissolve(.5)

    "Exploran junto a Bob la vieja cabaña abandonada. Está bastante deteriorada, pero podría servir como refugio temporal."

    b "Esto servirá por ahora. Vamos a reunir a los demás."

    jump return_meeting_point

label find_better_shelter:
    scene bg jungle1 1 at truecenter
    with Dissolve(.5)

    "Tú y Bob deciden seguir buscando, esperando encontrar algo mejor."

    if cansancio < 3:
        $ actualizar_boton_imagen()
        $ update_stat("cansancio", cansancio - 1)
        $ show_variable_changed_popup("El cansancio ha aumentado", rojo)           
        # Ocultar y volver a mostrar la pantalla para actualizar la imagen
        hide screen combined_ui
        show screen combined_ui

    b "Por aquí no hay nada."
    y "Tienes razón Bob, la cabaña puede ser nuestra mejor opción. Volvamos con los demás."

    jump return_meeting_point

label search_west:
    scene bg jungle1 1 at truecenter
    with Dissolve(.5)
    $ search_west = True

    "Decides buscar en la parte oeste de la isla sol[e], esperando encontrar algo útil."

    $ choice_position = "default" # default alta superior
    menu:
        "{i}Podría subir esa colina escarpada para tener una mejor vista de los alrededores.{/i}":
            $ desicion_intro += 1
            $ integridad_mas[capitulo_actual] += 1
            $ reporte_fue_a_colina = True
            jump climb_hill

        "{i}A lo largo de la costa podría encontrar algunas cosas del naufragio arrastrados por el mar.{/i}":
            $ desicion_intro += 1
            $ responsabilidad_mas[capitulo_actual] += 1
            $ reporte_fue_a_playa = True
            jump search_coastline

label climb_hill:
    scene bg jungle hill at truecenter
    with Dissolve(.5)

    "Subes una colina para tener una mejor vista de la isla. Desde la cima, vés un posible refugio a lo lejos."

    "Tomas nota mental de la ubicación y regresas al punto de encuentro."

    jump return_meeting_point

label search_coastline:
    scene bg beach storm1 at truecenter
    with Dissolve(.5)

    "Buscas a lo largo de la costa y encuentras algunos suministros arrastrados por el mar que podrían ser útiles."

    $ choice_position = "default" # default alta superior
    menu:
        "Recoger el bote salvavidas." if not stuff_bote:
            $ stuff_bote = True
            $ boton_imagen = "bote_icon.png"
            show screen top_right_button(boton_imagen)
            jump return_meeting_point

        "Recoger la caja de madera cerrada." if not stuff_caja_grande:
            $ stuff_caja_grande = True
            $ boton_imagen = "caja_icon.png"
            show screen top_right_button(boton_imagen)
            jump return_meeting_point

        "Recoger el bidón de agua lleno." if not stuff_bidon_agua:
            $ stuff_bidon_agua = True
            $ agua += 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            jump beber_agua

label beber_agua:
    if sed < 3:
        $ choice_position = "default" # default alta superior
        menu:
            "Debería beber algo de agua, estoy con la garganta seca.":
                pause 0.5
                "Glup... glup... glup..."
                pause 0.5
                $ agua -= 4
                $ actualizar_boton_imagen()
                $ update_stat("sed", sed + 1)
                $ show_variable_changed_popup("La sed ha disminuido", verde)
                hide screen combined_ui
                show screen combined_ui
                jump beber_agua

            "Mejor reservar el agua. Quizás sea muy difícil conseguir agua potable en la isla.":
                jump return_meeting_point
    else:
        $ choice_position = "default" # default alta superior
        menu:
            "Mejor reservar el agua. Quizás sea muy difícil conseguir agua potable en la isla.":
                jump return_meeting_point

label return_meeting_point:
    scene bg jungle claro at truecenter
    with Dissolve(.5)

    show marina sonriendo at right
    with Dissolve(.5)

    show bob parado hablando at left
    with Dissolve(.5)

    b "Hay una vieja cabaña abandonada en la parte sur. Está bastante deteriorada, pero tiene algunos elementos útiles y podría servir como refugio temporal."

    if reporte_regresar_busqueda == True:
        show marina preocupada at right
        with Dissolve(.5)
        m "[nombre_personaje] sugirió que volviéramos. No hemos encontrado nada."
    else:  
        show marina hablando at right
        with Dissolve(.5)
        m "También hay una cueva en la parte norte de la isla. Es fresca en el interior, lo cual es perfecto porque me estoy sintiendo mal por tanto calor en esta isla."
    
    if search_west: 
        b "¿Cómo te fué a ti, [nombre_personaje]?"
        
        if reporte_fue_a_colina:
            y "Subí una colina y vi un claro a lo lejos, junto a una saliente, donde podríamos hacer un refugio."
            jump decide_shelter
        else:
            y "Llegué hasta la costa y estuve buscando algunos restos del naufragio."
            m "¿Y..? ¿Encontraste algo?"
            jump como_te_fue
    else:
        jump decide_shelter

label como_te_fue:
    if desicion_intro < 1000:
        $ choice_position = "default" # default alta superior
        menu:
            "Las cosas que encontré van a ser claves para que todo el grupo pueda sobrevivir.":
                y "Encontré algunos suministros arrastrados por el mar a lo largo de la costa. Podrían ser útiles."
                b "Muy buenas noticias, sin duda serán útiles."
                $ desicion_intro += 1
                $ reporte_celebra_recursos = True
                $ honestidad_mas[capitulo_actual] += 1
                jump decide_shelter

            "Mejor ocultar lo que encontré para usarlo solo o al menos para poder decidir qué hacer luego.":
                y "No encontré nada útil. Lo siento."
                m "Qué mala suerte, aún estamos sin refugio y sin recursos."
                $ desicion_intro += 1
                $ reporte_oculta_recursos = True
                $ integridad_menos[capitulo_actual] += 1
                jump decide_shelter

label decide_shelter:
    y "Hay que decidir dónde hacer el refugio."
    if search_west: 
        $ choice_position = "alta" # default alta superior
        menu:
            "Mejor hacer el refugio en la cueva que encontró Marina.": 
                $ marina += 1
                $ bob -= 1
                $ desicion_intro += 1
                $ reporte_refugio_cueva = True
                $ integridad_mas[capitulo_actual] += 1
                jump setup_cave

            "Sin duda la cabaña que encontró Bob es la mejor opción.":
                $ bob += 1
                $ marina -= 1
                $ desicion_intro += 1
                $ reporte_refugio_cabaña = True
                $ integridad_mas[capitulo_actual] += 1
                jump setup_hut

            "Desde el claro podremos ver al mar por si llega el rescate. Mejor armar un refugio allí." if reporte_fue_a_colina:
                $ desicion_intro += 1
                $ reporte_refugio_claro = True
                $ responsabilidad_mas[capitulo_actual] += 1
                $ marina -= 1
                $ bob -= 1
                jump setup_clearing
    else:
        $ choice_position = "default" # default alta superior
        menu:
            "Mejor hacer el refugio en la cueva que encontramos con Marina." if search_north:
                $ marina += 1
                $ bob -= 1
                $ desicion_intro += 1
                $ reporte_refugio_cueva = True
                $ integridad_mas[capitulo_actual] += 1
                jump setup_cave

            "Sin duda la cabaña que encontramos con Bob es la mejor opción." if search_south:
                $ bob += 1
                $ marina -= 1
                $ integridad_mas[capitulo_actual] += 1
                $ desicion_intro += 1
                $ reporte_refugio_cabaña = True
                jump setup_hut
            
            "Sin duda la cabaña que encontró Bob es la mejor opción." if search_north:
                $ bob += 1
                $ marina -= 1
                $ integridad_mas[capitulo_actual] += 1
                $ desicion_intro += 1
                $ reporte_refugio_cabaña = True
                jump setup_hut
            
            "Mejor hacer el refugio en la cueva que encontró Marina." if search_south:
                $ marina += 1
                $ bob -= 1
                $ desicion_intro += 1
                $ reporte_refugio_cueva = True
                $ integridad_mas[capitulo_actual] += 1
                jump setup_cave


label setup_cave:
    scene bg jungle cave at truecenter
    with Dissolve(.5)

    $ refugio = "cueva"

    "Tú y el grupo establecen un refugio en la cueva. No es perfecto, pero los mantendrá a salvo por ahora."

    "El grupo se instala, preparándose para los desafíos que se avecinan."

    jump chapter_3_end

label setup_hut:
    scene bg jungle hut at truecenter
    with Dissolve(.5)

    $ refugio = "cabaña"

    "Tú y el grupo establecen refugio en la cabaña. Necesita algunas reparaciones, pero servirá por ahora."

    "El grupo se instala, preparándose para los desafíos que se avecinan."

    jump chapter_3_end

label setup_clearing:
    scene bg jungle hill at truecenter
    with Dissolve(.5)

    $ refugio = "claro"

    "Tú y el grupo establecen refugio en el claro. Está abierto, pero la saliente natural proporciona algo de protección."

    "El grupo se instala, preparándose para los desafíos que se avecinan."

    jump chapter_3_end

label chapter_3_end:
    "Esto concluye el Capítulo 3. El grupo ha encontrado refugio, pero aún quedan muchos desafíos por delante y un giro inesperado de la historia."

    # Generar contenido para los pop-ups de relaciones
    $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura"], es_relacion=True)
    $ relaciones_cap3_bob = bob
    $ relaciones_cap3_marina = marina
    $ relaciones_cap3_laura = laura
    
    # Calcular el total de decisiones y obtener la lista de variables específicas para la introducción
    $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
    
    # Generar contenido para los pop-ups de decisiones
    $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

    # Mostrar los pop-ups
    show screen relaciones_popup(contenido=relaciones_contenido)
    show screen decisiones_popup(contenido=decisiones_contenido)
        
    # Ocultar los pop-ups con dissolve
    hide screen relaciones_popup with dissolve
    hide screen decisiones_popup with dissolve
    $ choice_position = "default" # default alta superior
    menu:
        "CONTINUAR":
            jump chapter_4_start
        "VOLVER A VER EL RESÚMEN":
            jump chapter_3_end

    return
############################################   #######   #######   #######   ##########################################################################################
############################################   #######   #######   #######   ##########################################################################################
## Aca comienza la PARTE 4 #################   #######   #######   #######   ##########################################################################################
############################################   #######   #######   #######   ##########################################################################################

label chapter_4_start:
    # Inicializar el capítulo actual
    $ capitulo_actual = 3

    if refugio == "cabaña":
        jump refugio_cabaña
    if refugio == "cueva":
        jump refugio_cueva
    if refugio == "claro":
        jump refugio_claro

label refugio_cabaña:
    scene bg jungle hut at truecenter
    with Dissolve(.5)
    jump refugio_init

label refugio_cueva:
    scene bg jungle cave at truecenter
    with Dissolve(.5)
    jump refugio_init

label refugio_claro:
    scene bg jungle clearing at truecenter
    with Dissolve(.5)
    jump refugio_init

label refugio_init:
    y "No es un hotel cinco estrellas, pero debería servir por ahora."
    if stuff_bidon_agua == True:
        $ update_stat("sed", sed - 1)
        $ show_variable_changed_popup("La sed ha aumentado", rojo)
        # Ocultar y volver a mostrar la pantalla para actualizar la imagen
        hide screen combined_ui
        show screen combined_ui
        jump beber_bidon # label en cap 1 detecta si es cap 0 o 4
    else:
        $ update_stat("hambre", hambre - 1)
        $ show_variable_changed_popup("El hambre ha aumentado", rojo)
        # Ocultar y volver a mostrar la pantalla para actualizar la imagen
        hide screen combined_ui
        show screen combined_ui
        jump init_buscar_comida

    

label refugio_init_sed:
        show bob saludando sucio at left
        with Dissolve(.5)
        b "[nombre_personaje], todos estanmos sedientos, ¿podrías compartir el agua que encontraste?"

        $ choice_position = "alta" # default alta superior
        menu:
            "Aún no encontramos otra fuente de agua, hay que racionarla.":
                y "Todos podemos beber un poco, pero solo un trago."
                y "hasta no encontrar agua potable, hay que cuidar la que nos queda."
                b "Tienes razón, si no la cuidamos, estaremos en problemas."
                $ desicion_intro += 1
                $ reporte_racionar_agua = True
                $ bob +=1
                jump refugio_init_reparten_agua
            "El agua es mia y es valiosa. Ellos van a desperdiciarla.":
                y "Yo me esforcé para conseguirla, yo decidiré cuando y cómo se usa."
                b "Es realmente increíble que seas tan egoista."
                $ desicion_intro += 1
                $ reporte_acaparar_agua = True
                $ bob -=1
                jump bob_discusion_agua
            "Bob no ha sido un gran compañero hasta ahora, no merece que lo ayude." if bob < 0:
                y "Tú deberías buscar tu propia agua, Bob."
                b "¿Tu propia agua? Ese bidón pertenecía a mi barco."
                y "Tu barco, el que se hundió bajo tu mando."
                b "¿Cuál es tu problema?"
                $ desicion_intro += 1
                $ reporte_acaparar_agua = True
                jump bob_discusion_agua

label bob_discusion_agua:
    show bob gr serio sucio at leftgr
    with Dissolve(.5)

    b "¿Crees que puedes sobrevivir por tu cuenta en esta isla?"
    b "Esto no es un juego, [nombre_personaje]. ¿No te das cuenta de que aquí nadie se salva solo?"

    $ choice_position = "default" # default alta superior
    menu:
        "Yo encontré el agua, y yo decido qué hacer con ella.":
            y "No me importa lo que pienses, Bob. Yo fui quién encontró el agua, y yo decido cómo usarla."
            show marina gr preocupada at right
            with Dissolve(.5)
            if marina > 0:
                m "Por favor, [nombre_personaje], piensa en el grupo. Sé que no es fácil, pero necesitamos apoyarnos entre todos."
                $ choice_position = "default" # default alta superior
                menu:
                    "Compartiré el agua.":
                        y "Está bien. Tienes razón, Marina. Compartiré el agua con todos."
                        $ desicion_intro += 1
                        $ reporte_reconsidera_racionar_agua_m = True
                        jump refugio_init_reparten_agua
                    "El agua es mía.":
                        y "¿No fuiste tu la que no quería perder tiempo recuperando cosas en la playa, Marina?"
                        y "El agua es mía."
                        $ desicion_intro += 1
                        $ reporte_acaparar_agua_chicana_m = True
                        jump marina_sed
            else:
                m "Esto no está bien. No lo puedo creer [nombre_personaje]."
                m "Necesitamos apoyarnos entre todos, o no saldremos de esta."
                jump marina_sed

        "Bob debería haber buscado su propia agua.":
            y "No es mi problema, Bob. Si querías agua, deberías haberla buscado tú mismo."
            show laura seria at center
            with Dissolve(.5)
            if laura > 0:
                l "[nombre_personaje], esto no es justo. Todos estamos haciendo lo mejor que podemos. Por favor, piénsalo un poco."
                $ choice_position = "default" # default alta superior
                menu:
                    "Compartiré el agua.":
                        y "Tienes razón, Laura. No se en qué estaba pensando. Compartamos el agua."
                        $ desicion_intro += 1
                        $ reporte_reconsidera_racionar_agua_l = True
                        jump refugio_init_reparten_agua
                    "El agua es mía.":
                        y "Lo siento, Laura, pero no puedo hacerlo. El agua es mía."
                        $ desicion_intro += 1
                        $ reporte_acaparar_agua_laura = True
                        jump marina_sed
            else:
                l "Esto no ayuda a nadie. Necesitamos encontrar una forma de trabajar juntos, no de dividirnos más."
                jump marina_sed

        "Será mejor que comparta el agua.":
            y "Está bien, Bob. Compartiré el agua, pero necesitamos encontrar más, y pronto."
            b "Gracias, [nombre_personaje]. Esto es lo que necesitamos: cooperación."
            b "Haré todo lo posible para encontrar más recursos."
            show marina hablando at right
            with Dissolve(.5)
            m "Has hecho lo correcto. Tendremos más posibilidades de sobrevivir si nos mantenemos unidos."
            show laura seria at center
            with Dissolve(.5)
            l "Bien. Espero que no tengamos que volver este tipo de discusiones."
            jump refugio_init_reparten_agua
    jump refugio_init_reparten_agua

label marina_sed:
    show marina preocupada at right
    with Dissolve(.5)

    m "¿Qué clase de persona eres?"
    if marina > 1:
        m "Hás hecho mucho por el grupo, hás tomado buenas desiciones. Hazme caso en esta, tenemos que mantenernos unidos."

        $ choice_position = "default" # default alta superior
        menu:
            "Tu adulación es manipulación, Marina. Esta también es una buena decisión. El agua es mia y no hay mas discusión.":
                m "Está claro que no se puede contar contigo."
                "Marina se aleja furiosa."
                hide marina
                with Dissolve(.5)
                l "Marina, espera..."
                hide laura
                with Dissolve(.5)
                "Ambas se alejan del refugio, se las escucha hablar mientras se internan en la jungla."
                $ desicion_intro += 1
                $ reporte_acusa_adulacion_marina = True
                jump bob_discusion
            "Mmmm Esta bien, pero solo un sorbo. No sabemos cuando encontraremos mas.":
                $ desicion_intro += 1
                $ reporte_reconsidera_racionar_agua_m = True
                jump refugio_init_reparten_agua
    else:
        m "Está claro que no se puede contar contigo."
        "Marina se aleja furiosa."
        hide marina
        with Dissolve(.5)
        l "Marina, espera..."
        hide laura
        with Dissolve(.5)
        "Ambas se alejan del refugio, se las escucha hablar mientras se internan en la jungla."
        jump bob_discusion

label refugio_init_reparten_agua:
    show marina hablando at right
    with Dissolve(.5)
    show laura seria at center
    with Dissolve(.5)
    if agua > 0:
        "Bob y Laura toman unos tragos de agua y pasan el bidón a Marina, que apenas toma un sorbo. Claramente todos quisieran beber un poco más, pero se contienen."
        $ agua = 1
        # Llamar a la función para actualizar la imagen del botón
        $ actualizar_boton_imagen()
        m "Ha quedado poca, deberíamos darle toda el agua que queda a Ingrid para que se recupere."
        b "Estoy de acuerdo, Ingrid lo necesita más que nosotros en este momento." 
        l "No me gusta decir esto pero hay que pensar que quizás ya no podamos ayudar más a Ingrid."
        l "Aún no despierta. Podemos darle agua cuando consigamos más."

        $ choice_position = "alta" # default alta superior
        menu:
            "Debería apoyar a Marina y Bob, en estos casos es mejor mantenerse con la mayoría.":
                y "Estoy con Marina y Bob en esta. Démosle lo que queda."
                $ desicion_intro += 1
                $ reporte_agua_ingrid_bm = True
                jump init_buscar_comida
            "Lo que queda de agua es para Ingrid, ella depende de nosotros.":
                y "Ingrid sobrevivirá si la cuidamos entre todos. Démosle el agua que queda."
                $ desicion_intro += 1
                $ reporte_agua_ingrid_y = True
                jump init_buscar_comida
            "Laura tiene razón, lo que queda de agua puede ser la diferencia para quienes estamos bien.":
                y "Aunque no nos guste hay que pensar en quienes tienen mas chances de sobrevivir. Guardemos el resto del agua hasta que encontremos más."
                show marina gr preocupada at rightgr
                $ desicion_intro += 1
                $ reporte_agua_ingrid_l = True
                if reporte_intro_status == "cosas":
                    if (reporte_cargar_ingrid_jungla or reporte_cargar_ingrid_jungla2 or reporte_cargar_ingrid_jungla3):
                        m "¿Te esforzaste por salvar a Ingrid cargándola hasta la playa y la vas a dejar morir ahora?"
                        m "Creí que te habia juzgado mal pero eres [le] mism[e] egoista que prefirió quedarse a juntar cosas."

                        $ choice_position = "default" # default alta superior
                        menu:
                            "Si no me hubiese quedado, no habría agua, y hasta ahora Marina no ha hecho nada útil.":
                                y "Tenemos agua porque decidí quedarme a buscarla."
                                y "¿Tú que has hecho hasta ahora?"
                                $ desicion_intro += 1
                                $ reporte_agua_ingrid_chicana_m = True
                                jump marina_discusion
                            "Está claro que Marina no va a poder tomar decisiones duras.":
                                y "Marina, esta es una situación desesperada. Debemos pensar en cómo sobrevivir."
                                m "No es así como vamos a sobrevivir. Tenemos que recordar que somos personas."
                                m "Debí esperar esto de ti [nombre_personaje], pero no de ti, Laura."
                                l "Yo solo dije lo que varios pensabamos, nada más."
                                "Marina se aleja furiosa."
                                $ desicion_intro += 1
                                $ reporte_agua_ingrid_decepcion_m = True
                                hide marina
                                with Dissolve(.5)
                                l "¡Marina! Espera..."
                                hide laura
                                with Dissolve(.5)
                                "Marina y Laura se meten en la selva. Se las escucha discutir mientras se alejan."
                                jump bob_discusion
                            "Marina tiene razón, hay que darle una oportunidad a Ingrid.":
                                y "Tranquila Marina, nadie la va a dejar morir."
                                y "Solo pensaba que si los que estamos bien mantenemos las fuerzas, podremos ayudar a Ingrid."
                                y "Pero tienes razón, lo mejor que le demos el agua que queda a Ingrid ahora."
                                $ desicion_intro += 1
                                $ reporte_agua_ingrid_oportunidad = True
                                jump init_buscar_comida
    else:
        "Todos observan el bidón vacio, la sensación de desesperanza crece."
        y "Parece que debemos buscar agua de forma urgente."
        jump init_buscar_comida

label bob_discusion:
    show bob gr parado enojado at leftgr
    with Dissolve(.5)
    b "Me sorprende tu actitud. Estamos todos en la misma situación aquí. Necesitamos apoyarnos."
    y "¿Yo soy el problema?"
    if bob > 2:
        y "Bob, sé que estás haciendo lo mejor que puedes, pero no puedo evitar pensar en quién es el principal responsable de que estemos esta situación."
        show bob gr parado hablando at leftgr
        with Dissolve(.5)
        b "Lo sé, [nombre_personaje]. Como capitán, la responsabilidad recae sobre mí. Pero créeme, estoy haciendo todo lo posible para mantenernos a salvo."

        $ choice_position = "default" # default alta superior
        menu:
            "Tengo confianza en Bob.":
                y "Lo sé, Bob. Confío en ti. Solo necesitaba decir lo que tenía en la cabeza."
                b "Gracias por tu confianza, y también por la comunicación."
                b "Vamos a salir de esta, juntos."
                $ desicion_intro += 1
                $ reporte_discusion_bob_confiar = True
                $ bob += 1
                jump opciones_campamento
            "Pese al esfuerzo, Bob no tiene un buen plan.":
                y "Agradezco tu esfuerzo, pero necesitamos un plan más claro para sobrevivir."
                b "Tienes razón. Vamos a organizarnos mejor. Gracias por señalarlo."
                $ desicion_intro += 1
                $ reporte_discusion_bob_objetar = True
                $ bob += 1
                jump opciones_campamento

    elif bob > 0:
        y "Bob, entiendo que estás asumiendo tu responsabilidad como capitán..."
        y "Pero no puedo evitar sentir que podrías haber hecho más para evitar el naufragio."
        show bob gr parado hablando at leftgr
        with Dissolve(.5)
        b "Entiendo cómo te sientes, [nombre_personaje]. Pero créeme, hice todo lo que estaba en mi poder para evitarlo."

        $ choice_position = "default" # default alta superior
        menu:
            "Trabajemos juntos.":
                y "Olvídalo, lo importante es que estamos vivos y nos tenemos los unos a los otros."
                b "Estoy de acuerdo. Vamos a enfocarnos en lo que podemos hacer ahora."
                $ desicion_intro += 1
                $ reporte_discusion_bob_concordia = True
                $ bob += 1
                jump opciones_campamento
            "Escucha más al equipo.":
                y "Quizás deberías escuchar más las ideas del grupo."
                b "Tienes razón. Estoy dispuesto a escuchar más. Gracias por decírmelo."
                $ desicion_intro += 1
                $ reporte_discusion_bob_sugerencia = True
                $ bob += 0
                jump opciones_campamento

    elif bob == 0:
        y "Bob, no quiero sonar duro, pero parece que te gusta dar órdenes. ¿No crees que deberíamos decidir las cosas entre todos?"
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        b "Entiendo tu punto, [nombre_personaje]. Pero alguien tiene que tomar decisiones rápidas en situaciones como esta."

        $ choice_position = "default" # default alta superior
        menu:
            "Bob debería consultar con el grupo.":
                y "Quizás, pero deberías consultar más con el grupo."
                b "Tienes razón. Intentaré hacerlo mejor."
                $ desicion_intro += 1
                $ reporte_discusion_bob_sugerencia = True
                $ bob += 0
                jump opciones_campamento
            "Bob no es un buen líder.":
                y "No estoy seguro de que seas la mejor persona para liderar."
                b "Eso es algo que podemos discutir cuando estemos todos."
                $ desicion_intro += 1
                $ reporte_discusion_bob_inapto = True
                $ bob -= 1
                jump opciones_campamento

    elif bob < 0:
        y "Bob, no puedo creer que sigas actuando como si fueras el jefe después de llevarnos a este desastre."
        show bob gr parado enojado at leftgr
        with Dissolve(.5)
        b "Sé que estás molesto, [nombre_personaje], pero no es momento para condenarme. Necesito que colabores conmigo."

        $ choice_position = "default" # default alta superior
        menu:
            "Bob sólo quiere que lo sigan.":
                y "¿Que colabore contigo? Tú sigues pensando que estás en tu barco."
                y "No somos tus marineros, para que nos des órdenes."
                b "Lo siento si te he dado esa impresión. Nunca pasé por esta situación."
                b "Hago lo que puedo con el entrenamiento que tuve."
                $ desicion_intro += 1
                $ reporte_discusion_bob_acusar = True
                $ bob -= 1
                jump opciones_campamento
            "Bob debe escuchar más.":
                y "Quizás deberías dejar de actuar como si supieras todo."
                b "Entiendo tu frustración, pero estoy haciendo lo mejor que puedo."
                $ desicion_intro += 1
                $ reporte_discusion_bob_reprochar = True
                $ bob -= 2
                jump opciones_campamento

    elif bob < -1:
        y "Bob, eres el responsable de que estemos aquí. ¿Cómo puedes siquiera pensar en liderar después de lo que hiciste?"
        show bob gr parado enojado at leftgr
        with Dissolve(.5)
        b "Sé que estás enojado, [nombre_personaje], pero no podemos cambiar lo que pasó. Solo podemos seguir adelante."

        $ choice_position = "default" # default alta superior
        menu:
            "No confío en Bob.":
                y "No quiero escucharte. No confío en ti."
                b "Lo entiendo. Pero si no trabajamos juntos, ninguno de nosotros sobrevivirá."
                $ bob -= 2
                $ desicion_intro += 1
                $ reporte_discusion_bob_desconfiar = True
                jump opciones_campamento
            "Bob debería dar un paso al costado.":
                y "Deberías dejar que alguien más tome las decisiones."
                b "Si eso es lo que el grupo decide, lo aceptaré. Pero ahora necesitamos enfocarnos en sobrevivir."
                $ desicion_intro += 1
                $ reporte_discusion_bob_votacion = True
                $ bob -= 1
                jump opciones_campamento

label marina_discusion:
    m "Está claro que no se puede contar contigo."
    "Marina se aleja furiosa"
    hide marina
    with Dissolve(.5)
    l "Marina, espera..."
    hide laura
    with Dissolve(.5)
    "Ambas se alejan del refugio, se las escucha hablar mientras se internan en la jungla"
    jump bob_discusion

label init_buscar_comida:
    show laura seria at center
    with Dissolve(.5)
    y "Ahora que tenemos un refugio, buscar comida y agua debe ser nuestra mayor prioridad."
    
    show bob parado hablando at left
    with Dissolve(.5)
    b "Es verdad, todos estamos habrientos y con sed. Sin agua Ingrid no creo que pueda resistir mucho más."
    
    show marina preocupada at right
    with Dissolve(.5)
    m "Alguien debería quedarse con Ingrid para cuidarla."
    show bob parado serio at left
    with Dissolve(.5)
    b "Si, es importante organizarnos."
    show bob pensando at left
    with Dissolve(.5)
    b "Marina, tú puedes cuidar a Ingrid. Laura, ¿puedes ir juntando algunas ramas y hojas? Con eso veré de mejorar un poco nuestro refugio." 
    b "[nombre_personaje], ¿podrías ir tú a recorrer un poco por los alrededores en busca de algo de comer o agua?"

    $ choice_position = "superior" # default alta superior
    menu:
        "Claro, Bob. Me alegra que alguien ponga un poco de orden. ¡Hagámoslo!":
            $ desicion_intro += 1
            $ reporte_comida_bob_lidera = True
            hide laura
            with Dissolve(.5)
            hide bob
            with Dissolve(.5)
            show marina triste at right
            with Dissolve(.5)

            "Todos se dirigen a sus tareas, aunque Marina no parecen estar del todo convencida."
            $ choice_position = "default" # default alta superior
            menu:
                "Algo le pasa a Marina, deberia preguntarle.":
                    y "¿Marina, podemos hablar un momento?"
                    if marina < 2:
                        m "Ahora no es un buen momento [nombre_personaje]. Ingrid me necesita."
                        hide marina
                        with Dissolve(.5)
                        jump explorar_solo
                    else:
                        m "Seguro. ¿Qué sucede [nombre_personaje]?"
                        y "No te veo muy segura de estas decisiones, ¿tu que opinas?"
                        m "Gracias por preguntar... En realidad me gustaría ser de mas utilidad." 
                        m "Si Bob y Laura se quedan por aquí, pueden turnarse para cuidar a Ingrid."
                        m "Yo podría ayudar a buscar comida."
                        menu:
                            "Tienes razón. ¡Bob! Marina y yo vamos a buscar comida, ¡asi cubriremos más terreno!":
                                b "¡Claro! Buena idea."
                                $ desicion_intro += 1
                                $ reporte_comida_marina_util = True
                                jump explorar_marina
                            "Bob es el líder aquí. Es mejor seguir sus instrucciones.":
                                m "Si, puede ser. Voy a cuidar a Ingrid."
                                $ desicion_intro += 1
                                $ reporte_comida_marina_acata = True
                                jump explorar_solo
                "Marina debería hacer lo que le piden." if marina < 0:
                    y "Marina, todos tenemos que hacer nuestra parte. Al menos te toca la parte más fácil."
                    "Marina claramente queda afectada por tus palabras y va rápidamente junto a Ingrid."
                    $ desicion_intro += 1
                    $ reporte_comida_marina_inutil = True
                    hide marina
                    with Dissolve(.5)
                    show laura seria at center
                    with Dissolve(.5)
                    l "No tenáas porqué ser tan groser[e]. Así va a ser díficil convivir."
                    $ marina_laura_exploran = True
                    hide laura
                    with Dissolve(.5)
                    "Laura se acerca a Marina y tras unas palabras se alejan en la jungla conversando."
                    jump bob_discusion
        "Estoy muy cansad[e], prefiero ser yo quien se quede a cuidar a Ingrid. Que vaya alguien más a recorrer la selva." if not (reporte_cargar_ingrid_jungla or reporte_cargar_ingrid_jungla2 or reporte_cargar_ingrid_jungla3 or reporte_ayudar_ingrid or reporte_ayudar_ingrid2):
            $ reporte_cuidar_ingrid = True
            $ desicion_intro += 1
            $ reporte_comida_pereza = True
            jump cuidar_ingrid
        "Tengo una idea mejor Bob... mejor vas tú a buscar comida y dejas de decirle a los otros lo que hacer." if bob < 0:
            $ desicion_intro += 1
            $ reporte_comida_liderazgo = True
            jump discutir_liderazgo_bob
        "Creo que solo uno de nosotros debe quedarse, los demás debemos salir a recorrer.":
            $ desicion_intro += 1
            $ reporte_comida_optimizar = True
            show bob parado serio at left
            with Dissolve(.5)
            show laura hablando at center
            with Dissolve(.5)
            l "¿Y quién se queda?"

            $ choice_position = "default" # default alta superior
            menu:
                "Laura, tu ya descansante bastante mientras buscabamos refugio.":
                    $ desicion_intro += 1
                    $ reporte_comida_chicana_l = True
                    show laura enojada at center
                    with Dissolve(.5)
                    if (reporte_ayudar_ingrid or reporte_ayudar_ingrid2) == False:
                        if laura < 0:
                            l "Has tenido una actitud bastante fea conmigo. ¿Qué sucede?"
                            l "Todos estamos atrapados aquí y queremos salir así que mejor mejora tus modos."
                        "Laura aprieta los labios antes de volver a hablar."
                        l "Bob, fíjate si puedes mejorar el refugio, yo me voy a buscar algo de comida y agua."
                        hide laura
                        with Dissolve(.5)
                        "Laura se aleja muy enojada, se mete en la jungla con movimientos fuertes y bruscos."
                        show marina hablando at right
                        with Dissolve(.5)
                        m "Espera Laura, ¡voy contigo!"
                        $ marina_laura_exploran = True
                        hide marina
                        with Dissolve(.5)
                        jump bob_discusion
                    
                    l "Tampoco es que estuve durmiendo la siesta, pero tienes razón."
                    l "Voy a explorar a ver si encuentro algo de comida o agua."
                    hide laura
                    with Dissolve(.5)
                    m "Espera Laura, ¡voy contigo!"
                    $ marina_laura_exploran = True
                    hide marina
                    with Dissolve(.5)
                    y "Yo cuidaré a Ingrid entonces."
                    $ reporte_cuidar_ingrid = True
                    jump cuidar_ingrid
                "Podemos elegir al azar, ¿el que saque el palito más corto?":
                    $ desicion_intro += 1
                    $ reporte_comida_azar = True
                    if marina > 1:
                        m "Si, suena divertido. Buena idea [nombre_personaje]"
                        $ palitos += 1
                    else:
                        m "Quizas mejor seguir el plan del Bob."
                    if laura > 1:
                        l "Está bien, es medio tonto pero por qué no. Busquemos unos palitos."
                        $ palitos += 1
                    else:
                        l "Me parece una tontería, [nombre_personaje]."
                    if bob > 1:
                        b "¿A la suerte? Bueno supongo que al final de cuentas lo importante es que alguien haga las cosas."
                        $ palitos += 1 
                    else:
                        b "Prefiero no confiar en la suerte. Pensemos nuestras decisiones."
                    if palitos < 2:
                        b "Parece que la mayoria no quiere intentar con los palitos, [nombre_personaje]." 
                        b "Sigamos el plan original, Marina con Ingrid, Laura y yo con el refugio."
                        b "Y tú, [nombre_personaje], ve a buscar algo de comer por los alrededores."
                        "Todos se dirigen a sus tareas, tu te internas en la jungla."
                        jump explorar_solo
                "Bob tú eres el único que puede atender a Ingrid si necesita algo, deberias quedarte":
                    b "Bueno, puedo ir tratando de mejorar el refugio mientras uds van a buscar comida. Quizás es lo mejor."
                    "Laura y Marina se internan en la selva, Bob va a ver a Ingrid y tu también te vas a explorar en busca de comida."
                    $ desicion_intro += 1
                    $ reporte_comida_bob_permanece = True
                    $ marina_laura_exploran = True
                    jump explorar_solo
        "Yo me he agotado cargando a Ingrid, realmente necesito recuperarme un poco. Me quedaré a cuidarla." if (reporte_cargar_ingrid_jungla or reporte_cargar_ingrid_jungla2 or reporte_cargar_ingrid_jungla3 or reporte_ayudar_ingrid or reporte_ayudar_ingrid2):
            $ reporte_cuidar_ingrid = True
            $ desicion_intro += 1
            $ reporte_comida_descansar = True
            jump cuidar_ingrid

label discutir_liderazgo_bob:
    show bob gr serio sucio at leftgr
    with Dissolve(.5)

    b "Escuchen, sé que ser el capitán del barco no me hace el líder aquí, pero alguien tiene que tomar decisiones rápidas si queremos sobrevivir."

    y "¿Decisiones rápidas? ¿Como las que nos llevaron a este desastre? Bob, no puedes seguir dando órdenes."

    b "Entiendo tu frustración, [nombre_personaje], pero esto no es un juego. He recibido entrenamiento para situaciones de emergencia. Estoy tratando de ayudar."

    $ choice_position = "default" # default alta superior
    menu:
        "Rechazar el liderazgo.":
            y "No necesitamos que nos digas que hacer, Bob. Todos podemos decidirlo juntos."
            b "Eso suena bien en teoría, pero en situaciones como esta, la indecisión puede ser mortal."
            y "¿Y qué pasa si tus decisiones nos llevan a otro desastre? No confío en ti para liderar."
            y "Esta bien. Me voy a explorar, ustedes hagan lo que quieran."
            $ desicion_intro += 1
            $ reporte_liderazgo_rechazar = True
            $ bob -= 1
            jump explorar_solo

        "Abogar por la libertad.":
            y "¿Por qué no dejamos que cada uno haga lo que le parezca mejor? No necesitamos que alguien nos diga qué hacer."
            b "Eso es un error. Si no trabajamos juntos, no sobreviviremos. Pero si eso es lo que quieres, haz lo que creas conveniente."
            y "Es lo que voy a hacer, me voy a explorar."
            $ desicion_intro += 1
            $ reporte_liderazgo_abogar = True
            $ bob -= 1
            jump explorar_solo

        "No confiar en Bob.":
            y "Bob, no creo que seas capaz de liderar. Hay un barco en el fondo de la bahía que lo demuestra."
            b "No puedo cambiar el pasado, así que deja de recordarmelo. Estoy haciendo lo mejor que puedo para mantenernos vivos."
            y "Pues yo no confío en ti. Haré las cosas a mi manera."
            y "¡Voy a explorar, no necesito tu permiso!"
            $ desicion_intro += 1
            $ reporte_liderazgo_desconfiar = True
            $ bob -= 2
            jump explorar_solo

        "Aceptar lioderazgo de Bob.":
            y "Está bien, Bob. Pero no abuses de tu posición. No eres el único que está haciendo lo mejor que puede."
            b "No lo haré. Solo quiero que todos tengamos la mejor oportunidad de salir de esto."
            b "Estás dispuest[e] a ir tu a buscar agua y comida, [nombre_personaje]?"
            y "Si, yo iré a explorar. No hay problema."
            $ desicion_intro += 1
            $ reporte_liderazgo_aceptar = True
            $ bob += 1
            jump explorar_solo

label opciones_campamento:
    show bob pensando at left
    with Dissolve(.5)
    b "Creo que es mejor que haga algo con este refugio. Pronto se hará de noche y todos necesitamos descansar."

    $ choice_position = "default" # default alta superior
    menu:
        "Estoy agotad[e]" if cansancio == 3:
            y "En realidad ya no puedo ni estar en pie. Voy a recostarme aquí un rato."
            $ desicion_intro += 1
            $ reporte_campamento_descansar = True
            jump refugio_siesta
        "Debería cuidar mis energías":
            y "Estoy muy cansad[e]. Voy a recostarme aquí un rato."
            $ desicion_intro += 1
            $ reporte_campamento_descansar = True
            jump refugio_siesta
        "Debería explorar":
            y "No puedo quedarme aquí sin hacer nada. Voy a explorar un poco."
            y "Quizás encuentre algo de comer o agua."
            show bob saludando sucio at left
            with Dissolve(.5)
            b "¡Buena suerte! Necesitamos ambas urgentemente."
            $ desicion_intro += 1
            $ reporte_campamento_explorar = True
            $ bob +=1
            jump explorar_solo
        "Voy a cuidar a Ingrid.":
            $ reporte_cuidar_ingrid2 = True
            $ desicion_intro += 1
            $ reporte_campamento_cuidar = True
            jump cuidar_ingrid

label refugio_siesta:
    show bob parado hablando at left
    with Dissolve(.5)
    b "Recupera fuerzas un rato, pero no olvides revisar cómo está Ingrid."

    hide bob
    with Dissolve(.5)
    "Te recuestas a descansar un poco. Y te quedas dormido."
    pause 1.5
    if bob < 0:
        "Duermes un largo rato. Despiertas y parece que Marina y Laura ya regresaron porque se escuchan sus voces fuera del refugio."
        m "¡¿Cómo que se durmió?!"
        b "Si... Cuando fui a chequear a Ingrid luego de arreglar un poco el refugio, vi que estaba sola."
        b "No me imaginé que [nombre_personaje] se echaría una siesta, solo dijo que iba a descansar un momento."
        "Te acercas a Ingrid, quien a pesar de la falta de tu cuidado, al menos no ha empeorado."
        "Sales al encuentro de los demás, que se ven muy decepcionados."
    else:
        show bob saludando sucio at left
        b "Ey... despierta. No querrás que Laura y Marina te vean durmiendo. No te preocupes, me encargué de cuidar a Ingrid."
        y "Gracias, Bob. En seguida salgo."
        hide bob
        with Dissolve(.5)
    jump marina_laura_regresan
    
label explorar_marina:
    y "Bueno Marina, vamos a buscar algo de comida."
    y "Mejor nos separamos para cubrir más area, ¿te parece?"
    m "Buena idea, yo iré por aquí..."
    $ marina_explora = True
    hide marina
    with Dissolve(.5)
    jump explorar_solo

label explorar_solo:
    hide marina
    with Dissolve(.5)
    hide bob
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)

    show bg jungle explore 1 at truecenter
    with Dissolve(.5)
    "Te internas en la jungla buscando fuentes de agua y alimento."

    $ choice_position = "alta" # default alta superior
    menu:
        "Bob se cree un líder pero no es el mejor para eso." if bob < 2:
            y "Bob nos hizo naufragar, no estoy seguro de que sea la mejor hacerle caso."
            $ bob -= 1
            jump explorar_solo_2
        "El grupo depende de mi, debo encontrar agua y comida.":
            y "No puedo fallarles, debo encontrar algo pronto."
            $ desicion_intro += 1
            $ reporte_recursos_responsable = True
            $ responsabilidad_mas[capitulo_actual] += 1
            jump explorar_solo_busqueda
        "No tengo ganas de hacer nada, mejor me quedo a cuidar a Ingrid.":
            y "No tengo ganas de recorrer la jungla, mejor me vuelvo."
            $ desicion_intro += 1
            $ reporte_recursos_irresponsable = True
            $ responsabilidad_menos[capitulo_actual] += 1
            jump volver_campamento

label cuidar_ingrid:
    "Ingrid no esta bien, ha perdido mucha sangre y no parece estar consciente."
    hide marina
    with Dissolve(.5)
    hide bob_discusion
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)

    if stuff_bidon_agua:
        y "Ingrid, ¿puedes escucharme? He traído un poco de agua. Tómalo despacio."
        "Ingrid no reacciona pero poco a poco puedes hacer que tome un poco de agua."
        $ agua -= 2
        # Llamar a la función para actualizar la imagen del botón
        $ actualizar_boton_imagen()
        if agua == 0:
            y "El bidón esta vacío, debemos encontrar agua cuanto antes."
            y "Bob, cuida a Ingrid, voy a explorar a ver si encuentro agua."
            b "Entendido, estaré pendiente de ella. ¡Suerte!"
            jump explorar_solo
    "Cuidas a Ingrid tratando de que este cómoda y ajustas el vendaje que hizo Bob."
    "Aprovechas a recostarte un poco y descansar."
    $ update_stat("cansancio", cansancio + 1)
    $ show_variable_changed_popup("El cansancio ha disminuido", verde)
    # Ocultar y volver a mostrar la pantalla para actualizar la imagen
    hide screen combined_ui
    show screen combined_ui
    "Te despiertas un par de horas después, te sientes menos cansad[e]."
    jump marina_laura_regresan 

label bob_discusion_2:
    " Falta agregar bob_discusion_2"

label explorar_solo_2:
    "Mejor me quedo por aquí, no quiero perderme en la selva."
    $ desicion_intro += 1
    $ reporte_descansar_jungla = True
    $ responsabilidad_menos[capitulo_actual] += 1
    "Descansas un par de horas, te despiertas menos cansad[e]."
    $ update_stat("cansancio", cansancio + 1)
    $ show_variable_changed_popup("El cansancio ha disminuido", verde)
    # Ocultar y volver a mostrar la pantalla para actualizar la imagen
    hide screen combined_ui
    show screen combined_ui
    "Te queda poco tiempo para explorar antes de que caiga la noche."

    $ choice_position = "default" # default alta superior
    menu:
        "Volver mientras hay luz.":
            y "Es mejor regresar antes de que caiga la noche. No quiero arriesgarme a perderme en la oscuridad."
            $ desicion_intro += 1
            $ reporte_recursos_resignacion = True
            $ compromiso_menos[capitulo_actual] += 1
            jump volver_campamento
        "Seguir explorando un poco más.":
            y "Seguiré explorando un poco más. Quizás encuentre algo útil antes de que oscurezca."
            $ desicion_intro += 1
            $ reporte_recursos_redobla_esfuerzo = True
            $ compromiso_mas[capitulo_actual] += 1
            "Te adentras un poco más en la jungla, buscando algo que pueda ser útil para el grupo."
            jump explorar_solo_busqueda


label explorar_solo_busqueda:
    scene bg jungle trail at truecenter
    with Dissolve(.5)

    "Sigues explorando la jungla y encuentras un sendero que parece haber sido usado antes. Quizás te lleve a algo interesante."
    $ choice_position = "default" # default alta superior
    menu:
        "Seguir el sendero para ver a dónde lleva.":
            y "Este sendero parece prometedor. Veamos a dónde lleva."
            $ desicion_intro += 1
            $ reporte_recursos_redobla_esfuerzo2 = True
            $ compromiso_mas[capitulo_actual] += 1
            jump seguir_sendero

        "Regresar al campamento antes de que oscurezca.":
            y "Es mejor regresar al campamento antes de que sea demasiado tarde."
            $ desicion_intro += 1
            $ reporte_recursos_resignacion2 = True
            $ compromiso_menos[capitulo_actual] += 1
            jump volver_campamento

label seguir_sendero:
    show bg jungle river at truecenter
    with Dissolve(.5)
    $ reporte_encontrar_agua_comida = True
    "Sigues el sendero y descubres un pequeño claro con algunas frutas comestibles y una fuente de agua cercana."
    y "¡Increíble! He encontrado un lugar con frutas y agua. Esto es justo lo que necesitamos."
    y "El agua esta fresca y parece bien limpia, supongo que puedo arriesgarme a tomarla."
    $ update_stat("sed", sed + 3)
    $ show_variable_changed_popup("Has saciado la sed", verde)
    # Ocultar y volver a mostrar la pantalla para actualizar la imagen
    hide screen combined_ui
    show screen combined_ui
    if stuff_bidon_agua:
        y "Es momento de recargar las reservas de agua."
        $ agua = 10
        # Llamar a la función para actualizar la imagen del botón
        $ actualizar_boton_imagen()
    jump sendero_fruta

label sendero_fruta:
    show bg jungle fruit at truecenter
    with Dissolve(.5)
    y "Las frutas son pequeñas pero parecen comestibles. No sé si es seguro comerlas, pero no tengo muchas opciones."
    "Pruebas una de las frutas, es dulce, como una ciruela silvestre. Te sientes un poco mejor."

    $ choice_position = "default" # default alta superior
    menu:
        "Comer hasta no tener mas hambre.":
            y "Estas frutas son deliciosas. No puedo dejar de comer."
            $ desicion_intro += 1
            $ reporte_comer_frutas_hasta_no_hambre = True
            $ update_stat("hambre", hambre + 3)
            $ show_variable_changed_popup("Has saciado el hambre", verde)
            # Ocultar y volver a mostrar la pantalla para actualizar la imagen
            hide screen combined_ui
            show screen combined_ui
            jump volver_campamento
        "Comer un par de frutas y llevar el resto.":
            y "Estas frutas son deliciosas. Llevaré algunas para el campamento."
            $ update_stat("hambre", hambre +1)
            $ show_variable_changed_popup("El hambre ha disminuido", verde)
            # Ocultar y volver a mostrar la pantalla para actualizar la imagen
            hide screen combined_ui
            show screen combined_ui
            $ desicion_intro += 1
            $ reporte_comer_algunas_frutas = True
            $ comida = 5
            jump volver_campamento
        "Llevar todas las frutas al campamento.": 
            y "Estas frutas son deliciosas. Llevaré todas para el campamento. Espero que sean suficientes para todos."
            $ comida = 10
            $ desicion_intro += 1
            $ reporte_lleva_fruta = True
            jump volver_campamento


label volver_campamento:
    if refugio == "cabaña":
        show bg jungle hut at truecenter
        with Dissolve(.5)
    if refugio == "cueva":
        show bg jungle cave at truecenter
        with Dissolve(.5)
    if refugio == "claro":
        show bg jungle clearing at truecenter
        with Dissolve(.5)

    show bob saludando sucio at left
    with Dissolve(.5)
    if reporte_marina_laura_exploran:
        y "¿Marina y Laura aun no regresan?"
        b "No, me están empezando a preocupar. Han salido a explorar hace mucho y ya es tarde."
        jump marina_laura_regresan    
    if reporte_comer_frutas_hasta_no_hambre:
        y "Hay frutas en la isla, encontré algunas y me las comí. Son comestibles."
        $ comida = 0
        show marina gr preocupada at rightgr
        with Dissolve(.5)
        if marina > 0:
            m "¿Y no trajiste algunas para el resto de nosotros?"
            m "Bueno, al menos ahora estás en mejores condiciones de ayudarnos."
            m "La próxima vez, piensa en el grupo, ¿sí?"
            $ marina -= 1
        else:
            m "¿T las comiste todas? ¿No pensaste en los demás? Esto no puede seguir así."
            $ marina -= 2
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        if bob > 0:
            b "Entiendo que tenías hambre, pero deberías haber pensado en el grupo."
            b "Por favor, no lo hagas de nuevo."
            $ bob -= 1
        else:
            b "Esto es inaceptable. No puedes seguir actuando así."
            $ bob -= 2
        show laura seria at center
        with Dissolve(.5)
        if laura > 0:
            l "Es un error, pero al menos uno de nosotros tiene energías para seguir ayudándonos."
            l "No podemos permitir que cometasmás errores así, [nombre_personaje]."
            $ laura -= 1
        else:
            l "¿Ni siquiera trajiste algunas para Ingrid? Esto es increíble."
            $ laura -= 2
    elif reporte_comer_algunas_frutas:
        y "He traído algunas frutas para compartir. No son muchas, pero algo es algo."
        show marina preocupada at right
        with Dissolve(.5)
        if marina > 0:
            m "¡Gracias, [nombre_personaje]! Buen trabajo."
            m "Esto nos ayudará a todos a recuperar algo de energía."
            $ marina += 1
        else:
            m "Bueno, algo es algo. Pero necesitaremos más para sobrevivir."
            $ marina += 0
        show bob saludando sucio at left
        with Dissolve(.5)
        if bob > 0:
            b "Es un buen comienzo. Si encontramos más lugares como ese, podríamos tener una fuente constante de alimento."
            $ bob += 1
        else:
            b "Servirá por ahora, pero necesitamos encontrar suficiente comida pronto."
            $ bob += 0
        show laura seria at center
        with Dissolve(.5)
        if laura > 0:
            l "Es un alivio tener algo para comer. Bien hecho, [nombre_personaje]."
            $ laura += 1
        else:
            l "Necesitamos más, pero aprovechemos al menos"
            $ laura += 0
    elif comida > 0:
        y "He traído frutas para todos. Espero que sean suficientes, al menos por ahora."
        y "La buena noticia es que en la isla hay comida, hay que buscar más."
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        if bob > 0:
            b "¡Buen trabajo! Esto nos ayudará a mantenernos fuertes."
            $ bob += 2
        else:
            b "Esto es útil, pero no podemos depender solo de las frutas. Necesitamos algo más."
            $ bob += 1
        show marina hablando at right
        with Dissolve(.5)
        if marina > 0:
            m "Esto es justo lo que necesitábamos, [nombre_personaje]. ¡Gracias por traer para todos!."
            $ marina += 2
        else:
            m "Están bien, pero no es suficiente con unas simples frutas. Sigamos buscando otras fuentes de alimento."
            $ marina += 1
        show laura seria at center
        with Dissolve(.5)
        if laura > 0:
            l "Es un gran alivio. Esto nos da un poco de esperanza."
            $ laura += 2
        else:
            l "Es un buen comienzo, pero no podemos relajarnos todavía."
            $ laura += 1
    elif reporte_marina_laura_exploran == False:
        y "No encontré nada útil. Lo siento."
        show marina gr preocupada at rightgr
        with Dissolve(.5)
        if marina > 0:
            m "No te preocupes, al menos lo intentaste. Seguiremos buscando."
            $ marina -= 1
        else:
            m "No puede ser que no hayas encontrado nada."
            $ marina -= 2
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        if bob > 0:
            b "Está bien, pero necesitamos resultados pronto. No podemos sobrevivir sin comida."
            $ bob -= 1
        else:
            b "Esto es preocupante. Necesitamos que la próxima vez hagas un mejor esfuerzo."
            $ bob -= 2
        show laura seria at center
        with Dissolve(.5)
        if laura > 0:
            l "Es un contratiempo, pero no te preocupes. Seguiremos buscando."
            $ laura -= 1
        else:
            l "¿Buscaste bien? No entiendo. Estuviste fuera un buen rato."
            $ laura -= 2

    if agua > 0:
        if stuff_bidon_agua:
            y "También encontré una fuente de agua y llené el bidón. Ahora tenemos agua para todos."
            show bob saludando sucio at left
            with Dissolve(.5)
            if bob > 0:
                b "¡Eso es excelente! El agua es vital para nuestra supervivencia."
                b "Tener ubicado un manantial va a ser muy útil."
                $ bob += 2
            else:
                b "Esto es útil, pero mientras no encontremos alguna fuente de agua más cerca, debemos seguir racionándola."
                $ bob += 1
            show marina hablando at right
            with Dissolve(.5)
            if marina > 0:
                m "Esto al menos nos da un poco de tiempo para planear mejor nuestras próximas acciones."
                $ marina += 2
            else:
                m "Es un buen comienzo, pero necesitamos hacer más viajes hasta allí para traer más agua."
                $ marina += 1
            show laura seria at center
            with Dissolve(.5)
            if laura > 0:
                l "¡Pensé que moriría de sed! Buen trabajo, [nombre_personaje]."
                $ laura += 2
            else:
                l "Ojalá tuviésemos otro bidón. Esto apenas alcanza, habrá que volver a buscar más."
                $ laura += 1
    elif sed == 3:
        y "Encontré una fuente de agua y bebí un poco para saciar mi sed, pero no tenemos nada donde transportarla."
        show marina preocupada at right
        with Dissolve(.5)
        if marina > 0:
            m "Al menos encontraste agua."
            $ marina += 1
        else:
            m "Debiste vovler antes, asi todos podiamos ir al lugar antes de que se hiciera tan tarde."
            $ marina += 0
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        if bob > 0:
            b "Ahora es tarde pero mañana debemos ir allí."
            $ bob += 1
        show laura seria at center
        with Dissolve(.5)
        if laura < 0:
            l "Solo espero que nos den las fuerzas para llegar..."
            $ laura += 0
    jump pregunta_descanso_jungla


label pregunta_descanso_jungla:
    if reporte_descansar_jungla:
        b "¿Cómo has demorado tanto? Es casi de noche."

        $ choice_position = "default" # default alta superior
        menu:
            "Reconocer que descansaste un rato":
                y "Me tomé un momento para descansar en la jungla. Ahora me siento un poco mejor."
                $ desicion_intro += 1
                $ reporte_descanso_reconoce = True
                show marina preocupada at right
                with Dissolve(.5)
                if marina > 0:
                    m "Es bueno que hayas descansado. Necesitamos estar en nuestras mejores condiciones."
                    $ marina += 1
                else:
                    m "Espero que ese descanso no haya sido una excusa para no hacer nada útil."
                    $ marina -= 1
                show bob gr serio sucio at leftgr
                with Dissolve(.5)
                if bob > 0:
                    b "Mientras no descuidemos nuestras prioridades, está bien. Pero no podemos permitirnos mucho tiempo para descansar."
                    $ bob += 1
                else:
                    b "Estamos luchando por nuestras vidas, [nombre_personaje]."
                    b "No podemos permitirnos que andes haciendo la siesta por allí, mientras el resto de nosotros trabajamos."
                    $ bob -= 1
                show laura seria at center
                with Dissolve(.5)
                if laura > 0:
                    l "Es importante que todos estemos en las mejores condiciones para seguir adelante."
                    $ laura += 1
                else:
                    l "Espero que ese descanso haya valido la pena. Los demás estuvimos trabajando duro."
                    $ laura -= 1
            "Ocultar que tomaste un descanso":
                y "No he parado ni un momento. Estuve recorriendo la jungla todo este tiempo."
                $ desicion_intro += 1
                $ reporte_descanso_miente = True
                show marina preocupada at right
                with Dissolve(.5)
                if marina > 0:
                    m "Es bueno que hayas estado trabajando duro. Necesitamos a todos dando lo mejor."
                    $ marina += 1
                show bob gr serio sucio at leftgr
                with Dissolve(.5)
                if bob > 0:
                    b "Eso es exactamente lo que necesitamos. Que todos se esfuercen al máximo."
                    $ bob += 1
                else:
                    b "Me cuesta creer eso. Estarías totalmente transpirado."
                    $ bob -= 1
                show laura seria at center
                with Dissolve(.5)
                if laura > 0:
                    l "Es admirable, pero recuerda que también necesitas administrar tus energías."
                    $ laura += 1
                else:
                    l "¿En serio? Yo te veo bastante relajado."
                    $ laura -= 1
    else:
        y "No tuve tiempo para descansar. Estuve recorriendo la jungla desde que nos separamos."
        $ desicion_intro += 1
        $ reporte_descanso_cero = True
        show bob gr serio sucio at leftgr
        with Dissolve(.5)
        if bob > 0:
            b "Dándolo todo es como saldremos de esta. Ahora debemos organizarnos para lo que sigue."
            $ bob += 1
        show marina preocupada at right
        with Dissolve(.5)
        if marina > 0:
            m "No te sobrecargues demasiado. Todos necesitamos estar en nuestra mejor forma."
            $ marina += 1
        show laura seria at center
        with Dissolve(.5)
        if laura > 0:
            l "Cuida un poco tus energías, ¿si?. Contamos contigo, [nombre_personaje]."
            $ laura += 1
        else:
            l "Nosotros también estuvimos aprovechando el tiempo."
            $ laura -= 1
    jump final_primer_dia

label marina_laura_regresan:
    show marina hablando at center
    with Dissolve(.5)
    m "¡Hemos encontrado agua!"
    show laura gr hablando at leftgr
    with Dissolve(.5)
    l "Pero vinos arboles sin nada de fruta, era ya muy tarde. Mañana hay que seguir buscando."
    show bob gr serio sucio at rightgr
    with Dissolve(.5)
    b "Si hay arboles frutales, podemos volver a buscarlos mañana. Es una buena noticia."
    y "¡Al menos tenemos agua! Una cosa a la vez."
    if stuff_bidon_agua:
        y "Mañana podremos también llenar el bidon nuevamente y tener reservas aseguradas."
    else: 
        y "Primero deben guiarnos a la fuente de agua para que el resto podamos beber. Quizás debamos encontrar un refugio mas cerca de alli."
        show marina sonriendo at center
        with Dissolve(.5)
        m "Es bastante cerca, dimos muchas vueltas buscando y nos cruzamos con un arroyo ya de regreso."
    jump final_primer_dia


label final_primer_dia:
    hide laura
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    show bob parado hablando at center
    with Dissolve(.5)
    b "Escuchen, ahora que todos estamos aquí, debemos organizarnos."
    b "Me pregunto cuándo despertará Ingrid"
    show marina preocupada at right
    with Dissolve(.5)
    m "No lo sé, no parece estar mejor. Necesitamos más agua y comida para ella."

    $ choice_position = "default" # default alta superior
    menu:
        "Valoremos el momento" if reporte_encontrar_agua_comida:
            y "Hemos encontrado agua y mañana buscaremos más frutos. Tratemos de relajarnos un poco."
            $ desicion_intro += 1
            $ reporte_p3_final_optimista = True
        "No creo que Ingrid sobreviva":
            y "Me preocupa Ingrid, ya hace mucho que está inconsciente. Aquí no podemos hacer mucho por ella."
            $ desicion_intro += 1
            $ reporte_p3_final_pesimista = True
        "Deberíamos descansar un poco y recuperar fuerzas.":
            y "Sin duda, pero por hoy un poco de descanso nos ayudará a pensar con claridad mañana."
            $ desicion_intro += 1
            $ reporte_p3_recuperar = True
            $ compromiso_mas[capitulo_actual] += 1

    hide marina
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)
    hide bob
    with Dissolve(.5)

    "El grupo intercambia miradas, conscientes de los desafíos que enfrentan. Aunque hay tensiones, también hay algunos que forman lazos y confían en sus compañeros."
    "Pronto cae la noche en la isla. Un cielo estrellado parece anunciar que no se avecinan nuevas tormentas."
    "Los sobrevivientes se acomodan como pueden. En el refugio algunos tratan de dormir, y los que no lo logran deambulan por los alrededores antes de volver a intentarlo."
    "La noche es tranquila, pero la incertidumbre persiste."

    jump interact_with_characters


label interact_with_characters:
    # Introduce a moment of interaction between the characters
    show bg jungle night stars at truecenter
    with Dissolve(.5)
    "Es un buen momento para acercarte a alguno de tus compañeros y conversar."
    $ choice_position = "alta" # default alta superior
    menu:
        "Hablar con Marina sobre cómo se siente." if reporte_wellness_m == False:
            $ desicion_intro += 1
            $ reporte_wellness_m = True
            show marina preocupada at right
            with Dissolve(.5)
            if marina > 0:
                y "Marina, ¿cómo te sientes después de todo lo que ha pasado?"
                m "Es difícil, pero trato de mantenerme fuerte. No podemos rendirnos ahora. Ingrid nos necesita, y no sabemos si hay más sobrevivientes."
                y "Lo estás haciendo muy bien. Todos contamos contigo"
            else:
                y "Marina, ¿cómo te sientes después de todo lo que ha pasado?"
                m "¿De verdad te importa? Eso si que es una novedad."
                y "Lo siento si te hice sentir así. Espero poder recuperar tu confianza."
            hide marina
            with Dissolve(.5)
            $ choice_position = "default" # default alta superior
            menu:
                "Marina parece estar enfocada en Ingrid y el grupo.":
                    y "Es admirable cómo Marina siempre pone a los demás primero."
                    $ marina += 1
                "Marina parece estar molesta conmigo." if marina < 1:
                    y "Quizás debería esforzarme más para demostrarle que me importa el grupo."
                    $ marina += 0
            jump interact_with_characters

        "Preguntar a Bob sobre su experiencia como capitán." if reporte_wellness_b == False:
            $ desicion_intro += 1
            $ reporte_wellness_b = True
            show bob gr serio sucio at leftgr
            with Dissolve(.5)
            if bob > 0:
                y "Bob, ¿alguna vez imaginaste que algo así podría pasar?"
                b "Nunca. He enfrentado tormentas, pero esto... esto es diferente. Ahora no solo soy un capitán, soy un sobreviviente."
                b "Pero no podemos perder la esperanza. Si seguimos organizados, saldremos adelante."
                y "Tu experiencia nos está ayudando mucho. Gracias por mantener la calma."
            else:
                y "Bob, ¿alguna vez imaginaste que algo así podría pasar?"
                b "No, pero no tengo tiempo para lamentarme. Alguien tiene que mantener la cabeza fría, y parece que no todos están dispuestos a hacerlo."
                y "No te preocupes, entiendo el mensaje. Haré lo mejor posible."
            hide bob
            with Dissolve(.5)

            $ choice_position = "default" # default alta superior
            menu:
                "Bob parece ser un líder natural.":
                    y "Es tranquilizador tener a alguien con experiencia como Bob en el grupo."
                    $ bob += 1
                "Bob parece estar frustrado conmigo." if bob < 1:
                    y "Quizás deba esforzarme más en demostrarle que puede contar conmigo."
                    $ bob += 0
            jump interact_with_characters

        "Conversar con Laura sobre su perspectiva." if reporte_wellness_l == False:
            $ desicion_intro += 1
            $ reporte_wellness_l = True
            show laura seria at center
            with Dissolve(.5)
            if laura > 0:
                y "Laura, ¿qué piensas de todo esto?"
                l "Es aterrador, Ingrid está herida, y no sabemos cuánto tiempo podremos sobrevivir con los pocos recursos que tenemos."
                l "Pero también me hace darme cuenta de lo que realmente importa. Tenemos que apoyarnos."
                y "Es cierto. Se que lo repetimos como un mantra, pero juntos lo lograremos."
                l "¡Ey! Parece funcionar bastante bien, ¿o no?"
                y "Ayuda a mantener las esperanzas altas, es verdad."
            else:
                y "Laura, ¿qué piensas de todo esto?"
                l "¿Quieres saberlo? Pienso que algunos aquí no están tomando esto tan en serio como deberían."
                y "Se que te refieres a mi. Haré lo posible por mejorar."
                l "Debes darte cuenta de lo que está en juego, [nombre_personaje]."
            hide laura
            with Dissolve(.5)

            $ choice_position = "default" # default alta superior
            menu:
                "Laura parece muy asustada. Debo tranquilizarla.":
                    y "Mañana conseguiremos más recursos. Una vez que Ingrid haya saciado su hambre, se recuperará más rápido."
                    $ laura += 1
                "Laura parece estar molesta conmigo." if laura < 1:
                    y "Quizás debería mostrar un mayor compromiso, con ella y con el grupo."
                    $ laura += 0
            jump interact_with_characters

        "Dejar que todos descansen por ahora.":
            if reporte_wellness_b == True and reporte_wellness_l == True and reporte_wellness_m == True:
                y "Me alegra haber podido hablar con todos, aunque el sueño haya sido intermitente."
            y "Deberíamos descansar. Mañana será otro día difícil."
            jump chapter_4_end

label chapter_4_end:
        # Generar contenido para los pop-ups de relaciones
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura"], es_relacion=True)
        $ relaciones_cap4_bob = bob
        $ relaciones_cap4_marina = marina
        $ relaciones_cap4_laura = laura
                    
        # Calcular el total de decisiones y obtener la lista de variables específicas para el capítulo
        $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 4 y el primer segmento. ¡Felicitaciones! El grupo ha enfrentado nuevos desafíos y sus relaciones han evolucionado."
        "En el siguiente segmento el grupo deberá tomar muy buenas decisiones para sobrevivir... y resolver un misterio."
                    
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump segment_1_end
            "VOLVER A VER EL RESÚMEN":
                jump chapter_4_end
    

label segment_1_end:
    # prueba de enviar reporte
    $ enviar_reporte(player_id)
    "El reporte fue enviado con exito!"
    jump chapter_5_start
return

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ACA TERMINA SEGMENTO 1                                         |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#################################################################################################  ########  ###############################################
##################################################################################################  ######  ##############################################################
## Aca comienza la PARTE 5 ########################################################################  ###  ################################################################
####################################################################################################     ##################################################################

label chapter_5_start:
    # Inicializar el capítulo actual (empieza en 0 por lo que es un numero menor que el capitulo, ej cap 2 debe tener la variable en 1)
    $ capitulo_actual = 4
    jump ingrid_despierta

label ingrid_despierta:
    # mañana siguiente, Ingrid despierta aun débil 
        # que el PJ sea el primero en despertar y darse cuenta, y pueda hacerse el dormido para que alguien más se encargue, y así poder dormir un poco más.
    # Mostrar imagen del refugio elegido
    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabaña":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing
    else:
        scene bg jungle night stars  # fallback por si no se definió bien

    with fade

    # Despertar del jugador
    "Los primeros rayos de luz filtrándose en el refugio te despiertan."
    "Parece que Bob, Laura y Marina aún duermen, y solo se escuchan los sonidos de la selva."
    "El silencio es quebrado por unos quejidos provenientes de donde duerme Ingrid."

    menu:
        "Parece que finalmente ha recuperado la conciencia. ¿Qué haces?"

        "Volver a dormir y dejar que otro se encargue.":
            "Suspiras, te giras hacia el otro lado y vuelves a cerrar los ojos."
            $ desicion_intro += 1
            $ reporte_dormir_mas = True
            jump despiertan_todos

        "Acercarte a Ingrid y ayudarla.":
            "Te levantas con cuidado y te acercas a Ingrid."
            $ desicion_intro += 1
            $ reporte_despertar_ingrid = True
            $ despierta_antes = True
            jump ayudar_ingrid_despertar

label ayudar_ingrid_despertar:
            
    "Aunque sus ojos están entreabiertos, Ingrid murmura sin sentido, pero parece querer incorporarse."
    "La ayudas a recostarse. Aún parece muy débil. Seguramente tenga hambre y sed."
    if comida > 0 or agua > 0:
        jump nutrir_ingrid
    else:
        "Deberá esperar a que despierten los demás y se decida cómo conseguir agua y comida."
        jump despiertan_todos


label nutrir_ingrid:
    if (agua > 0 and not bebio) or (comida > 0 and not comio):   
        menu:
            "Qué quieres hacer?"
            # Opción si hay agua
            "Darle un poco de agua." if agua > 0 and not bebio:
                "Le acercas agua a Ingrid, ayudándola con cuidado a beber."
                $ agua -= 1
                $ bebio = True
                # ACÁ HAY QUE ACTUALIZAR EL ICONO???
                jump nutrir_ingrid

            # Opción si hay comida
            "Darle algo de comida." if comida > 0 and not comio:
                "Revisas las provisiones y le ofreces un poco de comida a Ingrid."
                $ comida -= 1
                $ comio = True
                # ACÁ HAY QUE ACTUALIZAR EL ICONO???
                jump nutrir_ingrid

            "Tratar de calmarla y esperar a que despierten los demás." if despierta_antes and not todos_despiertos:
                y "Tranquila, Ingrid, estás bien. Sufrimos un naufragio, pero algunos logramos sobrevivir."
                jump despiertan_todos
        
            "Con eso se va a sentir un poco mejor." if not despierta antes and (comio or bebio):
                y "Eso te hará bien."
                jump dejarla_descansar
        
    elif comio and agua <= 0:
        "Aunque aún no tengamos agua para ella, un poco de comida en el estómago le hará recuperar fuerzas."
        if despierta_antes:
            jump despiertan_todos
        if not despierta_antes:
            jump dejarla_descansar

    elif bebio and comida <= 0:
        "Aunque no tengamos comida, estar hidratada la ayudará a sentirse mejor."
        if despierta_antes:
            jump despiertan_todos
        if not despierta_antes:
            jump dejarla_descansar

label despiertan_todos:
    $ todos_despiertos = True
    pause 1
    if despierta_antes:
        "Bob es el primero en despertar, y se le ilumina la cara cuando ve a Ingrid conciente."
    else:
        "Despiertas con un grito de júbilo de Bob."
    show bob saludando sucio at center
    with Dissolve(.5)
    b "¡Ingrid! ¡Ingrid despertó!"
    "Marina y Laura comienzan a levantarse, y ambas sonríen cuando comprenden de qué se trata. Frotándose los ojos, se levantan y se acercan."
    show marina hablando at left
    with Dissolve(.5)
    m "¡Ingrid! Nos tenías preocupados."
    show laura hablando at right
    with Dissolve(.5)
    show bob parado serio at center
    with Dissolve(.5)
    l "Debí haberte ido a buscar cuando vi que demorabas en volver al claro. ¿Qué fue lo que pasó?"
    "Ingrid trata de responder, pero aún no tiene fuerzas para hablar."
    b "Será mejor que descanses un poco. Perdiste algo de sangre, pero hemos estado cuidando de ti."
    m "Debería comer algo y beber agua."
    if comio or bebio:
        y "Yo ya le di un poco. Seguramente con eso y algo de descanso pronto podrá contarnos qué pasó."
        m "Entonces dejémosla descansar."
        jump dejarla_descansar
    elif comida > 0 or agua > 0:
        y "Voy a ver qué tenemos."
        jump nutrir_ingrid
    elif comida <= 0 and agua <= 0:
        b "Hoy tenemos que encontrar agua sí o sí."
        l "Y comida."
        m "Dejémosla descansar por ahora."
        jump dejarla_descansar

label dejarla_descansar:
    hide marina
    with Dissolve(.5)
    hide bob
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)
    "El grupo sale al exterior del refugio para dejar que Ingrid siga descansando."
    pause 1
    "La alegría de verla despertar se disipa un poco de sus rostros cuando ven la selva nuevamente."
    show bob pensando at center
    with Dissolve(.5)
    show laura seria at right
    with Dissolve(.5)
    show marina preocupada at left
    with Dissolve(.5)
    "Faltan muchos desafíos aún."
    if comida <= 5 or agua <=5:
        ### La unica manera de que la comida no sea 0 hasta ahora es que haya encontrado los frutos
        show bob gr pensando at center
        with Dissolve(.5)
        b "Estoy preocupado por los recursos básicos, no demoremos mucho en seguir explorando."
        show bob pensando at center
        with Dissolve(.5)
        show laura gr seria at right
        with Dissolve(.5)
        l "Podemos hacer dos expediciones."
        show laura seria at right
        with Dissolve(.5)
        show marina gr preocupada at left
        with Dissolve(.5)
        m "¿Será seguro dejar a Ingrid sola, por más que haya despertado?"
        show marina preocupada at left
        with Dissolve(.5)
        show bob gr pensando at center
        with Dissolve(.5)
        b "No del todo, pero al menos estará conciente en caso de que aparezca algún peligro."
        show bob pensando at center
        with Dissolve(.5)
        menu:
            "Ahora que Ingrid ha despertado, es seguro dejarla sola.":
                y "Ingrid estará bien, no hemos encontrado evidencias de depredadores en la isla, y el clima no ha empeorado."
                y "Necesitamos del esfuerzo de todos para seguir encontrando recursos."
                jump p5_explorar
            "Será mejor que uno de nosotros se quede a cuidarla, por si acaso.":
                y "No quisiera correr riesgos, es mejor que uno de nosotros se quede."
                y "Tampoco querría que nadie vaya solo, así que sugiero que el resto forme una expedición única."
                jump elegir_cuidador

label elegir_cuidador:
    b "Todos hemos descansado bastante. Tal vez sea mejor que me quede yo, que conozco sobre primeros auxilios."
    menu:
        "Bob podría ser de ayuda en la expedición.":
            y "Tenía esperanzas de que vinieras en la expedición, Bob."
            if stuff_bote:
                y "Quisiera que revisáramos el bote que rescaté de la playa. Tal vez podamos usarlo para pescar."
            elif stuff_caja_grande:
                y "Me gustaría que me ayudes a cargar una caja grande que rescaté de la playa. Tal vez haya algo que nos sirva."
            else:
                y "Deberíamos ver si el bote que vi en la playa sigue ahí. Tal vez nos sirva para pescar."
            b "Buena idea, [nombre_personaje]."
            m "Yo podría quedarme."
            
            menu:
                "Me gustaría traer a Marina para tener la oportunidad de arreglar las cosas con ella." if marina < 2:
                    y "No lo sé, después de todo Ingrid llegó a la orilla junto a Laura, tal vez sea mejor que ella se quede."
                    l "Yo tampoco tengo problema en quedarme."
                    m "Bien, iré con ustedes entonces."
                    $ laura_se_queda = True
                    jump p5_explorar

                "Se nota que a Marina se le dan bien los cuidados." if laura > 1:
                    y "Genial entonces. Laura, Bob y yo iremos a explorar."
                    $ marina_se_queda = True
                    jump p5_explorar

                "Me gustaría pasar un rato con Laura y poder limar asperezas con ella." if laura < 2:
                    y "Genial entonces. Laura, Bob y yo iremos a explorar."
                    $ marina_se_queda = True
                    jump p5_explorar

        "Es un buen punto.":
            y "Tienes razón, Bob. Marina, Laura y yo exploraremos."
            $ bob_se_queda = True
            jump p5_explorar


label p5_explorar:
    # if not bidon entonces tienen que pensar una forma de cargar agua.
        # atar esto a la decisión de ir primero a la playa a por el bote o la caja, o si primero explorar.
        # (PJ propone caparazón de tortuga o concha marina para ir a playa, o coco o caña de bambú para ir a la jungla)
    
    # discuten como la encontraron, debe ponerse en evidencia las desiciones y acciones de todos durante el capitulo 2 y 4 
    # grupo se separa en dos grupos, uno va a buscar agua y el otro a buscar comida, oportunidad para reforzar lazos o restaurar relaciones
    # ajustar stats a lo largo del capitulo, es importante que si algun stat queda en rojo, pueda pasar que se pierda alguna desicion
    # en rojo deben ajustarse algunas opciones de manera que el jugador sepa que las tiene pero que no le da el cuero por el estado en que está
    # Si tienen bidon pueden cargar agua, si no, deben encontrar alguna manera de llevarle agua a Ingrid. 
    # Si tienen caja, podrian encontrar raciones y algunas herramientas como algun cuchillo y tenedor, algun elemento de cocina.
    # Si tienen bote, podrian encontrar un kit de pesca, una bengala, etc 
    # recogen frutos, no hay muchos pero ven aves y algunos hurones. Tambien huellas de algun animal mas pesado, podria ser un jabalí 
    # Termina con decidir proximos pasos, se plantean diversas opciones, da para discusion y apoyo segun relacion
    # Todos confian en el rescate, es clave que Bob se muestre poco confiado pero sin revelar nada
    #jump chapter_5_end

label chapter_5_end:
        # Generar contenido para los pop-ups de relaciones
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura", "ingrid"], es_relacion=True)
        $ relaciones_cap5_bob = bob
        $ relaciones_cap5_marina = marina
        $ relaciones_cap5_laura = laura
        $ relaciones_cap5_ingrid = ingrid
                    
        # Calcular el total de decisiones y obtener la lista de variables específicas para el capítulo
        $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 5, el primero del segundo segmento. El grupo ha logrado resolver muchos problemas pero aun queda mucho por hacer. La supervivencia dependerá de las desiciones que tomen."
                    
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump chapter_6_start
            "VOLVER A VER EL RESÚMEN":
                jump chapter_5_end


#################################################################################################  ########  #####  ##########################################
##################################################################################################  ######  ######  ########################################################
## Aca comienza la PARTE 6 ########################################################################  ###  ########  ########################################################
####################################################################################################     #########  #########################################################

label chapter_6_start:
    # Inicializar el capítulo actual (empieza en 0 por lo que es un numero menor que el capitulo, ej cap 2 debe tener la variable en 1)
    $ capitulo_actual = 5
    jump ingrid_enferma

label ingrid_enferma:
    # casi al anochecer, Ingrid empiza con una fiebre muy alta. Tiene una infeccion
    # Ingrid les explica como son algunas plantas que pueden usarse como antibioticos y poco despues queda inconsciente por la fiebre
    # discusion si ir a buscar y arriesgarse a perderse en la jungla de noche o esperar a la mañana siguiente
    # Se forman bandos, es importante que haya una postura opuesta a la del jugador, sin importar cual sea
    # Un grupo va a buscar plantas y el otro se queda por no estar de acuerdo en arriesgarse a perderse en la jungla de noche.
    # branch: si va o si se queda, si se queda hay oportunidad de reforzar vinculos y replantearse si es la desicion correcta. 
    # Puede decidir sumarse a la busqueda solo
    # el equipo que va a buscar se termina separando, si es el jugador le pasan cosas 
    # (se tropieza en la penumbra y rueda por un terraplen, se pincha con una planta de espinas, etc)
    # escuchan cerca un gruñido furioso de un jabali, peude ser causa de que se separen
    # todos vuelven al campamento, menos uno. Ya es de noche, discusion de si ir o no a buscar a quien falta
    # Se culpabiliza a quienes querian buscar plantas al atardecer
    # Oportunidad para sumarse a responsabilizar o calmar los animos y recomponer el grupo
    # Termina con 2 yendo a buscar a quien falta y trayendola de vuelta al refugio 
    # o con la persona extraviada llegando de madrugada exhausta si no se arriesgaron a volver a la jungla
    # Vuelve con las plantas y se le aplican a Ingrid en la herida
    jump chapter_6_end

label chapter_6_end:
        # Generar contenido para los pop-ups de relaciones
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura", "ingrid"], es_relacion=True)
        $ relaciones_cap6_bob = bob
        $ relaciones_cap6_marina = marina
        $ relaciones_cap6_laura = laura
        $ relaciones_cap6_ingrid = ingrid
                    
        # Calcular el total de decisiones y obtener la lista de variables específicas para el capítulo
        $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 6, pese a todo el esfuerzo Ingrid se debate entre la vida y la muerte. La proxima mañana se verá si la fiebre remite. Es una noche tensa y de poco descanso."
                    
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump chapter_7_start
            "VOLVER A VER EL RESÚMEN":
                jump chapter_6_end

#################################################################################################  ########  #####  ####  ######################################
##################################################################################################  ######  ######  ####  ####################################################
## Aca comienza la PARTE 7 ########################################################################  ###  ########  ####  ####################################################
####################################################################################################     #########  ####  #####################################################

label chapter_7_start:
    # Inicializar el capítulo actual (empieza en 0 por lo que es un numero menor que el capitulo, ej cap 2 debe tener la variable en 1)
    $ capitulo_actual = 6
    jump ingrid_recupera

label ingrid_recupera:
    # a la mañana todos están muy cansados
    # Ingrid se despierta sin fiebre, puede hacer cosas pero aun está debil
    # se propone ir a alguno de los otros posibles refugios y ver si alli hay algo de utilidad 
    # si en capitulo 3 el jugador no vio el claro, deberia haberlo visto en el cap5 y proponerlo como lugar de exploracion
    # branch: ir a cabaña o ir a cueva o ir a claro en saliente (uno de estos es el lugar donde estan refugiados por lo que siempre hay dos opciones a explorar)
    # Alguien se queda con ingrid para ayudarla a seguir buscando hierbas utiles, el resto va al otro lugar
    # en el primer lugar (sea cual sea encuentran algo util
    # En la cabaña alguna herramienta,  algo para hacer fuego, en la cueva una buena cantidad hongos comestibles y en el saliente unos cuantos nidos con huevos
    # En el segundo lugar se encuentran con otro grupo de supervivientes, que han encontrado lo que habia en ese lugar y tienen todo muy organizado
    # Se introducen a Charles, Erika y Tomás, que son los nuevos personajes. Uno esta en el campamento y los otros van llegando luego
    # Cada uno tiene habilidades para mantener el grupo funcionando, lograron recuperar varias cosas de la playa (una de las que no eligio el jugador y alguna otra cosa)
    # Se plantea tema de rescate y Bob advierte que la tormenta los dejo muy lejos de las rutas y de donde se supone que debian estar.
    # Se da una discusion sobre que refugio es mejor para juntarse todos
    # Deberian ir surgiendo dos lideres en oposicion, puede ser que el jugador tome el rol del otro lider o que apoye a uno frente al otro
    
    jump chapter_7_end
     

label chapter_7_end:
        # Generar contenido para los pop-ups de relaciones
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura", "ingrid", "charles", "erika", "tomas"], es_relacion=True)
        $ relaciones_cap7_bob = bob
        $ relaciones_cap7_marina = marina
        $ relaciones_cap7_laura = laura
        $ relaciones_cap7_ingrid = ingrid
        $ relaciones_cap7_charles = charles
        $ relaciones_cap7_erika = erika
        $ relaciones_cap7_tomas = tomas
                    
        # Calcular el total de decisiones y obtener la lista de variables específicas para el capítulo
        $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 7, el encuentro con otro grupo de supervivientes trae nuevas oportunidades pero tambien nuevos problemas. ¿Serán una ayuda o un peligro si llegan momentos críticos?"
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump chapter_8_start
            "VOLVER A VER EL RESÚMEN":
                jump chapter_7_end

#################################################################################################  ########  #####  ####  ####  ##################################
##################################################################################################  ######  ######  ####  ####  ################################################
## Aca comienza la PARTE 8 ########################################################################  ###  ########  ####  ####  ################################################
####################################################################################################     #########  ####  ####  #################################################

label chapter_8_start:
    # Inicializar el capítulo actual (empieza en 0 por lo que es un numero menor que el capitulo, ej cap 2 debe tener la variable en 1)
    $ capitulo_actual = 7
    jump tormenta_preparativos

label tormenta_preparativos:
    # Se ve en el horizonte una gran tormenta
    # El equipo se separa para obtener las cosas necesarias para reforzar el refugio
    # ver cual es el punto critico, fuego, comida, agua, protegerse de la tormenta, segun el refugio elegido y las opciones de los capitulso anteriores
    # durante toda la previa a la tormenta se dan encontronazos entro los dos lideres con visiones muy opuestas de como y que hacer
    # la tormenta llega con tremenda fuerza, rompiendo parte del refugio, generando peligros y disparado miedos
    # antes o durante la tormenta puede incluirse al jabali que rompe, persigue o complcia de algun modo, que se sienta una amenaza
    # como el equipo se vincula y apoya o no en esos momentos
    # los dos lideres van formando su grupo de apoyo 
    # termina con la tormenta amainando y el refugio dañado, y varias de las cosas perdidas o arruinadas
    # un equipo responsabiliza al otro de las perdidas y la discusion termina en el grupo dividiendose en dos
    jump chapter_8_end 

label chapter_8_end:
        # Generar contenido para los pop-ups de relaciones
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura", "ingrid", "charles", "erika", "tomas"], es_relacion=True)
        $ relaciones_cap7_bob = bob
        $ relaciones_cap7_marina = marina
        $ relaciones_cap7_laura = laura
        $ relaciones_cap7_ingrid = ingrid
        $ relaciones_cap7_charles = charles
        $ relaciones_cap7_erika = erika
        $ relaciones_cap7_tomas = tomas
                    
        # Calcular el total de decisiones y obtener la lista de variables específicas para el capítulo
        $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el segmento 2, el grupo ha pasada una dura prueba. La tormenta ha pasado pero la isla tiene peligros acechando en la jungla."
        "Ha llegado el momento de considerar que quizás no haya ningún equipo de rescate aún buscando."
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump segment_2_end
            "VOLVER A VER EL RESÚMEN":
                jump chapter_8_end

label segment_2_end:
    # prueba de enviar reporte
    $ enviar_reporte(player_id)
    "El reporte fue enviado con exito!"
    jump chapter_9_start
 
return

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ACA TERMINA SEGMENTO 1                                         |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

###################################################################################  ####   #####   #########################################################
###################################################################################  #######  ##  ######################################################################
## Aca comienza la PARTE 9 ########################################################  #######  ##  #################################################################
###################################################################################  #####   ####   #################################################################

label chapter_9_start:
    "Aca comienza el segmento 3"