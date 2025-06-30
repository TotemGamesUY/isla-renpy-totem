

image fondo_inicio = "main_01.jpg"

# name of the character.

define m = Character("Marina Lee", color="#dfcdd6")
define b = Character("Capt. Bob Williams", color="#546ace")
define l = Character("Laura Esteban", color="#d4373f")
define y = Character("[nombre_personaje] [[Tú]", color="#1d7c3a")
define c = Character("Charles Grey", color="#5b746c")
define k = Character("Erika Smith", color="#e07c4d")
define t = Character("Tomás Greenson", color="#b19621")
define i = Character("Ingrid Sversson", color="#6c742d")


#define el player id
default player_id = ""
define player_name = ""
define player_lastname = ""
define player_ids = ["Jugador1", "jugador2", "Jugador3", "jugador4", "vero", "fabrizio", "rod", "jime", "maria", "g3r", "5u3"]  # Lista de IDs válidos para android
default input_id = ""  # Variable para almacenar el ID ingresado por el jugador
default input_codigo_capitulo = "" # Codigo que pide para continuar jugando los capitulos

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
transform centerleft:
    xalign 0.35
    yalign 1.25
transform centerright:
    xalign 0.65
    yalign 1.25

init python:
    posiciones_grupo = [left, centerleft, centerright, right]

# Variables de genero
default genero = "Femenino"
default e = "a"
default le = "la"
default n = "n"

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
image bg inside cave  = im.Scale("bg inside_cave.jpg", config.screen_width, config.screen_height)
image bg inside cabin  = im.Scale("bg inside_cabin.jpg", config.screen_width, config.screen_height)
image bg inside shelter  = im.Scale("bg inside_shelter1.jpg", config.screen_width, config.screen_height)
image bg beach sunny = im.Scale("bg beach sunny.jpg", config.screen_width, config.screen_height)
image bg jungle night explore1 = im.Scale("bg jungle night explore1.jpg", config.screen_width, config.screen_height)
image bg jungle night explore2 = im.Scale("bg jungle night explore2.jpg", config.screen_width, config.screen_height)
image bg jungle night explore3 = im.Scale("bg jungle night explore3.jpg", config.screen_width, config.screen_height)
image bg jungle night search = im.Scale("bg jungle night search.jpg", config.screen_width, config.screen_height)
image bg cave fungi = im.Scale("cave fungi.jpg", config.screen_width, config.screen_height)
image bg horizon_storm_clouds = im.Scale("storm horizon.jpg", config.screen_width, config.screen_height)
image bg jungle_storm_approaching = im.Scale("storm_horizon2.jpg", config.screen_width, config.screen_height)
image bg jungle_storm_aftermath = im.Scale("jungle_storm_aftermatch.jpg", config.screen_width, config.screen_height)
image bg comic 1 = im.Scale("comic_1.jpg", config.screen_width, config.screen_height)
# PLACEHOLDERS:

#webp animados
image fondo_animado = im.Scale("fondo_hojas.webp", config.screen_width, config.screen_height)


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

image erika sonriendo = "Erika sonriendo.png"
image erika enojada = "Erika enojada.png"
image erika parada = "Erika parada.png"
image erika sorprendida = "Erika sorprendida.png"
image erika gr enojada = "Erika enojada gr.png"
image erika gr parada = "Erika parada gr.png"
image erika conversando = "Erika conversando.png"
image erika gr conversando = "Erika conversando gr.png"
image erika gr sonriendo = "Erika sonriendo gr.png"
image erika gr sorprendida = "Erika sorprendida gr.png"

image ingrid enojada = "ingrid.100.enojada.png"
image ingrid cintura = "ingrid.100.manos.cintura.png"
image ingrid risita = "ingrid.100.risita.png"
image ingrid seria = "ingrid.100.seria.png"
image ingrid sonriente = "ingrid.100.sonriente.png"
image ingrid triste = "ingrid.100.triste.png"
image ingrid gr enojada = "ingrid.200.enojada.png"
image ingrid gr cintura = "ingrid.200.manos.cintura.png"
image ingrid gr risita = "ingrid.200.risita.png"
image ingrid gr seria = "ingrid.200.seria.png"
image ingrid gr sonriente = "ingrid.200.sonriente.png"

# Lista de imagenes "grupo" para cada personaje para la sepracion en grupos
image marina grupo ="Marina_hablando.png"
image bob grupo ="Bob_parado_serio.png"
image laura grupo ="Laura_parada_seria.png"
image erika grupo ="Erika parada.png"
image ingrid grupo ="ingrid.100.manos.cintura.png"
image charles grupo ="charles.png"
image tomas grupo ="tomas.png"


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
default marina_ofrece_comida = False
default bob_se_queda = False
default marina_se_queda = False
default laura_se_queda = False
default encontraron_agua = False
default reporte_todos_explorar = False
default reporte_algunos_explorar = False
default comidant_ingrid = False
default bebidant_ingrid = False
default va_con_bob = False
default va_con_marina = False
default va_con_laura = False
default exploran_tres = False
default exploran_todos = False
default reporte_advierte_agua = False
default inventan_cantimploras = False
default reporte_conejillos_de_indias = False
default marina_laura_arroyo_frutos = False
default reporte_esconde_bote = False
default reporte_comparte_bote = False
default reporte_esconde_caja = False
default reporte_comparte_caja = False
default caja_abierta = False
default reporte_no_buscar_de_noche = False
default reporte_ocultar_marina = False
default reporte_asustar_marina = True
default reporte_cuida_ingrid_cap7 = False
default reporte_refugio_visitado_1 = ""
default reporte_refugio_visitado_2 = ""
default reporte_opinion_refugio = ""
default reporte_conflicto_entre_lideres = ""
default confianza_ingrid = 0
default jugador_lider = 0
default jugador_mediador = 0
default destino_exploracion_1 = ""
default destino_exploracion_2 = ""
default opciones_exploracion = []
default opciones_exploracion2 = []
default objeto_faltante = []
default opciones_texto = []
default reporte_ingrid_te_convence = False
default reporte_oyen_jabali = False
default confianza_tomas = 0
default confianza_charles = 0
default reporte_respetuoso_tomas = False
default reporte_intenta_conectar_tomas = False
default reporte_broma_charles = False
default reporte_desconfia_charles = False 
default apoyo_laura = False
default apoyo_ingrid = False
default apoyo_charles = False
default estrategia_agresiva = False
default estrategia_pacifica = 0
default estrategia_pasiva = 0
default player = 0
default apoyo_tomas = 0
default apoyo_bob = 0
default apoyo_erika = 0
default grupo_jugador = []
default grupo_bob = []
default grupo_erika = []
default apoyo_lider_jugador = 0
default apoyo_lider_bob = 0
default apoyo_lider_erika = 0
default relacion_fuerte_jugador = []
default relacion_conflictiva_jugador = []
default personaje_indeciso = ""
default dialogo_personajes = {}
default climb_hill = False
default reporte_cautela_hongos = False
default reporte_descuido_hongos = False
default yesca = False
default reporte_se_muestra_firme = False
default reporte_se_muestra_cauteloso = False
default reporte_se_muestra_abierto = False
default reporte_apoya_union = False
default reporte_indeciso_union = False
default reporte_opone_union = False
default reporte_secreto_rescate = False
default reporte_verdad_rescate = False
default reporte_apoya_liderazgo_erika = False
default reporte_apoya_liderazgo_bob = False
default reporte_postula_liderazgo = False
default reporte_evade_liderazgo = False
default enfoque_preparacion = ""
default equipo_bob = False
default equipo_erika = False
default equipo_jugador_opcion1 = False
default equipo_jugador_opcion2 = False
default jugador_es_lider = False


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
default liderazgo = 0
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

# logica para que asigne el fondo interior/exterior dinamico 
# scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
init python:
    fondos_refugios = {
        "cueva": {
            "exterior": "bg jungle cave",
            "interior": "bg inside cave"
        },
        "cabana": {
            "exterior": "bg jungle hut",
            "interior": "bg inside cabin"
        },
        "claro": {
            "exterior": "bg jungle hill",
            "interior": "bg inside shelter"
        }
    }

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

# para resolver como reaccionan a las ordenes
init python:
    reactividad_directa = ["tomas", "ingrid"]
    reactividad_gentil = ["marina", "laura"]
    obstinado = "charles"

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
default empático_mas = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default empatico_menos = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default honestidad_mas = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default honestidad_menos = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default integridad_mas = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default integridad_menos = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default responsabilidad_mas = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default responsabilidad_menos = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default compromiso_mas = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default compromiso_menos = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default colaboración_mas = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]
default colaboración_menos = [0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0]

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
                
                if input_id in player_ids:
                    $ player_id = input_id  # Asignar el ID válido
                    
                    "ID válido registrado: [player_id]."
                    hide screen pedir_id_screen
                    
                    jump start_game  # Sale del label si el ID es válido
                
                else:
                    "ID inválido. Intenta nuevamente."

            else:
                "Debes ingresar un ID válido."

label pedir_codigo_capitulo:
    while True:  # Se repite hasta que el ID sea válido
        show screen pedir_codigo_capitulo_screen
        $ resultado = ui.interact()
        
        if resultado:

            hide screen pedir_codigo_capitulo_screen

            if renpy.android:  # Solo mostrar en Android   
                if persistent.cantidad_capitulos == 4 and resultado == "44":
                    jump chapter_5_start
                elif persistent.cantidad_capitulos == 8 and resultado == "88":
                    jump chapter_9_start
            else :
                if persistent.cantidad_capitulos == 2 and resultado == "22":
                    jump chapter_3_start
                elif persistent.cantidad_capitulos == 4 and resultado == "44":
                    jump chapter_5_start
                elif persistent.cantidad_capitulos == 6 and resultado == "66":
                    jump chapter_7_start
                elif persistent.cantidad_capitulos == 8 and resultado == "88":
                    jump chapter_9_start
                elif persistent.cantidad_capitulos == 10 and resultado == "install523":
                    jump chapter_11_start
                
        else:
            "Código inválido. Intenta nuevamente."

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
        call pedir_id from _call_pedir_id
    else:
        jump start_game

label start_game:
    $ persistent.cantidad_capitulos = 0
    $ persistent.cantidad_capitulos += 1

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
            $ n = "n"
        "Femenino":
            $ genero = "Femenino"
            $ le = "la"
            $ e = "a"
            $ n = "na"
    jump comic

label comic:
    scene bg comic 1 at truecenter
    $ persistent.game_started = True
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
    # show screen decisiones_popup(contenido=decisiones_contenido)

    "{size=-15}Las decisiones pueden afectar la relación con los demás supervivientes. Sin ser inherentemente buenas o malas las decisiones tienen consecuencias.{/size}"
    
    
    "Aquí termina la introducción. En el siguiente capítulo tus decisiones definirán el destino de los supervivientes. ¿Preparad[e] para descubrir los secretos de la isla?"
    # Ocultar los pop-ups con dissolve
    hide screen relaciones_popup with dissolve
    # hide screen decisiones_popup with dissolve

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
    $ persistent.cantidad_capitulos += 1

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
            $ reporte_grupo = True
            $ liderazgo += 1
            jump p1islaInvestigarLead
        "Lidere usted la búsqueda, capitán.":
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            $ desicion_intro += 1
            $ reporte_búsqueda_sigue = True
            $ reporte_grupo = True
            jump p1islaInvestigarLead
        "Mejor sigo por mi cuenta, adiós.":
            hide bob
            with Dissolve(.5)
            hide marina
            with Dissolve(.5)
            $ desicion_intro += 1
            $ reporte_búsqueda_separado = True
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
            "Reafirmar la desición.":
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
    with Dissolve(0.5)
    hide bob
    with Dissolve(0.5)
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
    # show screen decisiones_popup(contenido=decisiones_contenido)
    
    "Aquí termina el capitulo, pero la historia aún tiene grandes desafíos y muchas decisiones de las que depende la superviviencia del grupo."
    # Ocultar los pop-ups con dissolve
    hide screen relaciones_popup with dissolve
    # hide screen decisiones_popup with dissolve
    $ choice_position = "default" # default alta superior
    menu:
        "CONTINUAR":
            jump chapter_3_start
            #jump final_cap3
        "VOLVER A VER EL RESÚMEN":
            jump final
    
label final_cap3:
    if renpy.android:
        jump chapter_3_start
    else:
        call pedir_codigo_capitulo from _call_pedir_codigo_capitulo

############################################   #######   ########   ################################################################################################
############################################   #######   ########   ################################################################################################
## Aca comienza la PARTE 3 #################   #######   ########   ################################################################################################
############################################   #######   ########   ################################################################################################

label chapter_3_start:
    # Inicializar el capítulo actual
    $ capitulo_actual = 2
    $ persistent.cantidad_capitulos +=1
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
    $ climb_hill = True

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
    "Esto concluye el Capítulo 3."

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
    # show screen decisiones_popup(contenido=decisiones_contenido)
    
    "El grupo ha encontrado refugio, pero aún quedan muchos desafíos por delante y un giro inesperado de la historia."

    # Ocultar los pop-ups con dissolve
    hide screen relaciones_popup with dissolve
    # hide screen decisiones_popup with dissolve
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
    $ persistent.cantidad_capitulos +=1

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
                y "Hasta no encontrar agua potable, hay que cuidar la que nos queda."
                show bob parado hablando at left
                with Dissolve(.5)
                b "Tienes razón, si no la cuidamos, estaremos en problemas."
                $ desicion_intro += 1
                $ reporte_racionar_agua = True
                $ bob +=1
                jump refugio_init_reparten_agua
            "El agua es mia y es valiosa. Ellos van a desperdiciarla.":
                y "Yo me esforcé para conseguirla, yo decidiré cuando y cómo se usa."
                show bob parado hablando at left
                with Dissolve(.5)
                b "Es realmente increíble que seas tan egoista."
                $ desicion_intro += 1
                $ reporte_acaparar_agua = True
                $ bob -=1
                jump bob_discusion_agua
            "Bob no ha sido un gran compañero hasta ahora, no merece que lo ayude." if bob < 0:
                y "Tú deberías buscar tu propia agua, Bob."
                show bob parado hablando at left
                with Dissolve(.5)
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
        show bob parado serio at left
        with Dissolve(.5)
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
                                $ marina -= 1
                                jump marina_discusion
                            "Está claro que Marina no va a poder tomar decisiones duras.":
                                y "Marina, esta es una situación desesperada. Debemos pensar en cómo sobrevivir."
                                m "No es así como vamos a sobrevivir. Tenemos que recordar que somos personas."
                                m "Debí esperar esto de ti [nombre_personaje], pero no de ti, Laura."
                                l "Yo solo dije lo que varios pensabamos, nada más."
                                "Marina se aleja furiosa."
                                $ marina -= 1
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
                else: # si fue por gente
                    m "Cuando estabamos los dos solos en la playa, pensaste primero en ayudar a la gente."
                    m "¿Cómo puedes ahora decir algo asi a la ligera?"
                        
                    $ choice_position = "alta" # default alta superior
                    menu:
                        "No me gusta que me cuestione":
                            y "No me hables en ese tono."
                            y "¿Tú que has hecho hasta ahora?"
                            $ marina -= 1
                            $ desicion_intro += 1
                            $ reporte_agua_ingrid_chicana_m = True
                            jump marina_discusion    
                        "Está claro que Marina no va a poder tomar decisiones duras.":
                            y "Marina, esta es una situación desesperada. Debemos pensar en cómo sobrevivir."
                            m "No es así como vamos a sobrevivir. Tenemos que recordar que somos personas."
                            m "Debí esperar esto de ti [nombre_personaje], pero no de ti, Laura."
                            l "Yo solo dije lo que varios pensabamos, nada más."
                            "Marina se aleja furiosa."
                            $ marina -= 1
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
            $ liderazgo += 1
            $ reporte_liderazgo_aceptar = True
            $ bob += 1
            jump explorar_solo

label opciones_campamento:
    show bob pensando at left
    with Dissolve(.5)
    b "Creo que es mejor que haga algo con este refugio. Pronto se hará de noche y todos necesitamos descansar."

    $ choice_position = "alta" # default alta superior
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
    "Te recuestas a descansar un poco. Y te quedas dormid[e]."
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
    hide bob
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
    y "El agua está fresca y parece bien limpia, supongo que puedo arriesgarme a tomarla."
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
            m "¿Te las comiste todas? ¿No pensaste en los demás? Esto no puede seguir así."
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
            m "Debiste volver antes, asi todos podiamos ir al lugar antes de que se hiciera tan tarde."
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
    hide bob

    show marina hablando at center
    with Dissolve(.5)
    m "¡Hemos encontrado agua!"
    $ encontraron_agua = True
    show laura gr hablando at leftgr
    with Dissolve(.5)
    l "Pero vimos árboles sin nada de fruta, era ya muy tarde. Mañana hay que seguir buscando."
    show bob gr serio sucio at rightgr
    with Dissolve(.5)
    b "Si hay árboles frutales, podemos volver a buscarlos mañana. Es una buena noticia."
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
    show bg jungle night stars at truecenter
    with Dissolve(.5)
    "Los sobrevivientes se acomodan como pueden. En el refugio algunos tratan de dormir, y los que no lo logran deambulan por los alrededores antes de volver a intentarlo."
    "La noche es tranquila, pero la incertidumbre persiste."

    jump interact_with_characters


label interact_with_characters:
    # Introduce a moment of interaction between the characters
    show bg jungle night stars at truecenter
    with Dissolve(.5)
    "Es un buen momento para acercarte a alguno de tus compañeros y conversar."
    $ choice_position = "superior" # default alta superior
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
        
        "No tengo nada que hablar con los demas en este momento.":
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
        # show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 4 y el primer segmento. ¡Felicitaciones! El grupo ha enfrentado nuevos desafíos y sus relaciones han evolucionado."
        "En el siguiente segmento el grupo deberá tomar muy buenas decisiones para sobrevivir... y resolver un misterio."
                    
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        # hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump chapter_5_start
                #jump segment_1_end
            "VOLVER A VER EL RESÚMEN":
                jump chapter_4_end
    

label segment_1_end:
    # prueba de enviar reporte
    $ enviar_reporte(player_id)
    "El reporte fue enviado con exito!"
    call pedir_codigo_capitulo from _call_pedir_codigo_capitulo_1
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
    $ persistent.cantidad_capitulos +=1

    jump ingrid_despierta

label ingrid_despierta:
    # mañana siguiente, Ingrid despierta aun débil 
        # que el PJ sea el primero en despertar y darse cuenta, y pueda hacerse el dormido para que alguien más se encargue, y así poder dormir un poco más.
    # Mostrar imagen del refugio elegido
    if refugio == "cueva":
        scene bg inside cave
    elif refugio == "cabaña":
        scene bg inside cabin
    elif refugio == "claro":
        scene bg inside shelter
    else:
        scene bg jungle night stars  # fallback por si no se definió bien

    with fade

    # Despertar del jugador
    "Los primeros rayos de luz filtrándose en el refugio te despiertan."
    "Parece que Bob, Laura y Marina aún duermen, y solo se escuchan los sonidos de la selva."
    "El silencio es quebrado por unos quejidos provenientes de donde duerme Ingrid."
    pause 0.5
    "Parece que finalmente ha recuperado la conciencia."
    $ choice_position = "default" # default alta superior
    menu:
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
        if todos_despiertos == False:
            "Podría ver qué tenemos y darle algo, o esperar a que los demás despierten."

        $ choice_position = "default" # default alta superior
        menu:
            "Darle un poco de agua." if agua > 0 and not bebio:
                "Le acercas agua a Ingrid, ayudándola con cuidado a beber."
                $ agua -= 1
                $ actualizar_boton_imagen()
                $ bebio = True
                jump nutrir_ingrid

            "Darle un poco de agua." if agua <= 0 and not bebio and not bebidant_ingrid:
                "El grupo no tiene reservas de agua disponibles."
                $ bebidant_ingrid = True
                jump nutrir_ingrid

            "Darle algo de comida." if comida > 0 and not comio:
                "Revisas las provisiones y le ofreces un poco de comida a Ingrid."
                $ comida -= 1
                $ comio = True
                jump nutrir_ingrid

            "Darle algo de comida." if comida <= 0 and not comio and not comidant_ingrid:
                "El grupo no tiene nada de comida."
                $ comidant_ingrid = True
                jump nutrir_ingrid

            "Tratar de calmarla y esperar a que despierten los demás." if despierta_antes and not todos_despiertos:
                y "Tranquila, Ingrid, estás bien, te golpeaste la cabeza. El capitán Bob, Marina y Laura estamos aquí."
                jump despiertan_todos
        
            "Con eso se va a sentir un poco mejor." if not despierta_antes and (comio or bebio):
                y "Eso te hará bien."
                jump dejarla_descansar
        
    elif comio and agua <= 0:
        "Aunque aún no tengamos agua para ella, un poco de comida en el estómago le hará recuperar fuerzas."
        if todos_despiertos:
            jump ingrid_debil
        else:
            if despierta_antes:
                jump despiertan_todos
            if not despierta_antes:
                jump dejarla_descansar

    elif bebio and comida <= 0:
        "Aunque no tengamos comida, estar hidratada la ayudará a sentirse mejor."
        if todos_despiertos:
            jump ingrid_debil
        else:
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
    jump ingrid_debil

label ingrid_debil:
    
    if marina_ofrece_comida == False:
        $ marina_ofrece_comida = True
        m "Debería comer algo y beber agua."
    if comio or bebio:
        y "Yo ya le di de lo que habia. Seguramente con eso y algo de descanso pronto podrá contarnos qué pasó."
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
    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabaña":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing
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
    b "Estoy preocupado por los recursos básicos, no demoremos mucho en seguir explorando."
    l "Podemos hacer dos expediciones."
    m "¿Será seguro dejar a Ingrid sola, por más que haya despertado?"
    b "No del todo, pero al menos estará conciente en caso de que aparezca algún peligro."
    m "¿Y qué peligros podrían ser esos?"
    $ choice_position = "default" # default alta superior
    menu:
        "Tal vez sea mejor no preocupar a Marina.":
            y "Por ejemplo, si empezara a llover, y el refugio se inundara, Ingrid ahora es capaz de darse cuenta y buscar un punto alto."
            $ desicion_intro += 1
            $ reporte_ocultar_marina = True
            "Bob te mira, y en su rostro notas que se dió cuenta de que no le dijiste a Marina todo lo que tenías en mente."
            $ bob += 1

        "A Marina le vendría bien un shock de realidad, a ver si espabila.":
            y "Marina, esto no es una excursión. No sabemos qué puede pasar ni qué peligros hay en la isla."
            y "Podría haber depredadores, podría volver la tormenta, podría pasarnos algo a nosotros, dejando a Ingrid sola."
            $ desicion_intro += 1
            $ reporte_asustar_marina = True
            "Bob y Laura sacuden la cabeza en desaprobación."
            $ bob -= 1
            $ laura -= 1
            show marina triste 
            with Dissolve(.5)
                
    m "Entiendo..."
    b "Hasta ahora no ha habido ninguna señal de peligro que podamos confirmar."
    l "Es verdad, hasta donde sabemos..."
    $ choice_position = "alta" # default alta superior
    menu:
        "Peligros o no, dejar a alguien es menos gente explorando":
            y "Ingrid estará bien, es verdad que no hemos encontrado evidencia de peligros en la isla, y el clima no ha empeorado por ahora."
            y "Necesitamos del esfuerzo de todos para seguir encontrando recursos."
            $ desicion_intro += 1
            $ liderazgo +=1
            $ reporte_todos_explorar = True
            jump p5_explorar

        "Será mejor que uno de nosotros se quede a cuidarla, por si acaso.":
            y "No quisiera correr riesgos, es mejor que uno de nosotros se quede."
            y "Tampoco querría que nadie vaya solo, así que sugiero que el resto forme una expedición única."
            $ desicion_intro += 1
            $ liderazgo +=1
            $ reporte_algunos_explorar = True
            jump elegir_cuidador
        
        "Bob seguro que puede organizar esto.":
            y "¿Tú que opinas Bob?"
            $ desicion_intro += 1
            $ reporte_algunos_explorar = True
            jump elegir_cuidador

label elegir_cuidador:
    b "Todos hemos descansado bastante. Tal vez sea mejor que me quede yo, que conozco sobre primeros auxilios."
    $ choice_position = "default" # default alta superior
    menu:
        "Bob podría ser de ayuda en la expedición.":
            y "Tenía esperanzas de que vinieras en la expedición, Bob."
            if stuff_bote:
                y "Quisiera que revisáramos el bote que rescaté de la playa. Tal vez podamos usarlo para pescar."
            elif stuff_caja_grande:
                y "Me gustaría que me ayudes a cargar una caja grande que rescaté de la playa. Tal vez haya algo que nos pueda servir."
            else:
                y "Deberíamos ver si el bote que vi en la playa sigue ahí. Tal vez nos sirva para pescar."
            b "Buena idea, [nombre_personaje]."
            m "Yo podría quedarme."
            $ choice_position = "alta" # default alta superior
            menu:
                "Me gustaría traer a Marina para tener la oportunidad de arreglar las cosas con ella." if marina < 2:
                    y "No lo sé, después de todo Ingrid llegó a la orilla junto a Laura."
                    y "Tal vez sea mejor que ella se quede, así ve una cara familiar."
                    l "No tengo problema con quedarme."
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
    if reporte_todos_explorar:
        "Antes de internarse en la jungla, deben decidir quién irá en cada una de las dos expediciones."
        "Bob parece ansioso, seguramente esté por proponer algo."
        $ choice_position = "superior" # default alta superior
        menu:
            "Podría ir con Bob y que juntos nos encarguemos de las cosas que quedaron en la playa.":
                y "¿Qué tal si vienes conmigo, Bob?"
                if stuff_bote:
                    y "Quisiera que revisáramos el bote que rescaté de la playa. Tal vez podamos usarlo para pescar."
                elif stuff_caja_grande:
                    y "Me gustaría que me ayudes a cargar una caja grande que rescaté de la playa. Tal vez haya algo que nos pueda servir."
                else:
                    y "Deberíamos ir a ver si el bote que vi en la playa sigue ahí. Tal vez nos sirva para pescar."
                show bob parado hablando at center
                with Dissolve(.5)
                b "Buena idea, [nombre_personaje]."                
                if encontraron_agua:
                    l "Genial, entonces Marina y yo iremos a buscar agua al lugar que encontramos ayer."
                elif reporte_encontrar_agua_comida:
                    l "Genial, entonces Marina y yo iremos al lugar que encontraste ayer."
                    $ marina_laura_arroyo_frutos = True
                else:
                    l "Genial, entonces Marina y yo nos adentraremos en la jungla a buscar agua y comida."
                $ va_con_bob = True
                $ liderazgo += 1
                hide bob
                with Dissolve(.5)
                hide marina
                with Dissolve(.5)
                hide laura
                with Dissolve(.5)
                jump p5playa
            
            "Me gustaría traer a Marina para tener la oportunidad de arreglar las cosas con ella." if marina < 2:
                y "Marina, siento que nos vendría bien tener un rato para conversar. ¿Hacemos equipo?"
                show marina triste at left
                with Dissolve(.5)        
                m "Me parece una buena idea. Limar asperezas será bueno para el grupo."                
                b "Excelente, entonces Laura y yo conformaremos la otra expedición."
                l "Me parece perfecto."
                $ va_con_marina = True
                $ liderazgo += 1
                jump p5_division_tareas
                    
            "Marina saca lo mejor de mi, haríamos buen equipo." if marina > 1:
                y "Marina, siento que nos complementamos bastante, ¿te gustaría ir en mi expedición?"
                show marina sonriendo at left
                with Dissolve(.5)
                m "Por favor, [nombre_personaje], me vas a hacer sonrojar. Me encantaría."                
                y "Laura, ¿estás de acuerdo en ir con Bob?"
                l "¡Por supuesto! No hay problema."
                $ va_con_marina = True
                $ liderazgo += 1
                jump p5_division_tareas

            "Me gustaría pasar un rato con Laura y poder limar asperezas con ella." if laura < 2:
                y "Laura, sé que empezamos con el pié izquierdo. Tal vez si vamos juntos podamos conversar un poco."
                show laura seria at right
                with Dissolve(.5)
                l "Es verdad, hablando se entienden las personas."
                y "Marina, estarás bien con Bob, ¿no?"
                m "¡Claro!"
                $ va_con_laura = True
                $ liderazgo += 1
                jump p5_division_tareas

            "Laura ha desmotrado una gran resiliencia, juntos seguro tendremos éxito." if laura > 1:
                y "Laura, me encantaría que fuéramos juntos, si estás de acuerdo."
                show laura sonriendo at right
                with Dissolve(.5)
                l "¡Estaba por proponerte lo mismo!"
                b "Excelente, entonces Marina y yo conformaremos la otra expedición."
                m "Me parece perfecto."
                $ va_con_laura = True
                $ liderazgo += 1
                jump p5_division_tareas
                            
            "Más allá de todo lo que ha pasado, Bob ha demostrado tener buen criterio. Quizá sea mejor ver qué propone.":
                pause 1

                if encontraron_agua:
                    b "¿Qué les parece si [nombre_personaje] y yo exploramos el área cercana a la playa?"
                    b "Podemos revisar la orilla a ver si la marea trajo algo más."
                    l "Genial, entonces Marina y yo iremos a buscar agua al lugar que encontramos ayer."
                    m "No olviden mantener los ojos abiertos por algo de comida. Nosotras haremos lo mismo."
                    $ va_con_bob = True
                    hide bob
                    with Dissolve(.5)
                    hide marina
                    with Dissolve(.5)
                    hide laura
                    with Dissolve(.5)
                    jump p5playa

                elif reporte_encontrar_agua_comida:
                    b "Estaba pensando, quizá sea mejor que no nos separemos. Ya sabemos dónde hay agua, gracias a [nombre_personaje]."
                    b "Podemos pasar por la playa a ver si hay algo que rescatar, y seguir hacia allí luego."
                    l "Buena idea, Bob. Entre todos podremos cargar bastantes recursos de vuelta al refugio."
                    y "Vamos, ¡a la playa!."
                    $ exploran_todos = True
                    hide bob
                    with Dissolve(.5)
                    hide marina
                    with Dissolve(.5)
                    hide laura
                    with Dissolve(.5)
                    jump p5playa

                else:
                    b "Dijiste que había cosas en la playa, ¿verdad [nombre_personaje]?"
                    b "Quizá tu y yo podríamos ir a ver si queda algo, o si la marea trajo algo más."
                    l "Genial, entonces Marina y yo iremos a explorar el interior de la jungla a ver si encontramos agua y comida."
                    m "¡Mantengan los ojos abiertos ustedes dos también!"
                    $ va_con_bob = True
                    hide bob
                    with Dissolve(.5)
                    hide marina
                    with Dissolve(.5)
                    hide laura
                    with Dissolve(.5)
                    jump p5playa

    else:
        "Los tres se internan en la jungla."
        $ exploran_tres = True
        hide bob
        with Dissolve(0.5)
        hide marina
        with Dissolve(0.5)
        hide laura
        with Dissolve(0.5)
        show bg jungle1 1 at truecenter
        with Dissolve(.5)

        if reporte_encontrar_agua_comida:
            y "Vamos, les mostraré dónde encontré los frutos, allí había agua."

            if not stuff_bidon_agua and bob_se_queda:
                show laura hablando at right
                with Dissolve(0.5)
                l "Ayer pensaba... En la jungla hay bastante bambú."
                l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
                show marina hablando at left
                with Dissolve(0.5)
                m "Podremos traer varios litros si hacemos unos cuantos."
                $ inventan_cantimploras = True
                hide laura
                with Dissolve(0.5)
                hide marina
                with Dissolve(0.5)          

            elif not stuff_bidon_agua and (laura_se_queda or marina_se_queda):
                show bob parado hablando at center
                with Dissolve(0.5)
                b "Ayer, cuando me costaba conciliar el sueño, preparé estos contenedores quebrando cañas de bambú."
                b "Podremos traer unos cuantos litros de vuelta al refugio."
                $ inventan_cantimploras = True
                hide bob
                with Dissolve(0.5)  

            jump arroyo_frutos

        elif encontraron_agua:
            y "Ayer cuando regresaron dijeron que habían encontrado agua. ¿Recuerdas cómo llegar hasta allí?"
            if laura_se_queda:
                show marina hablando at center
                with Dissolve(0.5)
                m "Si, es por aquí, ¡síganme!"
                hide marina
                with Dissolve(0.5)
            elif marina_se_queda:
                show laura hablando at center
                with Dissolve(0.5)
                l "Si, es por aquí, ¡síganme!"
                hide laura
                with Dissolve(0.5)
            elif bob_se_queda:
                show laura hablando at center
                with Dissolve(0.5)
                l "Si, es por aquí, ¡síguenos!"
                hide laura
                with Dissolve(0.5)
            jump manantial_marina_laura

        else:
            y "Vamos, tenemos que encontrar agua y comida lo antes posible."
            jump exploracion_profunda

label p5_division_tareas:
    if reporte_encontrar_agua_comida and va_con_laura:
        y "Laura, ¿qué te parece si vamos al lugar que encontré ayer?"
        l "Sin duda. Por más que no queden más frutas, el agua nos vendrá bien."
        b "Marina y yo buscaremos comida entonces."
        m "¡Mucha suerte, equipo!"
        hide bob
        with Dissolve(.5)
        hide marina
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        jump arroyo_frutos

    elif reporte_encontrar_agua_comida and va_con_marina:
        y "Marina, ¿qué te parece si vamos al lugar que encontré ayer?"
        m "Es la única fuente de agua que conocemos, así que hagámoslo."
        b "Laura y yo nos enfocaremos en encontrar algo para comer entonces."
        l "Por favor, ¡tengan cuidado!"
        hide bob
        with Dissolve(.5)
        hide marina
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        jump arroyo_frutos

    elif encontraron_agua and va_con_laura:
        y "Laura, tal vez sea buena idea que vayamos a ese lugar que encontraron ayer con Marina."
        l "Si, traigamos algo de agua. Bob y Marina pueden concentrarse en buscar comida."
        b "¿Estamos todos de acuerdo entonces?"
        m "Nos vemos aquí al regreso. ¡Suerte!"
        hide bob
        with Dissolve(.5)
        hide marina
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        jump manantial_marina_laura
    
    elif encontraron_agua and va_con_marina:
        y "Marina, tal vez sea buena idea que vayamos a ese lugar que encontraron ayer con Laura."
        m "Si, un grupo debe ir a la segura."
        b "Bien, entonces Laura y yo exploraremos en busca de comida."
        l "¡Hagámoslo!"
        hide bob
        with Dissolve(.5)
        hide marina
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        jump manantial_marina_laura

    else:
        b "Salgamos para lados opuestos, así cubriremos más terreno."
        l "Estoy de acuerdo, hoy es el día, tenemos que encontrar algo sí o sí."
        m "¡Estoy segura de que lo lograremos!"
        hide bob
        with Dissolve(.5)
        hide marina
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        jump exploracion_profunda

label exploracion_profunda:
    show bg jungle1 1 at truecenter
    with Dissolve(.5)
    pause 1
    "Explorando la jungla encuentran un sendero que parece haber sido usado antes."
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    "Lo siguen y descubren un pequeño claro con algunas frutas comestibles y una fuente de agua cercana."
    jump arroyo_frutos

label arroyo_frutos:
    show bg jungle river at truecenter
    with Dissolve(.5)
    if bob_se_queda and not reporte_encontrar_agua_comida:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Sabía que lo lograríamos si perseverábamos!"
        show laura sonriendo at right
        with Dissolve(.5)
        l "El agua está fresca y clara, y parece haber suficientes frutos para que todos podamos comer hoy."
        "Laura y Marina corren a beber agua del arroyo."
        $ choice_position = "superior" # default alta superior
        menu:
            "No sabemos si está limpia, habría que hervirla antes. No es bueno que beban.":
                y "¡Esperen! Será mejor que hirvamos el agua antes de beberla."
                $ desicion_intro += 1
                $ marina += 1
                $ laura += 1
                $ liderazgo += 1
                $ reporte_advierte_agua = True
                l "Odio decirlo, porque tengo mucha sed, pero [nombre_personaje] tiene razón."
                m "Uff, bueno. ¿Podemos al menos comer un par de frutos antes de llevar todo de vuelta al campamento?"
                l "No veo por qué no."
                $ update_stat("hambre", hambre +1)
                $ show_variable_changed_popup("El hambre ha disminuido", verde)
                hide screen combined_ui
                show screen combined_ui

            "Esa agua podría tener parásitos. Esperaré a ver cómo se sienten cuando regresemos.":
                "Haces de cuenta que bebes una vez que Laura y Marina terminan y se distraen con los frutos."
                $ desicion_intro += 1                
                $ reporte_conejillos_de_indias = True

        if stuff_bidon_agua:
            y "Rellenemos el bidón, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle comida a Ingrid."
            m "¡Van a estar tan contentos cuando vean todo lo que llevamos!"
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle comida a Ingrid."
            m "¡Ella y Bob van a estar tan contentos cuando vean todo lo que llevamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, Laura!"
            y "Manos a la obra entonces."
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif marina_se_queda and not reporte_encontrar_agua_comida:
        show laura sonriendo at left
        with Dissolve(.5)
        l "¡Miren este oasis!"
        show bob parado hablando at right
        with Dissolve(.5)
        b "El agua está fresca y clara, y parece haber suficientes frutos para que todos podamos comer hoy."
        "Laura y Bob corren a beber agua del arroyo."
        $ choice_position = "alta" # default alta superior
        menu:
            "No sabemos si está limpia, habría que hervirla antes. No es bueno que beban.":
                y "¡Esperen! Será mejor que hirvamos el agua antes de beberla."
                $ desicion_intro += 1
                $ reporte_advierte_agua = True
                b "Odio decirlo, porque tengo mucha sed, pero [nombre_personaje] tiene razón."
                l "Uff, bueno. ¿Podemos al menos comer un par de frutos antes de llevar todo de vuelta al campamento?"
                b "No veo por qué no."
                $ update_stat("hambre", hambre +1)
                $ show_variable_changed_popup("El hambre ha disminuido", verde)
                hide screen combined_ui
                show screen combined_ui
                $ laura += 1
                $ bob += 1
                $ liderazgo += 1

            "Esa agua podría tener parásitos. Esperaré a ver cómo se sienten cuando regresemos.":
                "Haces de cuenta que bebes una vez que Laura y Bob terminan y se distraen con los frutos." 
                $ desicion_intro += 1
                $ reporte_conejillos_de_indias = True

        if stuff_bidon_agua:
            y "Rellenemos el bidón, recojamos todos los frutos y volvamos."
            b "Si, debemos llevarle comida a Ingrid."
            l "¡Ella y Marina van a estar tan contentas cuando vean todo lo que llevamos!"
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            b "Si, debemos llevarle comida a Ingrid."
            l "¡Ella y Marina van a estar tan contentas cuando vean todo lo que llevamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            b "¡Qué buena idea, Laura!"
            y "Manos a la obra entonces."
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif laura_se_queda and not reporte_encontrar_agua_comida:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Sabía que lo lograríamos si perseverábamos!"
        show bob parado hablando at right
        with Dissolve(.5)
        b "El agua está fresca y clara, y parece haber suficientes frutos para que todos podamos comer hoy."
        "Marina y Bob corren a beber agua del arroyo."
        menu:
            "No sabemos si está limpia, habría que hervirla antes. No es bueno que beban.":
                y "¡Esperen! Será mejor que hirvamos el agua antes de beberla."
                $ desicion_intro += 1
                $ marina += 1
                $ bob += 1
                $ liderazgo += 1
                $ reporte_advierte_agua = True
                b "Odio decirlo, porque tengo mucha sed, pero [nombre_personaje] tiene razón."
                m "Uff, bueno. ¿Podemos al menos comer un par de frutos antes de llevar todo de vuelta al campamento?"
                b "No veo por qué no."
                $ update_stat("hambre", hambre +1)
                $ show_variable_changed_popup("El hambre ha disminuido", verde)                
                hide screen combined_ui
                show screen combined_ui
            "Esa agua podría tener parásitos. Esperaré a ver cómo se sienten cuando regresemos.":
                "Haces de cuenta que bebes una vez que Marina y Bob terminan y se distraen con los frutos."
                $ desicion_intro += 1
                $ reporte_conejillos_de_indias = True

        if stuff_bidon_agua:
            y "Rellenemos el bidón, recojamos todos los frutos y volvamos."
            b "Si, debemos llevarle comida a Ingrid."
            m "¡Ella y Laura van a estar tan contentas cuando vean todo lo que llevamos!"
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            b "Si, debemos llevarle comida a Ingrid."
            m "¡Ella y Laura van a estar tan contentas cuando vean todo lo que llevamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            b "Por aquí hay bastante bambú."
            b "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, Bob!"
            y "Manos a la obra entonces."
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif bob_se_queda and reporte_encontrar_agua_comida:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Agua, al fin!"
        show laura sonriendo at right
        with Dissolve(.5)
        l "Está fresca y clara."
        "Los tres corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui
        
        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            m "¡Vamos!"
            $ agua = 10
            $ actualizar_boton_imagen()

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            m "¡Vamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, Laura!"
            y "Manos a la obra entonces."
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5          
            "Al terminar de cargarlas, emprenden la vuelta al refugio."
            
    elif marina_se_queda and reporte_encontrar_agua_comida:
        show laura sonriendo at right
        with Dissolve(.5)
        l "¡Agua, al fin!"
        show bob pensando at left
        with Dissolve(.5)
        b "Está fresca y clara."
        "Los tres corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui
        
        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            b "Si, debemos llevarle agua a Ingrid."
            l "¡Vamos!"
            $ agua = 10
            $ actualizar_boton_imagen()

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú y volvamos."
            b "Si, debemos llevarle agua a Ingrid."
            l "¡Vamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            b "¡Qué buena idea, Laura!"
            y "Manos a la obra entonces."
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()

            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Al terminar de cargarlas, emprenden la vuelta al refugio."

    elif laura_se_queda and reporte_encontrar_agua_comida:
        show marina sonriendo at right
        with Dissolve(.5)
        l "¡Agua, al fin!"
        show bob pensando at left
        with Dissolve(.5)
        b "Está fresca y clara."
        "Los tres corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui
        
        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            b "Si, debemos llevarle agua a Ingrid."
            m "¡Vamos!"
            $ agua = 10
            $ actualizar_boton_imagen()

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú y volvamos."
            b "Si, debemos llevarle agua a Ingrid."
            m "¡Vamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            b "Por aquí hay bastante bambú."
            b "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, Bob!"
            y "Manos a la obra entonces."
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Al terminar de cargarlas, emprenden la vuelta al refugio."

    elif va_con_marina and not reporte_encontrar_agua_comida:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Sabía que lo lograríamos si perseverábamos!"
        "Marina corre a beber agua del arroyo."
        $ choice_position = "superior" # default alta superior
        menu:
            "No sabemos si está limpia, habría que hervirla antes. No es bueno que beba.":
                y "¡Espera, Marina! Será mejor que hirvamos el agua antes de beberla."
                $ desicion_intro += 1
                $ marina += 1
                $ reporte_advierte_agua = True
                m "Uff, bueno. ¿Podemos al menos comer un par de frutos antes de llevar todo de vuelta al campamento?"
                y "No veo por qué no."
                $ update_stat("hambre", hambre +1)
                $ show_variable_changed_popup("El hambre ha disminuido", verde)
                hide screen combined_ui
                show screen combined_ui
                $ desicion_intro += 1
                $ liderazgo += 1

            "Esa agua podría tener parásitos. Esperaré a ver cómo se siente cuando regresemos.":
                "Haces de cuenta que bebes una vez que Marina termina y se distrae con los frutos."
                $ desicion_intro += 1
                $ reporte_conejillos_de_indias = True

        if stuff_bidon_agua:
            y "Rellenemos el bidón, recojamos todos los frutos y volvamos."
            m "¡Van a estar tan contentos cuando vean todo lo que llevamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            m "¡Van a estar tan contentos cuando vean todo lo que llevamos!"
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            m "Por aquí hay bastante bambú."
            m "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            y "¡Qué buena idea, Marina! Manos a la obra entonces."
            if marina > 0:
                "Despues de todo, hacemos muy buen equipo, [nombre_personaje]."
                $ marina += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif va_con_laura and not reporte_encontrar_agua_comida:
        show laura sonriendo at left
        with Dissolve(.5)
        l "El agua está fresca y clara, ¡y parece haber suficientes frutos para que todos podamos comer hoy!"
        $ choice_position = "superior" # default alta superior
        menu:
            "No sabemos si está limpia, habría que hervirla antes. No es bueno que beba.":
                y "¡Espera, Laura! Será mejor que hirvamos el agua antes de beberla."
                $ desicion_intro += 1
                $ laura += 1
                $ reporte_advierte_agua = True
                l "Uff, bueno. ¿Podemos al menos comer un par de frutos antes de llevar todo de vuelta al campamento?"
                y "No veo por qué no."
                $ update_stat("hambre", hambre +1)
                $ show_variable_changed_popup("El hambre ha disminuido", verde)
                hide screen combined_ui
                show screen combined_ui
                $ desicion_intro += 1
                $ liderazgo += 1

            "Esa agua podría tener parásitos. Esperaré a ver cómo se siente cuando regresemos.":
                "Haces de cuenta que bebes una vez que Marina termina y se distrae con los frutos."
                $ desicion_intro += 1
                $ reporte_conejillos_de_indias = True

        if stuff_bidon_agua:
            y "Rellenemos el bidón, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle comida a Ingrid."
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle comida a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            y "¡Qué buena idea, Laura! Manos a la obra entonces."
            if laura > 0:
                "Despues de todo, hacemos muy buen equipo, [nombre_personaje]."
                $ laura += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif va_con_marina and reporte_encontrar_agua_comida:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Agua, al fin!"
        y "Está fresca y clara."
        "Ambos corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            m "Por aquí hay bastante bambú."
            m "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            y "¡Qué buena idea, Marina! Manos a la obra entonces."
            m "Despues de todo, no hacemos tan mal equipo, [nombre_personaje]."
            $ marina += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."
            
    elif va_con_laura and reporte_encontrar_agua_comida:
        show laura sonriendo at left
        with Dissolve(.5)
        l "¡Agua, al fin!"
        y "Está fresca y clara."
        "Ambos corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            y "¡Qué buena idea, Laura! Manos a la obra entonces."
            l "Despues de todo, no hacemos tan mal equipo, [nombre_personaje]."
            $ laura += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif exploran_todos:
        show laura sonriendo at right
        with Dissolve(.5)
        l "¡Agua!"
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Al fin!"
        show bob parado hablando at center
        with Dissolve(.5)
        b "Parece fresca y clara."        
        "Todos corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            m "Gracias, [nombre_personaje], por traernos hasta aquí."
            b "Buen trabajo."
            $ liderazgo += 1
            $ bob += 1
            $ marina += 1
            $ laura += 1
            $ agua = 10
            $ actualizar_boton_imagen()
            $ comida = 10

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            m "Gracias, [nombre_personaje], por traernos hasta aquí."
            b "Buen trabajo."
            $ liderazgo += 1
            $ bob += 1
            $ marina += 1
            $ laura += 1
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10

        else:
            b "Tenemos que encontrar una forma de transportar el agua."
            y "Por aquí hay bastante bambú."
            y "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, [nombre_personaje]! Manos a la obra entonces."
            l "Despues de todo, tienes madera de líder, [nombre_personaje]."
            $ laura += 1
            $ liderazgo += 1
            $ bob += 1
            $ marina += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()
            $ comida = 10
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    hide bob
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)
    jump retorno_refugio

label manantial_marina_laura:
    "Recorren la jungla a gran velocidad, atentos por si ven comida, pero tratando de llegar rápido para poder volver con luz."
    show bg jungle river at truecenter
    with Dissolve(.5)

    if va_con_marina:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Aquí está! El manantial del que les hablamos."
        y "Está fresca y clara."
        "Ambos corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()              

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()            

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            m "Por aquí hay bastante bambú."
            m "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            y "¡Qué buena idea, Marina! Manos a la obra entonces."
            m "Despues de todo, no hacemos tan mal equipo, [nombre_personaje]."
            $ marina += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()           
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif va_con_laura:
        show laura sonriendo at left
        with Dissolve(.5)
        l "¡Aquí está! El manantial del que les hablamos."
        y "Está fresca y clara."
        "Ambos corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            y "¡Qué buena idea, Laura! Manos a la obra entonces."
            l "Despues de todo, no hacemos tan mal equipo, [nombre_personaje]."
            $ laura += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif exploran_tres and bob_se_queda:
        show laura sonriendo at right
        with Dissolve(.5)
        l "¡Aquí está! El manantial del que les hablamos."
        show marina sonriendo at left
        with Dissolve(.5)
        m "Está fresca y clara."
        "Los tres corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, Laura!"
            y "Manos a la obra entonces."
            l "Despues de todo, no hacemos tan mal equipo, nosotros tres."
            $ laura += 1
            $ marina += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif exploran_tres and marina_se_queda:
        show laura sonriendo at right
        with Dissolve(.5)
        l "¡Aquí está! El manantial del que les hablamos."
        show bob pensando at left
        with Dissolve(.5)
        b "Está fresca y clara."
        "Los tres corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            l "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            l "Por aquí hay bastante bambú."
            l "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            b "¡Qué buena idea, Laura!"
            y "Manos a la obra entonces."
            l "Despues de todo, no hacemos tan mal equipo, nosotros tres."
            $ laura += 1
            $ bob += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."

    elif exploran_tres and laura_se_queda:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Aquí está! El manantial del que les hablamos."
        show bob pensando at right
        with Dissolve(.5)
        b "Está fresca y clara."
        "Los tres corren a beber agua del arroyo."
        $ actualizar_boton_imagen()
        $ update_stat("sed", sed + 3)
        $ show_variable_changed_popup("La sed ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui

        if stuff_bidon_agua:
            y "Rellenemos el bidón y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        elif inventan_cantimploras:
            y "Llenemos las cantimploras de bambú, recojamos todos los frutos y volvamos."
            m "Si, debemos llevarle agua a Ingrid."
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   

        else:
            y "Tenemos que encontrar una forma de transportar el agua."
            b "Por aquí hay bastante bambú."
            b "Podemos usarlo para transportar agua si quebramos las cañas en cada sección."
            m "¡Qué buena idea, Bob!"
            y "Manos a la obra entonces."
            m "Despues de todo, no hacemos tan mal equipo, nosotros tres."
            $ marina += 1
            $ bob += 1
            pause 1
            $ inventan_cantimploras = True
            $ agua = 10
            $ boton_imagen = "bidon_lleno_icon.png"
            show screen top_right_button(boton_imagen)
            $ stuff_button_1 = "bidon"
            $ actualizar_boton_imagen()   
            "Les lleva un tiempo, pero logran hacer unas cantimploras con el bambú."
            pause .5
            "Juntan todo lo que consiguieron y emprenden la vuelta al refugio."
            
    hide bob
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    jump retorno_refugio

label p5playa:
    if exploran_todos:
        if not (reporte_esconde_bote or reporte_esconde_caja or reporte_comparte_bote or reporte_comparte_caja):
            "Luego de volver tras sus pasos del día anterior durante un rato, los cuatro llegan juntos a la playa."
        else:
            "El sol les ciega un poco."
        hide marina
        with Dissolve(.5)
        hide bob
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        show bg beach sunny at truecenter
        with Dissolve(.5)
        
        if stuff_bote and not (reporte_comparte_bote or reporte_esconde_bote):
            $ choice_position = "default" # default alta superior 
            menu:
                "El bote que rescaté de la playa no está muy lejos de aquí. Tal vez Bob pueda revisarlo.":
                    y "Bob, acompáñame, no estamos muy lejos de donde resguardé el bote que recuperé."
                    $ desicion_intro += 1
                    $ reporte_comparte_bote = True
                    show bob pensando at center
                    with Dissolve(.5)
                    b "¡Excelente! Veamos como está."
                    show laura hablando at right
                    with Dissolve(.5)
                    l "Marina, acompáñame a la playa, veamos si quedó algo allí."
                    show marina hablando at center
                    with Dissolve(.5)
                    m "Ay... ¡Espero que si!"
                    hide marina
                    with Dissolve(.5)
                    hide laura
                    with Dissolve(.5)
                    pause .5
                    "Luego de quitar las hojas que usaste para proteger el bote, lo voltean."
                    "Bob lo revisa minuciosamente."
                    show bob gr serio sucio at leftgr
                    with Dissolve(.5)
                    b "El casco no está perforado, y no ha entrado agua en las reservas de flotación. Pero faltan los remos."
                    y "Seguramente podamos construir unos."
                    b "Este bote será de gran ayuda, [nombre_personaje]."
                    $ bob += 1           
                    b "Improvisaremos unas cañas e intentaremos pescar."
                    y "Lo volveré a resguardar."
                    "Vuelves a cubrir el bote con las hojas que usaste para protegerlo y se dirigen a la orilla."
                    hide bob
                    with Dissolve (.5)

                "El bote está escondido cerca de aquí, pero mejor será no decir nada hasta que sea necesario.":
                    "Siguen caminando hasta la orilla y comienzan a buscar algo para recuperar."
                    $ desicion_intro += 1
                    $ reporte_esconde_bote = True
                    jump p5playa

        elif stuff_caja_grande and not (reporte_comparte_caja or reporte_esconde_caja):
            $ choice_position = "default" # default alta superior 
            menu:
                "La caja que rescaté de la playa no está muy lejos de aquí. Tal vez sería bueno revisarla.":
                    y "Vengan, acompáñenme. Dejé la caja que encontré en la playa resguardada por aquí cerca."
                    $ desicion_intro += 1
                    $ reporte_comparte_caja = True
                    pause .5
                    "Remueves las hojas que usaste para proteger la caja."
                    show marina hablando at left
                    with Dissolve(.5)
                    m "¿Creen que podremos abrirla entre todos?"
                    show bob pensando at center
                    with Dissolve(.5)
                    b "Si, hagamos fuerza a la cuenta de tres."
                    show laura hablando at right
                    with Dissolve(.5)
                    pause 0.5
                    l "Uno..."
                    pause 0.5
                    l "Dos..."
                    pause 0.5
                    l "¡Tres!"
                    pause 0.5
                    "Dentro de la caja hay una pistola de bengalas, una pala, instrumentos para hacer fuego, un cuchillo, una parrilla y una brújula."
                    y "¡Miren todo esto!"
                    m "¡Qué dicha!"
                    l "¡Ahora podremos cocinar algo!"
                    "Bob mira el contenido de la caja, pensativo."
                    m "Bob, ¿qué pasa?"
                    b "¿Eh? No, nada, estaba pensando en todo lo que podremos hacer con esto."
                    b "Sin duda es un gran botín."
                    y "¡Vamos a ver si resolvemos el problema del agua!"

                "La caja está escondida cerca de aquí, pero mejor será no decir nada hasta que no haya alternativa.":
                    "Siguen caminando hasta la orilla y comienzan a buscar algo para recuperar."
                    $ desicion_intro += 1
                    $ reporte_esconde_caja = True
                    jump p5playa

        else:
            "Parece que la marea trajo más restos del naufragio luego de que la tormenta amainó."
            pause 0.5
            "Laura y Marina comienzan a desenterrar algo de la arena."
            if stuff_caja_grande:
                "Parece que se trata de un bote."
                show marina hablando at left
                with Dissolve(.5)
                m "Bob, ¿crees que podremos usarlo para irnos de aquí?"
                show bob pensando at center
                with Dissolve(.5)
                b "No, si bien parece estar intacto, no es una embarcación para hacerse a la mar."
                show laura hablando at right
                with Dissolve(.5)
                l "Ni siquiera tiene remos."
                y "Eso podemos fabricarlo nosotros."
                b "Si, y unas cañas, ¡para poder pescar!"
                $ stuff_bote = True    
                $ boton_imagen = "bote_icon.png"
                show screen top_right_button(boton_imagen)
                $ stuff_button_1 = "bote"

            elif stuff_bote:
                "Parece que es una caja de madera."
                show marina hablando at left
                with Dissolve(.5)
                m "¿Creen que podremos abrirla entre todos?"
                show bob pensando at center
                with Dissolve(.5)
                b "Si, hagamos fuerza a la cuenta de tres."
                show laura hablando at right
                with Dissolve(.5)
                pause 0.5
                l "Uno..."
                pause 0.5
                l "Dos..."
                pause 0.5
                l "¡Tres!"
                pause 0.5
                "Dentro de la caja hay una pistola de bengalas, una pala, instrumentos para hacer fuego, un cuchillo, una parrilla y una brújula."
                y "¡Miren todo esto!"
                m "¡Qué dicha!"
                l "¡Ahora podremos cocinar algo!"
                "Bob mira el contenido de la caja, pensativo."
                m "Bob, ¿qué pasa?"
                b "¿Eh? No, nada, estaba pensando en todo lo que podremos hacer con esto."
                b "Sin duda es un gran botín."
                $ caja_abierta = True

            else:
                "Esforzándose entre todos para remover la arena, descubren un bote con una caja de madera adentro."
                show marina hablando at left
                with Dissolve(.5)
                m "Bob, ¿crees que podremos usar este bote para irnos de aquí?"
                show bob pensando at center
                with Dissolve(.5)
                b "No, si bien parece estar intacto, no es una embarcación para hacerse a la mar."
                show laura hablando at right
                with Dissolve(.5)
                l "Ni siquiera tiene remos."
                y "Eso podemos fabricarlo nosotros."
                b "Si, y unas cañas, ¡para poder pescar!"
                $ stuff_bote = True    
                $ boton_imagen = "bote_icon.png"
                show screen top_right_button(boton_imagen)
                $ stuff_button_1 = "bote"
                pause .5
                m "¿Creen que podremos abrir la caja entre todos?"
                b "Si, hagamos fuerza a la cuenta de tres."
                pause 0.5
                l "Uno..."
                pause 0.5
                l "Dos..."
                pause 0.5
                l "¡Tres!"
                pause 0.5
                "Dentro de la caja hay una pistola de bengalas, una pala, instrumentos para hacer fuego, un cuchillo, una parrilla y una brújula."
                y "¡Miren todo esto!"
                m "¡Qué dicha!"
                l "¡Ahora podremos cocinar algo!"
                "Bob mira el contenido de la caja, pensativo."
                m "Bob, ¿qué pasa?"
                b "¿Eh? No, nada, estaba pensando en todo lo que podremos hacer con esto."
                b "¡Sin duda es un gran botín!"
                $ caja_abierta = True
            
        "Contentos con los hallazgos, los cuatro se meten a la selva para buscar agua."
        $ update_stat("cansancio", cansancio - 1)
        $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
        hide marina
        with Dissolve(.5)
        hide bob
        with Dissolve(.5)
        hide laura
        with Dissolve(.5)
        jump arroyo_frutos

    elif va_con_bob:
        if not (reporte_esconde_bote or reporte_esconde_caja or reporte_comparte_bote or reporte_comparte_caja):
            "Luego de volver tras sus pasos del día anterior durante un rato, los cuatro llegan juntos a la playa."
        else:
            "El sol les ciega un poco."
        
        show bg beach sunny at truecenter
        with Dissolve(.5) 
        if stuff_bote and not (reporte_comparte_bote or reporte_esconde_bote):
            $ choice_position = "default" # default alta superior 
            menu:
                "El bote que rescaté de la playa no está muy lejos de aquí. Tal vez Bob pueda revisarlo.":
                    y "Bob, acompáñame, no estamos muy lejos de donde resguardé el bote que recuperé."
                    $ desicion_intro += 1
                    $ reporte_comparte_bote = True
                    show bob pensando at left
                    with Dissolve(.5)
                    b "¡Excelente! Veamos como está."
                    pause .5
                    "Luego de quitar las hojas que usaste para proteger el bote, lo voltean."
                    "Bob lo revisa minuciosamente."
                    show bob gr serio sucio at leftgr
                    with Dissolve(.5)
                    b "El casco no está perforado, y no ha entrado agua en las reservas de flotación. Pero faltan los remos."
                    y "Seguramente podamos construir unos."
                    b "Este bote será de gran ayuda, [nombre_personaje]."
                    $ bob += 1           
                    b "Improvisaremos unas cañas e intentaremos pescar."
                    y "Lo volveré a resguardar."
                    "Vuelves a cubrir el bote con las hojas que usaste para protegerlo y se dirigen a la orilla."
                    $ stuff_bote = True    
                    $ boton_imagen = "bote_icon.png"
                    show screen top_right_button(boton_imagen)
                    $ stuff_button_1 = "bote"
                    hide bob
                    with Dissolve (.5)

                "El bote está escondido cerca de aquí, pero mejor será no decir nada hasta que sea necesario.":
                    "Siguen caminando hasta la orilla y comienzan a buscar algo para recuperar."
                    $ desicion_intro += 1
                    $ reporte_esconde_bote = True
                    jump p5playa

        elif stuff_caja_grande and not (reporte_comparte_caja or reporte_esconde_caja):
            $ choice_position = "default" # default alta superior 
            menu:
                "La caja que rescaté de la playa no está muy lejos de aquí. Tal vez sería bueno revisarla.":
                    y "Vamos, acompáñanme. Dejé la caja que encontré en la playa resguardada por aquí cerca."
                    $ desicion_intro += 1
                    $ reporte_comparte_caja = True
                    pause .5
                    "Remueves las hojas que usaste para proteger la caja."
                    y "¿Crees que podremos abrirla entre los dos?"
                    show bob pensando at center
                    with Dissolve(.5)
                    b "Si, hagamos fuerza a la cuenta de tres."
                    pause 0.5
                    b "Uno..."
                    pause 0.5
                    b "Dos..."
                    pause 0.5
                    b "¡Tres!"
                    pause 0.5
                    "Dentro de la caja hay una pistola de bengalas, una pala, instrumentos para hacer fuego, un cuchillo, una parrilla y una brújula."
                    y "¡Mira todo esto!"                    
                    "Bob mira el contenido de la caja, pensativo."
                    y "Bob, ¿qué pasa?"
                    b "¿Eh? No, nada, estaba pensando en todo lo que podremos hacer con esto."
                    b "Sin duda es un gran botín."
                    y "¡Vamos a ver si hay algo más en la playa!"
                    $ caja_abierta = True

                "La caja está escondida cerca de aquí, pero mejor será no decir nada hasta que no haya alternativa.":
                    "Siguen caminando hasta la orilla y comienzan a buscar algo para recuperar."
                    $ desicion_intro += 1
                    $ reporte_esconde_caja = True
                    jump p5playa
        else:
            "Caminan hasta la orilla"
            "Parece que la marea trajo más restos del naufragio luego de que la tormenta amainó."
            pause 0.5
            "Bob ve algo y comienza a desenterrarlo."
            if stuff_caja_grande:
                "Parece que se trata de un bote."                
                y "Bob, ¿crees que podremos usarlo para irnos de aquí?"
                show bob pensando at center
                with Dissolve(.5)
                b "No, si bien parece estar intacto, no es una embarcación para hacerse a la mar."                
                b "Ni siquiera tiene remos."
                y "Eso podemos fabricarlo nosotros."
                b "Si, y unas cañas, ¡para poder pescar!"
                $ stuff_bote = True    
                $ boton_imagen = "bote_icon.png"
                show screen top_right_button(boton_imagen)
                $ stuff_button_1 = "bote"

            elif stuff_bote:
                "Parece que es una caja de madera."
                y "¿Crees que podremos abrirla?"
                show bob pensando at center
                with Dissolve(.5)
                b "Si, hagamos fuerza a la cuenta de tres."                
                pause 0.5
                b "Uno..."
                pause 0.5
                b "Dos..."
                pause 0.5
                b "¡Tres!"
                pause 0.5
                "Dentro de la caja hay una pistola de bengalas, una pala, instrumentos para hacer fuego, un cuchillo, una parrilla y una brújula."
                y "¡Mira todo esto!"                
                "Bob mira el contenido de la caja, pensativo."
                y "Bob, ¿qué pasa?"
                b "¿Eh? No, nada, estaba pensando en todo lo que podremos hacer con esto."
                b "Sin duda es un gran botín."
                $ caja_abierta = True

            else:
                "Esforzándose entre los dos para remover la arena, descubren un bote con una caja de madera adentro."
                y "Bob, ¿crees que podremos usar este bote para irnos de aquí?"
                show bob pensando at center
                with Dissolve(.5)
                b "No, si bien parece estar intacto, no es una embarcación para hacerse a la mar."                
                b "Ni siquiera tiene remos."
                y "Eso podemos fabricarlo nosotros."
                b "Si, y unas cañas, ¡para poder pescar!"
                $ stuff_bote = True    
                $ boton_imagen = "bote_icon.png"
                show screen top_right_button(boton_imagen)
                $ stuff_button_1 = "bote"
                pause .5
                y "¿Crees que podremos abrir la caja entre los dos?"
                b "Si, hagamos fuerza a la cuenta de tres."
                pause 0.5
                b "Uno..."
                pause 0.5
                b "Dos..."
                pause 0.5
                b "¡Tres!"
                pause 0.5
                "Dentro de la caja hay una pistola de bengalas, una pala, instrumentos para hacer fuego, un cuchillo, una parrilla y una brújula."
                y "¡Mira todo esto!"                
                "Bob mira el contenido de la caja, pensativo."
                y "Bob, ¿qué pasa?"
                b "¿Eh? No, nada, estaba pensando en todo lo que podremos hacer con esto."
                b "¡Sin duda es un gran botín!"
                $ caja_abierta = True

        "Contentos con los hallazgos, emprenden el retorno al refugio."
        hide bob
        with Dissolve(.5)
        jump retorno_refugio
    
label retorno_refugio:
    show bg jungle1 1 at truecenter
    with Dissolve(.5)

    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)

    if comida <=2 and (exploran_todos or exploran_tres):
        "En el camino de vuelta, encuentran unos pocos frutos de una especie que hasta ahora no habían visto, parecen sabrosos."
        $ comida += 5
        "Comen algunos y llevan el resto para el campamento."
        $ update_stat("hambre", hambre +1)
        $ show_variable_changed_popup("El hambre ha disminuido", verde)
        hide screen combined_ui
        show screen combined_ui            
        "También ven huellas de grandes pezuñas."
        "Se miran, pero nadie quiere decir lo obvio."
        "Antes de continuar te acercas a un árbol en el que parece que las huellas se detienen."
        "Hay marcas en la madera, como si algo con grandes colmillos hubiera estado rascando la corteza."

    elif exploran_todos or exploran_tres:
        "En el camino de vuelta, encuentran huellas de grandes pezuñas."
        "Se miran, pero nadie quiere decir lo obvio."
        "Antes de continuar te acercas a un árbol en el que parece que las huellas se detienen."
        "Hay marcas en la madera, como si algo con grandes colmillos hubiera estado rascando la corteza."
        
    if refugio == "cabaña":
        show bg jungle hut at truecenter
        with Dissolve(.5)
    elif refugio == "cueva":
        show bg jungle cave at truecenter
        with Dissolve(.5)
    elif refugio == "claro":
        show bg jungle clearing at truecenter
        with Dissolve(.5)

    "Luego de una ardua jornada de exploración, el refugio ya está a la vista."

    if exploran_todos:
        show marina sonriendo at left
        with Dissolve(.5)
        m "¡Vamos! Ingrid necesita comer y beber algo."
        hide marina
        with Dissolve(.5)
        "Los cuatro entran al refugio."

    elif exploran_tres:
        if laura_se_queda or bob_se_queda:
            show marina sonriendo at left
            with Dissolve(.5)
            m "¡Vamos! Ingrid necesita comer y beber algo."
            hide marina
            with Dissolve(.5)
        elif marina_se_queda:
            show laura sonriendo at right
            with Dissolve(.5)
            l "¡Vamos! Ingrid necesita comer y beber algo."
            hide laura
            with Dissolve(.5)
        "Los tres entran al refugio."

    else:
        if va_con_bob:
            "Se encuentran con Laura y Marina poco antes de llegar."
            show bob saludando sucio at center
            with Dissolve(.5)
            show marina hablando at left
            with Dissolve(.5)
            show laura seria at right
            with Dissolve(.5)
            b "¡Marina, Laura! Me alegra verlas de nuevo."
            show laura hablando at right
            with Dissolve(.5)
            l "Lo mismo digo, Bob."
            show laura seria at right
            with Dissolve(.5)
            m "¿Pudieron encontrar algo?"
            b "¡Por suerte si!"

            if reporte_comparte_bote:
                b "Revisamos el bote que [nombre_personaje] había rescatado de la playa."
                b "Servirá para pescar, pero no para irnos de la isla."
                y "Tendremos que construir unas cañas de pescar, así como unos remos."
                b "Y ustedes, ¿encontraron algo?"
                show bob parado serio at center
                with Dissolve(.5)
                m "¡Trajimos agua!"
                show marina sonriendo at left
                with Dissolve(.5)
                l "Y además, encontramos algunos frutos cuando volvíamos."
                show laura sonriendo at right
                with Dissolve(.5)
                $ comida += 5
                m "Y algo más..."
                show marina preocupada at left
                with Dissolve(.5)
                l "Encontramos grandes huellas de pezuñas."
                show laura hablando at right
                with Dissolve(.5)
                m "Laura dice que puede ser un jabalí."
                show marina triste at left
                with Dissolve(.5)
                l "También había marcas de colmillos en la corteza de un árbol."
                show laura seria at right
                with Dissolve(.5)
                b "Tranquila, Marina. Estaremos preparados."
                y "Llegado el caso, lo atraparemos. Suena mucho mas apetecible que unos frutos..."
                m "Entremos, Ingrid necesita beber y comer algo."
                "Los cuatro entran al refugio."

            elif reporte_comparte_caja:
                b "Revisamos la caja que [nombre_personaje] había rescatado de la playa."
                b "Tenía unas cuantas cosas útiles."
                "Le muestras las distintas herramientas a Laura y Marina."
                y "Y ustedes, ¿encontraron algo?"
                show bob parado serio at center
                with Dissolve(.5)
                m "¡Trajimos agua!"
                show marina sonriendo at left
                with Dissolve(.5)
                l "Y además, encontramos algunos frutos cuando volvíamos."
                show laura sonriendo at right
                with Dissolve(.5)
                $ comida += 5
                m "Y algo más..."
                show marina preocupada at left
                with Dissolve(.5)
                l "Encontramos grandes huellas de pezuñas."
                show laura hablando at right
                with Dissolve(.5)
                m "Laura dice que puede ser un jabalí."
                show marina triste at left
                with Dissolve(.5)
                l "También había marcas de colmillos en la corteza de un árbol."
                show laura seria at right
                with Dissolve(.5)
                b "Tranquila, Marina. Estaremos preparados."
                y "Llegado el caso, lo atraparemos. Suena mucho mas apetecible que unos frutos..."
                m "Entremos, Ingrid necesita beber y comer algo."
                "Los cuatro entran al refugio."

        elif va_con_marina:
            "Se encuentran con Laura y Bob poco antes de llegar."
            show bob saludando sucio at center
            with Dissolve(.5)
            show marina hablando at left
            with Dissolve(.5)
            show laura hablando at right
            with Dissolve(.5)
            b "¡Marina, [nombre_personaje]! Me alegra verles de nuevo."
            m "Lo mismo digo, Bob."
            l "¿Pudieron encontrar algo?"
            y "¡Por suerte si!"

            if reporte_encontrar_agua_comida or encontraron_agua:
                m "Trajimos agua. ¿Y ustedes?"
                b "Nosotros encontramos algunos frutos cuando volvíamos."
                $ comida += 5
                l "Y algo más..."
                show bob parado serio at center
                with Dissolve(.5)
                b "Encontramos grandes huellas de pezuñas."
                l "Bob dice que puede ser un jabalí."
                show laura seria at right
                with Dissolve(.5)
                b "También había marcas de colmillos en la corteza de un árbol."
                show bob parado hablando at center
                with Dissolve(.5)
                m "¡Qué miedo!"
                show marina triste at left
                with Dissolve(.5)
                b "Tranquila, Marina. Estaremos preparados."
                show bob parado serio at center
                with Dissolve(.5)
                y "Llegado el caso, lo atraparemos. Suena mucho mas apetecible que unos frutos..."
                m "Entremos, Ingrid necesita beber y comer algo."
                "Los cuatro entran al refugio."

            else:
                m "Trajimos agua y unos cuantos frutos. ¿Y ustedes?"
                show bob parado serio at center
                with Dissolve(.5)
                b "Nosotros solamente encontramos grandes huellas de pezuñas."
                show laura seria at right
                with Dissolve(.5)
                l "Bob dice que puede ser un jabalí."
                b "También había marcas de colmillos en la corteza de un árbol."
                show marina triste at left
                with Dissolve(.5)
                m "¡Qué miedo!"
                b "Tranquila, Marina. Estaremos preparados."
                y "Llegado el caso, lo atraparemos. Suena mucho mas apetecible que unos frutos..."
                m "Entremos, Ingrid necesita beber y comer algo."
                "Los cuatro entran al refugio."

        elif va_con_laura:
            "Se encuentran con Marina y Bob poco antes de llegar."
            show bob saludando sucio at center
            with Dissolve(.5)
            show marina hablando at left
            with Dissolve(.5)
            show laura hablando at right
            with Dissolve(.5)
            b "¡Laura, [nombre_personaje]! Me alegra verles de nuevo."
            l "Lo mismo digo, Bob."
            m "¿Pudieron encontrar algo?"
            y "¡Por suerte si!"

            if reporte_encontrar_agua_comida or encontraron_agua:
                l "Trajimos agua. ¿Y ustedes?"
                b "Nosotros encontramos algunos frutos cuando volvíamos."
                $ comida += 5
                show marina preocupada at left
                with Dissolve(.5)
                m "Y algo más..."
                show bob parado serio at center
                with Dissolve(.5)
                b "Encontramos grandes huellas de pezuñas."
                m "Bob dice que puede ser un jabalí."
                b "También había marcas de colmillos en la corteza de un árbol."
                show marina triste at left
                with Dissolve(.5)
                m "¡Me da mucho miedo!"
                b "Tranquila, Marina. Estaremos preparados."
                show bob parado hablando at center
                with Dissolve(.5)
                y "Llegado el caso, lo atraparemos. Suena mucho mas apetecible que unos frutos..."
                l "Entremos, Ingrid necesita beber y comer algo."
                "Los cuatro entran al refugio."

            else:
                l "Trajimos agua y unos cuantos frutos. ¿Y ustedes?"
                show bob parado hablando at center
                with Dissolve(.5)
                b "Nosotros solamente encontramos grandes huellas de pezuñas."
                show marina preocupada at left
                with Dissolve(.5)
                m "Bob dice que puede ser un jabalí."
                b "También había marcas de colmillos en la corteza de un árbol."
                show bob parado serio at center
                with Dissolve(.5)
                m "¡Me da mucho miedo!"
                show marina triste at left
                with Dissolve(.5)
                b "Tranquila, Marina. Estaremos preparados."   
                y "Llegado el caso, lo atraparemos. Suena mucho mas apetecible que unos frutos..."
                l "Entremos, Ingrid necesita beber y comer algo."
                "Los cuatro entran al refugio."
    hide bob
    hide laura
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    if refugio == "cueva":
        scene bg inside cave
    elif refugio == "cabaña":
        scene bg inside cabin
    elif refugio == "claro":
        scene bg inside shelter

    "Dentro del refugio, Ingrid parece estar algo incómoda, pero está despierta."
    if bob_se_queda:
        show bob parado serio at right
        with Dissolve(.5)
        "Bob se encuentra a su lado, y los saluda con la cabeza al verles entrar."
    elif laura_se_queda:
        show laura sonriendo at right
        with Dissolve(.5)
        "Laura se encuentra a su lado, y sonríe cuando los ve."
    elif marina_se_queda:
        show marina sonriendo at right
        with Dissolve(.5)
        "Marina se encuentra a su lado, y deja escapar un pequeño grito de júbilo cuando se da cuenta de que volvieron."
    "Ingrid sigue recostada, y apenas le alcanza la voz para saludarlos."
    "Entre todos reparten el agua y la comida."
    "Afuera, en la jungla, el sol comienza a ponerse y los ruidos de la noche reemplazan a los del día."

    jump chapter_5_end

label chapter_5_end:
        # Generar contenido para los pop-ups de relaciones
        $ relaciones_contenido = generar_lista_popup("RELACIONES", ["marina", "bob", "laura", "ingrid"], es_relacion=True)
        $ relaciones_cap5_bob = bob
        $ relaciones_cap5_marina = marina
        $ relaciones_cap5_laura = laura
        $ relaciones_cap5_ingrid = ingrid
                    
        # Calcular el total de decisiones y obtener la lista de variables específicas para el capítulo
        # $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        # $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        # show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 5, el primero del segundo segmento. El grupo ha logrado resolver muchos problemas pero aun queda mucho por hacer. La supervivencia dependerá de las desiciones que tomen."
                    
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        # hide screen decisiones_popup with dissolve
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
    $ persistent.cantidad_capitulos +=1
    jump cap6_inicio

label cap6_inicio:
    # Ambiente: final del día, tono inquietante
    # Ingrid comienza a desvariar por fiebre. Puede haber diálogo reflexivo antes del brote
    # El jugador puede elegir cómo reaccionar (preocuparse, minimizar, delegar)
    # Ingrid, antes de caer inconsciente, describe algunas plantas útiles → se activa la misión

    $ capitulo_actual = 6
    scene bg jungle night stars at truecenter
    with fade

    show screen combined_ui

    "La noche cae lenta sobre la isla. El calor no cede, y la humedad parece espesa como el silencio que envuelve al refugio."

    show ingrid gr seria at leftgr
    with Dissolve (0.5)

    i "No me siento... {w=0.5} nada bien... Mi cabeza arde... y la vista se me nubla..."
    
    "{i}Ingrid tambalea y apoya una mano en la pared de bambú improvisada. El grupo la rodea, su frente brilla con sudor frío.{/i}"

    y "Con permiso, Ingrid."

    "{i}Apoyas tu mano sobre su frente y sientes que está muy caliente.{/i}"

    y "¡Estás ardiendo en fiebre, Ingrid!"

    i "En la jungla... hay plantas... que podrían ayudar."
    i "Busquen {i}cúrcuma{/i} y {i}equinácea{/i}... Tienen propiedades antibióticas si se hierven..."

    "{i}Ingrid intenta seguir explicando, pero su voz se apaga en un suspiro antes de desplomarse lentamente.{/i}"

    hide ingrid
    with Dissolve (1.5)

    $ reporte_fiebre_ingrid = True
    $ ingrid -= 1  # tensión emocional

    "El grupo reacciona de inmediato. Bob le toma el pulso, Laura se tapa la boca angustiada, Marina busca trapos húmedos."
    
    "Afuera la jungla está muy oscura."

    $ choice_position = "alta"

    menu:
        "Me acerco y la recuesto con cuidado, tratando de calmar a los demás.":
            $ reporte_ayuda_ingrid = True
            $ ingrid += 1
            $ liderazgo += 1

            y "Marina, dame eso, por favor."

            "{i}Marina te pasa un trapo humedecido.{/i}"

            y "Esto debería ayudar a que baje la fiebre."
            
            y "No se preocupen. Por ahora está estable."

        "Me mantengo cerca, pero dejo que otros la asistan. No soy médic[e].":
            $ reporte_observa_ingrid = True

            "{i}Decides no intervenir directamente, pero prestás atención y te aseguras de no estorbar.{/i}"

        "Me alejo un poco. No quiero estar cerca si esto se complica.":
            $ reporte_aleja_ingrid = True
            $ ingrid -= 1
            $ bob -= 1
            $ marina -= 1
            $ laura -= 1

            "{i}Los demás te miran y en seguida notas la decepción en sus ojos.{/i}"

            "{i}Aunque nadie te dice nada, sientes la presión.{/i}"

    pause 0.5

    # Avanza a discusión sobre las plantas medicinales
    jump cap6_1_formacion_grupos

label cap6_1_formacion_grupos:
        # Todos discuten si salir ahora o esperar
    # Se genera un conflicto de posiciones: elección del jugador + reacción del grupo
    # Se define grupo de salida y grupo que se queda
    # Si el jugador propone algo, un personaje se le opone (Laura y Bob pueden ser útiles para polarizar)

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)

    "{i}El aire se llena de tensión. Ingrid yace inmóvil y su respiración agitada es lo único que interrumpe el murmullo de la jungla.{/i}"
    
    "{i}La oscuridad de la noche es espesa afuera.{/i}"

    show bob parado serio at right
    with Dissolve(0.5)

    b "Si hay algo que pueda ayudarla, tenemos que encontrarlo esta noche."

    b "Si esperamos al amanecer, podría ser tarde."

    show laura seria at left
    with Dissolve(0.5)

    l "¿Salir a esta hora? ¿Con esta oscuridad?"
    
    l "Es una locura. Nos vamos a perder, o algo peor."

    show marina preocupada at center
    with Dissolve(0.5)

    m "Me da mucho miedo, pero si alguien más va a buscar las plantas, yo también voy."

    l "No tenemos linternas y el terreno es peligroso incluso de día..."

    "{i}Los ojos de todos recaen sobre ti. Eres un[e] más del grupo, pero también alguien que empieza a tener influencia en el.{/i}"

    $ choice_position = "alta"
    y "Lo que sea que decidamos, debe ser ya."

    menu:
        "Ingrid necesita esas plantas. No me voy a quedar de brazos cruzados.":
            $ reporte_decide_buscar_de_noche = True
            $ liderazgo +=1
            $ marina += 1
            $ laura -= 1
            $ bob += 1
            y "Yo voy, Marina. No podemos perder más tiempo."
            y "Si alguien quiere venir, bien. Si no, iré igual."
            "{i}Luego de un breve silencio, Bob asiente y se comienza a preparar para la búsqueda.{/i}"
            "{i}Marina contiene un suspiro tenso y hace lo mismo.{/i}"
            hide bob
            with Dissolve (0.5)
            hide marina
            with Dissolve (0.5)
            l "Es una mala idea, me sorprende que no vean el riesgo."
            l "Yo me quedo con Ingrid."
            hide laura
            with Dissolve (0.5)
            jump cap6_3_buscadores

        "Deberiamos esperar todos. No servirá de nada perderse. Es mejor salir al amanecer.":
            $ reporte_no_buscar_de_noche = True
            $ laura += 1
            $ bob -= 1 
            y "Piénsenlo. Si algo le pasara a alguno de nosotros allá afuera, ¿qué hacemos?"
            y "No estamos como para, además de una persona enferma, tener que cuidar de un herido."
            "{i}Bob frunce el ceño y Laura abre las manos, agradeciendo que alguien le de la razón.{/i}"
            "{i}Marina simplemente asiente, en silencio.{/i}" 
            jump cap6_3_refugio

        "Yo prefiero esperar. Que cada uno haga lo que le parezca.":
            $ reporte_buscar_quien_quiera = True
            $ laura += 1
            $ bob -= 1
            y "Creo que es muy peligroso, yo no voy a ir."
            y "Si deciden arriesgarse, es responsabilidad de ustedes."
            "{i}Bob frunce el ceño y Laura abre las manos, agradeciendo que alguien le de la razón.{/i}"
            "{i}Marina simplemente asiente, en silencio.{/i}"        
            jump cap6_NPCs_buscan

label cap6_NPCs_buscan:
    b "Ingrid necesita ayuda. Voy a intentar encontrar esas plantas."
    hide bob
    with Dissolve (0.5)
    m "Yo también voy, ojalá las encontremos y nos veamos pronto."
    hide marina
    with Dissolve (0.5)
    l "Es una mala idea, me sorprende que no vean el riesgo."
    jump cap6_3_refugio

label cap6_3_refugio:

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)

    if reporte_no_buscar_de_noche:
        "{i}El grupo intenta confortar a Ingrid, pero la tensión en el aire hace que los minutos parezcan horas.{/i}"
        show marina preocupada at left
        with Dissolve(0.5)
        m "No me lo puedo sacar de la cabeza... ¿y si esta espera le cuesta la vida?"
        show laura seria at right
        with Dissolve(0.5)
        l "No podíamos salir a ciegas. Lo lógico era cuidarla acá. La decisión está tomada."
        "{i}Te sientas cerca del fuego improvisado.{/i}"
        "{i}Las sombras parpadean sobre los rostros agotados y afuera la oscuridad es total.{/i}"
        "{i}A tu lado, Marina mira al suelo sin hablar.{/i}"
    else:
        "{i}Laura y tú intentan confortar a Ingrid. Los minutos parezcan horas{/i}"
        "{i}Te sientas cerca del fuego improvisado.{/i}"
        "{i}Las sombras parpadean sobre sus rostros agotados.{/i}"
        "{i}Los quejidos de Ingrid son lo único que rompe la tensión del silencio.{/i}"

    $ choice_position = "alta"

    menu:
        "Me acerco a Ingrid y le humedezco la frente con el paño húmedo.":
            $ reporte_cuidado_pasivo = True
            $ ingrid += 1
            "{i}La fiebre no baja, pero el paño fresco parece darle algo de alivio.{/i}"

        "Intento mantener al grupo tranquilo. Hablo con Marina y Laura." if reporte_no_buscar_de_noche:
            $ reporte_contenido_emocional = True
            $ marina += 1
            $ laura += 1
            y "Estamos haciendo lo mejor que podemos. Si salimos sin saber ni donde pisamos, podría haber más de un herido."

        "Me mantengo al margen. Esta tensión me supera.":
            $ reporte_aislado_refugio = True
            if reporte_no_buscar_de_noche:
                $ marina -= 1
            "{i}Observás el fuego en silencio. No puede sacarte los ruidos de la selva de la cabeza.{/i}"
                    
        "Mejor hacer pasar el tiempo hablando con Laura."if reporte_buscar_quien_quiera:
            $ reporte_aislado_refugio = True
            $ laura += 1
            "{i}Conversan en voz baja, durante un largo rato, contándose cómo eran sus vidas antes del naufragio.{/i}"

    # Oportunidad de cambiar de opinión
    jump cap6_3_refugio_opcion_salida

label cap6_3_refugio_opcion_salida:

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)

    "{i}Las ramas crujen con el viento. Los sonidos nocturnos parecen más fuertes a medida que la ansiedad se acumula.{/i}"

    $ choice_position = "alta"

    menu:
        "Debo salir a buscar las plantas. Ingrid no mejora, no puede esperar hasta el amanecer.":
            $ reporte_salio_en_solitario = True
            "{i}Agarras una rama larga y te deslizas entre los árboles sin hacer ruido.{/i}"
            jump cap6_3_salida_en_solitario

        "Mejor seguir esperando. Es demasiado arriesgado salir. Debo sostener la decisión que tomé.":
            $ reporte_sostiene_decision = True
            "{i}Cerrás los puños. Comienzas a dudar que haya sido una buena idea quedarse, pero dar marcha atrás tampoco es una opción.{/i}"
            show bob bob parado serio at right
            with Dissolve (0.5)
            b "Ingrid está cada vez peor, voy a buscar esas plantas ahora mismo."
            hide bob 
            with Dissolve (0.5)
            show marina preocupada at left
            with Dissolve(0.5)
            m "¡Espera Bob! Yo tambien voy."
            hide marina 
            with Dissolve (0.5)
            "{i}Laura se encoje de hombros.{/i}"
            pause .5
            "{i}Conversan en voz baja, durante un largo rato, contándose cómo eran sus vidas antes del naufragio.{/i}"
            jump cap6_4_reunion

label cap6_3_salida_en_solitario:
    hide marina
    hide bob
    hide ingrid
    hide laura

    "{i}Avanzas un buen rato entre los arboles en una oscuridad casi completa, buscando las plantas.{/i}"
    pause .5
    scene bg jungle night explore2 at truecenter
    "{i}Das un paso en falso, y caes rodando cuesta abajo entre hojas mojadas y barro.{/i}"
    
    $ reporte_caida_terraplen = True

    y "¡Ahhh...!"

    scene bg jungle night search at truecenter
    with Dissolve(0.5)

    $ choice_position = "default"
    menu:
        "cansancio:[cansancio] Hacer un gran esfuerzo fisico para intentar agarrarte de algo" if cansancio >= 2:
            "{i}Logras frenar la caída aferrándote a una raíz. El golpe en seco deja una punzada aguda en tu brazo.{/i}"           
            $ update_stat("sed", sed - 1)
            $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
            $ choice_position = "alta"
            menu:
                "Ignorar el golpe. Ingrid me necesita.":
                    $ reporte_ignora_herida = True
                    "{i}Cambias de mano el bastón improvisado, apoyando el peso en el otro brazo.{/i}"
                    "{i}Te incorporas como puedes para continuar la búsqueda.{/i}"
                "Examinar el brazo. Podría ser serio.":
                    $ reporte_verifica_herida = True
                    "{i}Parece ser solo una raspadura, improvisas un vendaje que sirva hasta que puedas lavar la herida.{/i}"
        
        "cansancio:[cansancio] Intentar agarrarte de algo pese al cansancio" if cansancio == 1:
            "{i}Estás tan agotad[e] que al intentar agarrarte de una roca te golpeas en las costillas.{/i}" 
            "{i}Ruedas por la pendiente, rebotando en algunos montones de hojas y ramas.{/i}"
            scene bg jungle night fall at truecenter
            with Dissolve(0.5)
            $ reporte_caida_rodar = True
            "{i}Te levantas en medio de la oscuridad. Las costillas te duelen mucho pero no parece ser grave.{/i}"
            "{i}Ladera arriba se escuchan algunas voces. Parece que Bob y Marina están cerca.{/i}"
            y "¡Aquí! ¡Aquí!"

        "Dejarte rodar, tratando de protegerte todo lo posible.":
            "{i}Ruedas por la pendiente, rebotando en algunos montones de hojas y ramas.{/i}"
            scene bg jungle night fall at truecenter
            with Dissolve(0.5)
            $ reporte_caida_rodar = True
            "{i}Te levantas en medio de la oscuridad.{/i}"
            "{i}Ladera arriba se escuchan algunas voces. Parece que Bob y Marina están cerca.{/i}"
            y "¡Aquí! ¡Aquí!"
    pause .5
    "{i} A lo lejos se sienten unos gruñidos. Escuchas a Bob gritando una advertencia entre ruidos de ramas rotas.{/i}"
    "{i}Comienzas a rodear la ladera ya que subir por donde caíste es imposible.{/i}"  
    jump cap6_volver_solo


label cap6_3_buscadores:
        # Eventos secuenciales con obstáculos:
    # - Tropezón / caída
    # - Espinas / rasguños (afecta 'cansancio' o variable reporte_herida)
    # - Ruido del jabalí (detonante de separación)
    # Un personaje se pierde
    # Fin: regreso parcial al refugio

    scene bg jungle night explore1 at truecenter
    with Dissolve(0.5)

    "{i}El aire húmedo de la selva nocturna se siente pesado.{/i}"
    "{i}Cada paso entre ramas crujientes parece capaz de despertar algo más que los grillos.{/i}"

    show marina hablando at left
    with Dissolve(0.5)

    m "Mantengan los ojos bien abiertos."

    show bob parado serio at right
    with Dissolve(0.5)

    b "Si, busquemos con cuidado, y no nos separem..."
    scene bg jungle night explore2 at truecenter
    with Dissolve(0.5)

    "{i}Das un paso en falso, y caes rodando cuesta abajo entre hojas mojadas y barro.{/i}"
    hide marina
    hide bob

    $ reporte_caida_terraplen = True

    y "¡Ahhh...!"

    scene bg jungle night search at truecenter
    with Dissolve(0.5)

    $ choice_position = "default"
    menu:
        "Hacer un gran esfuerzo fisico para intentar agarrarte de algo." if cansancio >= 2:
            "{i}Lográs frenar la caída aferrándote a una raíz. El golpe en seco deja una punzada aguda en tu brazo.{/i}" 
            $ update_stat("cansancio", cansancio - 1)
            $ show_variable_changed_popup("El cansancio ha aumentado", rojo)

            show bob parado serio at left
            with Dissolve(0.5)
            b "Ey, [nombre_personaje], ¿estás bien?"
            $ choice_position = "alta"

            menu:
                "Ignorar el golpe, Ingrid me necesita.":
                    $ reporte_ignora_herida = True
                    "{i}Apoyás el peso en el otro brazo. Te incorporas como puedes para continuar la búsqueda.{/i}"
                    y "Si, si, no es nada."
                "Examinar el brazo. Podría ser serio.":
                    $ reporte_verifica_herida = True
                    y "No sé, me duele el brazo."
                    b "Déjame ver..."
                    b "Parece solo una raspadura. Hagámosle un vendaje, pero debes lavarlo cuanto antes.{/i}"
            pause .5
            y "Gracias, Bob. Sigamos con la búsqueda."
            show marina preocupada at right
            with Dissolve(0.5)
            m "¡Qué susto me diste, [nombre_personaje]!"
            y "No ha sido nada, Marina. Sigamos buscando."
            jump cep6_jabali_grupo
        
        "cansancio:[cansancio] Intentar agarrarte de algo pese al cansancio" if cansancio == 1:
            "{i}Estás tan agotad[e] que al intentar agarrarte de una roca te golpeas en las costillas.{/i}" 
            "{i}Ruedas por la pendiente, rebotando en algunos montones de hojas y ramas.{/i}"
            scene bg jungle night fall at truecenter
            with Dissolve(0.5)
            "{i}Te levantas en medio de la oscuridad, apenas se ve nada. A lo lejos se siente una voz que grita tu nombre{/i}"
            y "¡Aqui! ¡Aquí!"
            "{i}Ladera arriba se sienten unos gruñidos. Escuchas a Bob gritando una advertencia a lo lejos.{/i}"
            "{i}Algo está pasando donde quedaron los demás.{/i}"
            $ reporte_caida_rodar = True
            jump cap6_volver_solo 

        "Dejarte rodar, tratando de protegerte todo lo posible.":
            "{i}Ruedas por la pendiente, rebotando en algunos montones de hojas y ramas.{/i}"
            scene bg jungle night fall at truecenter
            with Dissolve(0.5)
            "{i}Te levantas en medio de la oscuridad, apenas se ve nada. A lo lejos se siente una voz que grita tu nombre{/i}"
            y "¡Aqui! ¡Aquí!"
            "{i}Ladera arriba se sienten unos gruñidos. Escuchas a Bob gritando una advertencia a lo lejos.{/i}"
            "{i}Algo está pasando donde quedaron los demás.{/i}"
            $ reporte_caida_rodar = True
            jump cap6_volver_solo    

label cep6_jabali_grupo:
    scene bg jungle night crisis at truecenter
    with Dissolve(0.5)

    "{i}Avanzan un poco más, pero algo cruje entre los árboles. Un gruñido ronco corta el silencio de la noche.{/i}"

    show marina gr hablando at leftgr
    with Dissolve(0.5)

    m "¿¡Escucharon!? Eso no fue un grillo..."

    $ reporte_oyen_jabali = True

    show bob gr parado hablando at rightgr
    with Dissolve(0.5)

    b "¡No se muevan! ¡Manténganse junt..."

    "{i}El crujido de las plantas junto a ti te hace saltar, sorprendido.{/i}"
    "{i}Marina sale corriendo, asustada. Sales detrás de ella pero cuando te das cuenta, no sabes donde está ella, ni tampoco Bob."
    hide marina
    hide bob
    with Dissolve(0.5)

    "{i}En la oscuridad se oyen ramas quebrarse. No sabes si son tus compañeros corriendo entre los arboles, o algo más, acechando furtivamente.{/i}"

    "{i}Un gruñido furioso llega desde atrás y saltas a un costado.{/i}"

    hide marina
    hide bob
    with Dissolve(0.5)

    jump cap6_volver_solo

label cap6_volver_solo:
    "{i}Cuando recuperas la calma te das cuenta de que ya no escuchas a Bob, ni tampoco a Marina.{/i}"
    "{i}El silencio se ha apoderado nuevamente de la jungla.{/i}"

    $ reporte_grupo_separado = True

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)
    $ update_stat("sed", sed - 1)
    $ show_variable_changed_popup("La sed ha aumentado", rojo)
    "{i}Logras regresar al campamento, jadeando, con hojas pegadas al rostro y el brazo dolorido.{/i}"

    show laura gr hablando at leftgr
    with Dissolve(0.5)

    l "¿¡Dónde están los demás!?"

    y "Hubo un ruido, un gruñido fuerte. Intenté encontrar a los demás, pero la oscuridad..."

    $ reporte_regreso_sin_grupo = True

    jump cap6_4_reunion

label cap6_4_reunion:
    # El grupo se reúne. Falta alguien.
    # Se genera una discusión fuerte, con culpabilización
    # El jugador puede optar por calmar, culpar, o irse en silencio
    # Se actualizan relaciones
    scene bg jungle night stars at truecenter
    with Dissolve(0.5)
    show laura seria at left
    with Dissolve(0.5)
    "{i}Mientras hablas con Laura, Bob vuelve, pero está solo.{/i}"
    if reporte_regreso_sin_grupo:
        if reporte_oyen_jabali:
            show bob parado hablando at right
            with Dissolve(0.5)
            b "Que alivio haber podido regresar al refugio."
            show laura seria  at left
            with Dissolve(0.5)
            l "¿¡Y Marina!?"

            b "Escuchamos un ruido fuerte. Un gruñido. Todos corrimos..."

            show laura gr enojada at leftgr
            with Dissolve(0.5)

            l "¿Y no se les ocurrió volver por ella?"
            show bob parado serio at right
            with Dissolve(0.5)

            show laura gr seria at leftgr
            with Dissolve(0.5)

            "{i}El silencio se vuelve más denso. Las llamas del fuego proyectan sombras que parecen temblar junto a las palabras que nadie quiere decir.{/i}"

            $ choice_position = "alta"

            menu:
                "No se puede culpar a nadie. Esto era impredecible.":
                    $ reporte_intervencion_neutra = True
                    y "Nadie quiso que esto pasara. Había algo allí fuera. Nos sorprendió."

                "Cuando Marina corrió, fui tras ella, pero Bob no.":
                    $ reporte_reclamo_por_salida = True
                    $ bob -= 1
                    y "¿Dónde estabas cuando fui tras Marina, Bob?"
                    show bob gr parado enojado at rightgr
                    with Dissolve(0.5)
                    b "Fué todo muy caótico, de un momento a otro ya no los vi."

                "Me quedo callad[e].":
                    $ reporte_silencio_tensionado = True
                    "{i}Te mantienes en silencio. Por dentro, te sientes responsable.{/i}"
        else:
            show bob parado serio at right
            with Dissolve(0.5)

            b "Aquí estás, ¡[nombre_personaje]!"
            b "Te vimos caer y corrimos a ver qué te había pasado, pero la oscuridad no nos dejaba ver el final de la colina."
            b "Luego escuchamos un gruñido y algo moviéndose entre los arbustos."
            b "Le dije a Marina que corra, pero cuando estuve fuera de peligro, no puede encontrarla."
            
            show laura enojada at left
            with Dissolve(0.5)

            l "¿¡Y no se te ocurrió volver por ella?"

            "{i}El silencio se vuelve más denso. Las llamas del fuego proyectan sombras que parecen temblar junto a las palabras que nadie quiere decir{/i}"

            $ choice_position = "alta"

            menu:
                "No se puede culpar a nadie. Esto era impredecible.":
                    $ reporte_apoyo_bob_jabali = True
                    $ bob += 1
                    y "No es culpa de Bob. Allí fuera no se veía nada."

                "Realmente me sorprende de Bob.":
                    $ reporte_reclamo_por_salida = True
                    $ bob -= 1
                    y "La verdad que no esperaba algo así de ti Bob. Hubiera imaginado que la buscarías hasta encontrarla."
                    show bob gr parado enojado at rightgr
                    with Dissolve(0.5)
                    b "Fué todo muy caótico, les pido que comprendan. No veía ni dónde estaba parado."

                "Me quedo callad[e] solamente para no crear más problemas.":
                    $ reporte_silencio_tensionado = True
                    "{i}Mantienes el rostro serio. Por dentro, sientes que Bob es responsable de que Marina esté perdida.{/i}"
    else:
        show bob parado hablando at right
        with Dissolve(0.5)
        b "Que alivio haber podido regresar al refugio."
        show laura seria  at left
        with Dissolve(0.5)
        l "¿¡Y Marina!?"

        b "Escuchamos un ruido fuerte. Un gruñido. Algo moviéndose en los arbustos. Ambos corrimos..."

        show laura gr enojada at leftgr
        with Dissolve(0.5)

        l "¿Y no se te ocurrió volver por ella?"
        show bob parado serio at right
        with Dissolve(0.5)

        show laura gr seria at leftgr
        with Dissolve(0.5)

        "{i}El silencio se vuelve más denso. Las llamas del fuego proyectan sombras que parecen temblar junto a las palabras que nadie quiere decir.{/i}"

        $ choice_position = "alta"

        menu:
            "No se puede culpar a nadie. Esto era impredecible.":
                $ reporte_intervencion_neutra = True
                y "Nadie quiso que esto pasara, Laura."

            "Realmente me sorprende de Bob.":
                $ reporte_reclamo_por_salida = True
                $ bob -= 1
                y "La verdad que no esperaba algo así de ti Bob. Hubiera imaginado que la buscarías hasta encontrarla."
                show bob gr parado enojado at rightgr
                with Dissolve(0.5)
                b "Fué todo muy caótico, les pido que comprendan. No veía ni dónde estaba parado."

            "Me quedo callad[e] solamente para no crear más problemas.":
                $ reporte_silencio_tensionado = True
                "{i}Mantienes el rostro serio. Por dentro, sientes que Bob es responsable de que Marina esté perdida.{/i}"
                    
    show bob parado hablando at right
    with Dissolve(0.5)

    b "Tenemos que decidir. ¿Esperamos hasta el amanecer o salimos ahora a buscarla?"

    jump cap6_5_decision_final

label cap6_5_decision_final:
    # El jugador puede:
    # - Ir a buscar a la persona perdida con alguien más
    # - Esperar en el refugio (desencadena resultado pasivo)
    # Resultado variable según decisiones pasadas (confianza, relación, cansancio)

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)
    show bob parado serio at right
    with Dissolve(0.5)
    show laura seria at left
    with Dissolve(0.5)


    "{i}El grupo vuelve a rodear el fuego. Nadie habla por un momento.{/i}"
    "{i}Están agotados, pero aún no han encontrado las plantas para Ingird, y Marina puede estar herida, sola, en la selva.{/i}"

    show laura enojada at left
    with Dissolve(0.5)

    l "¡No aguanto más!"
    l "¿Van a ir a buscarla o esperan que mágicamente aparezca sana y salva?"

    show bob parado hablando at right
    with Dissolve(0.5)

    b "¿Van a...? O sea que tú no irías."
    show laura gr enojada at leftgr
    with Dissolve(0.5)
    l "¡De ninguna manera! Yo dije claramente que era un error ir a la selva de noche."
    $ choice_position = "alta"

    menu:
        "Debemos ir a buscarla. Aunque sea de noche, no podemos dejarla sola.":
            $ reporte_decide_buscar_marina = True
            $ bob += 1
            $ laura +=1
            y "Si ella estuviera aquí, insistiría en salir a buscarnos. No podemos fallarle ahora."
            "{i}Bob asiente. Se preparan con lo poco que tienen y se internan nuevamente en la selva.{/i}"
            jump cap6_rescate_en_la_noche

        "Mejor esperar hasta el amanecer. Ahora es peligroso y no ayudaría que más personas se pierdan.":
            $ reporte_decide_esperar_marina = True
            $ laura -= 1
            $ bob -= 1
            y "Si vamos ahora puede volver a pasar lo mismo. Esperemos a la primera luz."
            "{i}El grupo no parece muy satisfecho. Ninguno logra conciliar el sueño. La duda los carcome.{/i}"
            jump cap6_espera_al_amanecer

        "Yo voy a buscarla, no mas errores.":
            $ reporte_decide_esperar_marina = True
            $ laura += 1
            $ bob -= 1
            $ liderazgo +=1
            y "Yo voy, ustedes esperen aqui."
            b "Yo puedo ayudar a buscarla también."
            y "El momento para no dejarla atrás ya pasó, Bob. Ahora déjame a mi resolver el problema."
            "{i}Bob queda en silencio ante tus palabras mientras te internas en la noche.{/i}"
            jump cap6_3_salida_en_solitario_marina

label cap6_rescate_en_la_noche:

    scene bg jungle night explore3 at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}De nuevo en la espesura. Esta vez, los pasos son más pesados.{/i}"
    "{i}El miedo les invade, y cada sombra parece un animal agazapado.{/i}"

    show bob gr parado hablando at rightgr
    with Dissolve(0.5)

    b "Debería haber vuelto por ella antes."

    y "Bob, de nada sirve lamentarse ahora."
    y "Hagamos silencio, así podemos escuchar si nos llama, o si algo acecha."

    $ update_stat("hambre", hambre - 1)
    $ show_variable_changed_popup("El hambre ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    hide bob
    with Dissolve(0.5)
    "{i}Tras unos minutos de búsqueda en el claro donde se separaron, escuchás un leve quejido. Te asomas entre los arbustos y ahí está...{/i}"

    show marina gr triste at leftgr
    with Dissolve(0.5)

    m "¿Eres tu,[nombre_personaje]? ¿Bob?"
    m "Uff... ¡que alivio! Pensé que no vería otro amanecer."

    b "¡Marina! Por todos los cielos..."

    "{i}La ayudás a levantarse. Está cubierta de barro y hojas secas, con un rasguño en el brazo y la mirada perdida.{/i}"

    m "Me escondí cuando todo se descontroló. Después fue muy tarde para volver."
    m "¡Pero encontré las plantas!"

    $ reporte_rescate_exitoso = True
    $ marina += 2
    $ bob += 1
    $ update_stat("sed", sed - 1)
    $ show_variable_changed_popup("La sed ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui
    $ reporte_regreso_marina = True

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)

    "{i}Regresan juntos. El refugio se ilumina con las últimas brasas y el alivio contenido en los rostros que los reciben.{/i}"

    show laura hablando at center
    with Dissolve(0.5)

    l "¡Marina!"

    m "Estoy bien, gracias a [nombre_personaje] y Bob."

    $ laura += 1

    jump cap6_final

label cap6_espera_al_amanecer:

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}La noche se estira más de lo habitual.{/i}"
    "{i}Cada rama que cruje es una pregunta y nadie duerme. Cada uno lucha con sus pensamientos en silencio.{/i}"

    show laura seria at left
    with Dissolve(0.5)

    l "No soporto no saber. Pero salir en medio de esta oscuridad solo haría todo peor."

    show bob gr serio sucio at rightgr
    with Dissolve(0.5)

    b "Tal vez. O tal vez no hicimos lo suficiente."

    "{i}El fuego se consume hasta que solo quedan unas brasas.{/i}"
    "{i}La selva murmura con viento leve a medida que comienza a amanecer.{/i}"

    scene bg jungle clearing at truecenter
    with Dissolve(0.5)

    "{i}Poco después una figura aparece en la entrada del refugio.{/i}"
    "{i}Cojeando, con el rostro pálido y el brazo rasguñado, la silueta de Marina es recortada por los primeros rayos de luz.{/i}"

    show marina gr triste at center
    with Dissolve(0.5)

    m "Pensé... que no volvía."
    m "Me perdí... pero encontré un claro."
    m "Esperé hasta que hubo algo luz."

    show bob parado hablando at right
    show laura gr sorprendida at leftgr
    with Dissolve(0.5)

    b "Marina..."

    l "¿Estás bien? ¡Te dimos por perdida!"

    m "Estoy... agotada. Pero estoy bien..."
    m "Y encontré las plantas."

    "{i}La ayudás a sentarse. Le ofrecés agua.{/i}"
    "{i}Nadie habla más.{/i}"
    "{i}Solo se escucha el canto del las aves desde las copas de los árboles.{/i}"

    $ reporte_marina_vuelve_sola = True
    $ marina -= 1

    jump cap6_final

label cap6_3_salida_en_solitario_marina:

    scene bg jungle clearing at truecenter
    with Dissolve(0.5)

    "{i}La oscuridad no es completa, pero sí suficiente para perderte si das un paso en falso.{/i}"

    $ update_stat("sed", sed - 1)
    $ show_variable_changed_popup("La sed ha aumentado", rojo)

    "{i}Después de unos minutos de buscar con cuidado, una silueta encorvada aparece junto a un tronco caído.{/i}"
    "{i}Se mueve lentamente, como si ya no tuviera energías.{/i}"

    show marina gr triste at leftgr
    with Dissolve(0.5)

    m "Ay... [nombre_personaje]."
    m "Pensé que... que nadie vendría."

    y "¿Estás herida? Te estuvimos esperando. ¿Qué pasó?"

    m "Escuché algo. Me asusté. Corrí. Me tropecé con una raíz... no pude gritar."
    m "Luego me escondí... y fue allí que encontré las plantas."

    "{i}La ayudás a ponerse de pie. Está temblorosa pero parece estar bien. Tomas su brazo con firmeza y comienzan el regreso.{/i}"

    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)

    $ reporte_encuentra_marina = True
    $ marina += 1
    

    jump cap6_final

label cap6_final:
    # Si hubo misión de rescate, se encuentran las plantas y al personaje
    # Si se esperó: la persona llega al amanecer extenuada
    # Se curan heridas de Ingrid con las plantas
    # Se muestran consecuencias → se cierra el capítulo
    hide marina
    if refugio == "cueva":
        scene bg jungle cave at truecenter
    elif refugio == "cabana":
        scene bg jungle hut at truecenter
    elif refugio == "claro":
        scene bg jungle clearing at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Reavivan el fuego para preparar una infusión con las plantas recolectadas.{/i}"
    "{i}Una olla improvisada burbujea sobre las llamas mientras Marina descansa.{/i}"

    show laura hablando at left
    show bob parado serio at right
    with Dissolve(0.5)
    $ ingrid += 1
    l "¿Esto funcionará?"

    b "Si Ingrid tenía razón y la preparación está bien hecha, deberíamos ver una mejoría pronto."

    "{i}Aplican con cuidado el líquido tibio sobre la herida de Ingrid en silencio.{/i}"
    "{i}Solo se escucha el lento goteo del agua condensada entre las hojas y los quejidos soñolientos de Ingrid.{/i}"
    "{i}Esperan pacientemente hasta que, al rato, Ingid abre los ojos nuevamente.{/i}"

    show ingrid gr triste at center
    with Dissolve(0.5)

    i "Se siente..."
    "{i}Ingrid hace un gran esfuerzo para hablar.{/i}"
    i "Se siente menos caliente."
    show ingrid gr sonriente at center
    with Dissolve(0.5)

    "{i}Todos sueltan un suspiro de alivio.{/i}"
    "{i}Visible en el rostro de todos, esta victoria es pequeña, pero real.{/i}"
    "{i}Esta noche tumultuosa ha dado sus frutos: el grupo ganó tiempo, confianza, y unidad en la incertidumbre.{/i}"

    "{size=-10}Tus decisiones de esta noche no pasaron desapercibidas. Los tropiezos, el cansancio, las heridas... todo deja huella.{/size}"


    jump chapter_6_end  

    return

#################################################################################################################

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
        # $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        # $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        # show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 6, pese a todo el esfuerzo Ingrid se debate entre la vida y la muerte. La proxima mañana se verá si la fiebre remite. Es una noche tensa y de poco descanso."
                    
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        # hide screen decisiones_popup with dissolve
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                #jump final_cap6
                jump chapter_7_start
            "VOLVER A VER EL RESÚMEN":
                jump chapter_6_end

label final_cap6:
    if renpy.android:
        jump chapter_7_start
    else:
        call pedir_codigo_capitulo from _call_pedir_codigo_capitulo_2

#################################################################################################  ########  #####  ####  ######################################
##################################################################################################  ######  ######  ####  ####################################################
## Aca comienza la PARTE 7 ########################################################################  ###  ########  ####  ####################################################
####################################################################################################     #########  ####  #####################################################

label chapter_7_start:
    # Inicializar el capítulo actual (empieza en 0 por lo que es un numero menor que el capitulo, ej cap 2 debe tener la variable en 1)
    $ capitulo_actual = 6
    $ persistent.cantidad_capitulos +=1
    hide bob
    hide marina
    hide Laura
    jump cap7_inicio

label cap7_inicio:

    $ update_stat("hambre", hambre + 1)
    show screen top_right_button(boton_imagen)

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
    #if refugio == "cueva":
    #    scene bg inside cave
    #elif refugio == "cabaña":
    #    scene bg inside cabin
    #elif refugio == "claro":
    #    scene bg inside shelter
    #with Dissolve(0.5)
    $ update_stat("cansancio", cansancio + 1)
    $ show_variable_changed_popup("El cansancio ha disminuido", verde)
    show screen combined_ui


    "{i}El amanecer se filtra entre hojas amplias y húmedas. Nadie dice nada al despertar y es claro que el descanso no fue suficiente para nadie.{/i}"
    jump cap7_sed

label cap7_sed:
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
                jump cap7_sed

            "{i}Mejor reservar el agua. Los demás también deben estar con sed.{/i}":
                y "Aquí aún queda agua, luego podremos ir a buscar más."

    $ renpy.hide_screen("character_top_right_button")
    $ renpy.with_statement(Dissolve(1.5))
    show ingrid seria at right
    with Dissolve(1.5)

    i "(débil) Me siento menos débil... creo que puedo moverme, aunque despacio."

    $ ingrid += 1

    show bob parado hablando at center
    with Dissolve(0.5)

    b "Necesitamos más herramientas, comida... cosas utiles. Hay que revisar los lugares que vimos como refugios."
    b "Ingrid no puede moverse mucho, así que uno de nosotros debería quedarse."

    show marina triste at left
    with Dissolve(0.5)

    if marina <= -1:
        m "Yo me puedo quedar... con suerte esta vez no se olvidan de nadie en medio de la selva."
    elif marina >= 2:
        m "Si puedo ayudar a Ingrid a levantarse del todo, cuenten conmigo."
    else:
        m "Podría quedarme con Ingrid, si quieren."
    
    i "(débil) Si Marina me ayuda, puedo seguir buscando más plantas útiles. Todavía me cuesta mantenerme en pie por mi cuenta."

    "{i}Está claro que el refugio actual no será suficiente. Hay lugares que podrían tener lo que falta.{/i}"

    python:
        opciones_exploracion = []
        opciones_texto = []

        if refugio != "cabana":
            opciones_exploracion.append("cabana")
            opciones_texto.append("Explorar la Cabaña")

        if refugio != "cueva":
            opciones_exploracion.append("cueva")
            opciones_texto.append("Explorar la Cueva")

        if refugio != "claro" and climb_hill:
            opciones_exploracion.append("claro")
            opciones_texto.append("Explorar el Claro")

    if len(opciones_exploracion) == 1:
        $ destino_exploracion_1 = opciones_exploracion[0]
        jump cap7_decidir_quien_va
    else:
        menu:
            "[opciones_texto[0]]":
                $ destino_exploracion_1 = opciones_exploracion[0]
                jump cap7_decidir_quien_va

            "[opciones_texto[1]]":
                $ destino_exploracion_1 = opciones_exploracion[1]
                jump cap7_decidir_quien_va
     
label cap7_decidir_quien_va:

    hide ingrid
    with Dissolve(0.5)

    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabana":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing
    with Dissolve(0.5)

    show bob parado hablando at center
    with Dissolve(0.5)

    b "Uno debería quedarse con Ingrid. El resto puede ir al lugar que elegimos. Recolectar. Revisar. Lo que aparezca, será útil."

    show laura seria at right
    with Dissolve(0.5)

    l "Yo también puedo quedarme. Aunque me gustaría ir, si hace falta."

    if marina <= -1:
        show marina enojada at left
        with Dissolve(0.5)
        m "Hagan lo que quieran. Ya estoy acostumbrada a no tener voz en las decisiones."
    elif marina >= 2:
        show marina hablando at left
        with Dissolve(0.5)
        m "Prefiero quedarme con Ingrid, si puedo ayudarla. Aun no estoy del todo repuesta."
    else:
        show marina triste at left
        with Dissolve(0.5)
        m "No me molesta quedarme o ir. Lo que sea más útil."

    $ choice_position = "default" # default alta superior
    menu:
        "Voy a ir a explorar con el grupo.":
            y "Yo estoy decidido a ir."
            $ jugador_va_explorar = True
            jump cap7_formar_grupo_exploracion

        "Prefiero quedarme con Ingrid y asistirla.":
            y "Tal vez esta vez sea mejor que sea yo el que se quede."
            b "Está bien, eres de los que más activo ha estado."
            l "¿Están seguros? ¿Marina, estarás bien viniendo con Bob y conmigo?"
            m "Si, estaré bien, supongo."
            "{i}Los tres se preparan para salir mientras vuleves con Ingrid.{/i}"
            $ jugador_va_explorar = False
            $ reporte_cuida_ingrid_cap7 = True
            jump cap7_refugio_con_ingrid

label cap7_formar_grupo_exploracion:

    "{i}El grupo comienza a organizarse para la exploración. Ingrid queda en el refugio, confiando en que traerán algo útil.{/i}"

    show bob parado serio at center
    show marina hablando at left
    show laura seria at right
    with Dissolve(0.5)

    b "Quien se queda entonces."

    m "Alguien tiene que decidir."

    "{i}Laura y Marina quieren ir pero estan dispuestas a quedarse. Bob no ha hecho mencion de querer quedarse en ningun momento.{/i}"

    $ choice_position = "alta" # default alta superior
    menu:
        "Tomar la iniciativa, Marina deberia quedarse.":
            $ liderazgo += 2
            $ marina -= 1
            y "Yo tomare la desicion."
            y "Marina, tu has pasado por una noche complicada. Te guste o no, esta exploracion también va a ser agotadora."

            m "Si quieres liderar, espero que sepas lo que haces."

        "Bob toma buenas decisiones.":
            $ bob += 2
            "{i}Miras a Bob indicandole que tome una desicion. Bob asiente con firmeza.{/i}"

            b "Marina, mejor que descanses y te recuperes. Vean si pueden encontrar plantas con Ingrid."

        "Laura se ofrecio, que se quede ella":
            $ laura -= 1
            y "Laura, si no te molesta quedarte, quizás sea lo mejor."

            l "Debería quedarse Marina, ella esta cansada de la noche y nos espera una larga caminata."
            $ liderazgo -= 1
            m "Si, no demoremos mas, yo me quedo."
            "{i}Marina se va con Ingrid pero no parece estar muy contenta.{/i}"
            hide marina
            with Dissolve (0.5)

    hide marina
    with Dissolve(0.5)

    "{i}El grupo está listo. La exploración comienza ahora.{/i}"

    jump explorar_primer_sitio

label cap7_refugio_con_ingrid:

    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabana":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing

    with Dissolve(0.5)

    show screen combined_ui

    "{i}Mientras los demás se preparan para salir, tu te quedas junto a Ingrid, acomodando unas hojas secas para que se recueste mejor.{/i}"

    show ingrid cintura at center
    with Dissolve(0.5)

    i "Gracias por quedarte... pero no deberías."

    y "¿Y por qué es eso?"

    i "Lo que necesitamos está allá afuera. Yo voy a estar bien. Iré buscando plantas por aqui cerca. Puedo arreglármelas."

    "{i}La mirás. Tiene ojeras, las manos temblorosas, pero hay determinación en su tono.{/i}"

    i "Es mejor que te sumes a la exploracion. Cuantos mas ojos haya en eso, mas posibilidades de encontrar algo util."

    $ choice_position = "alta" # default alta superior

    menu:
        "Aceptar ir después de todo":
            $ reporte_ingrid_te_convence = True
            $ ingrid += 2
            "Tienes razón. No quería dejarte sola."

            i "Y yo agradezco eso. Pero me alcanza con saber que vas a volver con algo bueno."

            jump cap7_union_con_grupo_explorador

        "Responder con firmeza pero afecto":
            $ ingrid += 1
            "Confío en que estarás bien, pero prometo volver rápido."

            i "Bueno, si lo prometes, se que puedo quedarme tranquila."

            "{i}Ingrid exhala con algo de ansiedad, pero asiente con confianza.{/i}"

            jump cap7_union_con_grupo_explorador

        "Me quedé por compromiso":
            $ confianza_ingrid -= 1
            "Me alegra que digas eso, en realidad queria ir pero..."

            i "No quiero ser una carga."

            "{i}La expresión de Ingrid es seria, pero no fría. Sabe que esta situación es difícil para todos.{/i}"

            jump cap7_union_con_grupo_explorador

label cap7_union_con_grupo_explorador:

    scene bg jungle path at truecenter
    with Dissolve(0.5)

    "{i}Te apresuras a tomar tus cosas, y sales en la dirección hacia la que partieron los demás.{/i}"
    "{i}Tras unos minutos, logras alcanzarlos.{/i}"
    
    show bob parado serio at center
    show laura seria at right
    show marina triste at left
    with Dissolve(0.5)

    b "[nombre_personaje]… ¿te arrepentiste?"

    y "Ingrid insistió. Dijo que era más útil yendo que quedándome."

    if marina <= -1:
        m "¿En serio? ¿Y si Ingrid empeora? Genial..."

        $ marina -= 1
    elif marina >= 2:
        m "Qué bueno que viniste. Eres un gran explorador."

        $ marina += 1

    else:
        m "Ok. Supongo que Ingrid tiene razón."

    if marina >= 1:
        m "De todas formas yo voy a volver con ella. Me preocupa cómo quedó. Ustedes sigan."

    else:
        m "Esto es una locura. Me vuelvo. Alguien tiene que estar con ella."

    $ reporte_marina_regresa = True

    hide marina with Dissolve(0.5)

    "{i}Marina se aleja sin mirar atrás. El grupo queda ahora compuesto por Bob, Laura y tú.{/i}"    
    pause .5
    "{i}En seguida se disponen a salir.{/i}" 
    jump explorar_primer_sitio

label explorar_primer_sitio:
    if destino_exploracion_1 == "cueva":

        scene bg jungle cave
        with Dissolve(0.5)
        "{i}Llegan a la entrada de la cueva. El aire es fresco y huele a humedad.{/i}"
        "{i}El interior está muy oscuro, así que se adentran con cautela.{/i}"
        l "Miren, ¡allí!"
        b "¡Son hongos!"
        scene bg cave fungi at truecenter
        with Dissolve(0.5)
        "{i}Bob y Laura comienzan a recolectar los hongos de las paredes y pisos de la cueva.{/i}"
        "{i}Laura olfatea uno. Bob la mira nervioso, intuyendo lo que está pensando.{/i}"
        l "Se parecen a los que solíamos recolectar con mi abuela, cuando era chica, para sus salsas."
        b "¿No será arriesgado comerlos? En la naturaleza hay muchas cosas que si bien son similares, varían dramáticamente en peligrosidad."
        menu:
            "Bob tiene razón. Mejor llevárselos a Ingrid antes de probarlos. Ella sabrá si son seguros.":
                $ desicion_intro += 1
                $ reporte_cautela_hongos = True
                y "¡Como las serpientes de coral y las culebras! Estoy con Bob. Llevémoselos a Ingrid, que parece saber de estas cosas."
            "Si Laura los reconoce, deben ser seguros. Que pruebe algunos y en el peor de los casos ya nos enteraremos si le caen mal.":
                $ desicion_intro += 1
                $ reporte_descuido_hongos = True
                y "No seas tan paranoico, Bob. Laura ya dijo que los ha comido antes."
        $ comida == 10
        y "Vamos, hay que aprovechar la luz para seguir explorando."

    elif destino_exploracion_1 == "cabana":

        scene bg jungle hut
        with Dissolve(0.5)
        "{i}La vieja cabaña se recorta entre los árboles como un esqueleto de madera.{/i}"
        "{i}Los escalones crujen mientras suben la escalera con cautela.{/i}"
        scene bg inside cabin
        with Dissolve(0.5)

        "{i}Atraviesan la puerta y comienzan a revolver entre restos de muebles viejos.{/i}"
        l "Uff... Aquí hay mucho polvo."
        b "Pero mira, ¡también hay cosas útiles!"
        "{i}Bob sostiene una piedra gris y una vara de metal en el aire.{/i}"
        y "¿Qué es eso, Bob?"
        l "Parece una piedra de afilar."
        b "Esto, mis queridos amigos, es una yesca y un pedernal."
        b "Con esto prender un fuego será mucho más fácil que frotando cañas secas o golpeando piedras."
        l "Qué suerte que vinimos, entonces."
        $ yesca = True
        "{i}No parece haber nada más en la cabaña que pueda serles útil, por lo que se disponen a seguir explorando.{/i}"
        
    elif destino_exploracion_1 == "claro":

        scene bg jungle clearing
        "{i}El claro está iluminado por la luz del sol y algunos árboles frutales llaman su atención.{/i}"
        "{i}Los frutos son muy duros y difícilmente sean comestibles, pero parecen atraer una enorme cantidad de pájaros.{/i}"
        l "Bob, [nombre_personaje], ayúdenme a trepar a la copa."
        "{i}Bob y tu entrecruzan los brazos para que Laura pueda subir.{/i}"
        l "¡Lo sabía! Hay un par de nidos con pequeños huevos."
        y "¡Excelente!"
        b "La proteína nos vendrá bien."
        l "Ayudenme a bajar y revisemos el resto de los árboles."
        "{i}Recolectan una docena de huevos de variados tamaños y se disponen a seguir explorando.{/i}"
        $ comida += 5
        
    jump cap7_antes_de_encuentro_nuevos

label cap7_antes_de_encuentro_nuevos:

    scene bg jungle trail at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    if climb_hill: # o sea, si se descubrió el claro en el capítulo 3
        "{i}El grupo avanza rumbo al único sitio descubierto anteriormente que les falta revisar.{/i}"
        "{i}Quizas allí puedan encontrar algo más.{/i}"
        python:
            opciones_exploracion2 = []            

            if refugio != "cabana" and destino_exploracion_1 != "cabana":
                opciones_exploracion2.append("cabana")

            if refugio != "cueva" and destino_exploracion_1 != "cueva":
                opciones_exploracion2.append("cueva")

            if refugio != "claro" and destino_exploracion_1 != "claro":
                opciones_exploracion2.append("claro")

        $ destino_exploracion_2 = opciones_exploracion2[0]

    elif search_west:
        "{i}Cuando estaban buscando el primer refugio, recorriste la parte oeste de la isla y fuiste a la playa, pero no subiste a la colina.{/i}"
        "{i}Quizá desde allí puedan ver qué otros lugares quedan por explorar.{/i}"
        $ destino_exploracion_2 = "claro"
    else:
        "{i}Cuando estaban en el claro, buscando refugio, nadie decidió explorar hacia el oeste.{/i}"
        "{i}Quizá en esa dirección haya algo interesante.{/i}"
        $ destino_exploracion_2 = "claro"

    if destino_exploracion_2 == "cueva":
        scene bg jungle cave
    elif destino_exploracion_2 == "cabana":
        scene bg jungle hut
    elif destino_exploracion_2 == "claro":
        scene bg jungle clearing

    show laura seria at left
    with Dissolve(0.5)

    l "Miren... eso..."

    show bob gr parado hablando at rightgr
    with Dissolve(0.5)

    b "Esto es... ¿un campamento habitado?"

    "{i}Bob se agacha y toca la tierra en un área despejada. Está nivelada. Ordenada. No es natural.{/i}"
    "{i}Más allá, hay señales claras: una lona improvisada, restos organizados de madera.{/i}"

    show laura gr hablando at leftgr
    with Dissolve(0.5)

    l "¡Entonces debe haber mas supervivientes!"

    $ choice_position = "alta" # default alta superior
    menu:
        "Me acerco con precaución. Puede haber alguien en problemas.":
            $ reporte_investiga_nuevo_grupo = True
            y "Si hay más sobrevivientes, tenemos que ayudarlos."
            $ liderazgo += 1

        "Me quedo observando. Prefiero evaluar la situación antes de actuar.":
            $ reporte_cautela_nuevo_grupo = True
            y "Alguien estuvo trabajando para armar esto, pero eso no significa que nos vayan a recibir de brazos abiertos."

        "Me preparo para cualquier escenario.":
            $ reporte_defensa_nuevo_grupo = True
            y "Quien sea que montó este campamento puede significar problemas. Tengamos cuidado."

    hide laura
    hide bob
    with Dissolve (0.5)
    jump cap7_encuentro_tomas_charles

label cap7_encuentro_tomas_charles:

    "{i}El sonido seco de madera crujiente rompe el silencio.{/i}"
    "{i}Miran en dirección al sonido y ven a un hombre junta ramas y las quiebra, apilándolas en un atado bajo su brazo.{/i}"
    "{i}Sus movimientos son precisos. No duda. No desperdicia energía.{/i}"

    show laura hablando at centerleft
    with Dissolve(.5)

    l "¡Ey! ¡Por aquí!"

    show bob parado serio at left
    with Dissolve(0.5)
    b "¿Qué tal, amigo? Ellos son [nombre_personaje] y Laura. Mi nombre es Bob."
    
    show tomas serio at right
    with Dissolve(0.5)
    t "Ah si... ¿no eras tú el capitán del barco? Yo soy Tomás."

    b "Mucho gusto, Tomás. Y si, efectivamente, yo era el capitán."

    t "Imaginé que más personas habrían logrado salvarse."

    t "Parece que hubiesen visto un fantasma. Me distraen, y le prometí al resto que me encargaría de la leña."

    "{i}Bob, Laura y tú intercambian miradas, entusiasmados ante la mención de más personas.{/i}"

    "{i}Observan el refugio con mas detenimiento, y las ven.{/i}"

    "{i}Bastante cerca, descansando, recostado contra una roca, hay otro sujeto que los mira, Parece curioso pero relajado.{/i}"

    "{i}Un poco más lejos hay una mujer. Está demasiado ocupada asegurando las ataduras de un toldo como para interesarse demasiado en ustedes.{/i}"

    "{i}Tu y tus compañeros se miran, los tres perplejos ante la indiferencia de este grupo.{/i}"

    b "Vaya... Y yo que pensaba que si encontrábamos más sobrevivientes, nos recibirían con una sonrisa."

    l "No me quejaría si fuera tu, Bob. Parece que aquí tienen todo bien aceitado. ¡Hasta descansos tienen!"

    $ choice_position = "alta" # default alta superior
    menu:
        "Me disculpo con Tomás, no es mi intención distraerlo.":
            $ reporte_respetuoso_tomas = True
            y "No te queremos molestar. Es bueno ver a alguien que le da valor al tiempo y esfuerzo de su trabajo."

        "Aunque Tomás no parezca muy receptivo, debemos saber más.":
            $ reporte_intenta_conectar_tomas = True
            y "¿Cuánto tiempo llevan organizándose así? Es impresionante."

        "Tomás no parece muy receptivo, mejor será hablar con los demás.":
            $ reporte_distante_tomas = True
            y "No te haremos perder más tiempo."

    "{i}Tomás se encoge de hombros, recoge otra rama, y sigue con su tarea sin prestarles demasiada atención.{/i}"

    hide tomas
    with Dissolve (0.5)
    scene bg jungle resting_spot at truecenter
    with Dissolve(0.5)

    "{i}Se acercan al sujeto que está descansando. Tiene sus piernas cruzadas, curioseando y sin preocupación aparente.{/i}"

    show charles hablando at right
    with Dissolve(0.5)

    c "No se preocupen por Tomás. Es así con todo el mundo."

    c "Yo soy Charles. Bienvenidos a nuestro humilde refugio."

    show bob parado serio at centerleft
    with Dissolve(0.5)
    show laura hablando at left
    with Dissolve(0.5)

    l "Tal vez tú sí puedas contarnos, ¿hace cuánto que están juntos?"

    "{i}Charles sonríe, relajado, sin mostrar el mismo fastidio que Tomás.{/i}"

    c "El tiempo suficiente para entender que es mejor dejar que otros hagan el trabajo duro."
    $ choice_position = "alta" # default alta superior
    menu:
        "Mejor apelar al humor para romper el hielo.":
            $ reporte_broma_charles = True
            y "Bueno, ¡al menos eres honesto!"

        "Me incomoda un poco. Parece demasiado despreocupado.":
            $ reporte_desconfia_charles = True
            y "¿No te preocupa ser una carga para el resto?"

        "Discutir su argumento sería una clara pérdida de tiempo.":
            $ reporte_no_interactua_charles = True
            y "Parece que tienes todo bajo control."

    "{i}Charles tan solo sonríe. Parece menos interesado en ustedes que en el hecho de que estén aquí.{/i}"    

    jump cap7_conflicto_tomas_charles

label cap7_conflicto_tomas_charles:

    scene bg jungle resting_spot at truecenter
    with Dissolve(0.5)

    show screen combined_ui
    hide Bob
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)
    show charles serio at right    
    with Dissolve(0.5)
    show tomas serio at center    
    with Dissolve(0.5)

    "{i}Atrás de ustedes se deja de escuchar el crujir de la madera. Tomás mira a Charles con un atado de ramas bajo el brazo.{/i}"
    "{i}Su expresión esconde el enfado que el tono de su voz delata cuando habla.{/i}"

    t "Algunos de nosotros trabajamos duro, mientras otros holgazanean descansando."

    c "No estaba descansando. Estaba vigilando, asegurándome de que no tuviéramos problemas."
    c "A estos los escuché acercándose hace rato. Pero parecen inofensivos, ¿no?"

    t "¿Ah, sí? Dime, [nombre_personaje], ¿tú que piensas?"

    "{i}Tomás cruza los brazos. Charles apenas se voltea, pero te mira atentamente.{/i}"

    $ choice_position = "alta" # default alta superior
    menu:
        "Apoyar a Tomás. Charles estaba holgazaneando.":            
            $ confianza_tomas += 1
            $ confianza_charles -= 1
            y "Si lo que Charles hacía era útil, yo no lo noté. No lo vi ni moverse desde que llegamos."

            t "Exacto."

            c "Vaya, qué rápid[e] eres para sacar conclusiones."

        "Apoyar a Charles. Tal vez sí estaba haciendo algo.":            
            $ confianza_charles += 1
            $ confianza_tomas -= 1
            y "No podemos asumir que no estaba en realidad vigilando, por más relajado que pareciera."

            t "Espero que de verdad sea el caso."

            c "Me alegra que alguien lo entienda."

        "No intervenir. No es mi problema.":
            y "Ah no. Yo mo me meto en esto."

            "{i}Ambos continúan discutiendo, como si vinieran haciéndolo desde que sobrevivieron al naufragio.{/i}"

    hide tomas
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)

    jump cap7_encuentro_nuevo_grupo

label cap7_encuentro_nuevo_grupo:

    scene bg jungle makeshift_camp at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    show erika parada at right
    with Dissolve(0.5)

    k "¿Recién llegaron y ya están causando problemas?"

    "{i}Frente a ustedes aparece una mujer de postura firme y mirada penetrante.{/i}"
    "{i}No parece alterada por su presencia. Solo los observa, evalúandolos.{/i}"

    show bob parado serio at center
    show laura seria at left
    with Dissolve(0.5)

    b "No era nuestra intención causar ningún problema."
    
    l "Recién llegamos."

    "{i}La mujer los recorre con su mirada, midiéndolos.{/i}"

    if liderazgo < 5:        
        "{i}Cuando vuelve a hablar, lo hace dirigiéndose a Bob, como si reconociera en el al líder del tu grupo."

    else:
        "{i}Cuando vuelve a hablar, lo hace dirigiéndose a ti, como si te reconociera como el líder de tu grupo."        

    show erika conversando at right
    with Dissolve(0.5)
    k "Yo soy Erika."
    
    if reporte_respetuoso_tomas:
        k "Ya conocieron a Tomás y vi que entendieron el valor que le damos aquí al trabajo."

    elif reporte_intenta_conectar_tomas:
        k "Disculpen si Tomás no contestó con precisión a sus preguntas. Prefiere concentrarse en su trabajo."

    elif reporte_distante_tomas:
        k "Tomás no estaba siendo insolente con ustedes, [nombre_personaje]. No todos tenemos las mismas prioridades, y el estaba trabajando."
    
    if confianza_tomas > confianza_charles:

        k "¿Qué decir de charles que no haya dicho ya [nombre_personaje]. Solo digamos que verlo trabajar no es algo que se da todos los días."
    
    elif confianza_tomas < confianza_charles:

        k "Si estás del lado de Charles, [nombre_personaje], comienzo a pensar que tu grupo ha sobrevivido a pesar de ti, y no gracias a ti."
    else:
        k "Han causado más problemas de los que creen."
        k "Charles quería descansar y ahora está siendo fastidiado por Tomás."
        k "Y Tomás, que quería trabajar, está perdiendo el tiempo recriminándole a Charles que no hace nada."
    show erika parada at right
    with Dissolve(0.5)
    "{i}Erika cruza los brazos. Su postura no es hostil pero tampoco amigable.{/i}"

    $ choice_position = "alta" # default alta superior
    menu:
        "Debo mostrar confianza. Quiero verme fuerte ante ella.":
            $ reporte_se_muestra_firme = True
            $ desicion_intro += 1
            $ liderazgo += 1
            y "No estamos aquí para causar problemas. Queremos saber qué y quién más hay en la isla, nada más."
            y "Mi nombre es [nombre_personaje]. Ellos son Laura y Bob."

        "No quiero que nos vea como una amenaza. Debo cuidar mis palabras.":
            $ reporte_se_muestra_cauteloso = True
            $ desicion_intro += 1
            y "Es bueno ver más sobrevivientes, y sobre todo, tan organizados."
            y "Mi nombre es [nombre_personaje]. Ellos son Laura y Bob."

        "Debo ser abierto y apelar a la colaboración mútua.":
            $ reporte_se_muestra_abierto = True
            $ desicion_intro += 1
            $ liderazgo += 1
            y "Mi nombre es [nombre_personaje]. Ellos son Laura y Bob."
            y "Estamos todos juntos en esto. Nos encantaría saber qué dificultades han tenido y en qué podemos ayudarnos."            

    "{i}Erika te observa por unos segundos. Luego da un leve asentimiento, como si estuviera procesando cada palabra.{/i}"
    show erika conversando at right
    with Dissolve(0.5)
    k "Nosotros llegamos todos juntos a la playa, aferrándonos a un único salvavidas."
    k "Desde entonces nos hemos manejado bastante bien entre los tres."

    l "Pudieron rescatar algo de la playa?"

    k "Al principio priorizamos buscar refugio, pero al día siguiente volvimos a ver qué quedaba."

    python:
        objeto_faltante = []

        if not stuff_bidon_agua:
            objeto_faltante.append("bidón de agua lleno")
        if not stuff_bote:
            objeto_faltante.append("bote")
        if not stuff_caja_grande:
            objeto_faltante.append("cajón")

    if len(objeto_faltante) == 1:
        k "Recuperamos un [objeto_faltante[0]]."
        if not stuff_caja_grande:
            k "Tenía unas cuantas cosas útiles dentro."
    else:
        k "Recuperamos un [objeto_faltante[0]] y un [objeto_faltante[1]]."
        if not stuff_caja_grande:
            k "El cajón tenía unas cuantas cosas útiles dentro."  
    
    l "Nosotros pasamos por algo parecido, pero tenemos una persona recuperándose de una herida."

    b "Y es por eso que quisiera proponer que nos organicemos para juntar ambos grupos."
    b "Ustedes están un poco mejor que nosotros, y sin duda nos vendrá bien su ayuda."
    b "Pero seguramente nosotros podamos ayudarles a organizarnos para que todo sea más fácil para todos."

    show erika parada at right
    with Dissolve(0.5)
    k "No lo se. Tener dos refugios conviviendo en la isla tampoco es una mala idea."
    k "Tomás, Charles, ¿ustedes qué piensan?"
    hide laura 
    with Dissolve(0.5)
    show bob parado serio at left
    with Dissolve(0.5)
    show tomas serio at centerleft
    with Dissolve(0.5)
    show charles hablando at centerright
    with Dissolve(0.5)

    t "Separados, apenas hemos sobrevivido. Juntos, podremos estar mejor."

    c "Creo que estamos lo suficientemente bien como para que ninguna de las dos opciones sea terrible para nadie."

    t "Estas bien gracias a Erika y a mi."
    t "Deberías apoyar la idea de la unión, Charles. Cuanta más gente, más se disimulará tu pereza."

    "{i}Los grupos ahora se observan unos a otros. Unificar los refugios traería ventajas, pero también posbiles fricciones.{/i}"
    menu:
        "Apoyar la unión. Es lo mejor en términos de organización.":
            $ reporte_apoya_union = True
            $ desicion_intro += 1
            y "La cantidad de recursos y habilidades combinadas nos daría más oportunidades. Separados, desperdiciamos posibilidades."

        "Mencionar que forzar una unión es arriesgado y podría causar tensiones innecesarias.":
            $ reporte_indeciso_union = True
            $ desicion_intro += 1
            $ laura += 1
            y "Es verdad que juntos tendríamos ventajas, pero esto no va a ser fácil y requeriría de esfuerzo y paciencia por parte de todos."

        "Oponerse. Prefiero mantener independencia.":
            $ reporte_opone_union = True
            $ desicion_intro += 1
            $ bob -= 1
            y "Más gente también significa más roces. No hay garantía de que funcione."
    hide bob
    with Dissolve(0.5) 
    show laura hablando at left
    with Dissolve(0.5)

    l "Decidan lo que decidan, todos lo entenderemos. No pretendemos imponerles nuestros problemas tampoco."

    k "Estamos de acuerdo en que queremos soluciones, y no problemas."

    t "Juntos podríamos dividirnos las tareas para que algunos se encarguen de pensar formas de salir de esta isla."

    l "O al menos mejorar nuestras chances de ser rescatados."

    k "Si es que nos están buscando siquiera."

    "{i}Las palabras de Erika provocan una reacción en Bob que el intenta disimular, y cuando nota que lo viste, esquiva tu mirada.{/i}"
    
    menu:
        "Bob sabe algo que nosotros no. No podemos permitirnos guardar secretos que puedan ser importantes para el resto.":            
            $ desicion_intro += 1
            $ bob -= 1
            y "Bob, ¿qué pasa que no estás tan confiado con que vayamos a ser rescatados?"
            $ reporte_secreto_rescate = True

        "Mejor no exponerlo frente al resto.":
            "{i}Decides preguntarle más tarde, pero Laura se te adelanta. Parece que ella también notó algo raro.{/i}"            
            $ desicion_intro += 1
            $ bob += 1
            l "Bob, ¿qué pasa que no estás tan confiado con que vayamos a ser rescatados?"
            $ reporte_verdad_rescate = True
    hide charles
    with Dissolve(0.5)
    hide tomas
    with Dissolve(0.5)
    show laura seria at left
    with Dissolve(0.5)
    show bob parado serio at center
    with Dissolve(0.5)
            
    "{i}Todas las miradas se clavan en el.{/i}"
    show erika enojada at right
    with Dissolve(0.5)

    k "Señor capitán, será mejor que hable, si quiere que estas negociaciones de unidad prosperen."

    "{i}Bob recorre los rostros de los demás, uno por uno. La desesperanza en su mirada anuncia la naturaleza de lo que sabe.{/i}"

    pause .5

    b "La tormenta nos alejó de cualquier ruta normal."
    b "Probablemente estamos muy lejos de los lugares en los que una misión de rescate buscaría primero."
    b "No significa que no hay esperanzas, pero si nos rescatan, será solo después de que expandan el área de búsqueda."
    show laura seria at left
    with Dissolve(0.5)
    "{i}Las noticias provocan una serie de reacciones.{/i}"
    "{i}Laura mira a Bob con un atisbo de decepción, a la que el responde agachando la cabeza.{/i}"
    "{i}Tomás intenta evitar que la desesperación se apodere de el, y Charles comienza a entender que esto va para largo.{/i}"
    "{i}Erica es la única que, mirando al vacío, parece estar calculando su próximo movimiento con la nueva información.{/i}"
    "{i}Luego se pone a observar al resto, deteniéndose en Laura y en ti.{/i}"
    
    show erika parada at right
    with Dissolve(0.5)

    k "Bob, parece que tendrás que dar algunas explicaciones a tus compañeros. Parecen sorprendidos con la noticia."
    k "Los dejaremos solos mientras nosotros debatimos sobre la idea de unificar los grupos."

    "{i}Erika, Charles y Tomás se apartan para decidir qué van a hacer.{/i}"

    hide erika
    with Dissolve(0.5)
    
    b "Nosotros también debemos tomar una decisión."

    if reporte_opone_union:

        b "Laura, [nombre_personaje] ya manifestó estar en contra de la idea. Tú decides."
        show laura hablando at left
        with Dissolve(0.5)
        l "Lo siento, [nombre_personaje], pero debemos darle una chance a mantenernos todos juntos."
    else:
        b "Pero ninguno de los dos ha dicho que esté en contra, así que asumiré que al menos están dispuestos a darle una chance."

    pause 1
    show bob parado serio at centerleft
    with Dissolve(0.5)
    "{i}Los otros tres regresan luego de unos minutos.{/i}"    

    show erika parada at center
    with Dissolve(0.5)
    show tomas serio at centerright
    with Dissolve(0.5)
    show charles hablando at right
    with Dissolve(0.5)

    k "Hemos tomado una decisión."
    t "Nos uniremos a ustedes."    

    "{i}Todos intercambian sonrisas que se vuelven risas de júbilo a medida que comprenden dos cosas muy distintas.{/i}"
    "{i}Han mejorado sus chances de supervivencia enormemente, y eso les devuelve la esperanza que las noticias de Bob les quitaron.{/i}"
    "{i}Van a tener que aprender a trabajar en equipo aún más que antes.{/i}"
    "{i}Un grupo más grande también significa más individualidades con las que convivir.{/i}"

    c "Dependiendo de cómo lo miremos, también podríamos decir que son ellos los que se unen a nosotros."

    "{i}Charles suelta una carcajada, dejando claro que se trata de una broma, y pronto todos están riendo junto a el.{/i}"
    
    t "Más allá de la broma, lo cierto es que tendremos que decidir cuál será nuestro principal."

    b "¿Por qué no nos acompañan de vuelta a nuestro refugio, así pueden ver qué tal está?"
    show bob parado serio at centerleft
    with Dissolve(0.5)
    show laura hablando at left
    with Dissolve(0.5)
    l "Y de esa forma podremos saber qué opinan Ingrid y Marina antes de decidir."

    "{i}El resto asiente. Juntan algunas cosas básicas y emprenden el viaje.{/i}"

    hide bob
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)
    hide tomas
    with Dissolve(0.5)

    jump cap7_evaluacion_refugio

label cap7_evaluacion_refugio:

    scene bg jungle1 at truecenter
    with Dissolve(0.5)

    "{i}Charles, Erika y Tomás se sorprenden gratamente al ver qué fácil que han aprendido a moverse a través de la jungla.{/i}"

    show screen combined_ui

    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabana":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing

    "{i}Le presentan a Ingrid y Marina los nuevos integrantes del grupo, y las ponen al tanto de todo.{/i}"

    show bob parado serio at right    
    with Dissolve(0.5)

    b "Bueno, ahora que estamos todos juntos, y han tenido oportunidad de ver el lugar, es hora que discutamos a dónde queremos refugiarnos."

    "{i}Todos comienzan a proponer argumentos defendiendo su posición.{/i}"

    b "A ver, a ver. Vamos a ordenarnos, de a uno. Comenzaré yo."       
    b "Creo que la cabaña es la mejor opción. Tiene una estructura sobre la que se puede expandir."

    if destino_exploracion_2 == "cabana":
        
        show erika parada at centerright
        with Dissolve(0.5)
        k "Además de que, como vieron, ya está muy bien organizada."

        show charles hablando at centerleft
        with Dissolve(0.5)    
        c "Y nos ahorraría la mudanza."

        show tomas serio at left
        with Dissolve(0.5)
        t "De todas formas vamos a ayudarlos con sus cosas."

    elif refugio == "cabana":
        
        show erika parada at centerright
        with Dissolve(0.5)
        k "Se nota que le han puesto esfuerzo, y no puedo esperar a proponerles algunas mejoras."

        show charles hablando at right
        with Dissolve(0.5)
        c "¿Tendríamos que traer todo para aquí?"

        show laura hablando at centerleft
        with Dissolve(0.5)
        l "PDe más está decir que los ayudaríamos."
       
    else:
        show erika parada at centerleft
        with Dissolve(0.5)
        k "La cabaña es el único sitio donde no se ha armado ningún refugio."

        show tomas serio at centerright
        with Dissolve(0.5)
        t "Este refugio no está mal. Si Bob dice que la cabaña puede estar aún mejor, opino que confiemos en el."

    hide bob
    with Dissolve(0.5)
    hide laura
    hide erika
    hide charles
    hide tomas
    with Dissolve(0.5)

    show marina triste at centerleft
    with Dissolve(0.5)        
    m "La cabaña no puede ser nuestro refugio definitivo. Es demasiado calurosa."
    m "A Ingrid y a mi nos vendría mejor la cueva para terminar de recuperarnos. Es más fresca."    

    show tomas serio at right
    with Dissolve(0.5)
    t "El claro en la colina nos da visión del mar. Si alguien nos busca, podríamos verlos primero."

    show charles hablando at centerright
    with Dissolve(0.5)
    c "¿Qué opinas tú, Ingrid?"

    show ingrid seria at left
    with Dissolve(0.5)

    i "Yo no seré de mucha ayuda con la, o las, mudanzas, así que prefiero que decidan ustedes."

    hide ingrid
    with Dissolve(0.5)

    show laura hablando at left
    with Dissolve(0.5)

    l "Yo estoy con Tomás en esta. La colina es una gran ventaja para hacer contacto. Podríamos crear un faro y que nos puedan ver desde lejos."

    "{i}Parece que todos los refugios tienen quien los prefiere.{/i}"

    menu:
        "Quedarse en la cabaña. Es el lugar más consistente.":
            $ preferencia_refugio = "cabaña"
            $ desicion_intro += 1
            $ erika += 1
            $ bob += 1
            $ charles += 1
            $ marina -= 1
            $ tomas -= 1
            $ laura -= 1
            $ refugio = "cabana"
            "La cabaña nos da las mejores opciones a futuro. Como dice Bob, es más fácil de mejorar."

        "Elegir la cueva. Marina tiene razón sobre el calor.":
            $ preferencia_refugio = "cueva"
            $ desicion_intro += 1
            $ erika -= 1
            $ bob -= 1
            $ charles += 1
            $ marina += 1
            $ tomas -= 1
            $ laura -= 1
            $ refugio = "cueva"
            "El clima es clave. Ya sufrimos los mosquitos durante el día. Si tampoco podemos descansar en paz, a largo plazo será un problema."

        "Mudarse al claro en la colina. Su ventaja estratégica es demasiado buena como para no aprovecharla.":
            $ preferencia_refugio = "colina"
            $ desicion_intro += 1
            $ erika -= 1
            $ bob -= 1
            $ charles -= 1
            $ marina -= 1
            $ tomas += 1
            $ laura += 1
            $ refugio = "claro"
            "Poder ver el mar es clave. Y la idea de Laura de hacer un faro también es buena."

    "{i}Tu opinión termina de inclinar la balanza.{/i}"
    "{i}La decisión está tomada. Algunos la aceptan. Otros tienen dudas.{/i}"    

    hide bob
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)
    hide tomas
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)

    "{i}Los grupos vuelven a dividirse para trasladar todo al lugar elegido.{/i}"
    
    jump cap7_formacion_alianzas

label cap7_formacion_alianzas:

    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabana":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing

    pause 1

    if refugio == "claro":
        "{i}Todos se vuelven a encontar en el refugio del claro un rato después.{/i}"
    elif refugio == "cabana":
        "{i}Todos se vuelven a encontar en la cabaña un rato después.{/i}"
    elif refugio == "cueva":
        "{i}Todos se vuelven a encontar en la cueva un rato después.{/i}"        
    
    "{i}Luego de desempacar sus cosas, todos se juntan en la entrada del refugio.{/i}"
    "{i}Otra decisión importante sigue pendiente.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    b "Ahora que estamos instalados, necesitamos encarar aquello que, al menos nostotros, hemos postergado."
    b "Debemos elegir alguien que lidere nuestros esfuerzos."

    show erika parada at centerleft
    with Dissolve(0.5)
    k "Estoy de acuerdo. No sirve tener un refugio si no vamos a tirar todos para una misma dirección."

    show laura hablando at left
    with Dissolve(0.5)
    l "Designar roles, como el de líder, va a ser escencial para seguir mejorando nuestras chances."
    hide laura
    with Dissolve(.5)
    
    show tomas serio at right
    with Dissolve(0.5)
    t "No tenemos por qué discutirlo demasiado. Nosotros trabajamos bien bajo el liderazgo de Erika."
    hide tomas
    with Dissolve(.5)

    show charles hablando at right
    with Dissolve(0.5)
    c "Es cierto. Pero cada uno tiene su forma de ver las cosas. Ellos por ejemplo, no tenían un líder definido."
    hide charles 
    with Dissolve(.5)

    if liderazgo >= 5:
        show laura hablando at left
        with Dissolve(0.5)
        l "Si bien no siempre hicimos lo que decían, tanto [nombre_personaje] como Bob han oficiado como líderes en diferentes momentos."
        "{i}Bob claramente se sorprende un poco ante las palabras de Laura.{/i}"  
        hide Laura
        with Dissolve(.5)

    "{i}Todos intercambian miradas. Algunas incluso aterrizan sobre ti.{/i}"
    if liderazgo >= 5:
        "{i}Especialmente luego de lo que dijo Laura.{/i}"

    menu:
        "Apoyar a Erika. Parece tener una personalidad idónea para el rol.":
            $ reporte_apoya_liderazgo_erika = True
            $ desicion_intro += 1
            $ erika += 3
            $ bob -= 1
            y "Lo que dice Tomás es cierto, Erika sería una buena candidata. En su campamento todo parecía ir sobre ruedas."
            if liderazgo >= 5:
                y "Y gracias Laura, por tus palabres tan amables."
            b "Estoy dispuesto a darle una oportunidad da cualquiera de l[e]s dos, si es lo que el grupo termina decidiendo."

        "Apoyar a Bob. Su adaptabilidad es clave en un entorno incierto.":
            $ reporte_apoya_liderazgo_bob = True
            $ desicion_intro += 1
            $ bob += 3
            $ erika -=1
            y "No siempre podemos seguir un plan rígido. Bob sabe reaccionar ante lo inesperado como nadie."
            if liderazgo >= 5:
                y "Y gracias Laura, por tus palabres tan amables."
            k "Estoy dispuesta a darle a Bob una oportunidad, si es lo que el grupo termina decidiendo."

        "Postularte para el rol de liderazgo. Es hora de hacerme responsable del grupo." if liderazgo >= 5:
            $ reporte_postula_liderazgo = True
            $ desicion_intro += 1
            $ bob -= 1
            $ erika -= 1
            $ liderazgo += 1
            y "Gracias Laura, por tus palabres tan amables."
            y "He estado en cada decisión difícil que tomamos hasta ahora. Me gustaría que siga siendo así."
            y "Quiero postularme yo también para el rol de líder."            
            "{i}Tu seguridad ha dejado su marca.{/i}"

        "Evitar tomar partido. No importa quién lidere si no trabajamos juntos.":
            $ reporte_evade_liderazgo = True
            $ desicion_intro += 1
            y "Lo que importa no es solo quién manda, sino que todos podamos funcionar como grupo."
            "{i}Tus palabras parecen resonar en los oídos de todos, que te miran bajo unos nuevos ojos.{/i}"
            b "Dicho como un verdadero líder, [nombre_personaje]."
            k "Por más que me cueste admitirlo, es cierto. Tu humildad es sincera. Creo que tú también deberías postularte para el rol."
            "{i}Los demás asienten, más o menos convencidos, pero todos te demuestran su apoyo.{/i}"

    show laura hablando at left
    with Dissolve(0.5)
    l "De todas formas, no tenemos por qué elegir ya mismo. Terminar de acondicionar el refugio antes de que anochezca es más importante."
    l "Ahora somos ocho compartiendo techo."

    "{i}La decisión queda pendiente.{/i}"
    "{i}Los rostros de algunos parecen anticipar el resultado. Otros, no tanto.{/i}"
    "{i}Por lo menos dejaron de postergar el hablar del tema.{/i}"

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
        # $ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        # $ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        # show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capítulo 7, el encuentro con otro grupo de supervivientes trae nuevas oportunidades pero tambien nuevos problemas. ¿Serán una ayuda o un peligro si llegan momentos críticos?"
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        # hide screen decisiones_popup with dissolve
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
    $ persistent.cantidad_capitulos +=1
    jump cap8_avisar_tormenta

label tormenta_preparativos:
    # Se ve en el horizonte una gran tormenta
    # El equipo se separa para obtener las cosas necesarias para reforzar el refugio
    # ver cual es el punto critico, fuego, comida, agua, protegerse de la tormenta, 
        #segun el refugio elegido y las opciones de los capitulso anteriores
    # durante toda la previa a la tormenta se dan encontronazos entro los dos lideres con visiones muy opuestas de como y que hacer
    # la tormenta llega con tremenda fuerza, rompiendo parte del refugio, generando peligros y disparado miedos
    # antes o durante la tormenta puede incluirse al jabali que rompe, persigue o complcia de algun modo, que se sienta una amenaza
    # como el equipo se vincula y apoya o no en esos momentos
    # los dos lideres van formando su grupo de apoyo 
    # termina con la tormenta amainando y el refugio dañado, y varias de las cosas perdidas o arruinadas
    # un equipo responsabiliza al otro de las perdidas y la discusion termina en el grupo dividiendose en dos
    jump chapter_8_end 

label cap8_avisar_tormenta:

    scene bg horizon_storm_clouds at truecenter
    with Dissolve(0.5)

    "{i}El cielo ha cambiado. Nubes oscuras se alzan en la distancia, avanzando lentamente, pero con determinación.{/i}"
    "{i}La tormenta está regresando.{/i}"

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)
    #if refugio == "cueva":
    #    scene bg jungle cave
    #elif refugio == "cabana":
    #    scene bg jungle hut
    #elif refugio == "claro":
    #    scene bg jungle clearing
    #with Dissolve(0.5)

    show bob parado serio at centerright
    with Dissolve(0.5)
    show erika parada at centerleft
    with Dissolve(0.5)

    k "Hay que empezar a reforzar el refugio. Si no nos preparamos ahora, después será imposible."

    show bob parado hablando at centerright
    with Dissolve(0.5)
    b "¿Reforzarlo? Primero asegurémonos de tener lo básico para sobrevivir."
    show bob parado serio at centerright
    with Dissolve(0.5)

    show laura hablando at left
    with Dissolve(0.5)
    show bob parado serio at centerright
    with Dissolve(0.5)

    l "Si el viento es fuerte, lo que tengamos se puede volar. Necesitamos seguridad primero."

    hide laura 
    with Dissolve(0.5)

    if refugio == "claro":
        show tomas serio at right
        with Dissolve(0.5)

        t "Si la lluvia es intensa, en la colina vamos a estar en problemas. No hay mucha protección allí."

        hide tomas
        with Dissolve(0.5)

    elif refugio == "cueva":
        show marina triste at left
        with Dissolve(0.5)

        m "La cueva puede inundarse. Si el agua sube demasiado, vamos a quedar atrapados."

        hide marina
        with Dissolve(0.5)

    elif refugio == "cabana":
        show charles hablando at right
        with Dissolve(0.5)

        c "El interior de la cabaña será casi como estar a la intemperie cuando empiece a soplar el vendaval."

        hide charles
        with Dissolve(0.5)    
    
    "{i}Erika y Bob claramente tienen maneras distintas de hacer las cosas, y formas diferentes de establecer las prioridades.{/i}"
    "{i}Bob no está errado, hay que seguir asegurando recursos. No sabemos cuánto tiempo estaremos aquí.{/i}"
    "{i}Por otro lado, todos los demás parecen más preocupados por cómo aguantará el refugio a la tormenta. Reforzarlo no es mala idea.{/i}"
    $ choice_position = "default" # default alta superior
    menu:
        "Apoyar el enfoque de Erika: organizar el refuerzo estructural del refugio.":
            $ enfoque_preparacion = "estructura"
            $ erika += 2
            y "No podremos resguardar ningún recurso si el refugio no resiste la tormenta, Bob."
            "{i}Bob asiente, resignándose.{/i}"

        "Apoyar el enfoque de Bob: asegurarse de tener provisiones antes que nada.":
            $ enfoque_preparacion = "recursos"
            $ bob += 2
            y "¿Cuánto durará la tormenta? Busquemos recursos ahora, porque salir a buscarlos con viento y lluvia más tarde es una locura."
            "{i}El solo imaginarlo hace que todos comiencen a pensarlo dos veces. De a uno, van asintiendo.{/i}"
            "{i}Erika sacude la cabeza, frustrada.{/i}"

        "Equilibrar ambos enfoques. Se debe trabajar en todo a la vez.":
            $ enfoque_preparacion = "equilibrado"
            $ bob += 1
            $ erika += 1
            y "Ahora somos más, podemos perfectamente dividirnos las tareas y asegurarnos que el refugio sea seguro y los recursos suficientes."
            "{i}Se miran entre todos y asienten.{/i}"

    hide erika
    with Dissolve(0.5)
    hide bob
    with Dissolve(0.5)

    jump cap8_prioridades_refugio

label cap8_prioridades_refugio:

    if refugio == "cueva":
        scene bg inside cave at truecenter
    elif refugio == "cabaña":
        scene bg inside cabin at truecenter
    elif refugio == "claro":
        scene bg inside shelter at truecenter
    with Dissolve(0.5)

    "{i}La tormenta se acerca. Cada minuto cuenta.{/i}"

    if enfoque_preparacion == "estructura":
        "{i}El grupo se reparte las tareas para asegurar la protección contra el viento y la lluvia.{/i}"
        
        show erika seria at centerleft
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)

        k "Tomás, allí en la zona cubierta por las lonas, revisa que todo esté bien atado."

        t "Le haré doble nudo a todo porque el viento hará lo posible por llevarse la toldería entera."

        show bob parado serio at centerright
        with Dissolve(0.5)

        b "Y mientras hacen eso, ¿qué pasa con la comida y el agua? No podemos aislarnos aquí, sin lo esencial."

        k "Nos ocuparemos después. Si no protegemos el refugio, perderemos todo."

    elif enfoque_preparacion == "recursos":
        "{i}El grupo prioriza buscar provisiones. Se dividen para encontrar alimentos, agua y materiales de emergencia.{/i}"
        
        show bob parado serio at centerright
        with Dissolve(0.5)
        show marina triste at right
        with Dissolve(0.5)

        b "Marina, ayudame a buscar almacenamiento para el agua. Si se contamina, será un problema."

        if inventan_cantimploras:
            m "Podemos hacer más cantimploras para almacenar el agua del refugio."            
            b "Que algunos se encarguen de buscar las cañas, y los demás las vamos cortando."
        else:
            m "Estuve pensando que podríamos hacer recipientes para el agua con cañas de bambú, que abundan por toda la isla."
            m "Quebrando las cañas en cada sección, podemos tener varias cantimploras."
            $ inventan_cantimploras = True

        show erika gr conversando at leftgr
        with Dissolve(0.5)

        k "¿Fabricar cantimploras? ¿Cuántas necesitamos? ¡Estaremos horas! El refugio es más importante."
        hide marina
        with Dissolve(0.5)
        show bob gr parado hablando at rightgr
        with Dissolve(0.5)
        b "El refugio, por más que lo reforcemos, puede transformarse en una trampa mortal."
        b "Quedar atrapados allí sin suministros podría ser peor que aguantar la tormenta sin reforzarlo."

    elif enfoque_preparacion == "equilibrado":
        "{i}El grupo distribuye las tareas. Algunos van a ir a buscar suministros, y otros se quedarán a reforzar el refugio."
        "{i}La inseguridad se nota en los rostros de todos, que temen no alcanzar ninguna de las dos metas a tiempo.{/i}"
        
        show bob parado serio at centerright
        show erika conversando at centerleft
        with Dissolve(0.5)

        k "Tratemos de ser lo más eficientes que podamos y lo lograremos."
        show erika parada at centerleft
        show bob parado enojado at centerright
        with Dissolve(0.5)
        b "O podría quedar todo a medias, por haber diluido los esfuerzos."


        "{i}La voz de Erika transmite seguridad, aunque sus ojos parecen admitir que Bob puede estar en lo cierto.{/i}"
        "{i}Se nota que ambos están haciendo un esfuerzo grande por tolerarse, pero la tensión constante en el aire es terrible.{/i}"

    hide tomas
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide bob
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)    

    jump cap8_acercamiento_personajes

label cap8_acercamiento_personajes:

    "{i}Antes de que todos se dispersen para prepararse, aún queda un momento para acercarse a alguien.{/i}"
    "{i}Forjar alianzas será importante para lo que viene.{/i}"
    if refugio == "cueva":
        "{i}Entras a la cueva para poder hablar con alguno de los demás supervivientes.{/i}"
        jump acercamiento_cueva
    elif refugio == "cabaña":
        "{i}Entras a la cabaña para poder hablar con alguno de los demás supervivientes.{/i}"
        jump acercamiento_cabin
    elif refugio == "claro":
        "{i}Te acercas al refugio en el claro para poder hablar con alguno de los demás supervivientes.{/i}"
        jump acercamiento_shelter

label acercamiento_cueva:
    scene bg inside cave at truecenter
    with Dissolve(0.5)
    jump cap8_hablar_con_personajes

label acercamiento_cabin:
    scene bg inside cabin at truecenter
    with Dissolve(0.5)
    jump cap8_hablar_con_personajes

label acercamiento_shelter:
    scene bg inside shelter at truecenter
    with Dissolve(0.5)
    jump cap8_hablar_con_personajes

label cap8_hablar_con_personajes:
    $ choice_position = "superior" # default alta superior
    menu:
        "Acercarse a Marina.":
            jump cap8_acercamiento_marina

        "Acercarse a Tomás.":
            jump cap8_acercamiento_tomas

        "Acercarse a Laura.":
            jump cap8_acercamiento_laura

        "Acercarse a Charles.":
            jump cap8_acercamiento_charles

        "Acercarse a Ingrid.":
            jump cap8_acercamiento_ingrid

    "{i}No hay tiempo para más. Ahora, el grupo debe prepararse para la tormenta.{/i}"

    jump cap8_separacion_grupo

label cap8_acercamiento_ingrid:

    show ingrid cintura at left
    with Dissolve(0.5)

    "{i}Ingrid observa el entorno con una expresión de análisis, aunque su agotamiento es evidente.{/i}"
    "{i}Sus dedos trazan patrones sobre la tierra, como si intentara resolver un problema invisible.{/i}"

    if ingrid > 0:
        "{i}Vuelve en sí cuando nota tu presencia. Parece dispuesta a escuchar.{/i}"

        menu:
            "Ingrid, ¿Cómo ves lo que viene?":
                $ ingrid += 1
                y "Me gustaría escuchar tu opinión."

                i "Algunos aquí aún actúan como si prepararse fuera debatible. Si no lo hacemos, nos espera el desastre."

            "Vamos a necesitar una mente fría en esta tormenta. Nadie mejor que tu, como ya lo has demostrado.":
                $ ingrid += 1
                y "Tu enfoque racional es clave. ¿Cómo crees que debemos proceder?"

                i "El tiempo apremia, hay que usar la lógica. No es tan difícil. Necesitamos optimizar cada decisión y movimiento."

    else:
        "{i}Ingrid nota la presencia, pero no parece demasiado receptiva. No tiene paciencia para ti.{/i}"

        menu:
            "No siempre es fácil entender lo que es claro para ti. Pero quiero intentarlo.":
                $ ingrid += 1
                y "Sé que ves cosas que otros pasan por alto."

                i "Si al menos todos intentaran pensar por un segundo, tal vez no estaríamos en esta situación."

            "Ingrid, vamos. Háblame. No tenemos tiempo para rencores.":
                y "No todos ven el problema como tu. ¿Cuál es tu opinión?"

                i "Las cosas básicas que algunos necesitan comprender, no necesitan ser señaladas por una científica, deberían ser obvias."

    "{i}Ingrid no parece conforme con las propuestas de Bob y Erika. Tal vez sea un buen momento para preguntarle a Ingrid por quién se inclina.{/i}"

    menu:
        "¿Cómo ves el tema pediente de decidir el liderazgo?":
            jump cap8_liderazgo_ingrid

        "Mejor no molestarla, parece querer mantenerse al margen de todo.":
            jump cap8_separacion_grupo

label cap8_liderazgo_ingrid:

    "{i}Ingrid entrecierra los ojos. Es un tema que claramente le ha dado vueltas en la cabeza.{/i}"

    i "Aún lo estoy considerando."

    menu:
        "Bob sabe improvisar. Sobrevivir es más importante que planificar cada detalle.":
            $ apoyo_bob += 1
            y "Bob se adapta bien a los imprevistos. Reaccionar rápido muchas veces puede ser de vida o muerte."

            i "Es verdad, la adaptación es clave. Pero sin estructura, esto se convierte en caos."

        "Erika mantiene el orden. Necesitamos estar más estructurados.":
            $ apoyo_erika += 1
            y "Si no tenemos una base de organización, nos vamos a hundir."

            i "Orden significa estructura. Y estructura significa posibilidad de estabilidad."

        "Yo podría liderar al grupo. Creo que puedo organizarnos bien sin perder la capacidad de adaptación." if ingrid >= 0:
            $ liderazgo += 1
            y "Además quiero que hagamos uso de nuestra mayor fortaleza, que es estar juntos y unidos."

            i "Si puedes balancear ambos enfoques, tal vez valga la pena darte una oportunidad."

    "{i}Tu postura quedó clara. Cuando llegue el momento, Ingrid ya tendrá su postura definida.{/i}"

    jump cap8_separacion_grupo

label cap8_acercamiento_charles:

    show charles serio at right
    with Dissolve(0.5)

    "{i}Charles observa la tormenta en la distancia, pensativo.{/i}"
    "{i} Sus manos juegan con un pedazo de madera, como si pudiera encontrar respuestas en la textura.{/i}"

    if charles < 0:
        "{i}Nota tu presencia, pero no parece particularmente interesado en hablar.{/i}"

        menu:
            "Sé que tuvimos diferencias, pero prefiero que trabajemos juntos en esto.":
                $ tomas += 1
                y "No tiene sentido ahondar esta grieta."

                c "Con la tormenta en puerta, mejor no ahondar en rencores pasados."

            "No vamos a llegar lejos si seguimos peleando. Mejor enfocarnos en lo que viene.":
                "No podemos darnos el lujo de perder más tiempo."

                c "Quizás tengas razón. Pero tendrás que ganarte mi confianza."

    else:
        "{i}Al notar tu presencia, Charles levanta la mirada. Parece abierto a la conversación.{/i}"

        menu:
            "Charles, me interesa saber qúe piensas de este dilema.":
                $ tomas += 1
                y "Quiero escuchar más ideas. Vendrán bien si tenemos que improvisar."

                c "No vamos a tener demasiado margen para improvisar cuando esto empiece."

            "¿Qué piensas hacer tú, Tomás?":
                
                y "No hablo solo de la tormenta."

                c "Haré lo que decidieron que era mejor. El problema, como bien dices, viene después."
                c "Las tormentas suelen desenterrar mucha cosa."

    "{i}Aunque sus palabras son crípticas y parece estar pensando más allá de lo inmediato, Charles tiene claras sus ideas.{/i}"
    "{i}Seguramente tenga claro por quién se inclinará cuando llegue el momento de decidir sobre el liderazgo.{/i}"

    menu:
        "¿A quién ves liderando el grupo?":
            jump cap8_liderazgo_charles

        "Tomás está pensando en cualquier cosa, menos en quién debe ser el líder. Mejor ni le pregunto.":
            jump cap8_separacion_grupo

label cap8_liderazgo_charles:

    "{i}Charles deja de jugar con el trozo de madera y fija la mirada. Es obvio que ya ha pensado en esto.{/i}"
    c "Aún lo estoy considerando."
    menu:
        "Bob sabe improvisar. Sobrevivir es más importante que planificar cada detalle.":
            $ apoyo_bob += 1
            y "Bob se adapta bien a los imprevistos. Reaccionar rápido muchas veces puede ser de vida o muerte."

            c "Bob improvisará bien, pero un solo error de juicio puede costarnos muy caro."

        "Erika mantiene el orden. Necesitamos estar más estructurados.":
            $ apoyo_erika += 1
            y "Si no tenemos una base de organización, nos vamos a hundir."

            c "A veces las estructuras más rígidas son las que más fácilmente se desmoronan. Hay fortaleza en la flexibilidad."

        "Yo podría liderar al grupo. Creo que puedo organizarnos bien sin perder la capacidad de adaptación." if charles >= 0:
            $ liderazgo += 1
            y "Además quiero que hagamos uso de nuestra mayor fortaleza, que es estar juntos y unidos."

            c "Tienes claro lo más indispensable. No hay recurso más importante que la unión del gurpo."

    "{i}Tu postura quedó clara. Cuando llegue el momento, Charles ya tendrá su postura definida.{/i}"

    jump cap8_separacion_grupo

label cap8_acercamiento_laura:

    show laura preocupada at left
    with Dissolve(0.5)
    $ laura += 1
    "{i}Laura mira hacia el cielo y luego al suelo, como si en ambos pudiera encontrar una señal.{/i}"
    "{i}Sus dedos juegan con un collar gastado que cuelga de su cuello.{/i}"

    if laura < 0:
        "{i}Su expresión se endurece levemente al notar tu presencia. No parece incómoda, pero tampoco entusiasmada.{/i}"

        menu:
            "Laura, sé que no hemos coincidido mucho, pero prefiero que trabajemos juntos.":
                $ laura += 1
                y "Lo que viene es más grande que cualquier diferencia."

                l "No puedo negar que es verdad. Solo espero que realmente lo demuestres."

            "No tenemos que llevarnos bien, pero sí trabajar juntos.":
                y "No vamos a llegar lejos si cada quien tira para su lado."

                l "Sobrevivir juntos, si. No es tan difícil."

    else:
        "{i}Laura gira su mirada hacia ti cuando te acercas. Aunque preocupada, está dispuesta a escuchar.{/i}"

        menu:
            "Laura, no importa lo que pase, quiero que sepas que me alegra que estemos juntos en esto.":
                $ laura += 1
                y "Siempre es mejor enfrentar las crisis junto a alguien en quien confiar."

                l "Eso significa mucho para mi, [nombre_personaje]. Gracias."

            "No bajes los brazos, ¿Si?":
                
                y "No podemos perder el impulso ahora."

                l "Eso intento, aunque cuesta."

    "{i}Las palabras de Laura siempre son sinceras. Si le preguntaras sobre el asunto del liderazgo, ella te diría lo que piensa.{/i}"

    menu:
        "¿Has estado pensando en qué decidirás con respecto a lo del liderazgo?":
            jump cap8_liderazgo_laura

        "Parece un poco distraída, no es el mejor momento.":
            jump cap8_separacion_grupo

label cap8_liderazgo_laura:

    "{i}Laura exhala con lentitud antes de responder. Ya ha pensado en esto, pero aún duda.{/i}"
    l "Aún lo estoy considerando."

    menu:
        "Bob sabe improvisar. Sobrevivir es más importante que planificar cada detalle.":
            $ apoyo_bob += 1
            y "Bob se adapta bien a los imprevistos. Reaccionar rápido muchas veces puede ser de vida o muerte."

            l "Bob sí que no baja los brazos. Eso es bueno."

        "Erika mantiene el orden. Necesitamos estar más estructurados.":
            $ apoyo_erika += 1
            y "Si no tenemos una base de organización, nos vamos a hundir."

            l "Eso suena más sencillo de lo que es. Tenemos que estar preparados para trabajar duro."

        "Yo podría liderar al grupo. Creo que puedo organizarnos bien sin perder la capacidad de adaptación." if laura >= 0:
            $ liderazgo += 1
            y "Además quiero que hagamos uso de nuestra mayor fortaleza, que es estar juntos y unidos."

            l "No es la primera vez que se me cruza por la cabeza, creo que ya lo sabes."

    "{i}Tu postura quedó clara. Cuando llegue el momento, Laura ya tendrá su postura definida.{/i}"

    jump cap8_separacion_grupo

label cap8_acercamiento_marina:

    show marina triste at left
    with Dissolve(0.5)

    "{i}Marina parece un poco abrumada por el ajetreo de los preparativos.{/i}"
    "{i}Trata de no estorbar mientras espera a los demás.{/i}"

    if marina < 0:
        "{i}Su agobio parece aumentar un poco cuando te acercas.{/i}"

        menu:
            "Marina, escucha. Se que hemos tenido algunos roces, pero antes de lo que se viene, quiero que sepas que cuentas conmigo.":
                $ marina += 1
                y "Así como siempre me demostraste que yo puedo contar contigo."

                m "Se siente bien escuchar tus palabras de reconocimiento. Muchas gracias. Se que cuento contigo."

            "No necesitamos ser amigos, simplemente dejar las diferencias de lado.":
                y "Va a ser lo mejor para todos."

                m "Lo dices como si te hubiese declarado la guerra. Por mi, está bien."

    else:
        "{i}Marina te sonríe cuando te acercas. Parece que el barullo de los preparativos ya no le molesta tanto.{/i}"

        menu:
            "Marina, fuiste la primera persona que encontré luego del naufragio. Pase lo que pase, me alegra haber llegado tan lejos juntos.":
                $ marina += 1
                "No se que habríamos hecho sin ti."

                l "Ya, calla, [nombre_personaje]. Debería decir lo mismo de ti, y lo sabes."

            "Marina, querida. No te distraigas y mantente alerta.":
                
                y"Contamos contigo."

                l "¿Eh? Si... no te preocupes, [nombre_personaje]."

    "{i}Marina tal vez aún no haya pensado en su preferencia para el liderazgo, pero vale la pena preguntar.{/i}"

    menu:
        "Con esto de elegir un líder ¿Has pensado ya a quién prefieres?":
            jump cap8_liderazgo_marina

        "Si tanto movimiento la tiene abrumada, preguntarle tal vez sería peor.":
            jump cap8_separacion_grupo

label cap8_liderazgo_marina:

    "{i}Marina se rasca la cabeza y sonríe.{/i}"
    m "Aún lo estoy considerando."

    menu:
        "Bob sabe improvisar. Sobrevivir es más importante que planificar cada detalle.":
            $ apoyo_bob += 1
            y "Bob se adapta bien a los imprevistos. Reaccionar rápido muchas veces puede ser de vida o muerte."

            m "Por supuesto, Bob ha sido imprescindible desde el primer día."

        "Erika mantiene el orden. Necesitamos estar más estructurados.":
            $ apoyo_erika += 1
            y "Si no tenemos una base de organización, nos vamos a hundir."

            m "No voy a mentirte... Me agrada bastante Erika. Lo da todo."

        "Yo podría liderar al grupo. Creo que puedo organizarnos bien sin perder la capacidad de adaptación." if marina >= 0:
            $ liderazgo += 1
            y "Además quiero que hagamos uso de nuestra mayor fortaleza, que es estar juntos y unidos."

            m "Me gusta verte hablar así. Estamos de acuerdo."

    "{i}Tu postura quedó clara. Cuando llegue el momento, Marina ya tendrá su postura definida.{/i}"

    jump cap8_separacion_grupo

label cap8_acercamiento_tomas:

    show tomas serio at left
    with Dissolve(0.5)

    "{i}Tomás está bastante ocupado preparando todo para ponerse manos a la obra.{/i}"    

    if tomas < 0:
        "{i}No se molesta en demostrar su fastidio al ser molestado.{/i}"

        menu:
            "Tomás, se que no soy de tu agrado, pero me gustaría cambiar eso.":
                $ tomas += 1
                y "Te propongo que trabajemos juntos, y verás que no somos tan distintos."

                t "Si lo que propones es trabajar, estás hablando mi idioma."

            "Seré breve, se que odias perder el tiempo. Es hora de dejar atras viejos rencores.":
                y "Es hora de trabajar juntos."

                t "Trabajando nunca tuve problemas con nadie. Es cuando no se trabaja que hay problemas."

    else:
        "{i}Te saluda con esfuerzo porque tiene las manos cargadas. Parece dispuesto a oírte mientras no lo estorbes.{/i}"

        menu:
            "Tomás, fuiste el primero en recibirnos en tu campamento. Mira lo lejos que hemos llegado.":
                $ tomas += 1
                y "Ahora nos toca aguantar juntos."

                t "Si sobrevivir está en nuestras posibilidades, no dudo que lo lograremos si trabajamos duro."

            "Tu si que no pierdes el tiempo, ¿eh Tomás? Esa tormenta debería pensárselo dos veces antes de acercarse.":
                
                "Tu entrega es... inspiradora."

                t "Solo hago mi trabajo, [nombre_personaje]."

    "{i}Tomás se ha mostrado muy leal a Erika, pero también ha dejado claro que tiene capacidad de pensamiento crítico y autónomo.{/i}"

    menu:
        "Oye, Tomás. Con respecto a la elección de un líder... ¿sigues pensando que Erika es la única opción?":
            jump cap8_liderazgo_tomas

        "Si hubiese alguna chance de que Tomás se decante por alguien más, no hace ningún esfuerzo en demostrarlo. Mejor no lo molesto.":
            jump cap8_separacion_grupo

label cap8_liderazgo_tomas:

    "{i}Tomás frunce el seño y exhala. Se detiene a pensar un momento.{/i}"
    t "Aún lo estoy considerando."

    menu:
        "Bob sabe improvisar. Sobrevivir es más importante que planificar cada detalle.":
            $ apoyo_bob += 1
            y "Bob se adapta bien a los imprevistos. Reaccionar rápido muchas veces puede ser de vida o muerte."

            t "Sigo pensando que me gané la lotería despertando junto a Erika en la playa, pero es cierto que Bob tiene lo suyo."

        "Erika mantiene el orden. Necesitamos estar más estructurados.":
            $ apoyo_erika += 1
            y "Si no tenemos una base de organización, nos vamos a hundir."

            t "Si hemos llegado tan lejos, se lo debemos a ella."

        "Yo podría liderar al grupo. Creo que puedo organizarnos bien sin perder la capacidad de adaptación." if tomas >= 0:
            $ liderazgo += 1
            t "Además quiero que hagamos uso de nuestra mayor fortaleza, que es estar juntos y unidos."

            m "Espero que estés seguro, y no exageres."

    "{i}Tu postura quedó clara. Cuando llegue el momento, Tomás ya tendrá su postura definida.{/i}"

    jump cap8_separacion_grupo

label cap8_separacion_grupo:

    hide laura
    with Dissolve(.5)
    hide tomas
    with Dissolve(.5)
    hide ingrid
    with Dissolve(.5)
    hide marina
    with Dissolve(.5)
    hide charles
    with Dissolve(.5)

    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabana":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Mientras todos se preparan, Erika y Bob siguen discutiendo, y las tensiones siguen aumentando.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    show erika parada at centerleft
    with Dissolve(0.5)

    "{i}Un relámpago ilumina el horizonte. Todos miran en esa dirección, esperando el sonido del trueno, que llega unos segundos más tarde.{/i}"
    show bob parado enojado at centerright
    with Dissolve(0.5)

    b "¡Perfecto! Ahora ya no habrá tiempo para ir a buscar suministros de todas formas. Espero que estén contentos."
    
    show erika enojada at centerleft
    with Dissolve(0.5)

    k "Escucha el rugido de ese trueno, Bob. Debemos reforzar el refugio ya mismo."

    "{i}Los grupos de trabajo comienzan a formarse según las prioridades establecidas y las afinidades de cada uno.{/i}"

    if apoyo_bob > apoyo_erika:

        show ingrid enojada at right
        with Dissolve(0.5)        

        i "El sonido del trueno se escuchó unos pocos segundos después de que vimos el rayo. La tormenta está cerca. Hay que actuar ya."

        hide ingrid
        with Dissolve(0.5)
        
        "{i}Bob comienza a coordinar los esfuerzos para revisar de qué disponen para reforzar el refugio.{/i}"
        
        hide erika
        with Dissolve(0.5)

        jump cap8_formacion_equipos

    elif apoyo_erika > apoyo_bob:

        show tomas serio at left
        with Dissolve(0.5)

        t "Esa tormenta se acerca muy rápido. Erika tenía razón. Reforcemos el refugio ya mismo."

        hide tomas
        with Dissolve(0.5)

        "{i}Erika comienza a revisar los puntos débiles del refugio, y le ordena al resto que haga lo mismo.{/i}" 
        
        hide bob
        with Dissolve(0.5)
        jump cap8_formacion_equipos

    elif liderazgo > 4:
        
        if laura >= 1:
            show laura preocupada at left
            with Dissolve(0.5)

            l "Si no hubiésemos perdido el tiempo, podríamos haber recolectado recursos y reforzado el refugio, como propuso [nombre_personaje]!"

            hide bob
            with Dissolve(0.5)
            hide erika
            with Dissolve(0.5)
            l "Debimos escucharte antes, así que ahora no cometeremos el mismo error."

            hide laura
            with Dissolve(0.5)
        else:
            show marina preocupada at left
            with Dissolve(0.5)

            m "Si no hubiésemos perdido el tiempo, podríamos haber recolectado recursos y reforzado el refugio, como propuso [nombre_personaje]!"

            hide bob
            with Dissolve(0.5)
            hide erika
            with Dissolve(0.5)
            m "Debimos escucharte antes, así que ahora no cometeremos el mismo error, [nombre_personaje]."

            hide marina
            with Dissolve(0.5)
        

        "{i}Este es un momento crucial. Articular entre la improvisación de Bob y la meticulosidad de Erika, podría consolidarte como líder.{/i}"

        "{i}Todos están listos para ponerse a trabajar. Solo hace falta un plan de acción.{/i}"   

        jump cap8_preparacion_tormenta

label cap8_preparacion_tormenta:

    scene bg jungle_storm_approaching at truecenter
    with Dissolve(0.5)

    "{i}El cielo está cubierto de nubes densas. El viento ha comenzado a aumentar su fuerza. La tormenta es inminente.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    show erika parada at centerleft
    with Dissolve(0.5)

    b "El tiempo apremia. Si no nos organizamos rápido, no vamos a resistir."

    k "No seamos imprudentes. Tenemos que coordinar nuestros esfuerzos."

    "{i}Las dos posturas son claras: rapidez y adaptación con Bob, o análisis y coordinación con Erika.{/i}"

    menu:
        "Priorizar una preparación rápida y efectiva":
            $ apoyo_bob += 2
            y "No hay tiempo que perder. Hagamos lo que podamos con el que nos queda."

            "{i}Bob asiente de inmediato.{/i}"

            b "Buena decisión. Movámonos ya."
            hide erika
            with Dissolve(0.5)
            hide bob 
            with Dissolve(0.5)
        "Optimizar los esfuerzos será lo mejor.":
            $ apoyo_erika += 2
            y "Erika, la coordinación de todos será clave para salir de esto."

            "{i}Erika cruza los brazos y asiente con una mirada determinada.{/i}"

            k "Si evitamos errores ahora, vamos a evitar problemas después."
            hide erika
            with Dissolve(0.5)
            hide bob 
            with Dissolve(0.5)

        "Manejar un equilibrio entre rapidez y estrategia":
            $ liderazgo += 2
            y "Erika, tu te encargarás de la prevención de los problemas. Bob, tu estarás a cargo de la contención."
            y "Mientras Erika conduce a parte del equipo en trabajar sobre lo que es previsible, Bob y los demás se encargaran de lo que vaya apareciendo."

            "{i}Erika y Bob intercambian una mirada tensa, pero entienden en seguida lo que estás haciendo, asignando a cada uno una tarea según su fortaleza.{/i}"

            b "Cada uno a lo suyo entonces."
            hide bob 
            with Dissolve(0.5)
            k "Me parece perfecto."
            hide erika
            with Dissolve(0.5)

    "{i}El grupo continúa reforzando el refugio y asegurando los recursos antes de la llegada de la tormenta.{/i}"    

    jump cap8_formacion_equipos

label cap8_formacion_equipos:

    scene bg jungle_player_refuge at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}La tormenta está cerca. No hay tiempo para perder.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    show erika seria at centerleft
    with Dissolve(0.5)

    b "Usemos lo que tenemos disponible. No podemos perder tiempo con medidas demasiado complejas."

    k "Si nos tomamos un momento para pensar qué queremos priorizar, podremos lograr un mejor resultado."

    hide tomas
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide bob
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)

    "{i}Es hora de poner un plan en marcha, sea el que sea.{/i}"

    menu:
        "Seguir a Bob: rapidez y adaptación con materiales disponibles.":
            $ equipo_bob = True
            jump cap8_proteccion_bob
        
        "Seguir a Erika: decidir qué queremos reforzar para enfocar los esfuerzos.":
            $ equipo_erika = True
            jump cap8_proteccion_erika

        "Proponer una alternativa, tomando parte de la idea de Bob pero integrando el entorno.":
            $ equipo_jugador_opcion1 = True
            jump cap8_proteccion_jugador_opcion1

        "Proponer una alternativa, tomando parte de la idea de Erika pero integrando el entorno.":
            $ equipo_jugador_opcion2 = True
            jump cap8_proteccion_jugador_opcion2

label cap8_proteccion_bob:

    scene bg jungle_player_refuge at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Bob lidera su estrategia con rapidez, enfocándose en usar lo disponible en lugar de perder tiempo en desarmar y armar.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    show marina triste at left
    with Dissolve(0.5)
    show charles hablando at right
    with Dissolve(0.5)

    b "No podemos quedarnos quietos midiendo cada centímetro. Tomamos lo que sirva y lo aseguramos."

    m "No soy buena trabajando tan a las apuradas."

    c "No vamos a solucionar todo, pero sí lo urgente."

    "{i}La estrategia de Bob es simple y efectiva, aunque es cierto que podría mejorar.{/i}"

    menu:
        "Tomar riesgos y acelerar el proceso.":
            y "Lo importante es todo quede mas o menos reforzado, aunque no sea perfecto."

            b "Esa es la actitud. Mejor cubrir todo a enfocarse en unas pocas cosas."

            "{i}Algunos dudan de la eficacia del proceso, pero siguen adelante.{/i}"

        "Asegurar bien los materiales antes de actuar.":            
            y "Si lo hacemos mal, puede ser peor."

            m "Finalmente alguien lo nota."

            "{i}El proceso es más lento, pero el resultado parece más confiable.{/i}"        

        "Imponerse y dirigir más activamente.":
            $ liderazgo += 1
            y "Será mejor poner un poco de orden. Demasiada improvisación es una receta para el desastre."

            c "Wow, alguien al fin apuesta al balance."

            "{i}El grupo se ajusta a la nueva dinámica, pero a algunos les cuesta un poco.{/i}"

    "{i}El resultado no es el mejor, pero en general, el refugio está un poco más protegido.{/i}"

    hide charles
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide bob
    with Dissolve(0.5)    

    jump cap8_finalizacion_proteccion

label cap8_proteccion_erika:

    scene bg jungle_player_refuge at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Erika lidera su estrategia con precisión. Cada decisión es calculada para evitar errores que puedan costar caro.{/i}"

    show erika seria at centerleft
    with Dissolve(0.5)
    show tomas serio at right
    with Dissolve(0.5)
    show laura preocupada at left
    with Dissolve(0.5)

    k "Si aseguramos cada punto crítico, podemos reducir el impacto de la tormenta."

    t "Esperemos que funcione. No tendremos segunda oportunidad."

    l "Con calma y precisión, podríamos evitar desastres."

    "{i}La estrategia de Erika es eficiente, pero podría ser un poco menos lenta.{/i}"

    menu:
        "Seguir estrictamente las mediciones de Erika.":
            "No podemos darnos el lujo de errores aquí."

            k "Exacto. Cada centímetro cuenta."

            "{i}El proceso es más lento, pero más seguro.{/i}"

        "Acelerar el proceso y asegurarlo sobre la marcha.":
            "Si tardamos demasiado, la tormenta nos golpeará sin preparación."

            t "Siempre y cuando no desarme lo que ya tenemos."

            "{i}La estructura queda lista, pero hay dudas sobre su resistencia.{/i}"        

        "Imponerse y tomar decisiones activas.":
            $ liderazgo += 1
            "Si seguimos dudando, la tormenta decidirá por nosotros."

            t "Si tiene razón, debemos asegurarnos de terminar el trabajo, no solo que quede bien."

            "{i}Algunos celebran la iniciativa, pero otros dudan.{/i}"

    "{i}El resultado no es el mejor, pero en general, el refugio está un poco más protegido.{/i}"

    hide tomas
    with Dissolve(0.5)   
    hide laura
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)

    jump cap8_finalizacion_proteccion

label cap8_proteccion_jugador_opcion1:

    scene bg jungle_player_refuge at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}El jugador plantea una alternativa propia para reforzar el refugio, basada en el entorno y los recursos disponibles.{/i}"

    if refugio == "cabaña":
        "{i}La cabaña es resistente, pero el techo podría ceder. Se necesita una estructura de soporte adicional.{/i}"

        show marina triste at left
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)

        m "Si reforzamos el techo con troncos, podríamos evitar un colapso."

        t "Podría funcionar, pero tiene que estar bien asegurado."

    elif refugio == "cueva":
        "{i}La cueva ofrece protección contra el viento, pero podría inundarse si la lluvia es intensa.{/i}"
        "{i}Se necesitan barreras para desviar el agua.{/i}"

        show laura preocupada at left
        with Dissolve(0.5)
        show charles hablando at right
        with Dissolve(0.5)

        l "Podríamos construir canales para dirigir el agua fuera."

        c "Debemos tener cuidado. Si la barrera cede, será una catástrofe."

    elif refugio == "colina":
        "{i}El claro en la colina ofrece visibilidad, pero está completamente expuesto.{/i}"
        "{i}Se necesita asegurar refugios individuales y bloquear el viento.{/i}"

        show ingrid cintura at left
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)

        i "Podríamos usar mantas y estructuras improvisadas para frenar el impacto del viento."

        t "Si logramos hacerlo bien, podríamos evitar que todo vuele."

    "{i}El jugador puede decidir cómo abordar la ejecución.{/i}"

    menu:
        "Tomar riesgos y avanzar rápido con lo disponible.":
            "Lo importante es que todo quede mas o menos reforzado, aunque no sea perfecto."

            "{i}El grupo se mueve rápido, pero la fiabilidad del plan es incierta.{/i}"

        "Asegurar cada paso antes de avanzar.":
            "No podemos permitirnos errores aquí."

            "{i}El proceso es más lento, pero más seguro.{/i}"        

        "Imponerse y tomar el liderazgo.":
            $ liderazgo += 1
            "Debemos trabajar rápido, pero también debemos trabajar bien."

            "{i}El liderazgo es bienvenido por algunos, pero agarra a otros por sorpresa.{/i}"

    "{i}El resultado no es el mejor, pero en general, el refugio está un poco más protegido.{/i}"

    hide tomas
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)    

    jump cap8_finalizacion_proteccion

label cap8_proteccion_jugador_opcion2:

    scene bg jungle_player_refuge at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}El jugador propone otra alternativa basada en los puntos críticos del refugio. Algunos dudan, pero otros apoyan la idea.{/i}"

    if refugio == "cabaña":
        "{i}La cabaña tiene buena estructura, pero los soportes pueden debilitarse.{/i}"
        "{i}Desarmando algunas secciones periféricas, podemos reforzar la habitación principal.{/i}"

        show tomas serio at right
        with Dissolve(0.5)
        show charles hablando at left
        with Dissolve(0.5)

        t "Podemos tomar los troncos del deck y usarlos para distribuir mejor la carga en las columnas que sostienen el techo."

        c "Solo espero que no se derrumbe todo mientras lo hacemos."

    elif refugio == "cueva":
        "{i}La cueva es estable, pero el suelo es húmedo. Se deben levantar plataformas para evitar filtraciones y mejorar la estabilidad.{/i}"

        show marina triste at left
        with Dissolve(0.5)
        show laura preocupada at right
        with Dissolve(0.5)

        m "Si ponemos piedras grandes en las áreas críticas, podríamos prevenir el deslizamiento."

        l "Podría funcionar, aunque dependerá del suelo."

    elif refugio == "colina":
        "{i}El claro en la colina ofrece visibilidad, pero es vulnerable. Se deben construir barreras de madera y roca para frenar el viento.{/i}"

        show ingrid seria at left
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)

        i "Si elevamos barreras estratégicas, podríamos reducir el impacto del viento."

        t "Siempre y cuando tengamos suficiente material para hacerlo bien."

    "{i}Es momento de decidir cómo ejecutar la estrategia.{/i}"

    menu:
        "Tomar riesgos y avanzar rápido con lo disponible.":
            "Lo importante es que todo quede mas o menos reforzado, aunque no sea perfecto."

            "{i}El grupo se mueve rápido, pero la fiabilidad del plan es incierta.{/i}"

        "Asegurar cada paso antes de avanzar.":
            "No podemos permitirnos errores aquí."

            "{i}El proceso es más lento, pero más seguro.{/i}"        

        "Imponerse y tomar el liderazgo.":
            $ liderazgo += 1
            "Debemos trabajar rápido, pero también debemos trabajar bien."

            "{i}El liderazgo es bienvenido por algunos, pero agarra a otros por sorpresa.{/i}"

    "{i}El resultado no es el mejor, pero en general, el refugio está un poco más protegido.{/i}"

    hide tomas
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5) 

    jump cap8_finalizacion_proteccion

label cap8_finalizacion_proteccion:

    hide bob
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide tomas
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)

    scene bg jungle_player_refuge at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Las últimas horas han sido intensas.{/i}"
    "{i}El esfuerzo por dejar las diferencias de lado, sumado al cansancio del trabajo, deja a todos agotados.{/i}"

    if equipo_bob:
        "{i}La estrategia de Bob logró reforzar lo esencial con rapidez, pero algunos dudan de la estabilidad de ciertas áreas.{/i}"
        
        show bob parado serio at centerright
        with Dissolve(0.5)
        show erika seria at centerleft
        with Dissolve(0.5)
        show charles hablando at left
        with Dissolve(0.5)

        c "Bueno, al menos tenemos algo."

        k "Si se cae después, no digas que no te avisé."

        b "Hicimos lo que teníamos que hacer."

    if equipo_erika:
        "{i}El plan de Erika siguió cada cálculo con precisión, pero la lentitud no permitió cubrir todas las áreas completamente.{/i}"
        
        show erika seria at centerleft
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)
        show laura preocupada at left
        with Dissolve(0.5)

        k "Sabía que lo lograríamos."

        l "Solo espero que haya sido suficiente."

        t "Seguimos el plan al pie de la letra, debería funcionar."

    if equipo_jugador_opcion1:
        "{i}La solución ejecutada por [nombre_personaje] fue bien recibida por algunos, pero otros aún dudan de su efectividad.{/i}"
        
        show marina triste at left
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)

        m "No diré que fue una mala idea, pero veremos si se mantiene."

        t "Si no cometimos fallos críticos, podría funcionar."

    if equipo_jugador_opcion2:
        "{i}La alternativa de [nombre_personaje] fue recibida con cierto escepticismo, aunque logró aplicarse.{/i}"
        
        show ingrid seria at left
        with Dissolve(0.5)
        show charles hablando at right
        with Dissolve(0.5)

        i "No era la opción más lógica, pero se llegó a algo."

        c "Y si no funciona, no tendremos que preocuparnos por mucho tiempo."
        c "¡Saldremos volando!"

    hide bob
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)
    hide laura
    with Dissolve(0.5)
    hide tomas
    with Dissolve(0.5)
    hide charles
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)

    "{i}Los últimos ajustes están hechos. La tormenta no dará más tiempo. Ahora solo queda esperar el impacto.{/i}"

    jump cap8_tormenta_golpea

label cap8_tormenta_golpea:

    scene bg jungle_storm_aftermath
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco

    show screen combined_ui

    "{i}El viento ruge, la lluvia cae con violencia. La tormenta golpea con toda su fuerza.{/i}"
    "{i}En segundos, el refugio se convierte en un caos.{/i}"

    show bob gr parado enojado at rightgr
    with Dissolve(0.5)

    b "¡Nos está desbordando! ¡Necesitamos reforzar todo ahora!"

    show erika gr enojada at leftgr
    with Dissolve(0.5)
    k "¡Si movemos lo que aseguramos antes, podríamos empeorar la situación!"

    "{i}La discusión se vuelve acalorada, mientras el refugio sigue siendo azotado.{/i}"

    menu:
        "Apoyar la decisión de Bob: improvisar rápido.":
            $ apoyo_bob += 2
            y "Tenemos que actuar antes de que la tormenta se lleve todo."

            "{i}Bob asiente con rapidez, pero Erika parece furiosa por la improvisación repentina.{/i}"

        "Apoyar la decisión de Erika: analizar la situación.":
            $ apoyo_erika += 2
            y "Si seguimos moviendo cosas sin lógica, vamos a perder más."

            "{i}Erika estudia detenidamente cada detalle de cómo la tormenta se impone sobre el refugio mientras Bob maldice por perder tiempo.{/i}"

        "Intentar mediar entre ambos, buscando equilibrio.":
            $ liderazgo += 2
            y "No podemos perder tiempo peleando. Encontremos un punto medio."

            "{i}Bob y Erika siguen frustrados, pero algunos del grupo intentan coordinarse mejor.{/i}"

    "{i}Mientras tanto, otro conflicto se desata.{/i}"

    hide bob
    with Dissolve(0.5)    
    hide erika
    with Dissolve(0.5)
    
    show laura enojada at right
    with Dissolve(0.5)

    l "¡Tenemos que asegurar no perder nada de lo que hemos conseguido con tanto esfuerzo, será esencial cuando la tormenta amaine!"

    show marina preocupada at left
    with Dissolve(0.5)      

    m "¡Las personas importan más que los recursos! ¡No podemos poner a nadie en peligro!"

    menu:
        "Apoyar a Laura: enfocarse en lo necesario para sobrevivir.":
            $ apoyo_laura += 2
            y "Si no tenemos lo básico, todo lo demás es irrelevante."
            
            "{i}Laura sigue adelante, pero Marina se frustra y se aleja.{/i}"

        "Apoyar a Marina: es imprudente arriesgar sus vidas en este vendaval.":
            $ apoyo_marina += 2
            y "No podemos arriesgarnos a perder a nadie."

            "{i}Marina se enfoca en ayudar a los demás.{/i}"
            "{i}Escuchas a Laura murmurar sobre cómo lo perderán todo.{/i}"

        "Buscar un punto medio, asegurando ambas cosas.":
            $ liderazgo += 2
            y "Podemos asegurar los recursos sin correr riesgos si nos organizamos bien."
            y "Marina, ayuda a Ingrid. Laura, vamos a poner a resguardo algo de leña. Necesitaremos calor para mantenernos secos."

            "{i}El grupo intenta coordinarse pero claramente el asunto no quedó del todo zanjado entre ellas.{/i}"

    hide laura
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)

    "{i}La tormenta se intensifica y la tensión y el estrés crecen.{/i}"
    "{i}Lo peor todavía está por venir.{/i}"

    jump cap8_crisis_personajes

label cap8_crisis_personajes:

    scene bg jungle_storm at truecenter
    with Fade(0.1, 0.4, 0.1)  # Simula un destello blanco

    show screen combined_ui

    "{i}La tormenta no da tregua. En medio del desastre, la tensión entre varios es como un barril de pólvora.{/i}"

    show ingrid enojada at left
    with Dissolve(0.5)
    show charles hablando at right
    with Dissolve(0.5)

    i "¡Si seguimos sin coordinación, esto será peor que el mismísimo naufragio!"

    c "¡Si no te gusta como trabajo, no te pongas en mi camino!"

    "{i}El enfrentamiento entre Ingrid y Charles escala rápidamente. Ambos tienen ideas opuestas sobre cómo actuar.{/i}"

    menu:
        "Apoyar a Ingrid: seguir una estrategia lógica.":
            $ apoyo_ingrid += 2
            y "Si seguimos improvisando a lo loco, todo va a fallar."

            "{i}Ingrid respira hondo, agradeciendo el respaldo. Charles maldice y se aleja.{/i}"

        "Apoyar a Charles: detenerse a pensar cada movimiento solo será peor.":
            $ apoyo_charles += 2
            y "Si seguimos trazando planes, vamos a perder el poco tiempo que tenemos."

            "{i}Charles sonríe, confiado. Ingrid aprieta los dientes, frustrada.{/i}"

        "Intentar calmar a ambos, enfocándose en el resultado.":
            $ liderazgo += 2
            y "Lo que importa es sobrevivir, no ganar discusiones."

            "{i}Ambos deciden intentar cooperar, al menos momentáneamente.{/i}"
    hide charles 
    with Dissolve(0.5)
    hide ingrid
    with Dissolve(0.5)
    pause .5

    "{i}Otro conflicto surge en el refugio.{/i}"

    show tomas serio at centerleft
    with Dissolve(0.5)

    t "¡Si esto sigue así, no quedará nada del refugio! Se está inundando todo. ¡Tal vez sea mejor que nos vayamos antes de quedar atrapados aquí!"

    show bob parado serio at centerright
    with Dissolve(0.5)

    b "Tomás, no dejes que el pánico se apodere de ti. Si salimos ahora, el viento nos va a destrozar. Quedarnos es la única opción."

    t "¿Quién dijo que yo tenía miedo? Estoy tratando de usar el sentido común, nada más."

    b "Bueno, te prometo que quedarnos aquí es lo que más sentido tiene."

    t "Está bien, pero no tienes por qué tratarme como si fuera un niño."    

    menu:
        "Apoyar a Tomás: Bob fue condescendiente con el.":
            $ apoyo_tomas += 2
            y "Bob, tal vez exageraste. Podrías haberle expresado tu opinión con más respeto."

            "{i}Bob sacude la cabeza sin aceptar la acusación y sigue trabajando en proteger el refugio.{/i}"

        "Apoyar a Bob: Tomás parecia no estar pensando con claridad.":
            $ apoyo_bob += 2
            y "Tomás, Bob solamente quiso tranquilizarte. Estabas proponiendo algo descabellado."

            "{i}Bob asiente agradeciéndote, mientras Tomás se muestra frustrado.{/i}"

        "Intentar evaluar la situación sin tomar partido.":
            $ liderazgo += 2
            y "Dejen de discutir tonterías y pónganse a trabajar. Este es el refugio que tenemos y lo protegeremos."

            "{i}Los tres retoman sus tareas, pero la tensión entre ellos dos sigue presente.{/i}"

    hide bob
    with Dissolve(0.5)
    hide tomas 
    with Dissolve(0.5)

    "{i}Cada decisión marca las posturas de cada uno en el grupo. La tormenta y las tensiones siguen intensificándose.{/i}"

    jump cap8_punto_de_quiebre

label cap8_punto_de_quiebre:

    scene bg jungle_storm at truecenter
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco

    show screen combined_ui

    "{i}El viento ruge con fuerza, la lluvia golpea en todas direcciones. El refugio está parcialmente inundado.{/i}"
    "{i}Los restos de algunas de las mejoras construídas por ustedes ahora vuelan por los aires como peligrosos proyectiles.{/i}"

    show bob parado serio at centerright
    show erika seria at centerleft
    with Dissolve(0.5)

    b "¡Esto no hubiera pasado si no hubiésemos perdido tanto tiempo!"

    k "¿Si hubiésemos seguido el plan desde el principio, quieres decir?"

    "{i}La animosidad entre Bob y Erika está en su punto más alto hasta ahora.{/i}"    

    menu:
        "Apoyar a Bob: perdimos mucho tiempo discutiendo las ideas de Erika.":
            $ apoyo_bob += 2
            y "Erika, mira nuestro refugio, volando por los aires allí fuera."
            y "Creo que quedó demostrado que había que actuar rápido desde el primer momento."

            "{i}Bob se endereza, sintiéndose validado, pero Erika rezonga entre dientes.{/i}"

        "Apoyar a Erika: solo aquello a lo que se le dedicó más planificación sigue en pié a esta altura, después de todo.":
            $ apoyo_erika += 2
            y "Bob, si aún nos queda algo, es gracias a los recaudos tomados por Erika."

            "{i}Erika asiente mientras sigue trabajando, pero Bob maldice por el tiempo perdido.{/i}"

        "Tomar control y mediar entre ambos.":
            $ liderazgo += 2
            y "Si le dedicamos muy poco tiempo a planificar, o demasiado, no lo se."
            y "Sin duda le dedicamos mucho más a escucharlos discutir que a trabajar."

            "{i}Tus palabras no parecen caerle muy bien a ninguno de los dos, pero siguen trabajando para disimularlo.{/i}"

    hide marina
    hide tomas
    hide bob 
    hide erika
    with Dissolve(0.5)

    "{i}Mientras se esfuerzan por asegurar lo poco que les queda, alguien grita una advertencia.{/i}"

    show ingrid triste at left
    with Dissolve(0.5)

    i "¡Algo se mueve afuera! ¡No estamos solos!"

    show charles hablando at right
    with Dissolve(0.5)
    c "¡Nada puede estar ahí afuera! ¡El viento es muy fuerte!"

    "{i}El viento y la lluvia apenas les permiten escuchar un trote pesado acercándose.{/i}"
    "{i}Escuchan un ronquido fuerte antes de divisar la silueta de un cuadrúpedo pesado en la entrada del refugio.{/i}"

    show bg jungle_storm_jabali at truecenter
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco

    "{i}Un jabalí se ha acercado, desorientado y agresivo. Cualquier movimiento en falso podría ser un desastre.{/i}"

    menu:
        "Intentar alejar al jabalí sin violencia.":
            $ estrategia_pacifica += 2
            y "Si logramos desviar su atención, podríamos evitar una confrontación."

            "{i}El grupo intenta auyentarlo, pero la criatura sigue inquieta.{/i}"

        "Atacar al jabalí para alejarlo por la fuerza.":
            $ estrategia_agresiva += 2
            y "Si nos quedamos quietos, podría ser peor."

            "{i}Los personajes reaccionan con rapidez, armándose con lo que pueden, pero nadie se anima a dar el primer paso.{/i}"

        "No hacer nada y observar su reacción.":
            $ estrategia_pasiva += 2
            y "Quizás no nos haya detectado aún."

            "{i}Todos dejan lo que están haciendo y se agachan, tratándo de esconderse. La duda es visible en los rostros de algunos.{/i}"
    
    show bg jungle_storm_jabali at truecenter
    with Fade(0.1,0.4,0.1)  # Simula un destello blanco
    "{i}El destello de un relámpago cercano los enceguece de repente y segundos mas tarde llega un trueno ensordecedor.{/i}"
    show bg jungle_storm_jabali at truecenter
    with Fade(0.1, 0.4, 0.1)  # Simula un destello blanco
    "{i}Escuchan nuevamente el pesado trote, esta vez alejándose. El ruido lo asustó y salió corriendo jungla adentro.{/i}"
    hide ingrid
    hide charles
    with Dissolve(0.5)
    "{i}La tormenta sigue intensificándose. Aquello que no vuela por los aires, está flotando en corrientes de agua que se van formando con la lluvia.{/i}"
    "{i}Llega un punto en el que lo único que pueden hacer es acurrucarse en un rincón de lo que queda del refugio para darse algo de calor entre todos.{/i}"

    show bg jungle_storm_jabali at truecenter
    with Fade(0.1, 0.4, 0.1)  # Simula un destello blanco
    pause 2.0
    "{i}Tras lo que parecen ser horas, la tormenta amaina y una extraña calma se apodera de la isla.{/i}"

    jump cap8_enfrentamiento_lideres

label cap8_enfrentamiento_lideres:

    scene bg jungle_aftermath_storm at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}La tormenta podrá haber terminado, pero en el refugio, se cocina otro tipo de tormenta.{/i}"
    show bob parado hablando at right
    with Dissolve(0.5)
    show erika enojada at centerleft
    with Dissolve(0.5)
    b "¡Esto fue un desastre! ¿Cuántas veces lo dije? Necesitábamos actuar rápido. En vez de eso, no paramos de perder tiempo."

    k "Lo que nos puso en peligro fue que a ti se te dió por hacer las cosas a lo loco."
    k " Si hubiésemos trabajado todos reforzando el refugio de forma ordenada y planificada, la tormenta no habría sido una amenaza."

    "{i}Ambos se miran con furia contenida. Nadie está dispuesto a ceder.{/i}"

    show tomas serio at left
    with Dissolve(0.5)

    t "(en voz baja) Esto ya no es una discusión..."

    show bob parado enojado at centerright
    with Dissolve(0.5)

    "{i}Bob da un paso hacia adelante, sin apartar la mirada de Erika.{/i}"

    b "Mira los daños. Fijate en las provisiones que perdimos, en cómo el refugio quedó al borde del colapso."
    b "Si hubiésemos explorado antes de que la tormenta comenzara, al tendríamos como recuperarnos."

    k "¿Explorar antes? ¿Cuánto tiempo pasó desde que lo propusiste hasta que se desató la tormenta?"
    k "Habrías quedado varado en medio del desastre, y habrías arrastrado a otros contigo."

    hide tomas
    with Dissolve (0.5)

    "{i}Bob te mira, buscando tu apoyo.{/i}"

    b "Tú que opinas. ¿No creés que la exploración nos habría dado una ventaja antes del desastre?"

    menu:
        "Sí, deberíamos haber hecho una recorrida rápida al menos.":
            $ apoyo_lider_bob += 2
            "{i}Bob asiente con la cabeza, gesticulando con las manos lo obvio de su argumento. Erika las levanta en el aire, exasperada.{/i}"

        "No, quedarse juntos era la mejor opción. El refugio demandaba nuestra atención urgente":
            $ apoyo_lider_erika += 2
            "{i}Erika exhala con un dejo de alivio. Bob resopla.{/i}"

        "¿Qué importa qué hubiese sido mejor?":
            "{i}Bob y Erika intercambian una mirada, sorprendidos.{/i}"

    "{i}La discusión sigue escalando, pero Erika cambia de estrategia.{/i}"

    k "Hubo otro problema que ignoraste, Bob. Ninguno de nosotros tiene entrenamiento para situaciones como ésta."
    k "No estamos acostumbrados, y si además de eso, no estamos organizados, el caos es inevitable."

    b "Si hubiesen confiado en mi desde el principio, yo me habría encargado de que no llegáramos a esto."

    k "¿De verdad creés que liderar es solo asegurarte que confíen en lo que tú le digas al grupo?"
    k "Tú también deberías confiar en aquellos a los que pretendes liderar, Bob. Yo lo hago."

    "{i}Ahora Erika se gira hacia ti. Esta vez, espera tu opinión.{/i}"

    menu:
        "La confianza es clave para la prosperidad decualquier grupo, Erika tiene razón":
            $ apoyo_lider_erika += 2
            "{i}Erika sonríe aliviada.{/i}"
            k "Al menos alguien entiende lo que significa trabajar con otras personas."

        "En situaciones como esta, saber seguir órdenes puede ser de vida o muerte.":
            $ apoyo_lider_bob += 2
            "{i}Bob suelta una risa seca. Finalmente, alguien que entiende que en una urgencia las cosas son distintas.{/i}"

        "Ambos se enfocaron más en tener razón que en tener éxito.":
            "{i}Hay un largo silencio. Erika y Bob cruzan miradas, sin saber bien cómo procesar tu respuesta.{/i}"

    "{i}Las palabras han sido dichas. Ahora todo se reduce a una única pregunta: ¿Quién liderará el grupo después de esto?{/i}"

    jump cap8_eleccion_liderazgo

label cap8_eleccion_liderazgo:

    scene bg jungle_division_decision at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}El grupo está fragmentado. Nadie quiere admitirlo, pero la separación del grupo es inevitable.{/i}"

    show bob parado serio at left
    show erika parada at right
    with Dissolve(0.5)

    "{i}Bob y Erika miran a todos y esperan para ver quién está con quién.{/i}"

    menu:
        "Apoyar a Bob como líder":
            y "Más allá de todo, Bob desde el principio se ha esforzado porque todos nos salvemos."
            y "Está claro que no van a ponerse de acuerdo, pero yo estoy con el."
            $ apoyo_lider_bob += 3
            "{i}Bob exhala con alivio y asiente.{/i}"
            jump cap8_dialogo_lider_bob

        "Apoyar a Erika como líder":
            y "En muy poco tiempo, Erika a dejado una muy buena impresión en mi."
            y "Y como parece que la ruptura es inevitable... Bob, lamento decirte que yo estoy con ella."
            $ apoyo_lider_erika += 3
            "{i}Erika cruza los brazos con firmeza.{/i}"
            jump cap8_dialogo_lider_erika

        "Tomar el liderazgo":            
            $ apoyo_lider_jugador += 3
            $ jugador_es_lider = True
            y "Erika, Bob, yo estoy cansado de que el resto de nosotros esté a la merced de sus diferencias irreconciliables."
            "{i}Las miradas de todos se centran en ti.{/i}"
            "{i}Para convertirte en líder tu próximo movimiento debe ser convencer a uno de ellos de que te siga.{/i}"
            "{i}Eso fortalecerá tu posición frente a los demás.{/i}"

            menu:
                "Intentar que Bob te siga":
                    if apoyo_lider_bob >= 0:
                        y "Aquellos que piensen lo mismo, vengan conmigo."
                        y "Bob, me gustaría que te nos unas, pero esta vez seré yo quien lidere."
                        "{i}Bob te observa, duda por un segundo, pero finalmente acepta.{/i}"
                        $ grupo_jugador.append("bob")
                    else:
                        "{i}Bob niega con la cabeza. No confía en tu liderazgo.{/i}"
                        "{i}Miras a Erika para ver si está interesada.{/i}"
                        k "Pfff... Prefiero seguirte a ti antes que liderar un grupo en el que esté el."
                        $ grupo_jugador.append("erika")

                "Intentar que Erika se una a tu grupo":
                    if apoyo_lider_erika >= 0:
                        y "Aquellos que piensen lo mismo, vengan conmigo."
                        y "Erika, me gustaría que te nos unas, pero no se si estás dispuesta a trabajar bajo el liderazgo de otra persona."
                        "{i}Erika frunce el ceño, pero finalmente accede con reticencia.{/i}"
                        $ grupo_jugador.append("erika")
                    else:
                        "{i}Erika se cruza de brazos y sacude la cabeza. No está dispuesta a seguirte.{/i}"
                        b "Yo estoy dispuesto a darte una chance como líder, si tu me das una chance de seguirte."
                        "{i}Bob y tú se miran. No sabes si es sincero o si quiere asegurarse de no estar bajo el liderazgo de Erika en el otro grupo.{/i}"
                        y "Está bien, Bob. Puedes venir con nosotros."
                        $ grupo_jugador.append("bob")

    hide bob
    with Dissolve (0.5)
    hide erika
    with Dissolve (0.5)

    "{i}Las decisiones están tomadas. Ahora cada persona debe decidir con quién quedarse.{/i}"

    jump cap8_formacion_grupos_finales

label cap8_dialogo_lider_bob:

    "{i}Bob te observa con una mirada firme.{/i}"

    b "Si estás conmigo, tenemos que hacer las cosas bien. No más indecisiones, no más pérdidas de tiempo. ¿Estás listo para eso?"

    menu:
        "Sí, hay que actuar rápido":
            "{i}Bob sonríe, contentos de que estén en la misma página.{/i}"

        "No siempre hay que apresurarse":
            "{i}Bob frunce el ceño, pero decide no discutirlo ahora.{/i}"

    "{i}El grupo empieza a separarse y cada persona se posiciona junto a Erika o junto a Bob.{/i}"

    jump cap8_formacion_grupos_finales

label cap8_dialogo_lider_erika:

    "{i}Erika te observa con atención, como analizando tu respuesta.{/i}"

    k "Si vas a estar en mi grupo, habrá reglas. Todo tiene que estar bien planeado. No podemos repetir los errores que nos trajeron aquí."

    menu:
        "Estoy de acuerdo, el orden es clave":
            "{i}Erika asiente, satisfecha.{/i}"

        "El orden es importante, pero también hay que saber adaptarse":
            "{i}Erika suspira. No te dice nada por ahora, pero se nota que se queda con las ganas.{/i}"

    "{i}El grupo empieza a separarse y cada persona se posiciona junto a Erika o junto a Bob.{/i}"

    jump cap8_formacion_grupos_finales

label cap8_formacion_grupos_finales:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)
    with Dissolve(0.5)

    "{i}Los grupos están definidos. Ahora cada uno debe decidir su camino.{/i}"

    python:
        personaje_indeciso = "ingrid"

        for personaje in ["tomas", "marina", "charles", "laura"]:
            if getattr(store, f"apoyo_{personaje}", 0) > 2:
                grupo_jugador.append(personaje)
            elif apoyo_lider_bob > apoyo_lider_erika:
                grupo_bob.append(personaje)
            else:
                grupo_erika.append(personaje)

        # Ajustar equilibrio de grupos
        if len(grupo_jugador) < 3:
            personaje_cambio = grupo_bob[-1] if len(grupo_bob) > len(grupo_erika) else grupo_erika[-1]
            grupo_jugador.append(personaje_cambio)
            grupo_bob.remove(personaje_cambio) if personaje_cambio in grupo_bob else grupo_erika.remove(personaje_cambio)

    "{i}Los personajes aparecen uno por uno.{/i}"

    python:
        personaje_anterior = None

        for personaje in grupo_jugador + grupo_bob + grupo_erika:

            personaje_img = f"{personaje} grupo"

            if personaje_anterior:
                renpy.hide(f"{personaje_anterior} grupo", layer="master")
                renpy.with_statement(Dissolve(0.5))

            renpy.show(personaje_img, at_list=[Position(xalign=0.5)], layer="master")
            renpy.pause(0.5)

            if personaje in grupo_jugador:
                mensaje_decision = f"{personaje} decide quedarse contigo."
                nueva_posicion = 0.2
            else:
                mensaje_decision = f"{personaje} decide irse con el otro grupo."
                nueva_posicion = 0.8

            renpy.pause(1.5)
            renpy.say("", mensaje_decision)

            renpy.show(personaje_img, at_list=[Position(xalign=nueva_posicion)], layer="master")
            renpy.pause(0.5)

            personaje_anterior = personaje

    "{i}El último personaje, Ingrid, duda por un momento.{/i}"

    show ingrid seria at center
    with Dissolve(0.5)

    menu:
        "Intentar convencer a Ingrid de quedarse":
            y "Ingrid, después de todo lo que pasamos juntos, ¿vamos a separarnos?"
            if getattr(store, "apoyo_ingrid", 0) > 2:
                "{i}Después de una larga pausa, Ingrid acepta, pero su expresión muestra incertidumbre.{/i}"
                python:
                    grupo_jugador.append("ingrid")
                    renpy.show("ingrid seria", at_list=[Position(xalign=0.2)], layer="master")
                    renpy.pause(0.5)
            else:
                "{i}Ingrid sacude la cabeza. No puede cambiar su decisión.{/i}"
                python:
                    renpy.show("ingrid seria", at_list=[Position(xalign=0.8)], layer="master")
                    renpy.pause(0.5)

        "Dejar que tome su decisión":
            "{i}Ingrid respira hondo y finalmente se aleja, pero antes de irse, te mira una última vez.{/i}"
            python:
                renpy.show("ingrid seria", at_list=[Position(xalign=0.8)], layer="master")
                renpy.pause(0.5)

    "{i}Los grupos están formados. No hay vuelta atrás.{/i}"
    jump mostrar_grupo_jugador

label mostrar_grupo_jugador:

    python:
        posiciones_restantes = [centerleft, centerright, right]  # Tus transforms definidos
        personaje_left = None

        # Determinar si Bob o Erika están en el grupo del jugador
        for posible_lider in ["bob", "erika"]:
            if posible_lider in grupo_jugador:
                personaje_left = posible_lider
                break

        # Ocultar todos por si ya estaban en pantalla
        for p in grupo_jugador:
            renpy.hide(f"{p} grupo", layer="master")

        # Mostrar personaje principal en left
        if personaje_left:
            renpy.show(f"{personaje_left} grupo", at_list=[left], layer="master")

        # Mostrar el resto en las posiciones restantes
        otros = [p for p in grupo_jugador if p != personaje_left]
        for idx, personaje in enumerate(otros):
            if idx < len(posiciones_restantes):
                transform_actual = posiciones_restantes[idx]
                renpy.show(f"{personaje} grupo", at_list=[transform_actual], layer="master")

    jump continuar

label cap8_end:
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
        # show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el segmento 2, el grupo ha pasada una dura prueba. La tormenta ha pasado pero la isla tiene peligros acechando en la jungla."
        "Ha llegado el momento de considerar que quizás no haya ningún equipo de rescate aún buscando."
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        # hide screen decisiones_popup with dissolve
        jump continuar

label continuar:
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                #jump segment_2_end
                jump chapter_9_start
            "VOLVER A VER EL RESÚMEN":
                jump continuar
                #jump chapter_8_end

label segment_2_end:
    # prueba de enviar reporte
    $ enviar_reporte(player_id)
    "El reporte fue enviado con exito!"
    call pedir_codigo_capitulo from _call_pedir_codigo_capitulo_3
    jump chapter_9_start
 
return

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# ACA TERMINA SEGMENTO 2                                         |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

###################################################################################  ####   #####   #########################################################
###################################################################################  #######  ##  ######################################################################
## Aca comienza la PARTE 9 ########################################################  #######  ##  #################################################################
###################################################################################  #####   ####   #################################################################

label chapter_9_start:
    "Aca comienza el segmento 3"
    $ persistent.cantidad_capitulos +=1
    jump cap9_hallazgo_huerta

label cap9_hallazgo_huerta:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)

    show screen combined_ui

    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}La vegetación se hace más densa a medida que avanzan. Las hojas crujen bajo las botas húmedas y las ramas crujen sobre sus cabezas.{/i}"
    "{i}Las últimas lluvias han empapado el suelo y desplazado raíces viejas, dejando un aroma terroso en el aire.{/i}"

    $ choice_position = "default"  # default alta superior
    menu:
        "Proponés separarse brevemente para cubrir más terreno.":
            $ decision_busqueda = "separarse"
            "Divididos en parejas, avanzan bordeando la maleza con cuidado. Cada rincón oculto se vuelve una promesa."

        "Proponés buscar indicios de plantas comestibles, observando patrones de sombra y suelo.":
            $ decision_busqueda = "planta_comestible"
            "Con ojos atentos al suelo y la vegetación baja, buscás hojas que reconozcas. En un claro inesperado, algo te llama la atención."

        "Te subís a un árbol para observar la zona desde la altura.":
            $ decision_busqueda = "subir_arbol"
            "Escalás con cuidado la corteza húmeda. Desde la copa distinguís un punto donde el follaje se abre: una silueta de platanales dorados en el centro."

    "{i}Con diferentes trayectorias, pero con igual sorpresa, todos convergen en el mismo lugar: un claro amplio y fértil cubierto de árboles frutales y surcos cubiertos de vegetales silvestres.{/i}"

    if "ingrid" in grupo_jugador:
        show ingrid feliz at center
        with Dissolve(0.5)

        if ingrid > 2:
            i "¡Esto parece un regalo... o un milagro. Si estás conmigo, todo parece posible."
        elif ingrid < -2:
            i "Hasta este lugar tiene mejor clima que tu últimamente. Pero sí, parece útil."
        else:
            i "Esto es lo mejor que vimos desde que llegamos. ¿Qué hacemos primero?"

        hide ingrid with Dissolve(0.5)

    elif "bob" in grupo_jugador:
        show bob sorprendido at center
        with Dissolve(0.5)
        b "Nunca pensé que encontraríamos algo así. Es un milagro... o una trampa. Pero hay que moverse."
        hide bob with Dissolve(0.5)

    elif "erika" in grupo_jugador:
        show erika seria at center
        with Dissolve(0.5)
        e "Este lugar fue trabajado. Alguien cultivó esto. No fue el viento."
        hide erika with Dissolve(0.5)

    "Mientras inspeccionan los márgenes, algunos del grupo encuentran piedras dispuestas en línea recta, maderas cortadas, herramientas oxidadas."
    "Hay una pala sin mango, un barril inclinado contra un árbol, raíces que crecieron sobre antiguos surcos de cultivo."

    "{i}No hay duda. Alguien vivió aquí hace tiempo. Plantó, cuidó... y lo abandonó.{/i}"

    jump cap9_aparicion_jabali

label cap9_aparicion_jabali:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)

    "{i}El grupo empieza a recolectar fruta con entusiasmo contenido. Algunos llenan mochilas, otros trepan ramas bajas para alcanzar los frutos más altos.{/i}"

    if "charles" in grupo_jugador:
        show charles alerta at center
        with Dissolve(0.5)
        c "Shhh… ¿Escucharon eso?"
        hide charles with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika alerta at center
        with Dissolve(0.5)
        e "Silencio. Hay algo grande moviéndose entre los matorrales."
        hide erika with Dissolve(0.5)
    elif "bob" in grupo_jugador:
        show bob alerta at center
        with Dissolve(0.5)
        b "Eso no es viento. ¡Cuidado!"
        hide bob with Dissolve(0.5)

    "{i}Un estruendo entre los arbustos. Ramas rotas. Una figura oscura emerge entre la sombra: un jabalí gigantesco, cubierto de barro, resoplando con furia.{/i}"
    "{i}Embiste sin aviso. Una mochila sale volando. Todos corren en distintas direcciones entre gritos y frutas esparcidas por el suelo.{/i}"

    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Después de unos minutos de caos, logran reagruparse varios metros más allá, jadeando.{/i}"

    if "ingrid" in grupo_jugador:
        show ingrid alterada at center
        with Dissolve(0.5)
        i "No podemos dejar ese lugar así... ¿Viste lo que había ahí? Tenemos que encontrar la forma de volver."
        hide ingrid with Dissolve(0.5)

    $ choice_position = "default"  # default alta superior
    menu:
        "Proponés retroceder, reagruparse y armar un plan":
            $ decision_inicial_jabali = "precaucion"
            "La idea de volver sin pensar no convence a nadie. Deciden reagruparse, analizar el terreno... y pensar con estrategia."

        "Proponés volver rápidamente a recuperar lo posible antes de que el animal regrese":
            $ decision_inicial_jabali = "impulsivo"
            "Algunos dudan, pero aceptan tu impulso. Avanzan... solo para ver al jabalí aún merodeando, rascando el suelo con sus colmillos."

        "Proponés observar desde una distancia segura y estudiar el comportamiento del jabalí":
            $ decision_inicial_jabali = "observacion"
            "Desde un claro oculto tras ramas bajas, observan. El animal parece haberse apropiado del espacio como si fuera suyo."

    "Sea cual sea el enfoque inicial, una conclusión se impone con urgencia: {i}si quieren esa comida, tendrán que sacar al jabalí de allí.{/i}"

    jump cap9_discusion_planes

label cap9_discusion_planes:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)
    show screen combined_ui

    "{i}Una vez alejados del claro, aún agitados por el susto, los miembros del grupo empiezan a discutir alternativas para recuperar el acceso al huerto.{/i}"
    "El jabalí no parece dispuesto a ceder el terreno. Pero tampoco ustedes."

    # Propuesta de plan conservador
    if "laura" in grupo_jugador:
        show laura pensativa at center
        with Dissolve(0.5)
        l "Podríamos colgar trapos con savia amarga o ceniza alrededor. Eso repele a muchos animales."
        hide laura with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika pensativa at center
        with Dissolve(0.5)
        e "Podríamos improvisar una barrera de olores fuertes. Es poco confiable… pero quizás funcione."
        hide erika with Dissolve(0.5)
    elif "bob" in grupo_jugador:
        show bob serio at center
        with Dissolve(0.5)
        b "Si marcamos el área con cenizas y orina, puede que el animal lo evite un tiempo. Puede funcionar."
        hide bob with Dissolve(0.5)

    # Propuesta de plan más complejo
    if "charles" in grupo_jugador:
        show charles serio at center
        with Dissolve(0.5)
        c "Podemos atraerlo con fruta hacia otro punto y bloquearle la vuelta con troncos inclinados. Pero va a ser riesgoso."
        hide charles with Dissolve(0.5)
    elif "bob" in grupo_jugador:
        show bob decidido at center
        with Dissolve(0.5)
        b "Un desvío con recompensa. Si lo guiamos bien y trabajamos rápido, podríamos encerrarlo sin lastimarlo."
        hide bob with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika concentrada at center
        with Dissolve(0.5)
        e "Diseñar un corredor natural con obstáculos. Suena ambicioso, pero si lo hacemos bien, sería definitivo."
        hide erika with Dissolve(0.5)

    "{i}Pero antes de decidir una estrategia concreta, surge la gran pregunta: ¿Deberían avisarle al otro grupo?{/i}"

    $ choice_position = "default"  # default alta superior
    menu:
        "Proponés compartir el hallazgo con el otro grupo":
            $ compartir_con_otro_grupo = True
            "Murmullos. Algunas miradas cruzadas. Pero tu tono firme disipa la duda. Nadie quiere una guerra por frutas."

        "Preferís resolverlo sin avisarles nada":
            $ compartir_con_otro_grupo = False
            "{i}El grupo te escucha en silencio. Es egoísta, quizás. Pero también práctico. Al menos por ahora... este problema es de ustedes.{/i}"

    # Reacción de personajes al dilema ético
    if "marina" in grupo_jugador:
        show marina preocupada at center
        with Dissolve(0.5)
        if compartir_con_otro_grupo:
            m "Tal vez esto nos ayude a recomponer un poco... No podemos vivir divididos para siempre, ¿no?"
        else:
            m "¿Y si lo descubren? No quiero que esto estalle más de lo que ya está."
        hide marina with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika neutral at center
        with Dissolve(0.5)
        if compartir_con_otro_grupo:
            e "Si los incluimos, tendremos que negociar cada paso. Pero quizás sea lo más inteligente."
        else:
            e "Mejor resolverlo primero. Luego vemos cómo compartir los frutos, no el lío."
        hide erika with Dissolve(0.5)
    elif "bob" in grupo_jugador:
        show bob serio at center
        with Dissolve(0.5)
        if compartir_con_otro_grupo:
            b "Tarde o temprano lo iban a saber. Mejor que sea ahora, con la voz tranquila."
        else:
            b "Bien. Por una vez, tenemos algo antes que ellos. Aprovechémoslo."
        hide bob with Dissolve(0.5)

    "Decisión tomada. Es hora de elegir cómo resolver el problema de los jabalíes."

    jump cap9_eleccion_estrategia

label cap9_eleccion_estrategia:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)
    show screen combined_ui

    "{i}Con el grupo atento, se presentan dos planes concretos para lidiar con el jabalí... o los jabalíes.{/i}"

    "Plan A: preparar una cerca con troncos inclinados, crear un corredor con frutas y redirigir al animal a un sector alejado del huerto. Es ambicioso y peligroso, pero puede funcionar a largo plazo."

    "Plan B: improvisar un perímetro con trapos, cenizas, plantas amargas y marcas olfativas que disuadan al animal. Más seguro, pero poco confiable con el tiempo."

    if jugador_es_lider:

        if "erika" in grupo_jugador:
            show erika seria at center
            with Dissolve(0.5)
            e "Hay que decidir ya. Tu tiens la última palabra."
            hide erika with Dissolve(0.5)
        elif "bob" in grupo_jugador:
            show bob serio at center
            with Dissolve(0.5)
            b "La gente te va a seguir, como sea. Así que asegurate de elegir bien."
            hide bob with Dissolve(0.5)

        $ choice_position = "default"
        menu:
            "Elegís el plan de desvío y bloqueo con trampa natural":
                $ plan_elegido = "bloqueo"

                "{i}Asentís con convicción. El grupo empieza a discutir cómo guiar al jabalí. Será riesgoso... pero puede funcionar.{/i}"

            "Preferís la opción más conservadora: trapos y ceniza como repelente":
                $ plan_elegido = "repelente"

                if "erika" in grupo_jugador:
                    show erika critica at center
                    with Dissolve(0.5)
                    e "Eso no va a durar. Ya lo intenté en el campo... y volvió con más hambre."
                    hide erika with Dissolve(0.5)
                elif "bob" in grupo_jugador:
                    show bob molesto at center
                    with Dissolve(0.5)
                    b "¿En serio? ¿Esperás que un trapo asuste a una bola de músculo y colmillos?"
                    hide bob with Dissolve(0.5)

                "{i}A pesar de tu decisión, los demás insisten y terminan inclinándose por el plan de desvío. Tu liderazgo, por ahora, es puesto en duda sutilmente.{/i}"
                $ plan_elegido = "bloqueo"

    else:  # jugador no es líder

        if "erika" in grupo_jugador:
            show erika decidida at center
            with Dissolve(0.5)
            e "Yo voto por atraerlo. Si nos organizamos, no hay riesgo mayor."
            hide erika with Dissolve(0.5)

        if "bob" in grupo_jugador:
            show bob crítico at center
            with Dissolve(0.5)
            b "Prefiero no ponerme a jugar con bestias. Con los trapos alcanza para ganar tiempo."
            hide bob with Dissolve(0.5)

        "{i}Los líderes del grupo no se ponen de acuerdo. Te miran. Tu voto será decisivo.{/i}"

        $ choice_position = "default"
        menu:
            "Apoyás el plan más ambicioso de desvío y bloqueo":
                $ voto_jugador = "bloqueo"
                "{i}Tu voz inclina la balanza. Inmediatamente se organizan para ejecutar el desvío. Empieza la planificación.{/i}"
                $ plan_elegido = "bloqueo"

            "Te inclinás por la estrategia más conservadora con trapos y cenizas":
                $ voto_jugador = "repelente"

                if "erika" in grupo_jugador:
                    show erika fastidiada at center
                    with Dissolve(0.5)
                    e "No puedo creer que tengan tanto miedo a pensar en grande."
                    hide erika with Dissolve(0.5)

                if "bob" in grupo_jugador:
                    show bob satisfecho at center
                    with Dissolve(0.5)
                    b "Pensás en el grupo. Me gusta eso."
                    hide bob with Dissolve(0.5)

                "{i}Pero a medida que el grupo evalúa la viabilidad, las dudas aparecen... y terminan optando por el plan de desvío y bloqueo, que resulta más consistente.{/i}"
                $ plan_elegido = "bloqueo"

    "El plan está definido. Pero requiere precisión. Separarse. Actuar rápido. Cooperar."

    jump cap9_formacion_equipos

label cap9_formacion_equipos:

    scene bg formacion_grupos with fade
    show screen combined_ui

    "Cada grupo requiere concentración total y trabajo coordinado. Las tareas se reparten, pero vos tenés la posibilidad de elegir en cuál querés estar."

    $ choice_position = "default"
    menu:
        "Distraer al jabalí con señuelos y ruido (riesgo alto)":
            $ grupo_jugador_elegido = 1
            $ reporte_toma_iniciativa_jabali = True
            "Elegís el riesgo. Te toca mover al jabalí y sobrevivir al intento."

        "Recolectar fruta y trazar el recorrido del desvío (riesgo medio)":
            $ grupo_jugador_elegido = 2
            $ reporte_equilibrio_operativo = True
            "Elegís el camino intermedio. Coordinación y agilidad serán clave."

        "Construir la barrera con troncos y ramas (esfuerzo físico, bajo riesgo)":
            $ grupo_jugador_elegido = 3
            $ reporte_evita_riesgo_directo = True
            "Elegís el trabajo físico. Menos exposición, pero más carga."

    # Liderazgos asignados a los otros dos grupos
    if grupo_jugador_elegido != 1:
        show erika decidida at center
        with Dissolve(0.5)
        e "Yo me encargo de distraer a esa bestia. No necesito aplausos, necesito que funcione."
        hide erika with Dissolve(0.5)

    if grupo_jugador_elegido != 2:
        show bob serio at center
        with Dissolve(0.5)
        b "Yo trazo el camino con la fruta. Si me siguen el ritmo, mejor. Si no... igual lo hago."
        hide bob with Dissolve(0.5)

    # Tomás se une automáticamente, con reacción según relación
    if tomas > 1:
        show tomas neutral at center
        with Dissolve(0.5)
        t "Sabía que ibas a elegir ese grupo. Contá conmigo, me sirve trabajar con alguien en quien confío."
    elif tomas < -1:
        show tomas molesto at center
        with Dissolve(0.5)
        t "No sé por qué te sigo... Pero no me quedo mirando desde afuera. Ya me equivoqué antes."
    else:
        show tomas neutral at center
        with Dissolve(0.5)
        t "Bueno... parece que el destino insiste en ponernos en el mismo equipo. Hagámoslo funcionar."
    hide tomas with Dissolve(0.5)

    $ grupo_jugador = []
    $ grupo_jugador.append("tomas")

    # Elección entre Marina y Charles como tercer miembro del grupo
    $ choice_position = "default"
    menu:
        "Pedirle a Marina que se sume":
            if marina >= 1:
                show marina feliz at center
                with Dissolve(0.5)
                m "¡Claro! Tu sabes escuchar y eso siempre mejora el trabajo en equipo."
            elif marina <= -1:
                show marina molesta at center
                with Dissolve(0.5)
                m "¿Yo con vos? Genial... justo lo que necesitaba para complicarme el día."
            else:
                show marina neutral at center
                with Dissolve(0.5)
                m "Está bien. Si Tomás va, no pienso quedarme atrás. Solo no me des órdenes absurdas."
            $ miembro_extra = "marina"
            $ grupo_jugador.append("marina")

        "Pedirle a Charles que se sume":
            if charles >= 1:
                show charles confiado at center
                with Dissolve(0.5)
                c "Eso esperaba. Entre los dos podemos mantener esto en orden... o al menos divertido."
            elif charles <= -1:
                show charles sarcástico at center
                with Dissolve(0.5)
                c "Perfecto. Un plan suicida con vos al mando. ¿Qué puede salir mal?"
            else:
                show charles serio at center
                with Dissolve(0.5)
                c "Bah... da igual. Al menos no estás respirándome encima todo el tiempo."
            $ miembro_extra = "charles"
            $ grupo_jugador.append("charles")

    hide marina
    hide charles
    with Dissolve(0.5)

    "{i}El grupo está formado. Tres personas. Una tarea. Y un animal enorme que no piensa ceder terreno.{/i}"

    # Redirigir a la microescena correspondiente con condicional clásico
    if grupo_jugador_elegido == 1:
        jump cap9_mision_equipo_1
    elif grupo_jugador_elegido == 2:
        jump cap9_mision_equipo_2
    elif grupo_jugador_elegido == 3:
        jump cap9_mision_equipo_3


label cap9_mision_equipo_1:

    scene bg señuelo_senda with fade
    show screen combined_ui

    "Te alejás del claro con Tomás y [miembro_extra], cargando piedras, botellas y una bolsa con restos de fruta pasada."
    "{i}El jabalí no está a la vista… pero sabés que acecha. Los tres avanzan entre maleza, marcando árboles con olor y dejando rastro.{/i}"

    show tomas alerta at center
    with Dissolve(0.5)
    t "No hagamos ruido por ahora. Dejalo venir primero... cuando se acerque, lo mareamos."
    hide tomas with Dissolve(0.5)

    $ choice_position = "default"
    menu:
        "Proponés lanzar los señuelos ahora, desde los dos lados":
            $ decision_señuelo = "anticipada"
            $ reporte_toma_iniciativa_jabali = True
            "{i}Coordinás con gestos y lanzás el primer objeto. El ruido rebota entre los árboles.{/i}"

        "Esperás a ver una señal visual del animal antes de actuar":
            $ decision_señuelo = "espera"
            $ reporte_decision_analitica = True
            "{i}Revisás el viento, el silencio… y ahí está: una sombra entre los arbustos. Ahora sí.{/i}"

    if miembro_extra == "marina":
        if marina > 1:
            show marina sonriente at center
            with Dissolve(0.5)
            m "Bien pensado. Me gusta que pensemos como equipo."
        elif marina < -1:
            show marina molesta at center
            with Dissolve(0.5)
            m "¿Eso era el plan? Avisame cuando tenga sentido lo que hacés."
        else:
            show marina seria at center
            with Dissolve(0.5)
            m "Te sigo... Pero si se pone feo, me subo a un árbol."
        hide marina with Dissolve(0.5)

    elif miembro_extra == "charles":
        if charles > 1:
            show charles confiado at center
            with Dissolve(0.5)
            c "Te la jugaste, y salió bien. Ese bicho se va a marear en serio."
        elif charles < -1:
            show charles sarcástico at center
            with Dissolve(0.5)
            c "Wow, qué táctica. ¿La leíste en un manual de qué-no-hacer?"
        else:
            show charles serio at center
            with Dissolve(0.5)
            c "Mmm... mientras me mantenga lejos del centro del problema, me sirve."
        hide charles with Dissolve(0.5)

    "{i}El jabalí aparece. Cae en la trampa sonora y avanza rápido… pero no hacia ustedes. Está siguiendo el recorrido que trazaron.{/i}"

    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "Corren con sigilo por una zanja lateral. Desde ahí, ven al animal cruzar el sendero marcado hacia el punto de bloqueo."

    "{i}No hay tiempo para celebrar: la emboscada tiene que cerrarse desde todos los frentes… y ustedes son la chispa inicial.{/i}"

    jump cap9_union_grupos

label cap9_mision_equipo_2:

    scene bg huerta_recoleccion with fade
    show screen combined_ui

    "Caminan bordeando el claro con cestos y restos de cañas. Tu tarea: recolectar fruta suficiente y ubicarla formando un corredor visual y olfativo."

    "Tomás va adelante, revisando que no queden ramas secas donde el jabalí pueda desviarse."

    show tomas concentrado at center
    with Dissolve(0.5)
    t "Si seguimos esta línea de piedras naturales, debería guiarse solo. Pero hay que marcarlo bien. Si se pierde, vuelve atrás."
    hide tomas with Dissolve(0.5)

    "Cerca de la zona media, ves un problema: el terreno es más escarpado de lo que parecía. Las frutas pueden rodar o quedar en sombra."

    $ choice_position = "default"
    menu:
        "Proponés desviar un poco el recorrido para ganar firmeza":
            $ decision_recorrido_jabali = "adapta"
            $ reporte_toma_iniciativa_ambiental = True
            "{i}Ajustás la ruta 3 metros hacia el este, donde hay más luz y raíz firme. No es lo previsto… pero puede ser mejor.{/i}"

        "Decidís mantener la línea, siguiendo lo acordado":
            $ decision_recorrido_jabali = "mantiene_plan"
            $ reporte_prioriza_consenso = True
            "{i}Preferís no cambiar lo pactado. Aunque el terreno no sea ideal, confías en que el resto lo sostendrá.{/i}"

    if miembro_extra == "marina":
        if marina > 1:
            show marina sonriente at center
            with Dissolve(0.5)
            m "Esa es la actitud. Resolver, no quejarse. ¡Vamos bien!"
        elif marina < -1:
            show marina molesta at center
            with Dissolve(0.5)
            m "¿Todo te parece dudoso o es que te gusta complicar las cosas?"
        else:
            show marina neutral at center
            with Dissolve(0.5)
            m "Mientras no perdamos tiempo... que el camino se entienda."
        hide marina with Dissolve(0.5)

    elif miembro_extra == "charles":
        if charles > 1:
            show charles divertido at center
            with Dissolve(0.5)
            c "Si esto funciona, voy a empezar a hacerte más caso. Solo _un poco_ más."
        elif charles < -1:
            show charles sarcástico at center
            with Dissolve(0.5)
            c "Hermoso. Un plan improvisado en medio de fruta podrida. Brillante."
        else:
            show charles serio at center
            with Dissolve(0.5)
            c "Ok. Lo sigo, pero no esperes entusiasmo de mi parte."
        hide charles with Dissolve(0.5)

    $ actualizar_boton_imagen()
    $ update_stat("sed", sed - 1)
    $ show_variable_changed_popup("La sed ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Con los últimos mangos colocados en curva, el camino queda listo. Si el animal lo sigue, llegará directo a la trampa.{/i}"

    jump cap9_union_grupos

label cap9_mision_equipo_3:

    scene bg construccion_barrera with fade
    show screen combined_ui

    "Junto a Tomás y [miembro_extra] arrastrás ramas gruesas, organizándolas en V invertida para formar un pasillo con troncos inclinados."

    "{i}La idea es que el jabalí entre... pero no pueda salir. El diseño depende de ángulos, espacio justo y algo de suerte.{/i}"

    show tomas cansado at center
    with Dissolve(0.5)
    t "Si clavamos esta rama acá, lo forzamos a tomar el camino hacia la curva. Pero no va a quedar estable... va a vibrar con el primer golpe."
    hide tomas with Dissolve(0.5)

    $ choice_position = "default"
    menu:
        "Proponés reforzar la base con piedras y maleza antes de clavarla":
            $ decision_estructura_segura = "refuerza"
            $ reporte_soluciona_conflicto_tecnico = True
            "{i}Recogés hojas secas, raíces gruesas y apoyás la rama con tres piedras laterales. Tarda más, pero queda firme.{/i}"

        "Decidís seguir el plan original y confiar en que resistirá":
            $ decision_estructura_segura = "apresura"
            $ reporte_prioriza_velocidad = True
            "{i}Ajustan la rama con fuerza entre dos puntos. No es elegante… pero queda lista a tiempo.{/i}"

    if miembro_extra == "marina":
        if marina > 1:
            show marina sonriente at center
            with Dissolve(0.5)
            m "Esto te sale bien. Te vi dudando antes, pero sos más ingenioso de lo que pensás."
        elif marina < -1:
            show marina molesta at center
            with Dissolve(0.5)
            m "Qué raro… ¿te parece inteligente apurar estructuras cuando hay un bicho suelto?"
        else:
            show marina neutral at center
            with Dissolve(0.5)
            m "Tendríamos que probarla antes de que sea tarde."
        hide marina with Dissolve(0.5)

    elif miembro_extra == "charles":
        if charles > 1:
            show charles divertido at center
            with Dissolve(0.5)
            c "Esto tiene estilo... rústico, pero estilo. Casi que me dan ganas de quedarme."
        elif charles < -1:
            show charles molesto at center
            with Dissolve(0.5)
            c "Sí, genial. Otro curso express de arquitectura selvática. Todo bajo control, ¿no?"
        else:
            show charles neutral at center
            with Dissolve(0.5)
            c "Bueno, mientras aguante el primer empujón, estamos bien."
        hide charles with Dissolve(0.5)

    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}La barrera está lista. Un pasillo de ramas tensas con el final cerrado. Si el animal entra, no saldrá por donde vino.{/i}"

    jump cap9_union_grupos

label cap9_union_grupos:

    scene bg plano_de_trampa with fade
    show screen combined_ui

    "Los tres grupos convergen en torno a la trampa. El jabalí ha entrado en el pasillo... pero algo está mal."

    "{i}Uno de los lados de la barrera no está listo. El animal empieza a retroceder. Si lo hace, puede escapar por el claro, o peor: atacarlos desde atrás.{/i}"

    show tomas tenso at center with Dissolve(0.5)
    t "¡Falta el cierre lateral! ¡No está bloqueado!"
    hide tomas with Dissolve(0.5)

    # Decisión crítica del jugador
    $ choice_position = "default"
    menu:
        "Tomar el liderazgo y organizar una solución rápida":
            jump cap9_reaccion_liderazgo

        "Dejar que otro tome el control (Bob reacciona)":
            jump cap9_reaccion_pasiva

label elegir_tono(personaje):
    "¿Cómo le hablás a [personaje]?"
    menu:
        "Con tono gentil y persuasivo":
            $ tono = "gentil"
        "Con tono directo y firme":
            $ tono = "directa"
    return

label cap9_reaccion_liderazgo:

    $ exito_total = 0
    $ reactividad_directa = ["tomas", "ingrid"]
    $ reactividad_gentil = ["marina", "laura"]
    $ obstinado = "charles"

    ########## PRIMERA INSTRUCCIÓN ##########

    "¿A quién le das la primera orden?"

    menu:
        "Tomas":
            $ elegido = "tomas"
        "Marina":
            $ elegido = "marina"

    "¿Cómo le hablás a [elegido]?"

    menu:
        "Con tono gentil y persuasivo":
            $ tono = "gentil"
        "Con tono directo y firme":
            $ tono = "directa"

    $ rel = globals()[elegido]
    $ impacto = 0

    if elegido == obstinado:
        $ impacto = -1
    elif tono == "directa" and elegido in reactividad_directa:
        $ impacto += 1
    elif tono == "gentil" and elegido in reactividad_gentil:
        $ impacto += 1
    elif tono == "directa" and elegido in reactividad_gentil:
        $ impacto -= 1
    elif tono == "gentil" and elegido in reactividad_directa:
        $ impacto -= 1

    if rel > 0:
        $ impacto += 1
    elif rel < 0:
        $ impacto -= 1

    $ exito_total += impacto

    if elegido == "tomas":
        if impacto >= 2:
            t "Hecho. No hace falta decirlo dos veces."
        elif impacto >= 0:
            t "Sí... lo hago. Solo decime si ves algo raro."
        else:
            t "¿Ahora te acordás de mí? Bueno... está bien. Pero no me pidas sonrisas."

    elif elegido == "marina":
        if impacto >= 2:
            m "Gracias por pedírmelo así. Ahora sí: a trabajar."
        elif impacto >= 0:
            m "Lo hago, pero después hablamos de cómo das órdenes, ¿ok?"
        else:
            m "¿Y vos quién te creés para ordenarme así? Lo hago, pero no por vos."


    ########## SEGUNDA INSTRUCCIÓN ##########

    "¿A quién le das la segunda orden?"

    menu:
        "Ingrid":
            $ elegido = "ingrid"
        "Laura":
            $ elegido = "laura"

    "¿Cómo le hablás a [elegido]?"

    menu:
        "Con tono gentil y persuasivo":
            $ tono = "gentil"
        "Con tono directo y firme":
            $ tono = "directa"

    $ rel = globals()[elegido]
    $ impacto = 0

    if elegido == obstinado:
        $ impacto = -1
    elif tono == "directa" and elegido in reactividad_directa:
        $ impacto += 1
    elif tono == "gentil" and elegido in reactividad_gentil:
        $ impacto += 1
    elif tono == "directa" and elegido in reactividad_gentil:
        $ impacto -= 1
    elif tono == "gentil" and elegido in reactividad_directa:
        $ impacto -= 1

    if rel > 0:
        $ impacto += 1
    elif rel < 0:
        $ impacto -= 1

    $ exito_total += impacto

    if elegido == "ingrid":
        if impacto >= 2:
            i "¡Ya voy! Me encanta que confíes en mí para esto."
        elif impacto >= 0:
            i "No hace falta tantas vueltas, lo hago. Pero apurémonos."
        else:
            i "¿Me das una orden justo ahora? Qué timing…"

    elif elegido == "laura":
        if impacto >= 2:
            l "Así sí. Sabés pedir ayuda sin sonar como un sargento."
        elif impacto >= 0:
            l "Voy... pero no me hables así de nuevo, ¿sí?"
        else:
            l "Tu tono ayuda tan poco como esa rama mal clavada. Pero lo hago."


    ########## TERCERA INSTRUCCIÓN ##########

    "¿A quién le das la tercera orden?"

    menu:
        "Bob":
            $ elegido = "bob"
        "Charles":
            $ elegido = "charles"

    "¿Cómo le hablás a [elegido]?"

    menu:
        "Con tono gentil y persuasivo":
            $ tono = "gentil"
        "Con tono directo y firme":
            $ tono = "directa"

    $ rel = globals()[elegido]
    $ impacto = 0

    if elegido == obstinado:
        $ impacto = -1
    elif tono == "directa" and elegido in reactividad_directa:
        $ impacto += 1
    elif tono == "gentil" and elegido in reactividad_gentil:
        $ impacto += 1
    elif tono == "directa" and elegido in reactividad_gentil:
        $ impacto -= 1
    elif tono == "gentil" and elegido in reactividad_directa:
        $ impacto -= 1

    if rel > 0:
        $ impacto += 1
    elif rel < 0:
        $ impacto -= 1

    $ exito_total += impacto

    if elegido == "bob":
        if impacto >= 2:
            b "Buena cabeza. Me gusta verte tomar control con claridad."
        elif impacto >= 0:
            b "Bueno, si no hay otra, lo hago. Pero apurate la próxima."
        else:
            b "Estás improvisando. Pero qué raro… igual lo hago."

    elif elegido == "charles":
        c "Ah, el show del mando. Qué emocionante. Voy a hacerlo... si no encuentro una excusa mejor."


    ########## EVALUACIÓN FINAL ##########

    if exito_total >= 4:
        $ reporte_resuelve_crisis_con_liderazgo = "excelente"
        show bob orgulloso at center with Dissolve(0.5)
        b "No lo digo mucho… pero lo hiciste bien."
        hide bob with Dissolve(0.5)

        show erika leve_smile at center with Dissolve(0.5)
        e "Eso fue precisión bajo presión. Bien jugado."
        hide erika with Dissolve(0.5)

    elif exito_total >= -1:
        $ reporte_resuelve_crisis_con_liderazgo = "resuelto"
        "{i}Funcionó. Justo a tiempo. Hay respiraciones pesadas, pero también miradas de alivio sincero.{/i}"

    else:
        $ reporte_resuelve_crisis_con_liderazgo = "marginal"
        "{i}El jabalí quedó atrapado por pura casualidad. Todos lo saben. Nadie dice nada.{/i}"

    jump cap9_resolucion_final_jabali

label cap9_resolucion_final_jabali:

    scene bg plano_de_trampa with fade
    show screen combined_ui

    "{i}El jabalí respira agitado, encerrado entre ramas, fruta pisoteada y tierra húmeda. El grupo observa en silencio, entre asombro y cansancio.{/i}"

    show tomas aliviado at center with Dissolve(0.5)
    t "Lo logramos. No puedo creerlo... pero lo logramos."
    hide tomas with Dissolve(0.5)

    show erika neutra at center with Dissolve(0.5)
    e "Ahora hay que decidir qué hacer con esto. Pero primero... que alguien diga que estamos vivos."
    hide erika with Dissolve(0.5)

    show marina emocionada at center with Dissolve(0.5)
    m "¿¡Lo vieron!? ¡Eso fue trabajo en equipo posta!"
    hide marina with Dissolve(0.5)

    "{i}Por ahora, el animal queda bajo vigilancia. Pero el grupo siente que algo cambió: si lograron eso juntos, quizás haya esperanza más allá del miedo.{/i}"

    jump cap9_recolecta_alimentos

label cap9_recolecta_alimentos:

    scene bg huerta_exterior with fade
    show screen combined_ui

    "Mientras algunos vigilan al jabalí desde la distancia, otros comienzan a llenar canastos con frutas y verduras recuperadas del huerto."

    "Pero pronto, las miradas empiezan a pesar más que los tomates."

    show bob serio at left
    show marina molesta at right
    with Dissolve(0.5)

    b "Esto no se reparte solo. ¿Vamos a contar por cabeza o por mérito?"
    m "¿Otra vez con eso? No quiero pelear por un boniato mugriento."

    hide bob
    hide marina
    with Dissolve(0.5)

    "{i}Erika respira hondo. Propone una solución clara: separar la recolección en dos montones proporcionales a la cantidad de integrantes de cada grupo.{/i}"

    show erika lider at center with Dissolve(0.5)
    e "Si somos más, nos toca más. Si somos menos, cuidamos mejor lo que tenemos. Justo es justo."
    hide erika with Dissolve(0.5)

    "{i}La tensión baja, aunque las miradas no se suavizan del todo. Pero el acuerdo se cumple.{/i}"

    jump cap9_encuentro_caja

label cap9_encuentro_caja:

    scene bg huerta_exterior sunset with fade
    show screen combined_ui

    "El cielo ya se tiñe de naranja y violeta. Los insectos cantan. El esfuerzo del día se siente en la espalda, pero también en el pecho."

    "{i}Se dividieron los alimentos. Se contuvo al jabalí. Y nadie resultó herido… al menos de gravedad.{/i}"

    show erika neutral at left
    show bob cansado at right
    with Dissolve(0.5)

    e "Que cada uno cargue algo. Si no nos comemos estos tubérculos hoy, van directo al abono."

    b "Yo quiero verlos chisporrotear sobre el fuego. ¿Quién corta primero?"

    hide erika
    hide bob
    with Dissolve(0.5)

    "Mientras el otro grupo se despide y toma rumbo hacia su refugio, ustedes acomodan los bultos y repasan los momentos del día con sonrisas desarmadas."

    "{i}Pero justo cuando te agachás para levantar una mochila húmeda... sentís un golpe seco contra la suela. Algo enterrado.{/i}"

    $ choice_position = "default"
    menu:
        "Patear el borde del objeto y revisar con disimulo":
            $ reporte_descubre_objeto = True
            "{i}Removés hojas, raíces y algo de barro. Es una caja metálica, rectangular, carcomida por óxido y agua.{/i}"

        "Ignorarlo, estás agotado y querés irte ya":
            $ reporte_ignora_curiosidad = True
            "{i}Te obligás a no mirar. El cansancio pesa más que la curiosidad. Quizás alguien más lo vea otro día.{/i}"
            jump cap9_cierre_dia

    "Llevan la caja hasta el refugio. Es pesada. Vieja. Y está cerrada."

    scene bg refugio_interior with fade
    stop music fadeout 1.5
    play music "sfx_campamento_noche.ogg"

    "{i}Ya es de noche. Las verduras chispean en la sartén de lata. El fuego calienta pies y ánimo. Y entre los tres rodean la caja como si fuera un tótem perdido.{/i}"

    "Tomás fuerza una bisagra con la hoja del cuchillo. Tarda. Cruje. Pero finalmente… se abre."

    ### Etapa 1: Dibujo de la cueva
    "{i}En la parte superior, protegida por tela seca, hay una hoja con un dibujo a tinta: una cueva frente al mar, vista desde arriba.{/i}"

    show tomas sorprendido at center
    with Dissolve(0.5)
    t "Esa debe ser la playa al este… la de los acantilados. Nunca bajamos hasta ahí."

    menu:
        "Parece hecha por alguien que conocía bien la zona.":
            pass
        "¿Y si esto no es un dibujo? ¿Y si es un mapa?":
            pass
    hide tomas with Dissolve(0.5)

    ### Etapa 2: Notas con símbolos
    "{i}Debajo, una libreta pequeña, escrita a mano, con símbolos raros y coordenadas imprecisas. Marcas como 'línea rota', 'abertura oculta', 'marea alta'.{/i}"

    if "marina" in grupo_jugador:
        show marina intrigada at center with Dissolve(0.5)
        m "¿Estos símbolos… no son los mismos que vimos tallados en el claro del sur?"
        hide marina with Dissolve(0.5)
    elif "charles" in grupo_jugador:
        show charles curioso at center with Dissolve(0.5)
        c "Mmm. Me encantan los mapas que no dicen nada hasta que alguien desaparece por seguirlos."
        hide charles with Dissolve(0.5)

    menu:
        "Quizás esté describiendo cómo llegar a esa cueva en secreto.":
            pass
        "Podría ser solo el delirio de alguien que se perdió.":
            pass

    ### Etapa 3: Yodo + venda
    "{i}Al costado, enrollada con cinta: una venda usada y un frasco cerrado de yodo. Hay barro entre las gasas, como si alguien lo hubiera enterrado de apuro.{/i}"

    if "ingrid" in grupo_jugador:
        show ingrid seria at center with Dissolve(0.5)
        i "Esto se dejó acá como último recurso… o como advertencia."
        hide ingrid with Dissolve(0.5)
    elif "laura" in grupo_jugador:
        show laura pensativa at center with Dissolve(0.5)
        l "Tal vez alguien se lastimó de verdad. Y no quería que lo siguieran."
        hide laura with Dissolve(0.5)

    menu:
        "Esto no es solo un hallazgo. Es una historia enterrada.":
            pass
        "Quizás todavía queda alguien ahí afuera..." :
            pass

    ### Etapa 4: Trozo de diario – joyas robadas
    "{i}Y al fondo, arrugado pero visible: un recorte de diario plastificado. La noticia: 'Millonario robo de joyas. Misterio y desconcierto sobre su paradero.'{/i}"

    show tomas asombrado at center with Dissolve(0.5)
    t "¿Estás diciendo que… lo que sea que hay ahí… es real?"
    hide tomas with Dissolve(0.5)

    menu:
        "No lo sé. Pero alguien lo creyó suficiente como para esconder esto.":
            pass
        "¿Y si seguimos las pistas mañana? Podríamos ser nosotros los que lo encuentren.":
            pass

    "{i}La caja queda abierta sobre una manta improvisada. Y vos, aunque el cuerpo pide dormir… no podés dejar de pensar en el dibujo, el símbolo, el mar oscuro.{/i}"

    "{i}Cuando al fin cerrás los ojos, soñás con cúpulas cubiertas de lianas, pasadizos húmedos, joyas perdidas… y jabalíes que custodian secretos en la selva.{/i}"

    jump cap10_inicio


label cap10_inicio:
    "hasta aca"