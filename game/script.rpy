

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
define r = Character("Rescatista", color="#546ace")
define p = Character("Pescador", color="#b19621")

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
image bg jungle night fall = im.Scale("bg jungle night fall.jpg", config.screen_width, config.screen_height)
image bg jungle night rescue = im.Scale("bg jungle night rescue.jpg", config.screen_width, config.screen_height)
image bg jungle night search = im.Scale("bg jungle night search.jpg", config.screen_width, config.screen_height)
image bg campfire = im.Scale("campfire.jpg", config.screen_width, config.screen_height)
image bg cave fungi = im.Scale("cave fungi.jpg", config.screen_width, config.screen_height)
image bg horizon_storm_clouds = im.Scale("storm horizon.jpg", config.screen_width, config.screen_height)
image bg jungle_storm_approaching = im.Scale("storm_horizon2.jpg", config.screen_width, config.screen_height)
image bg jungle_storm_aftermath = im.Scale("jungle_storm_aftermatch.jpg", config.screen_width, config.screen_height)
image bg timber pile = im.Scale("bg timber pile.jpg", config.screen_width, config.screen_height)
image bg jungle resting_spot = im.Scale("bg_jungle_resting_spot.jpg", config.screen_width, config.screen_height)
image bg jungle makeshift_camp = im.Scale("bg jungle makeshift_camp.jpg", config.screen_width, config.screen_height)
image bg jungle dense = im.Scale("bg jungle dense.jpg", config.screen_width, config.screen_height)
image bg jungle orchard = im.Scale("bg jungle_orchard3.jpg", config.screen_width, config.screen_height)
image bg jungle board = im.Scale("bg jungle_boar.jpg", config.screen_width, config.screen_height)
image bg plano_de_trampa = im.Scale("jungle trap.jpg", config.screen_width, config.screen_height)
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
image ingrid gr triste = "ingrid.200.triste.png"
image ingrid gr enojada = "ingrid.200.enojada.png"
image ingrid gr cintura = "ingrid.200.manos.cintura.png"
image ingrid gr risita = "ingrid.200.risita.png"
image ingrid gr seria = "ingrid.200.seria.png"
image ingrid gr sonriente = "ingrid.200.sonriente.png"

image charles boca abierta = "charles.100.boca.abierta.png"
image charles brazos cruzados = "charles.100.brazos.cruzados.png"
image charles dedos v = "charles.100.dedos.V.png"
image charles enojado = "charles.100.enojado.png"
image charles sonriente = "charles.100.sonriente.png"
image charles triste = "charles.100.triste.png"
image charles gr boca abierta = "charles.200.boca.abierta.png"
image charles gr brazos cruzados = "charles.200.brazos.cruzados.png"
image charles gr dedos v = "charles.200.dedos.V.png"
image charles gr enojado = "charles.200.enojado.png"
image charles gr sonriente = "charles.200.sonriente.png"
image charles gr triste = "charles.200.triste.png"

image tomas enojado = "tomas.100.enojado.png"
image tomas hablando = "tomas.100.hablando.png"
image tomas risa = "tomas.100.risa.png"
image tomas serio = "tomas.100.serio.png"
image tomas sonriendo = "tomas.100.sonriendo.png"
image tomas gr enojado = "tomas.200.enojado.png"
image tomas gr hablando = "tomas.200.hablando.png"
image tomas gr risa = "tomas.200.risa.png"
image tomas gr serio = "tomas.200.serio.png"
image tomas gr sonriendo = "tomas.200.sonriendo.png"

# Lista de imagenes "grupo" para cada personaje para la sepracion en grupos
image marina grupo ="Marina_hablando.png"
image bob grupo ="Bob_parado_serio.png"
image laura grupo ="Laura_parada_seria.png"
image erika grupo ="Erika parada.png"
image ingrid grupo ="ingrid.100.manos.cintura.png"
image charles grupo ="charles.100.brazos.cruzados.png"
image tomas grupo ="tomas.100.serio.png"


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
default reporte_buscar_quien_quiera = False
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
default apoyo_marina = 0
default grupo_jugador = []
default grupo_jabaporco = []
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
default bob_es_lider = False
default erika_es_lider = False
default elegido = ""
default decision_cueva = ""
default tarea_jugador1 = ""
default tarea_jugador2 = ""
default tarea_jugador3 = ""
default compartio_info = False
default personajes_desaparecidos = []
default compartio_info_caja = None  # Puede ser True o False
default cruce1 = ""  # Guarda a quién te cruzaste
default cruce2 = ""
default invitar_marina = False
default invitar_bob = False
default invitar_erika = False
default invitar_ingrid = False
default invitar_charles = False
default invitar_tomas = False
default equipo_exploracion = []
default decision_rocas_tardia = ""
default decision_seguir = ""           # ¿Explorar más o no?
default reaccion_charles = ""          # Postura ante lo que hizo Charles
default relacion_subida = []           # Personajes con los que se mejora vínculo
default relacion_bajada = []           # Personajes que se sienten defraudados
default reloj_marea = 0                # Tiempo narrativo antes del cierre de la cueva
default decision_post_espera = ""
default cap12_choice = ""
default influencia_charles = 0
default proyecto = ""

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
        "cabaña": {
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
            jump final_cap3
            #jump final_cap3
        "VOLVER A VER EL RESÚMEN":
            jump final
    
label final_cap3:
    if renpy.android:
        jump chapter_3_start
    else:
        call pedir_codigo_capitulo from _call_pedir_codigo_capitulo2

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
                jump segment_1_end
                #jump segment_1_end
            "VOLVER A VER EL RESÚMEN":
                jump chapter_4_end
    

label segment_1_end:
    # prueba de enviar reporte
    $ enviar_reporte(player_id)
    "El reporte fue enviado con exito!"
    call pedir_codigo_capitulo from _call_pedir_codigo_capitulo4


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
                    show bob pensando at left
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
        "Hacer un gran esfuerzo fisico para intentar agarrarte de algo" if cansancio >= 2:
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
        
        "Intentar agarrarte de algo pese al cansancio" if cansancio == 1:
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
        
        "Intentar agarrarte de algo pese al cansancio" if cansancio == 1:
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
    scene bg jungle night explore1 at truecenter
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

    scene bg jungle night rescue at truecenter
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

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)

    "{i}Poco después una figura aparece en la entrada del refugio.{/i}"
    "{i}Cojeando, con el rostro pálido y el brazo rasguñado, la silueta de Marina es recortada por los primeros rayos de luz.{/i}"

    show marina triste at left
    with Dissolve(0.5)

    m "Pensé... que no volvía."
    m "Me perdí... pero encontré un claro."
    m "Esperé hasta que hubo algo luz."

    show bob parado hablando at right
    show laura hablando at center
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

    jump cap6_final_dia

label cap6_3_salida_en_solitario_marina:

    scene bg jungle night explore at truecenter
    with Dissolve(0.5)

    "{i}La oscuridad no es completa, pero sí suficiente para perderte si das un paso en falso.{/i}"

    $ update_stat("sed", sed - 1)
    $ show_variable_changed_popup("La sed ha aumentado", rojo)

    scene bg jungle night rescue at truecenter
    with Dissolve(0.5)

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

    scene bg campfire at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Reavivan el fuego para preparar una infusión con las plantas recolectadas.{/i}"
    "{i}Una olla improvisada burbujea sobre las llamas mientras Marina descansa.{/i}"

    show laura hablando at center
    show bob parado serio at left
    with Dissolve(0.5)
    $ ingrid += 1
    l "¿Esto funcionará?"

    b "Si Ingrid tenía razón y la preparación está bien hecha, deberíamos ver una mejoría pronto."

    "{i}Aplican con cuidado el líquido tibio sobre la herida de Ingrid en silencio.{/i}"
    "{i}Solo se escucha el lento goteo del agua condensada entre las hojas y los quejidos de Ingrid.{/i}"
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    "{i}Esperan pacientemente hasta que, al rato, Ingid abre los ojos nuevamente.{/i}"
    hide bob
    show laura seria at centerleft
    with Dissolve(0.5)
    show ingrid gr triste at rightgr
    with Dissolve(0.5)

    i "La fiebre..."
    show marina triste at left
    with Dissolve(0.5)
    "{i}Ingrid hace un gran esfuerzo para hablar.{/i}"
    show ingrid gr sonriente at rightgr
    with Dissolve(0.5)
    i "...la fiebre se ha ido."


    "{i}Todos sueltan un suspiro de alivio.{/i}"
    show laura sonriendo
    with Dissolve(0.5)
    show marina sonriendo at left
    with Dissolve(0.5)
    "{i}Visible en el rostro de todos, esta victoria es pequeña, pero real.{/i}"
    "{i}Esta noche tumultuosa ha dado sus frutos: el grupo ganó tiempo, confianza, y unidad en la incertidumbre.{/i}"

    "{i}Tus decisiones de esta noche no pasaron desapercibidas. Los tropiezos, el cansancio, las heridas... todo deja huella.{/i}"

    $ ingrid +=2
    jump chapter_6_end  

label cap6_final_dia:
    # Si hubo misión de rescate, se encuentran las plantas y al personaje
    # Si se esperó: la persona llega al amanecer extenuada
    # Se curan heridas de Ingrid con las plantas
    # Se muestran consecuencias → se cierra el capítulo
    hide marina

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)

    show screen combined_ui

    "{i}Reavivan el fuego para preparar una infusión con las plantas recolectadas.{/i}"
    "{i}Una olla improvisada burbujea sobre las llamas mientras Marina descansa.{/i}"

    show laura hablando at center
    show bob parado serio at left
    with Dissolve(0.5)
    $ ingrid += 1
    l "¿Esto funcionará?"

    b "Si Ingrid tenía razón y la preparación está bien hecha, deberíamos ver una mejoría pronto."

    "{i}Aplican con cuidado el líquido tibio sobre la herida de Ingrid en silencio.{/i}"
    "{i}Solo se escucha el lento goteo del agua condensada entre las hojas y los quejidos de Ingrid.{/i}"
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    "{i}Esperan pacientemente hasta que, al rato, Ingid abre los ojos nuevamente.{/i}"
    hide bob
    show laura seria at centerleft
    with Dissolve(0.5)
    show ingrid gr triste at rightgr
    with Dissolve(0.5)

    i "La fiebre..."
    show marina triste at left
    with Dissolve(0.5)
    "{i}Ingrid hace un gran esfuerzo para hablar.{/i}"
    show ingrid gr sonriente at rightgr
    with Dissolve(0.5)
    i "...la fiebre se ha ido."


    "{i}Todos sueltan un suspiro de alivio.{/i}"
    show laura sonriendo
    with Dissolve(0.5)
    show marina sonriendo at left
    with Dissolve(0.5)
    "{i}Visible en el rostro de todos, esta victoria es pequeña, pero real.{/i}"
    "{i}Esta noche tumultuosa ha dado sus frutos: el grupo ganó tiempo, confianza, y unidad en la incertidumbre.{/i}"

    "{i}Tus decisiones de esta noche no pasaron desapercibidas. Los tropiezos, el cansancio, las heridas... todo deja huella.{/i}"

    $ ingrid +=2
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
                    
        "Aquí termina el capítulo 6, pese a todo el esfuerzo Ingrid aún no está recuperada del todo. Es una noche tensa y de poco descanso."
                    
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
        call pedir_codigo_capitulo from _call_pedir_codigo_capitulo6

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

        if refugio != "cabaña":
            opciones_exploracion.append("cabaña")
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
    elif refugio == "cabaña":
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
        show marina triste at left
        with Dissolve(0.5)
        m "Hagan lo que quieran. Ya estoy acostumbrada a no tener voz en las decisiones."
    elif marina >= 2:
        show marina hablando at left
        with Dissolve(0.5)
        m "Prefiero quedarme con Ingrid, si puedo ayudarla. Aun no estoy del todo repuesta."
    else:
        show marina hablando at left
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
    elif refugio == "cabaña":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing

    with Dissolve(0.5)

    show screen combined_ui

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)

    "{i}Mientras los demás se preparan para salir, tu te quedas junto a Ingrid, acomodando unas hojas secas para que se recueste mejor.{/i}"

    show ingrid cintura at center
    with Dissolve(0.5)

    i "Gracias por quedarte... pero no deberías."

    y "¿Y por qué es eso?"

    i "Lo que necesitamos está allá afuera. Yo voy a estar bien. Iré buscando plantas por aqui cerca. Puedo arreglármelas."

    "{i}La mirás. Tiene ojeras, las manos temblorosas, pero hay determinación en su tono.{/i}"
    show ingrid risita at center
    with Dissolve(0.5)
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

    scene bg jungle trail at truecenter
    with Dissolve(0.5)

    "{i}Te apresuras a tomar tus cosas, y sales en la dirección hacia la que partieron los demás.{/i}"
    "{i}Tras unos minutos, logras alcanzarlos.{/i}"
    
    show bob parado serio at center
    show laura seria at right
    show marina triste at left
    with Dissolve(0.5)

    b "[nombre_personaje]... ¿te arrepentiste?"

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

    elif destino_exploracion_1 == "cabaña":

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

            if refugio != "cabaña" and destino_exploracion_1 != "cabaña":
                opciones_exploracion2.append("cabaña")

            if refugio != "cueva" and destino_exploracion_1 != "cueva":
                opciones_exploracion2.append("cueva")

            if refugio != "claro" and destino_exploracion_1 != "claro":
                opciones_exploracion2.append("claro")

        $ destino_exploracion_2 = opciones_exploracion2[0]

    elif search_west:
        y "Cuando estaba buscando el primer refugio, recorrí la parte oeste de la isla y fui hasta la playa, pero no subi a la colina."
        y "Quizá desde allí puedan ver qué otros lugares quedan por explorar."
        $ destino_exploracion_2 = "claro"
    else:
        y "Cuando estabamos buscando refugio, nadie decidió explorar hacia el oeste."
        y "Quizá en esa dirección haya algo interesante."
        $ destino_exploracion_2 = "claro"

    if destino_exploracion_2 == "cueva":
        scene bg jungle cave
    elif destino_exploracion_2 == "cabaña":
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
    hide bob 
    with Dissolve(0.5)
    show laura gr hablando at leftgr
    with Dissolve(0.5)

    l "¡Entonces debe haber mas supervivientes!"
    hide laura
    with Dissolve(0.5)

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

    scene bg timber pile
    with Dissolve(.5)

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

    show tomas hablando at right
    with Dissolve(0.5)

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

    show charles boca abierta at right
    with Dissolve(0.5)

    c "No se preocupen por Tomás. Es así con todo el mundo."

    c "Yo soy Charles. Bienvenidos a nuestro humilde refugio."
    show charles sonriente at right
    with Dissolve(0.5)

    show bob parado serio at centerleft
    with Dissolve(0.5)
    show laura hablando at left
    with Dissolve(0.5)

    l "Tal vez tú sí puedas contarnos, ¿hace cuánto que están juntos?"

    "{i}Charles sonríe, relajado, sin mostrar el mismo fastidio que Tomás.{/i}"

    c "El tiempo suficiente para entender que es mejor dejar que otros hagan el trabajo duro."
    show charles brazos cruzados at right
    with Dissolve(0.5)
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
    show charles brazos cruzados at right
    hide Bob
    with Dissolve(.5)
    hide laura
    with Dissolve(.5)
    show tomas serio at center    
    with Dissolve(0.5)

    "{i}Atrás de ustedes se deja de escuchar el crujir de la madera. Tomás mira a Charles con un atado de ramas bajo el brazo.{/i}"
    "{i}Su expresión esconde el enfado que el tono de su voz delata cuando habla.{/i}"
    show tomas enojado at center    
    with Dissolve(0.5)

    t "Algunos de nosotros trabajamos duro, mientras otros holgazanean descansando."

    c "No estaba descansando. Estaba vigilando, asegurándome de que no tuviéramos problemas."
    c "A estos los escuché acercándose hace rato. Pero parecen inofensivos, ¿no?"

    t "¿Ah, sí? Dime, [nombre_personaje], ¿tú que piensas?"
    show tomas hablando at center    
    with Dissolve(0.5)

    "{i}Tomás cruza los brazos. Charles apenas se voltea, pero te mira atentamente.{/i}"

    $ choice_position = "alta" # default alta superior
    menu:
        "Apoyar a Tomás. Charles estaba holgazaneando.":            
            $ confianza_tomas += 1
            $ confianza_charles -= 1
            y "Si lo que Charles hacía era útil, yo no lo noté. No lo vi ni moverse desde que llegamos."

            t "Exacto."
            show charles enojado at right    
            with Dissolve(0.5)

            c "Vaya, qué rápid[e] eres para sacar conclusiones."

        "Apoyar a Charles. Tal vez sí estaba haciendo algo.":            
            $ confianza_charles += 1
            $ confianza_tomas -= 1
            y "No podemos asumir que no estaba en realidad vigilando, por más relajado que pareciera."

            t "Espero que de verdad sea el caso."
            show charles sonriente at right    
            with Dissolve(0.5)

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

    show bob parado serio at centerleft
    with Dissolve(0.5)
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
    hide bob
    with Dissolve(0.5)
    show bob parado serio at left
    with Dissolve(0.5)
    show tomas serio at centerleft
    with Dissolve(0.5)
    show erika conversando at centerright
    with Dissolve(0.5)

    t "Separados, apenas hemos sobrevivido. Juntos, podremos estar mejor."

    show charles brazos cruzados at right
    with Dissolve(0.5)

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
    show erika parada at right
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

    show bob parado hablando at center
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
    show charles sonriente at right
    with Dissolve(0.5)

    k "Hemos tomado una decisión."
    t "Nos uniremos a ustedes."    
    show laura sonriendo
    with Dissolve(0.5)
    show tomas risa
    with Dissolve(0.5)
    "{i}Todos intercambian sonrisas que se vuelven risas de júbilo a medida que comprenden dos cosas muy distintas.{/i}"
    show bob saludando sucio
    with Dissolve(0.5)
    show erika sonriendo
    with Dissolve(0.5)
    "{i}Han mejorado sus chances de supervivencia enormemente, y eso les devuelve la esperanza que las noticias de Bob les quitaron.{/i}"
    "{i}Van a tener que aprender a trabajar en equipo aún más que antes.{/i}"
    "{i}Un grupo más grande también significa más individualidades con las que convivir.{/i}"

    c "Dependiendo de cómo lo miremos, también podríamos decir que son ellos los que se unen a nosotros."
    show charles dedos v at right
    with Dissolve(0.5)

    "{i}Charles suelta una carcajada, dejando claro que se trata de una broma, y pronto todos están riendo junto a el.{/i}"
    show charles brazos cruzados at right
    with Dissolve(0.5)
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

    scene bg jungle trail at truecenter
    with Dissolve(0.5)

    "{i}Charles, Erika y Tomás se sorprenden gratamente al ver qué fácil que han aprendido a moverse a través de la jungla.{/i}"

    show screen combined_ui

    if refugio == "cueva":
        scene bg jungle cave
    elif refugio == "cabaña":
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

    if destino_exploracion_2 == "cabaña":
        
        show erika parada at centerright
        with Dissolve(0.5)
        k "Además de que, como vieron, ya está muy bien organizada."

        show charles boca abierta at centerleft
        with Dissolve(0.5)    
        c "Y nos ahorraría la mudanza."

        show tomas serio at left
        with Dissolve(0.5)
        t "De todas formas vamos a ayudarlos con sus cosas."

    elif refugio == "cabaña":
        
        show erika parada at centerright
        with Dissolve(0.5)
        k "Se nota que le han puesto esfuerzo, y no puedo esperar a proponerles algunas mejoras."

        show charles boca abierta at centerleft
        with Dissolve(0.5)
        c "¿Tendríamos que traer todo para aquí?"

        show laura hablando at center
        with Dissolve(0.5)
        l "De más está decir que los ayudaríamos."
       
    else:
        show erika parada at centerright
        with Dissolve(0.5)
        k "La cabaña es el único sitio donde no se ha armado ningún refugio."

        show tomas serio at left
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

    show charles boca abierta at centerright
    with Dissolve(0.5)
    c "¿Qué opinas tú, Ingrid?"

    show ingrid seria at left
    with Dissolve(0.5)
    show charles brazos cruzados at centerright
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
            $ refugio = "cabaña"
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

    hide marina
    with Dissolve(0.5)
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
    elif refugio == "cabaña":
        scene bg jungle hut
    elif refugio == "claro":
        scene bg jungle clearing

    pause 1

    if refugio == "claro":
        "{i}Todos se vuelven a encontar en el refugio del claro un rato después.{/i}"
    elif refugio == "cabaña":
        "{i}Todos se vuelven a encontar en la cabaña un rato después.{/i}"
    elif refugio == "cueva":
        "{i}Todos se vuelven a encontar en la cueva un rato después.{/i}"        
    
    "{i}Luego de desempacar sus cosas, todos se juntan en la entrada del refugio.{/i}"
    "{i}Otra decisión importante sigue pendiente.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    b "Ahora que estamos instalados, necesitamos encarar aquello que, al menos nosotros, hemos postergado."
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

    show charles brazos cruzados at right
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
    #elif refugio == "cabaña":
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

    elif refugio == "cabaña":
        show charles brazos cruzados at right
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
        
        show erika conversando at centerleft
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

    show charles brazos cruzados at right
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
                $ charles += 1
                y "Quiero escuchar más ideas. Vendrán bien si tenemos que improvisar."

                c "No vamos a tener demasiado margen para improvisar cuando esto empiece."

            "¿Qué piensas hacer tú, Charles?":
                
                y "No hablo solo de la tormenta."

                c "Haré lo que decidieron que era mejor. El problema, como bien dices, viene después."
                c "Las tormentas suelen desenterrar mucha cosa."

    "{i}Aunque sus palabras son crípticas y parece estar pensando más allá de lo inmediato, Charles tiene claras sus ideas.{/i}"
    "{i}Seguramente tenga claro por quién se inclinará cuando llegue el momento de decidir sobre el liderazgo.{/i}"

    menu:
        "¿A quién ves liderando el grupo?":
            jump cap8_liderazgo_charles

        "Charles está pensando en cualquier cosa, menos en quién debe ser el líder. Mejor ni le pregunto.":
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

    show laura seria at left
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
    elif refugio == "cabaña":
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
            show laura enojada at left
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

    scene bg jungle makeshift_camp at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}La tormenta está cerca. No hay tiempo para perder.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    show erika enojada at centerleft
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

    scene bg jungle makeshift_camp at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Bob lidera su estrategia con rapidez, enfocándose en usar lo disponible en lugar de perder tiempo en desarmar y armar.{/i}"

    show bob parado serio at centerright
    with Dissolve(0.5)
    show marina triste at left
    with Dissolve(0.5)
    show charles brazos cruzados at right
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

    scene bg jungle makeshift_camp at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Erika lidera su estrategia con precisión. Cada decisión es calculada para evitar errores que puedan costar caro.{/i}"

    show erika enojada at centerleft
    with Dissolve(0.5)
    show tomas serio at right
    with Dissolve(0.5)
    show laura enojada at left
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

    scene bg jungle makeshift_camp at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Tu planteas una alternativa propia para reforzar el refugio, basada en el entorno y los recursos disponibles.{/i}"

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

        show laura enojada at left
        with Dissolve(0.5)
        show charles boca abierta at right
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

    "{i}Puedes decidir cómo abordar la ejecución.{/i}"

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

    scene bg jungle makeshift_camp at truecenter
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Tú propones otra alternativa basada en los puntos críticos del refugio. Algunos dudan, pero otros apoyan la idea.{/i}"

    if refugio == "cabaña":
        "{i}La cabaña tiene buena estructura, pero los soportes pueden debilitarse.{/i}"
        "{i}Desarmando algunas secciones periféricas, podemos reforzar la habitación principal.{/i}"

        show tomas serio at right
        with Dissolve(0.5)
        show charles boca abierta at left
        with Dissolve(0.5)

        t "Podemos tomar los troncos del deck y usarlos para distribuir mejor la carga en las columnas que sostienen el techo."

        c "Solo espero que no se derrumbe todo mientras lo hacemos."

    elif refugio == "cueva":
        "{i}La cueva es estable, pero el suelo es húmedo. Se deben levantar plataformas para evitar filtraciones y mejorar la estabilidad.{/i}"

        show marina triste at left
        with Dissolve(0.5)
        show laura enojada at right
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

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
    with Dissolve(0.5)

    show screen combined_ui

    "{i}Las últimas horas han sido intensas.{/i}"
    "{i}El esfuerzo por dejar las diferencias de lado, sumado al cansancio del trabajo, deja a todos agotados.{/i}"

    if equipo_bob:
        "{i}La estrategia de Bob logró reforzar lo esencial con rapidez, pero algunos dudan de la estabilidad de ciertas áreas.{/i}"
        
        show bob parado serio at centerright
        with Dissolve(0.5)
        show erika enojada at centerleft
        with Dissolve(0.5)
        show charles brazos cruzados at left
        with Dissolve(0.5)

        c "Bueno, al menos tenemos algo."

        k "Si se cae después, no digas que no te avisé."

        b "Hicimos lo que teníamos que hacer."

    if equipo_erika:
        "{i}El plan de Erika siguió cada cálculo con precisión, pero la lentitud no permitió cubrir todas las áreas completamente.{/i}"
        
        show erika enojada at centerleft
        with Dissolve(0.5)
        show tomas serio at right
        with Dissolve(0.5)
        show laura enojada at left
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
        show charles brazos cruzados at right
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
    
    show laura gr enojada at rightgr
    with Dissolve(0.5)

    l "¡Tenemos que asegurar no perder nada de lo que hemos conseguido con tanto esfuerzo, será esencial cuando la tormenta amaine!"

    show marina gr preocupada at leftgr
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

    scene bg jungle_storm_aftermath  at truecenter
    with Fade(0.1, 0.4, 0.1)  # Simula un destello blanco

    show screen combined_ui

    "{i}La tormenta no da tregua. En medio del desastre, la tensión entre varios es como un barril de pólvora.{/i}"

    show ingrid gr enojada at leftgr
    with Dissolve(0.5)
    show charles gr brazos cruzados at rightgr
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

    show tomas gr serio at leftgr
    with Dissolve(0.5)

    t "¡Si esto sigue así, no quedará nada del refugio! Se está inundando todo. ¡Tal vez sea mejor que nos vayamos antes de quedar atrapados aquí!"

    show bob gr parado enojado at rightgr
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

    scene bg jungle_storm_aftermath at truecenter
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco

    show screen combined_ui

    "{i}El viento ruge con fuerza, la lluvia golpea en todas direcciones. El refugio está parcialmente inundado.{/i}"
    "{i}Los restos de algunas de las mejoras construídas por ustedes ahora vuelan por los aires como peligrosos proyectiles.{/i}"

    show bob gr parado enojado at rightgr
    show erika gr enojada at leftgr
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

    show ingrid gr triste at leftgr
    with Dissolve(0.5)

    i "¡Algo se mueve afuera! ¡No estamos solos!"

    show charles gr boca abierta at rightgr
    with Dissolve(0.5)
    c "¡Nada puede estar ahí afuera! ¡El viento es muy fuerte!"

    "{i}El viento y la lluvia apenas les permiten escuchar un trote pesado acercándose.{/i}"
    "{i}Escuchan un ronquido fuerte antes de divisar la silueta de un cuadrúpedo pesado en la entrada del refugio.{/i}"

    scene bg jungle_storm_aftermath at truecenter
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
    
    scene bg jungle_storm_aftermath at truecenter
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco
    "{i}El destello de un relámpago cercano los enceguece de repente y segundos mas tarde llega un trueno ensordecedor.{/i}"
    scene bg jungle_storm_aftermath at truecenter
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco
    "{i}Escuchan nuevamente el pesado trote, esta vez alejándose. El ruido lo asustó y salió corriendo jungla adentro.{/i}"
    hide ingrid
    hide charles
    with Dissolve(0.5)
    "{i}La tormenta sigue intensificándose. Aquello que no vuela por los aires, está flotando en corrientes de agua que se van formando con la lluvia.{/i}"
    "{i}Llega un punto en el que lo único que pueden hacer es acurrucarse en un rincón de lo que queda del refugio para darse algo de calor entre todos.{/i}"

    scene bg jungle_storm_aftermath at truecenter
    with Fade(0.1, 1.0, 0.1)  # Simula un destello blanco
    pause 2.0
    "{i}Tras lo que parecen ser horas, la tormenta amaina y una extraña calma se apodera de la isla.{/i}"

    jump cap8_enfrentamiento_lideres

label cap8_enfrentamiento_lideres:

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
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

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)
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

    $ bob_es_lider = True

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

    $ erika_es_lider = True

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

    "{i}Las personas aparecen una por una.{/i}"

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

    "{i}La última persona, Ingrid, duda por un momento.{/i}"
    hide charles
    with Dissolve(0.5)
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
    hide ingrid
    with Dissolve(0.5) 
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
                jump segment_2_end
                #jump chapter_9_start
            "VOLVER A VER EL RESÚMEN":
                jump continuar
                #jump chapter_8_end

label segment_2_end:
    # prueba de enviar reporte
    $ enviar_reporte(player_id)
    "El segundo reporte fue enviado con exito!"
    call pedir_codigo_capitulo from _call_pedir_codigo_capitulo8
    jump chapter_9_start

label final_segundo_segmento:
    "Aquí termina el segundo segmento, pronto estará disponible el ultimo segmento donde las desiciones serán clave no solo para sobrevivir sino para resolver el misterio de la isla."
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

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)

    "{i}Descansan todos juntos entre lo que queda de su refugio.{/i}"
    $ cansancio = 3
    $ show_variable_changed_popup("El cansancio ha disminuido", verde)   
    hide screen combined_ui
    show screen combined_ui
    
    "{i}Reparten la comida entre los dos grupos para recuperar las energías gastadas durante la tormenta.{/i}"
    $ hambre = 3
    $ show_variable_changed_popup("El hambre ha disminuido", verde)    
    hide screen combined_ui
    show screen combined_ui

    "{i}El agua, por suerte, no es algo que escasee.{/i}"
    $ sed = 3
    $ show_variable_changed_popup("La sed ha disminuido", verde)    
    hide screen combined_ui
    show screen combined_ui

    if bob_es_lider:
        show bob parado serio at left with Dissolve(.5)
        b "Deberíamos priorizar reabastecernos de alimento."

        show erika parada at right with Dissolve(0.5)
        k "¿Esa es tu manera de liderar, Bob? ¿Diciendo lo obvio?"

        "{i}Bob decide ignorarla y comienza a caminar hacia la entrada del refugio.{/i}"

        hide erika with Dissolve(.5)

        b "Los que estén conmigo, vamos. No hay tiempo que perder."
        b "Creo que podemos estar de acuerdo en que hay que priorizar reabastecernos de alimento."

    elif erika_es_lider:
        show erika parada at right with Dissolve(0.5)
        k "Debemos recorrer aquellos lugares de la isla que no hemos explorado, para encontrar comida pronto."

        show laura seria at left with Dissolve(.5)
        l "¿Esa es la gran estrategia de la que tanto nos hablaste?"
        l "Explorar por descarte. Brillante."

        "{i}La ironía no pasa desapercibida para Erika, pero decide ignorarlo y salir afuera.{/i}"

        hide bob with Dissolve(.5)

        k "¡Equipo! Vamos, tenemos mucho terreno por cubrir."

    elif "bob" in grupo_jugador:
        show bob parado serio at left with Dissolve(.5)
        
        "{i}Bob se te acerca y te habla en voz baja.{/i}"

        b "Deberíamos priorizar reabastecernos de alimento."

        y "Si, vamos. Acompáñame."

        "{i}Te diriges a la entrada del refugio con Bob detrás tuyo.{/i}"

        y "Aquellos que decidieron seguirme, ¡vamos!"
        y "Debemos encontrar comida."

        "{i}Los integrantes de tu grupo salen con ustedes.{/i}"

    elif "erika" in grupo_jugador:
        show erika parada at right with Dissolve(.5)
        
        "{i}Erika se te acerca para decidir los próximos pasos.{/i}"

        k "¿Te parece bien si aprovechamos que estamos con las energías recargadas para salir a buscar alimento?"        

        "{i}Asientes y te diriges a la entrada del refugio con Erika detrás tuyo.{/i}"

        y "Aquellos que decidieron seguirme, ¡vamos!"
        y "Debemos encontrar comida."

        "{i}Los integrantes de tu grupo salen con ustedes.{/i}"

    jump cap9_hallazgo_huerta

label cap9_hallazgo_huerta:

    scene bg jungle explore 1
    with Dissolve(.5)

    "{i}Recorren la selva, tratando de evitar aquellos lugares en los que ya buscaron sin éxito.{/i}"
    "{i}A medida que se internan en territorios inexplorados, el terreno deja de ser familiar, y el paso se enlentece.{/i}"    
    scene bg jungle dense
    with Dissolve(.5)
    "{i}La vegetación se hace más densa a medida que avanzan. Las hojas crujen bajo las botas húmedas y las ramas crujen sobre sus cabezas.{/i}"
    "{i}Las últimas lluvias han empapado el suelo y desplazado raíces viejas, dejando un aroma a petricor en el aire.{/i}"

    show screen combined_ui
    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    $ choice_position = "default"  # default alta superior
    menu:
        "Propones separarse brevemente para cubrir más terreno.":
            $ decision_busqueda = "separarse"
            "Divididos en parejas, avanzan bordeando la maleza con cuidado. Cada rincón oculto se vuelve una promesa."

        "Propones buscar indicios de plantas comestibles, observando patrones de sombra y suelo.":
            $ decision_busqueda = "planta_comestible"
            "Con ojos atentos al suelo y la vegetación baja, buscas hojas que reconozcas. En un claro inesperado, algo te llama la atención."

        "Te subes a un árbol para observar la zona desde la altura.":
            $ decision_busqueda = "subir_arbol"
            "Escalas con cuidado la corteza húmeda. Desde la copa distingues un punto donde el follaje se abre: una silueta de platanales dorados en el centro."

    "{i}Con diferentes trayectorias, pero con igual sorpresa, todos convergen en el mismo lugar.{/i}"
    scene bg jungle orchard
    with Dissolve(.5)
    "{i}Frente a ustedes, un claro amplio y fértil cubierto de árboles frutales y surcos cubiertos de vegetales silvestres.{/i}"

    if "ingrid" in grupo_jugador:
        show ingrid sonriendo at center
        with Dissolve(0.5)

        if ingrid > 2:
            i "¡Esto parece un... un milagro. Debo decir, [nombre_personaje], que eres un auténtico amuleto de la suerte."
        elif ingrid < -2:
            i "Uff... esta humedad... casi tan pesada como tú. Pero al menos hay comida."
        else:
            i "Esta es la mayor cantidad de comida que vimos desde que llegamos. ¿Qué hacemos primero?"

        hide ingrid with Dissolve(0.5)

    elif "bob" in grupo_jugador:
        show bob pensando at center
        with Dissolve(0.5)
        b "Nunca pensé que encontraríamos algo así. Casi parece demasiado bueno, así que tengan cuidado, pero movámonos."
        hide bob with Dissolve(0.5)

    elif "erika" in grupo_jugador:
        show erika conversando at center
        with Dissolve(0.5)
        k "Este lugar fue trabajado. Alguien cultivó esto. Estos surcos no son producto de la erosión natural."
        hide erika with Dissolve(0.5)

    "{i}Mientras inspeccionan los márgenes, algunos del grupo encuentran piedras dispuestas en línea recta, maderas cortadas, herramientas oxidadas.{/i}"
    "{i}Hay una pala sin mango, un barril inclinado contra un árbol, raíces que crecieron sobre antiguos surcos de cultivo.{/i}"
    "{i}No hay duda. Alguien vivió aquí hace tiempo. Plantó y cuidó esta huerta... y  por alguna razón, la abandonó.{/i}"

    jump cap9_aparicion_jabali

label cap9_aparicion_jabali:

    "{i}El grupo empieza a recolectar fruta con entusiasmo contenido{/i}."
    "Algunos levantan frutos maduras del suelo mientras otros trepan ramas bajas para alcanzar otros que aún no han caído."

    if "charles" in grupo_jugador:
        show charles boca abierta at center
        with Dissolve(0.5)
        c "Shhh… ¿Escucharon eso?"
        hide charles with Dissolve(0.5)

    elif "erika" in grupo_jugador:
        show erika sorprendida at center
        with Dissolve(0.5)
        k "Silencio. Hay algo grande moviéndose entre los matorrales."
        hide erika with Dissolve(0.5)

    elif "bob" in grupo_jugador:
        show bob parado serio at center
        with Dissolve(0.5)
        b "Eso no es el viento. ¡Cuidado!"
        hide bob with Dissolve(0.5)

    "{i}Un estruendo de ramas rotas se escucha entre los arbustos. Una figura oscura emerge entre la sombra.{/i}"
    show bg jungle_boar
    with Dissolve(0.5)
    "{i}Un jabalí gigantesco, cubierto de barro, resopla con furia.{/i}"
    show bg jungle dense
    with Dissolve(0.5)
    "{i}Embiste sin aviso. La fruta sale volando por los aires. Todos corren en distintas direcciones entre gritos.{/i}"

    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Después de unos minutos de caos, logran reagruparse varios metros más lejos, jadeando.{/i}"

    if "ingrid" in grupo_jugador:
        show ingrid alterada at center
        with Dissolve(0.5)
        i "No podemos abandonar este lugar... ¿Vieron toda la fruta que había ahí? Tenemos que encontrar la forma de volver."
        hide ingrid with Dissolve(0.5)

    elif "erika" in grupo_jugador:
        show erika conversando at center
        with Dissolve(0.5)
        k "Debemos asegurar ese plantío. Hay mucha comida allí."
        hide erika with Dissolve(0.5)

    elif "bob" in grupo_jugador:
        show bob pensando at center
        with Dissolve(0.5)
        b "No podemos dejar que ese jabalí nos acose a cada paso. Debemos asegurar esa comida."
        hide bob with Dissolve(0.5)

    $ choice_position = "alta"  # default alta superior
    menu:
        "Propones retroceder, reagruparse y armar un plan":
            $ decision_inicial_jabali = "precaucion"
            "La idea de volver sin pensar no convence a nadie. Deciden reagruparse, analizar el terreno y pensar con estrategia."

        "Propones volver rápidamente a recuperar lo posible antes de que el animal regrese":
            $ decision_inicial_jabali = "impulsivo"
            "Algunos dudan, pero aceptan tu impulso. Avanzan... solo para ver al jabalí aún merodeando, rascando el suelo con sus colmillos."

        "Proponés observar desde una distancia segura y estudiar el comportamiento del jabalí":
            $ decision_inicial_jabali = "observacion"
            "Desde un claro oculto tras ramas bajas, observan. El animal parece haberse apropiado del espacio como si fuera suyo."

    "{i}Si quieren esa comida, tendrán que sacar al jabalí de allí.{/i}"

    jump cap9_discusion_planes

label cap9_discusion_planes:    
    scene bg jungle parte1_herida_cargar with Dissolve(0.5)

    "{i}Aún agitados por el susto, los miembros del grupo empiezan a discutir alternativas para recuperar el acceso al huerto.{/i}"
    "{i}El jabalí no parece dispuesto a ceder el terreno. Pero tampoco ustedes.{/i}"

    # Propuesta de plan conservador
    if "laura" in grupo_jugador:
        show laura hablando at center
        with Dissolve(0.5)
        l "Podríamos colgar trapos con savia amarga o ceniza alrededor. Eso repele a muchos animales."
        hide laura with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika parada at right
        with Dissolve(0.5)
        k "Podríamos improvisar una barrera de olores fuertes. Es poco confiable... pero quizás funcione."
        hide erika with Dissolve(0.5)
    elif "bob" in grupo_jugador:
        show bob parado serio at left
        with Dissolve(0.5)
        b "Si marcamos el área con cenizas y savia, tal vez el animal lo evite un tiempo. Puede funcionar."
        hide bob with Dissolve(0.5)

    # Propuesta de plan más complejo
    if "charles" in grupo_jugador:
        show charles serio at center
        with Dissolve(0.5)
        c "Podemos atraerlo con fruta hacia otro punto y bloquearle el retorno con troncos inclinados. Pero va a ser riesgoso."
        hide charles with Dissolve(0.5)
    elif "bob" in grupo_jugador:
        show bob parado hablando at left
        with Dissolve(0.5)
        b "Si lo cebamos bien y trabajamos rápido, podríamos encerrarlo sin lastimarlo."
        hide bob with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika conversando at right
        with Dissolve(0.5)
        k "Podríamos diseñar un corredor natural con obstáculos para devolverlo a la selva. Eso al menos nos dará tiempo para juntar fruta."
        hide erika with Dissolve(0.5)

    "{i}Pero antes de decidir una estrategia concreta, surge la gran pregunta: ¿Deberían avisarle al otro grupo?{/i}"

    $ choice_position = "default"  # default alta superior
    menu:
        "Proponés compartir el hallazgo con el otro grupo":
            $ compartir_con_otro_grupo = True
            y "Deberíamos buscar al otro grupo y compartir el hallazgo, quizá puedan ayudarnos."
            "Los otros quedan pensativos. Cruzan miradas, dudan. Nadie objeta."

        "Mejor resolver el problema nosotros. Una vez que se obtenga la comida, podemos compartirla con ellos.":
            $ compartir_con_otro_grupo = False
            "{i}Todos se miran, pero por más que parece que varios piensan lo mismo, nadie dice nada.{/i}"

    # Reacción de personajes al dilema ético
    if "marina" in grupo_jugador:
        show marina hablando at center
        with Dissolve(0.5)

        if compartir_con_otro_grupo:
            m "Tal vez si lo hacemos, esto ayude a recomponer un poco las cosas."
            m "No podemos vivir divididos para siempre, ¿no?"            
        else:
            m "Si no compartimos el hallazgo con los demás, podría ser peor si descubren que nos guardamos el secreto."
        hide marina with Dissolve(0.5)

    elif "erika" in grupo_jugador:
        show erika conversando at left
        with Dissolve(0.5)

        if compartir_con_otro_grupo:
            k "Si los incluimos, tendremos que negociar cada fruto. Pero quizás sea lo más inteligente."
        else:
            k "Se que todos estamos pensando lo mismo, pero es mejor resolver por nuestra cuenta antes de comunicar a los demás del hallazgo."
        hide erika with Dissolve(0.5)

    elif "bob" in grupo_jugador:
        show bob parado hablando at right
        with Dissolve(0.5)

        if compartir_con_otro_grupo:
            b "Tarde o temprano ellos también encontrarán este lugar. Mejor que sea ahora y entre todos espantaremos al jabalí, como ya hicimos."
        else:
            b "Se que todos están preocupados sobre qué haremos con respecto al otro grupo cuando aseguremos la fruta."
            b "Pero ese es un dilema que llegará luego de que nos deshagamos de ese jabalí."
        hide bob with Dissolve(0.5)
    
    if compartir_con_otro_grupo:
        "{i}Decisión tomada. Comienzan a volver sobre sus pasos, esperando encontrar al otro grupo aún en el refugio.{/i}"
        pause .5
        "{i}De repente, escuchan algo moverse rápido en su dirección. Se preparan, atentos.{/i}"
        "{i}Se mueve con demasiada gracia para ser el jabalí.{/i}"
        "{i}Es entonces cuando los ven. Uno a uno, reconocen a los integrantes del otro grupo, corriendo hacia ustedes.{/i}"

        if "erika" in grupo_jugador:
            show bob parado serio at centerleft
            with Dissolve(0.5)
            b "(jadeando) Creo... que... lo perdimos."
            
            show erika sorprendida at centerright
            with Dissolve(0.5)
            k "No me digan que vienen corriendo de un jabalí."

            b "Se puso... agresivo... apenas nos vió."

            k "Por casualidad, ¿estaba cubierto de barro?"

            b "No se... creo que no... Tenía... tenía el lomo moteado."

            k "Quizás haya mas de uno. Nosotros encontramos otro, que está impidiéndonos el acceso a una huerta abandonada." 
               
            hide bob with Dissolve(.5)
            hide erika with Dissolve(.5)                      

        if "bob" in grupo_jugador:
            show erika sorprendida at centerright
            with Dissolve(0.5)
            k "(jadeando) Debemos... estar... suficientemente... lejos."

            show bob parado serio at centerleft
            with Dissolve(0.5)
            b "¿De qué corrían?"

            k "Jabalí... nos sorprendió... solo atinamos a correr."

            b "Este jabalí, ¿tenía el lomo cubierto de barro?"

            k "No, tenía... vi su lomo moteado."

            b "No es el mismo que vimos nosotros entonces."

            y "Encontramos un huerto abandonado, pero otro jabalí está merodeando por allí."

            hide bob with Dissolve(.5)
            hide erika with Dissolve(.5) 

    else:
        "{i}Se mantienen en silencio durante un momento. Solucionar el problema del jabalí será difícil sin los otros, sin duda.{/i}"
        "{i}Pero de repente, escuchan algo moverse rápido en su dirección. Se preparan, atentos.{/i}"
        "{i}Se mueve con demasiada gracia para ser el jabalí.{/i}"
        "{i}Es entonces cuando los ven. Uno a uno, reconocen a los integrantes del otro grupo, corriendo hacia ustedes.{/i}"

        if "erika" in grupo_jugador:
            show bob parado serio at centerleft
            with Dissolve(0.5)
            b "(jadeando) Creo... que... lo perdimos."
            
            show erika sorprendida at centerright
            with Dissolve(0.5)
            k "No me digan que vienen corriendo de un jabalí."

            b "Se puso... agresivo... apenas nos vió."

            k "Por casualidad, ¿estaba cubierto de barro?"

            b "No se... creo que no... Tenía... tenía el lomo moteado."

            k "Nosotros encontramos otro, que está impidiéndonos el acceso a una huerta abandonada." 
               
            hide bob with Dissolve(.5)
            hide erika with Dissolve(.5)                      

        if "bob" in grupo_jugador:
            show erika sorprendida at centerright
            with Dissolve(0.5)
            k "(jadeando) Debemos... estar... suficientemente... lejos."

            show bob parado serio at centerleft
            with Dissolve(0.5)
            b "¿De qué corrían?"

            k "Jabalí... nos sorprendió... solo atinamos a correr."

            b "Este jabalí, ¿tenía el lomo cubierto de barro?"

            k "No, tenía... vi su lomo moteado."

            b "No es el mismo que vimos nosotros entonces."

            y "Encontramos un huerto abandonado, pero otro jabalí está merodeando por allí."

            hide bob with Dissolve(.5)
            hide erika with Dissolve(.5) 

    "{i}Mientras los demás recuperan el aliento, los actualizan sobre la situación, y sobre sus posibles planes para hacerse con la fruta.{/i}"           
    "{i}Es hora de elegir cómo resolver el problema del jabalí.{/i}"
    "{i}Una vez más, todos los integrantes de ambos grupos trabajarán juntos.{/i}"
    "{i}Se alejan hasta encontrar un claro donde elaborar algún plan.{/i}"

    jump cap9_eleccion_estrategia

label cap9_eleccion_estrategia:
    scene bg jungle resting_spot at truecenter
    with Dissolve(.5) 


    "{i}Luego de muchas opiniones y un largo rato discutiendo, los planes propuestos son dos.{/i}"

    "{i}Plan A: preparar una cerca con troncos, crear un corredor con frutas y redirigir al animal lejos del huerto.{/i}"
    "{i}Es ambicioso y peligroso, pero es más seguro que funcione.{/i}"

    "{i}Plan B: improvisar un perímetro con trapos, cenizas, plantas amargas y marcas olfativas que disuadan al animal.{/i}"
    "{i}Supone menores riesgos, pero no saben si funcionará, y si lo hace, van a tener que reponer los repelentes periódicamente."

    if jugador_es_lider:

        if "erika" in grupo_jugador:
            show erika conversando at center
            with Dissolve(0.5)
            k "Hay que decidir ya. ¿Qué hacemos, [nombre_personaje]?"
            hide erika with Dissolve(0.5)
        elif "bob" in grupo_jugador:
            show bob parado serio at center
            with Dissolve(0.5)
            b "La gente te va a seguir, y hablo de todos. Así que asegurate de elegir bien."
            hide bob with Dissolve(0.5)

        $ choice_position = "default"
        menu:
            "Eliges usar cebos para devolver al animal a la jungla y bloquear su acceso al huerto.":
                $ plan_elegido = "bloqueo"
                "{i}Algunos no parecen contentos, pero la gran mayoría apoya tu decisión y te lo hace saber.{/i}"
                "{i}Inmediatamente se organizan para ejecutar el desvío. Empieza la planificación.{/i}"

            "Prefieres usar trapos y ceniza como repelente y correr menos riesgos.":
                $ plan_elegido = "repelente"

                if "bob" in grupo_jugador:
                    show erika enojada at center
                    with Dissolve(0.5)
                    k "Eso no va a durar. Y volverá con más hambre."
                    hide erika with Dissolve(0.5)
                elif "erika" in grupo_jugador:
                    show bob parado enojado at center
                    with Dissolve(0.5)
                    b "¿En serio? ¿Esperás que un trapo asuste a una bola de músculo y colmillos?"
                    hide bob with Dissolve(0.5)

                "{i}Si bien nadie quiere correr riesgos, los demás ignoran tu propuesta y terminan inclinándose por el plan de bloqueo{/i}."
                "{i}Tu liderazgo es puesto en duda por primera vez.{/i}"
                $ liderazgo -= 1
                $ plan_elegido = "bloqueo"

    else:  # jugador no es líder

        if "erika" in grupo_jugador:
            show erika decidida at center
            with Dissolve(0.5)
            k "Yo propongo atraerlo fuera del huerto. Si nos organizamos, no hay riesgo mayor."
            hide erika with Dissolve(0.5)

        if "bob" in grupo_jugador:
            show bob crítico at center
            with Dissolve(0.5)
            b "Hagamos que se aleje con repelentes. Podemos organizarnos para reponerlos a tiempo para mantener el huerto seguro."
            hide bob with Dissolve(0.5)        

        $ choice_position = "default"
        menu:
            "Apoyás el plan de usar cebos para devolver al animal a la jungla.":
                $ voto_jugador = "bloqueo"
                "{i}Algunos no parecen contentos, pero la gran mayoría también apoya esa idea, y te lo hacen saber.{/i}"
                "{i}Inmediatamente se organizan para ejecutar el desvío. Empieza la planificación.{/i}"
                $ plan_elegido = "bloqueo"

            "Te inclinás por usar trapos y ceniza como repelente y correr menos riesgos.":
                $ voto_jugador = "repelente"

                if "erika" in grupo_jugador:
                    show erika fastidiada at center
                    with Dissolve(0.5)
                    k "Eso no va a durar. Y volverá con más hambre."
                    hide erika with Dissolve(0.5)                

                "{i}Si bien nadie quiere correr riesgos, los demás ignoran tu propuesta y terminan inclinándose por el plan de desvío{/i}."
                $ plan_elegido = "bloqueo"

    "El éxito requiere precisión así como rapidez, pero sobre todo, requiere trabajo en equipo."

    jump cap9_formacion_equipos

label cap9_formacion_equipos:

    "Llega el momento de repartir las tareas. Es tu oportunidad para inclinarte por la que prefieras, antes de que alguien más lo haga."

    $ choice_position = "alta"
    menu:
        "Distraer al jabalí con señuelos y ruido (riesgo alto)":
            $ grupo_jugador_elegido = 1
            $ reporte_toma_iniciativa_jabali = True
            "Eliges el riesgo. Te tocará encauzar al jabalí y estarás en la primera línea si se pone agresivo."

        "Recolectar fruta y trazar el recorrido del desvío (riesgo medio)":
            $ grupo_jugador_elegido = 2
            $ reporte_equilibrio_operativo = True
            "Eliges algo menos arriesgado. No estarás en riesgo si el jabalí se pone agresivo... a no ser que ocurran imprevistos."

        "Construir la barrera con troncos y ramas (esfuerzo físico, bajo riesgo)":
            $ grupo_jugador_elegido = 3
            $ reporte_evita_riesgo_directo = True
            "Eliges el trabajo físico. Al menos eso evitará estar expuesto si el plan va mal."

    # Liderazgos asignados a los otros dos grupos
    if grupo_jugador_elegido != 1:
        show erika parada at center
        with Dissolve(0.5)
        k "Yo me encargaré de distraer a esa bestia. Solamente espero que funcione, por mi propio bien."
        hide erika with Dissolve(0.5)

    if grupo_jugador_elegido != 2:
        show bob parado serio at center
        with Dissolve(0.5)
        b "Yo trazaré el camino con la fruta. Si algo sale mal, me gustaría estar cerca para ayudar a que nadie termine lastimado."
        hide bob with Dissolve(0.5)

    # Tomás se une automáticamente, con reacción según relación
    if tomas > 1:
        show tomas sonriendo at center
        with Dissolve(0.5)
        t "Sabía que elegirías esa tarea. Cuenta conmigo, siempre es mejor trabajar con alguien que me cae bien."
    elif tomas < -1:
        show tomas enojado at center
        with Dissolve(0.5)
        t "Iré contigo [nombre_personaje]. Este plan debe funcionar. Me aseguraré de que no lo arruines."
    else:
        show tomas serio at center
        with Dissolve(0.5)
        t "Yo iré con [nombre_personaje]. Hagámos lo mejor que podamos."
    hide tomas with Dissolve(0.5)

    $ grupo_jabaporco = []
    $ grupo_jabaporco.append("tomas")

    # Elección entre Marina y Charles como tercer miembro del grupo
    $ choice_position = "default"
    menu:
        "Pedirle a Marina que se sume":
            if marina >= 1:
                show marina sonriendo at center
                with Dissolve(0.5)
                m "¡Claro! Tu sabes escuchar y eso siempre mejora el trabajo en equipo."
            elif marina <= -1:
                show marina hablando at center
                with Dissolve(0.5)
                m "¿Yo, contigo? ¿Otra vez? Justo lo que necesitaba..."
            else:
                show marina hablando at center
                with Dissolve(0.5)
                m "Está bien. Si Tomás va, no pienso quedarme atrás."
            $ miembro_extra = "marina"
            $ grupo_jabaporco.append("marina")

        "Pedirle a Charles que se sume":
            if charles >= 1:
                show charles sonriente at center
                with Dissolve(0.5)
                c "¡Claro! Alguien tiene que acompañarlos, o Tomás te matará del aburrimiento antes de que el jabalí haya olfateado el cebo."
            elif charles <= -1:
                show charles boca abierta at center
                with Dissolve(0.5)
                c "Por más aburrido que me parezcas, Tomas trabaja por dos... Voy con ustedes."
            else:
                show charles triste at center
                with Dissolve(0.5)
                c "Supongo que todos tenemos que ayudar tarde o temprano."
            $ miembro_extra = "charles"
            $ grupo_jabaporco.append("charles")

    hide marina
    hide charles
    with Dissolve(0.5)

    "{i}El resto va con Erika o con Bob. Ustedes tres se preparan para lo que se apuntaron.{/i}"

    # Redirigir a la microescena correspondiente con condicional clásico
    if grupo_jugador_elegido == 1:
        jump cap9_mision_equipo_1
    elif grupo_jugador_elegido == 2:
        jump cap9_mision_equipo_2
    elif grupo_jugador_elegido == 3:
        jump cap9_mision_equipo_3


label cap9_mision_equipo_1:

    scene bg jungle explore 1 with fade
    show screen combined_ui

    "{i}Te alejas del claro con Tomás y [miembro_extra], cargando piedras y una bolsa con restos de fruta pasada.{/i}"
    "{i}El jabalí no está a la vista, pero sabes que acecha.{/i}"
    "{i}Los tres avanzan entre maleza, marcando árboles con olor y dejando rastro.{/i}"

    show tomas hablando at right
    with Dissolve(0.5)
    t "No hagamos ruido por ahora. Dejalo venir primero... cuando se acerque, lo mareamos."
    hide tomas with Dissolve(0.5)

    $ choice_position = "default"
    menu:
        "Propones lanzar los señuelos ahora, desde los dos lados.":
            $ decision_señuelo = "anticipada"
            $ reporte_toma_iniciativa_jabali = True
            "{i}Coordinas con los demás a través de gestos y lanzas una piedra. El ruido rebota entre los árboles.{/i}"

        "Esperás a ver una señal visual del animal antes de actuar.":
            $ decision_señuelo = "espera"
            $ reporte_decision_analitica = True
            "{i}Tratás de observar atentamente y ahí está: una sombra entre los arbustos. Ahora sí, lanzas una piedra.{/i}"

    if miembro_extra == "marina":
        if marina > 1:
            show marina hablando at left
            with Dissolve(0.5)
            m "Bien pensado. Eso lo atraerá de inmediato."
        elif marina < -1:
            show marina preocupada at left
            with Dissolve(0.5)
            m "¿Ese era el plan? ¿En serio?"
        else:
            show marina triste at left
            with Dissolve(0.5)
            m "Si esto se pone feo, yo me subo a un árbol."
        hide marina with Dissolve(0.5)

    elif miembro_extra == "charles":
        if charles > 1:
            show charles sonriente at left
            with Dissolve(0.5)
            c "Buen disparo, [nombre_personaje]. No hay chance de que no haya oído eso."
        elif charles < -1:
            show charles brazos cruzados at left
            with Dissolve(0.5)
            c "Si eso lo atrae, es solo suerte de principiante."
        else:
            show charles boca abierta at left
            with Dissolve(0.5)
            c "Solo... asegúrate de que se mantenga lejos de mi."
        hide charles with Dissolve(0.5)

    "{i}El jabalí parece haber escuchado el ruido. Avanza rápido...{/i}"
    "{i}Pero no hacia ustedes, por suerte.{/i}"
    "{i}Está siguiendo el recorrido que trazaron.{/i}"

    $ actualizar_boton_imagen()
    $ update_stat("hambre", hambre - 1)
    $ show_variable_changed_popup("El hambre ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Corren en sigilo por el costado del camino que construyeron. Desde ahí, ven al animal cruzar el sendero marcado hacia el punto de bloqueo.{/i}"
    "{i}No hay tiempo para celebrar: la emboscada tiene que cerrarse desde todos los frentes y ustedes solo hicieron parte del trabajo.{/i}"

    jump cap9_union_grupos

label cap9_mision_equipo_2:

    scene bg huerta_exterior with fade
    show screen combined_ui

    "{i} Van bordeando el claro con unos cestos improvisados con hojas de palmera. La tarea es recolectar fruta suficiente y ubicarla formando un corredor visual y olfativo.{/i}"
    "{i}Tomás va adelante, asegurándose de que nada haga que el jabalí pueda desviarse.{/i}"

    show tomas hablando at center
    with Dissolve(0.5)
    t "Si seguimos esta línea de piedras naturales, debería guiarse solo."
    t "Pero hay que marcarlo bien. Si se pierde, volverá a la huerta, donde sabe que hay comida."
    hide tomas with Dissolve(0.5)

    "{i}Aproximadamente a la mitad del recorrido ves un problema. El terreno es más escarpado de lo que parecía.{/i}"
    "{i}Las frutas pueden rodar, el animal podría no verlas, o podría incluso decidir que la huerta tiene comida más fácil de conseguir si se cansa.{/i}"

    $ choice_position = "default"
    menu:
        "Propones desviar un poco el recorrido para hacerlo menos empinado.":
            $ decision_recorrido_jabali = "adapta"
            $ reporte_toma_iniciativa_ambiental = True
            "{i}Ajustas la ruta varios metros hacia el este, donde hay más luz y la pendiente es menos pronunciada.{/i}"
            "{i}No es una solución segura, pero sin duda aumenta las chances de éxito.{/i}"

        "Decides mantener la línea, siguiendo lo acordado":
            $ decision_recorrido_jabali = "mantiene_plan"
            $ reporte_prioriza_consenso = True
            "{i}Prefieres no cambiar lo pactado. Aunque el terreno no sea ideal, confías en que el resto del plan es suficientemente sólido.{/i}"

    if miembro_extra == "marina":
        if marina > 1:
            show marina sonriendo at center
            with Dissolve(0.5)
            m "¡Vamos bien! Creo que funcionará."
        elif marina < -1:
            show marina preocupada at center
            with Dissolve(0.5)
            m "Cuando esto falle por tus malas decisiones, espero que el jabalí vaya tras de ti, y no de mi."
        else:
            show marina hablando at center
            with Dissolve(0.5)
            m "Nuestro trabajo es fácil. Espero que a los demás les esté yendo igual de bien."
        hide marina with Dissolve(0.5)

    elif miembro_extra == "charles":
        if charles > 1:
            show charles divertido at center
            with Dissolve(0.5)
            c "Si esto funciona, voy a empezar a hacerte más caso. Solo un poco más."
        elif charles < -1:
            show charles sarcástico at center
            with Dissolve(0.5)
            c "Si esto funciona, el mérito será únicamente de la fruta."
        else:
            show charles serio at center
            with Dissolve(0.5)
            c "Mientras haya fruta, el jabalí seguirá el camino, tengamos fe."
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

    "{i}Junto a Tomás y [miembro_extra] arrastran ramas gruesas, organizándolas para formar un embudo que conduzca al camino de frutas.{/i}"
    "{i}La idea es que el jabalí entre pero no pueda salir. El diseño depende de ángulos, espacio justo y algo de suerte.{/i}"

    show tomas hablando at center
    with Dissolve(0.5)
    t "Si clavamos esta rama acá, lo forzamos a tomar el camino hacia la curva. Pero no va a quedar estable... va a moverse con el primer golpe."
    hide tomas with Dissolve(0.5)

    $ choice_position = "default"
    menu:
        "Propones reforzar la base con piedras y maleza antes de clavarla":
            $ decision_estructura_segura = "refuerza"
            $ reporte_soluciona_conflicto_tecnico = True
            "{i}Buscas el punto exacto donde las raíces se etrecruzan y hundes la rama con tres piedras laterales sirviendo de refuerzo.{/i}"

        "Decides seguir el plan original y confiar en que resistirá":
            $ decision_estructura_segura = "apresura"
            $ reporte_prioriza_velocidad = True
            "{i}Tratan de clavar la rama lo más profundo que pueden. No es elegante, pero queda lista a tiempo para seguir con las siguientes.{/i}"

    if miembro_extra == "marina":
        if marina > 1:
            show marina sonriente at center
            with Dissolve(0.5)
            m "Creo que elegiste una tarea acorde a tus habilidades. Eres muy ingenioso."
        elif marina < -1:
            show marina enojada at center
            with Dissolve(0.5)
            m "Juro que parecen simios. No es tan difícil. Lo importante es que el jabalí crea que el paso està obstruído, no que realmente lo esté."
        else:
            show marina hablando at center
            with Dissolve(0.5)
            m "Si me resiste a mi, resistirá al jabalí."
        hide marina with Dissolve(0.5)

    elif miembro_extra == "charles":
        if charles > 1:
            show charles sonriendo at center
            with Dissolve(0.5)
            c "Una solución rápida y una ejecución eficaz. Felicitaciones, [nombre_personaje]."
        elif charles < -1:
            show charles enojado at center
            with Dissolve(0.5)
            c "Si el arquitecto se apura, tal vez lo terminemos a tiempo..."
        else:
            show charles brazos cruzados at center
            with Dissolve(0.5)
            c "Bueno, mientras aguante el primer empujón, estamos bien."
        hide charles with Dissolve(0.5)

    $ actualizar_boton_imagen()
    $ update_stat("cansancio", cansancio - 1)
    $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Por último aprontan la barrera para bloquear el paso una vez que el animal haya atravezado el tramo final.{/i}"

    jump cap9_union_grupos

label cap9_union_grupos:

    scene bg plano_de_trampa with fade
    show screen combined_ui

    "Los tres grupos convergen en torno a la trampa. El jabalí ha entrado en el pasillo, pero algo está mal."

    "{i}Uno de los lados de la barrera se cayó, y obstaculiza el camino.{/i}"
    "{i}El animal empieza a retroceder. Si regresa, puede escapar por el claro, o peor, atacarlos desde atrás.{/i}"

    show tomas enojado at left with Dissolve(0.5)
    t "¡Tenemos que hacer algo, antes de que pueda regresar al claro!"
    hide tomas with Dissolve(0.5)

    # Decisión crítica del jugador
    $ choice_position = "default"
    menu:
        "Tomar el liderazgo y organizar una solución rápida":
            jump cap9_reaccion_liderazgo

        "Dejar que otro tome el control":
            jump cap9_reaccion_pasiva

label cap9_reaccion_pasiva:
    $ exito_total = 0

    if "erika" in grupo_jugador or erika_es_lider:
        show erika conversando at center with Dissolve(.5)
        k "¡Tomás, con cautela! ¡Distráelo para que se de vuelta!"
        k "Ingrid, Laura, ¡cuando no esté mirando, restauren la barrera lo más rápido que puedan."
        k "Y tu, [nombre_personaje], asegúrate de atraerlo de nuevo al camino apenas lo hayan hecho."

        menu:
            "Seguir las instrucciones de Erika al pie de la letra.":
                "{i}Esperas atento a que los demás hagan su parte del plan.{/i}"
                "{i}Primero, Tomás lo distrae. Luego Ingrid y Laura corren a levantar las ramas caídas.{/i}"
                pause .5
                "{i}Cuando terminan de restaurar la barrera, comienzas a atraer al jabalí.{/i}"
                $ exito_total += 1                
                "{i}El jabalí se da vuelta en seguida, y de pronto carga. Ingrid y Laura apenas logran saltar a tiempo.{/i}"
                "{i}La bestia redirecciona al carga hacia ti, y tu reaccionas dando unos pasos hacia atrás, tropezando.{/i}"
                "{i}El jabalí roza la barrera, que resiste, y termina yéndose hacia la jungla, acorde al plan original.{/i}"
                pause .5
                "{i}Tratas de levantarte y te das cuenta de que te torciste el tobillo.{/i}"
                "{i}Esperas unos instantes y el dolor baja, no parece ser grave. Logras incorporarte{/i}"
                "{i}Tal vez no era necesario complacer a Erika con tanto entusiasmo...{/i}"
            "Priorizar la seguridad de Ingrid y Laura.":
                "{i}Esperas atento a que los demás hagan su parte del plan.{/i}"
                "{i}Primero, Tomás lo distrae. Luego Ingrid y Laura corren a levantar las ramas caídas.{/i}"
                pause .5
                "{i}Cuando ellas terminan, esperas a que te confirmen que están a salvo antes de comenzar a atraer al jabalí.{/i}"
                $ exito_total += 4                
                "{i}El jabalí se da vuelta y comienza a seguir el rastro de frutas que le vas dejando.{/i}"
                pause .5
                "{i}Termina yéndose hacia la jungla, acorde al plan original.{/i}"
                
            "Priorizar tu seguridad.":
                "{i}Esperas atento a que los demás hagan su parte del plan.{/i}"
                "{i}Primero, Tomás lo distrae. Luego Ingrid y Laura corren a levantar las ramas caídas.{/i}"
                pause .5
                "{i}Cuando ellas terminan, y saltan la barrera, comienzas a atraer al jabalí.{/i}"
                $ exito_total -= 2                 
                "{i}Te cuesta mucho que te escuche o vea, porque estás muy lejos, pero acercarte más sería peligroso.{/i}"
                "{i}Comienza a deambular. Claramente ya no te está prestando atención.{/i}"
                "{i}Por suerte es atraído por los trozos de fruta que colocaron al principio.{/i}"
                pause .5
                "{i}Termina yéndose hacia la jungla, acorde al plan original.{/i}"

    elif "bob" in grupo_jugador or bob_es_lider:
        show bob pensando at center with Dissolve(.5)
        b "¡Tomás, rápido! ¡Has que vuelva tras sus pasos para darnos algo de tiempo!"
        b "Cuando se alla alejado, Ingrid y Laura corran a levantar las ramas que cayeron de la barrera."
        b "Por último, [nombre_personaje], tu deberás asegurarte de atraerlo de vuelta cuando hayan terminado."

        menu:
            "Seguir las instrucciones de Erika al pie de la letra.":
                "{i}Esperas atento a que los demás hagan su parte del plan.{/i}"
                "{i}Primero, Tomás lo distrae. Luego Ingrid y Laura corren a levantar las ramas caídas.{/i}"
                pause .5
                "{i}Cuando terminan de restaurar la barrera, comienzas a atraer al jabalí.{/i}"
                $ exito_total += 1                
                "{i}El jabalí se da vuelta en seguida, y de pronto carga. Ingrid y Laura apenas logran saltar a tiempo.{/i}"
                "{i}La bestia redirecciona al carga hacia ti, y tu reaccionas dando unos pasos hacia atrás, tropezando.{/i}"
                "{i}El jabalí roza la barrera, que resiste, y termina yéndose hacia la jungla, acorde al plan original.{/i}"
                pause .5
                "{i}Tratas de levantarte y te das cuenta de que te torciste el tobillo.{/i}"
                "{i}Esperas unos instantes y el dolor baja, no parece ser grave. Logras incorporarte{/i}"
                "{i}Tal vez no era necesario complacer a Bob con tanto entusiasmo...{/i}"

            "Priorizar la seguridad de Ingrid y Laura.":
                "{i}Esperas atento a que los demás hagan su parte del plan.{/i}"
                "{i}Primero, Tomás lo distrae. Luego Ingrid y Laura corren a levantar las ramas caídas.{/i}"
                pause .5
                "{i}Cuando ellas terminan, esperas a que te confirmen que están a salvo antes de comenzar a atraer al jabalí.{/i}"
                $ exito_total += 4                
                "{i}El jabalí se da vuelta y comienza a seguir el rastro de frutas que le vas dejando.{/i}"
                pause .5
                "{i}Termina yéndose hacia la jungla, acorde al plan original.{/i}"
                
            "Priorizar tu seguridad.":
                "{i}Esperas atento a que los demás hagan su parte del plan.{/i}"
                "{i}Primero, Tomás lo distrae. Luego Ingrid y Laura corren a levantar las ramas caídas.{/i}"
                pause .5
                "{i}Cuando ellas terminan, y saltan la barrera, comienzas a atraer al jabalí.{/i}"
                $ exito_total -= 2                 
                "{i}Te cuesta mucho que te escuche o vea, porque estás muy lejos, pero acercarte más sería peligroso.{/i}"
                "{i}Comienza a deambular. Claramente ya no te está prestando atención.{/i}"
                "{i}Por suerte es atraído por los trozos de fruta que colocaron al principio.{/i}"
                pause .5
                "{i}Termina yéndose hacia la jungla, acorde al plan original.{/i}"

    hide erika with Dissolve(.5)
    hide bob with Dissolve(.5)

    ########## EVALUACIÓN FINAL ##########

    if exito_total >= 4:
        $ reporte_resuelve_crisis_con_liderazgo = "excelente"
        show bob saludando sucio at center with Dissolve(0.5)
        b "Lo hiciste muy bien, [nombre_personaje]."
        hide bob with Dissolve(0.5)

        show erika sonriendo at center with Dissolve(0.5)
        k "Es impresionante lo bien que trabajas bajo presión."
        hide erika with Dissolve(0.5)

    elif exito_total >= -1:
        $ reporte_resuelve_crisis_con_liderazgo = "resuelto"
        "{i}Funcionó justo a tiempo. Todavía están en shock, pero empiezan a asomar sonrisas de alivio.{/i}"

    else:
        $ reporte_resuelve_crisis_con_liderazgo = "marginal"
        "{i}El jabalí quedó atrapado por pura casualidad, y es una suerte que no tengan que lamentar heridos.{/i}"
        "{i}Todos lo saben, pero nadie dice nada.{/i}"

    jump cap9_resolucion_final_jabali

label elegir_tono(personaje):
    # ESTO AL FINAL NO SE USA
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

    "{i}Alguien debe distraer al jabalí para que otra persona se encargue de despejar el camino.{/i}"

    menu:
        "Decirle a Tomás que lo haga.":
            $ elegido = "tomas"
        "Decirle a Marina que lo haga.":
            $ elegido = "marina"

    "{i}La claridad en las órdenes es imprescindible, pero en este momento es importante cuidar la comunicación.{/i}"

    menu:
        "Pedir a [elegido] que se encargue de esta tarea, con tono gentil y persuasivo":
            $ tono = "gentil"
        "Ordenarle a [elegido] que se ponga manos a la obra, con tono directo y firme":
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
            t "Cuenta con eso."
        elif impacto >= 0:
            t "¿Distraer al jabalí? Bueno... está bien..."
        else:
            t "¡Qué fácil es para ti pedirle a otros que corran el riesgo!"

    elif elegido == "marina":
        if impacto >= 2:
            m "Si me lo pides con esos modos, lo haré con gusto."
        elif impacto >= 0:
            m "Entiendo que estamos en apuros, pero no es necesario que me des órdenes de ese modo."
        else:
            m "Si no fuera porque no quiero defraudar al resto, ni lo haría, con la forma en la que me lo pides."

    "{i}Luego de encontrar una posición elevada al costado del camino, [elegido] comienza a silbar, atrayendo la atención del jabalí.{/i}"

    ########## SEGUNDA INSTRUCCIÓN ##########

    "{i}Ahora alguien tiene que despejar el camino y restaurar la barrera.{/i}"

    menu:
        "Decirle a Ingrid que se encargue.":
            $ elegido = "ingrid"
        "Decirle a Laura que se encargue.":
            $ elegido = "laura"

    "{i}Ya tenés claro que cada persona responde a distintos tonos y formas al pedirles ayuda.{/i}"

    menu:
        "Decirle a [elegido] que se ocupe, con tono gentil y persuasivo.":
            $ tono = "gentil"
        "Darle la orden a [elegido] de que vaya a restaurar la barrera, con tono directo y firme.":
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
            i "¡Estoy en eso ya mismo!."
        elif impacto >= 0:
            i "Alcanza con que sea claro con lo que hay que hacer."
        else:
            i "¿Y a ti quién te nombró mariscal de campo? Yo me encargo solamente porque alguien tiene que hacerlo."

    elif elegido == "laura":
        if impacto >= 2:
            l "Estaba por ofrecerme, de hecho. ¡Yo me encargo!"
        elif impacto >= 0:
            l "Ya voy... pero no me hables así de nuevo, ¿sí?"
        else:
            l "¿Con ese tono? Deberías estar agradecido de que no tengo opción."


    ########## TERCERA INSTRUCCIÓN ##########

    "{i}Luego de unos segundos, [elegido] logra restaurar la barrera. Alguien debe atraer al jabalí nuevamente hacia el camino.{/i}"

    menu:
        "Decirle a Bob que lo haga.":
            $ elegido = "bob"
        "Decirle a Charles que lo haga.":
            $ elegido = "charles"

    "{i}Es importante que [elegido] entienda claramente lo que tiene que hacer.{/i}"

    menu:
        "Sugerirle a [elegido] que es la persona más indicada, usando un tono gentil y persuasivo":
            $ tono = "gentil"
        "Dirigirte a [elegido] con tono directo y firme, asegurándote de que tus órdenes sean claras.":
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
            b "Ha aflorado un buen líder en ti. Cuenta conmigo."
        elif impacto >= 0:
            b "Supongo que no hay alternativa."
        else:
            b "Está bien, pero después me critican a mi por improvisar en la marcha, ¿vieron?"

    elif elegido == "charles":
        if impacto >= 2:
            c "Por supuesto, yo lo atraeré."
        elif impacto >= 0:
            c "¿Eso fue un pedido, o una orden? En fin, yo me encargo."
        else:
            c "¿Jugando a ser el mandamás? Ahí voy, pero no porque tu me lo ordenes."

    "{i}El jabalí vuelve a encarar en la posición, siguiendo las últimas frutas.{/i}"
    "{i}Cuando ya está lejos, bajan la barrera, impidiéndole el retorno.{/i}"
    ########## EVALUACIÓN FINAL ##########

    if exito_total >= 4:
        $ reporte_resuelve_crisis_con_liderazgo = "excelente"
        show bob orgulloso at center with Dissolve(0.5)
        b "Lo hiciste muy bien, [nombre_personaje]."
        hide bob with Dissolve(0.5)

        show erika leve_smile at center with Dissolve(0.5)
        k "Es impresionante lo bien que trabajas bajo presión."
        hide erika with Dissolve(0.5)

    elif exito_total >= -1:
        $ reporte_resuelve_crisis_con_liderazgo = "resuelto"
        "{i}Funcionó justo a tiempo. Todavía están en shock, pero empiezan a asomar sonrisas de alivio.{/i}"

    else:
        $ reporte_resuelve_crisis_con_liderazgo = "marginal"
        "{i}El jabalí quedó atrapado por pura casualidad, y es una suerte que no tengan que lamentar heridos.{/i}"
        "{i}Todos lo saben, pero nadie dice nada.{/i}"

    jump cap9_resolucion_final_jabali

label cap9_resolucion_final_jabali:

    scene bg plano_de_trampa with fade
    show screen combined_ui

    "{i}El jabalí respira agitado a lo lejos mientras come un trozo de fruta pisoteada y se sigue alejando al interior de la jungla.{/i}"
    "{i}El grupo observa en silencio, recuperando el aliento mientras contemplan el éxito de su trabajo en equipo.{/i}"

    show ingrid sonriente at right with Dissolve(0.5)
    t "Lo logramos. No puedo creerlo... pero lo logramos."  

    show marina sonriendo at center with Dissolve(0.5)    
    m "¿¡Lo vieron!? ¡Eso fue trabajo en equipo de los mejores!"    

    "{i}Si lograron esto trabajando juntos, quizás haya esperanza más allá de las diferencias.{/i}"
    
    hide ingrid with Dissolve(0.5)
    hide erika with Dissolve(0.5)
    hide marina with Dissolve(0.5)
    hide tomas with Dissolve(0.5)
    hide charles with Dissolve(0.5)
    hide laura with Dissolve(0.5)
    hide bob with Dissolve(0.5)

    jump cap9_recolecta_alimentos

label cap9_recolecta_alimentos:

    scene bg jungle orchard at truecenter 
    with Dissolve(0.5)

    "{i}Mientras algunos vigilan al jabalí desde la distancia, otros comienzan a llenar canastos con frutas y verduras recuperadas del huerto.{/i}"

    "{i}Pero pronto, las miradas empiezan a pesar más que los zapallos.{/i}"

    show laura seria at left
    with Dissolve(0.5)

    l "Entonces... ¿Cómo vamos a repartir esta pequeña cosecha?"

    show marina preocupada at right
    with Dissolve(0.5)
    m "Les pido por favor que sean civilizados. No quiero pelear por un boniato mugriento, como cuando discutieron en las ruinas del refugio."

    hide laura
    with Dissolve(0.5)
    hide marina
    with Dissolve(0.5)

    show erika enojada at center 
    with Dissolve(0.5)

    "{i}Erika respira hondo y propone separar la comida en de forma proporcional a la cantidad de integrantes de cada grupo.{/i}"

    k "Si somos más, nos toca más. Si somos menos, cuidamos mejor lo que tenemos. Justo es justo."
    hide erika with Dissolve(0.5)

    "{i}No todos parecen estar del todo conformes, pero todos terminan aceptando esas condiciones.{/i}"

    jump cap9_encuentro_caja

label cap9_encuentro_caja:

    scene bg huerta_exterior sunset with fade
    show screen combined_ui

    "{i}El cielo ya se tiñe de naranja y violeta. Los insectos cantan.{/i}"
    "{i}El esfuerzo del día se siente en las espaldas cansadas, pero también en los pechos, hinchados de orgullo por el logro.{/i}"
       
    show erika parada at left
    with Dissolve(0.5)
    show bob parado hablando at right
    with Dissolve(0.5)

    k "Les sugiero que no se demoren en comer estos vegetales. En este clima, se pondrán feos rápidamente."

    b "Yo ya quiero verlos chisporrotear sobre el fuego."

    hide erika
    hide bob
    with Dissolve(0.5)

    "{i}Mientras el otro grupo se despide y enfila rumbo hacia su refugio, recorres el lugar por si quedó algo por levantar.{/i}"

    "{i}Al caminar por encima de un pequeño terraplén, sientes un golpe seco contra la suela.{/i}"
    "{i}Debajo de una capa fina de tierra, hay algo hueco semienterrado.{/i}"

    $ choice_position = "default"
    menu:
        "Patear el borde del objeto y revisar con cuidado.":
            $ reporte_descubre_objeto = True
            "{i}Remueves la tierra y quitas algunas raíces. Es una caja metálica, rectangular, carcomida por el óxido.{/i}"
            "{i}Pides ayuda a los demás para cargarla.{/i}"

        "Ignorarlo, estás agotado y quieres irte ya.":
            $ reporte_ignora_curiosidad = True
            "{i}Tu curiosidad no es mas grande que tu cansancio, así que tras un rápido vistazo, decides marcharte.{/i}"
            if "bob" in grupo_jugador or bob_es_lider:
                show bob pensando at right
                with Dissolve (0.5)
                b "¿Qué es? Quizás sea algo util."
                "{i}Observas mientras Bob lo desentierra y revisa una caja metálica, rectangular, carcomida por el óxido.{/i}"

            elif "erika" in grupo_jugador or erika_es_lider:
                show erika conversando at right
                with Dissolve (0.5)
                k "¿Qué es? Quizás sea algo util."
                "{i}Observas mientras Erika lo desentierra y revisa una caja metálica, rectangular, carcomida por el óxido.{/i}"

            "{i}Entre los dos, la cargan.{/i}" 

            hide bob with Dissolve(.5)
            hide erika with Dissolve(.5)

    "Se van turnando de dos en dos para llevarla hasta el refugio, porque es algo pesada."

    ##############################
    # VIERNES 4 HASTA ACÁ
    ##############################

    scene bg jungle night stars at truecenter
    with Dissolve(0.5)

    "{i}Ya de noche, de vuelta en el refugio, las verduras chispean en la sartén de lata.{/i}"
    "{i}El fuego y la comida caliente son la recompensa de un día lleno de acción.{/i}"
    "{i}Luego de cenar, la atención empieza a desviarse hacia la caja.{/i}"
    "{i}La rodean e intercambian miradas, esperando a ver quién será el primero que intente abrirla.{/i}"

    if "tomas" in grupo_jugador:
        "{i}Tomás fuerza una bisagra con una roca puntiaguda.. Tarda, cruje, pero finalmente se abre.{/i}"
        "{i}Tus compañeros no dejan de sorprenderte. No conoces sus historias, y cada nueva habilidad que despliegan es inesperada.{/i}"
    
    elif "charles" in grupo_jugador:
        "{i}Charles fuerza una bisagra con una roca puntiaguda.. Tarda, cruje, pero finalmente se abre.{/i}"
        "{i}Tus compañeros no dejan de sorprenderte. No conoces sus historias, y cada nueva habilidad que despliegan es inesperada.{/i}"

    elif "bob" in grupo_jugador:
        "{i}Bob fuerza una bisagra con una roca puntiaguda. Tarda, cruje, pero finalmente se abre.{/i}"
        "{i}Tus compañeros no dejan de sorprenderte. No conoces sus historias, y cada nueva habilidad que despliegan es inesperada.{/i}"

    elif "erika" in grupo_jugador:
        "{i}Erika fuerza una bisagra con una roca puntiaguda.. Tarda, cruje, pero finalmente se abre.{/i}"
        "{i}Tus compañeros no dejan de sorprenderte. No conoces sus historias, y cada nueva habilidad que despliegan es inesperada.{/i}"

    ### Etapa 1: Dibujo de la cueva
    "{i}En la parte superior, protegida por tela seca, hay una hoja de papel.{/i}"
    "{i}Está deteriorada por el tiempo, pero se nota un dibujo hecho en tinta de una cueva frente al mar, vista desde arriba.{/i}"

    if "tomas" in grupo_jugador:
        show tomas sorprendido at center
        with Dissolve(0.5)
        t "Esa debe ser la playa al este... la de los acantilados. Nunca bajamos hasta ahí."
        hide tomas with Dissolve(0.5)

    elif "charles" in grupo_jugador:
        show charles boca abierta at center
        with Dissolve(0.5)
        c "Esa debe ser la playa al este... la de los acantilados. Nunca bajamos hasta ahí."
        hide charles with Dissolve(0.5)

    elif "erika" in grupo_jugador:
        show erika sorprendida at center
        with Dissolve(0.5)
        k "Esa debe ser la playa al este... la de los acantilados. Nunca bajamos hasta ahí."
        hide erika with Dissolve(0.5)

    menu:
        "Parece hecha por alguien que conocía bien la zona.":
            y "El trazo parece ser preciso."
            y "Si nos acercamos a la zona, reconoceremos la entrada a la cueva guiándonos con el dibujo."

        "¿Y si esto no es solamente un dibujo?":
            y "Fíjense como el dibujo está hecho visto desde arriba... ¡Esto es un mapa!"    

    ### Etapa 2: Notas con símbolos
    "{i}Debajo de la tela hay una libreta pequeña, con escrituras, símbolos raros y coordenadas imprecisas.{/i}"
    "{i}Hay marcas como 'línea rota', 'abertura oculta', o 'marea alta'.{/i}"

    if "marina" in grupo_jugador:
        show marina preocupada at center with Dissolve(0.5)
        m "Estos símbolos... ¿dónde los vi antes?"  
        hide marina with Dissolve(0.5)
    elif "charles" in grupo_jugador:
        show charles boca abierta at center with Dissolve(0.5)
        c "Mmmm... ¡que gran idea! Seguir notas crípticas de libretas mohosas... ¿acaso nunca vieron una película de terror?"

    menu:
        "Quizás se trate de algún tipo de indicación.":
            y "¿Qué tal si se trata de la ubicación de la cueva, o instrucciones de cómo entrar de forma segura?"
        "Podría ser solo el delirio de otro náufrago.":
            y "Alguien con peor suerte que la nuestra debe de haberlo hecho. El hambre y la sed le hacen trampas a la mente."

    ### Etapa 3: Yodo + venda
    "{i}Por último, enrollada con cinta al fondo de la caja, hay una venda usada y un frasco cerrado de yodo.{/i}"
    "{i}Hay tierra entre las gasas, como si alguien hubiese llenado la caja a medida que cavaba el pozo.{/i}"

    if "ingrid" in grupo_jugador:
        show ingrid manos cintura at center with Dissolve(0.5)
        i "Parece que alguien estaba en apuros cuando enterró esto."
        hide ingrid with Dissolve(0.5)
    elif "laura" in grupo_jugador:
        show laura hablando at center with Dissolve(0.5)
        l "Tal vez alguien se lastimó y no quería que lo siguieran. El olor a sangre atrae depredadores."
        hide laura with Dissolve(0.5)

    menu:
        "Aquí pasó algo. Algo importante.":
            y "Esto no es solo un hallazgo. Es una historia enterrada."
        "Quizás todavía quede alguien ahí afuera." :
            y "¿Qué tal si esta persona sigue viva?"
            y "Qué tal si no estamos solos en la isla?"

    ### Etapa 4: Trozo de diario – joyas robadas
    "{i}Por último, al fondo de la caja, arrugado pero visible, encuentran un recorte de diario plastificado.'{/i}"
    "{i}La noticia lee: 'Millonario robo de joyas. Misterio y desconcierto sobre su paradero.'{/i}"

    if "tomas" in grupo_jugador:

        show tomas hablando at center with Dissolve(0.5)
        t "¿Estás diciendo que... lo que sea que hay ahí... es real?"
        hide tomas with Dissolve(0.5)

    elif "marina" in grupo_jugador:

        show marina hablando at center with Dissolve(0.5)
        t "¿Estás diciendo que... lo que sea que hay ahí... es real?"
        hide marina with Dissolve(0.5)

    elif "charles" in grupo_jugador:

        show charles boca abierta at center with Dissolve(0.5)
        t "¿Estás diciendo que... lo que sea que hay ahí... es real?"
        hide charles with Dissolve(0.5)

    elif "laura" in grupo_jugador:

        show laura hablando at center with Dissolve(0.5)
        t "¿Estás diciendo que... lo que sea que hay ahí... es real?"
        hide laura with Dissolve(0.5)

    menu:
        "Alguien se tomó muchas molestias para esconder esto.":
            y "No estoy seguro, pero tenemos que investigar más. Tal vez saquemos algo bueno de este naufragio después de todo."
        "Hoy ya es muy tarde, pero mañana deben investigar todo esto.":
            y "Descansemos, y mañana organizaremos una expedición... ¡a ver si las joyas están en esa cueva!"

    "{i}La caja queda abierta sobre una manta improvisada.{/i}"
    "{i}Cada dibujo, símbolo, trazo y coordenada invade tu mente mientras tratas de conciliar el sueño.{/i}"
    "{i}Cuando al fin cierras los ojos, sueñas con cúpulas cubiertas de lianas, pasadizos húmedos...{/i}"
    "{i}Sueñas con joyas perdidas... y jabalíes que custodian los secretos de la selva...{/i}"

    jump cap_9_continuar

label cap9_end:
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

label cap_9_continuar:
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                #jump segment_2_end
                jump chapter_10_start
            "VOLVER A VER EL RESÚMEN":
                jump cap_9_continuar
                #jump chapter_8_end
 
return

#######################################################################################   #####   ####################################################################
##########################################################################################  ##  ######################################################################
## Aca comienza la PARTE 10 ##############################################################  ##  ######################################################################
########################################################################################   ####   ####################################################################

label chapter_10_start:

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
    jump cap10_inicio_discusion_cueva

label cap10_inicio_discusion_cueva:

    $ persistent.cantidad_capitulos += 1
    $ decision_cueva = ""
    $ primera_tarea_realizada = False

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
    show screen combined_ui

    "{i}El calor de la mañana ya se cuela al interior del refugio.{/i}"
    "{i}Algunos reavivan las brasas del fuego de la noche para calentar el desayuno. Otros miran la caja abierta, en silencio.{/i}"

    if "marina" in grupo_jugador:
        if marina > 1:
            show marina hablando at left with Dissolve(0.5)
            m "Después de todo lo que pasó ayer... ¿No sienten que esa caja nos debe algo?"
        elif marina < -1:
            show marina preocupada at left with Dissolve(0.5)
            m "Ayer casi morimos por meternos con un jabalí, y ahora quieren jugar a los piratas y los tesoros... Genial."
        else:
            show marina hablando at left with Dissolve(0.5)
            m "Alguien enterró eso por una razón. Quizás deberíamos prestarle atención."
        hide marina with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika seria at center with Dissolve(0.5)
        k "Sea cual sea el misterio detrás de esa caja, merece ser investigado."
        hide erika with Dissolve(0.5)
    else:
        show bob parado serio at center with Dissolve(0.5)
        b "Prefiero que nos preocupemos en seguir vivos antes que salir a explorar misterios basados en dibujitos y leyendas."
        hide bob with Dissolve(0.5)

    if "tomas" in grupo_jugador:
        show tomas serio at right with Dissolve(0.5)
        t "¿De qué nos sirve un tesoro si no podemos salir de aquí? Yo digo que nos ocupemos de mejorar nuestra situación actual."
        hide tomas with Dissolve(0.5)

    if jugador_es_lider:
        "{i}Las miradas se clavan en vos. Esperan algo concreto. Una decisión.{/i}"
    else:
        "{i}Aunque no sos el líder, notás que los demás esperan tu opinión.{/i}"
        "{i}Quizás por tu heroísmo de ayer. O quizá porque tu fuiste el que encontró la caja.{/i}"

    $ choice_position = "default"
    menu:
        "No necesitan más misterios. Necesitan estabilidad. Y que todos conserve sus energías.":
            $ decision_cueva = "ignorar"
            y "Lo más responsable es enfocarse en sobrevivir y esperar el rescate."
        "Lo que viste te intriga. Pero sería un error arrastrar al grupo sin preparación. Primero, lo urgente.":
            $ decision_cueva = "restaurar_primero"
            y "Una vez que hayamos fortalecido el refugio, podremos explorar."
        "Lo que encontraron no parece casual. Sientes que es una pieza de algo más.":
            $ decision_cueva = "priorizar_exploracion"
            y "Investiguemos lo antes posible. Lo que haya ahí también podría ser vital para nuestra supervivencia."   

    if "erika" in grupo_jugador:
        if decision_cueva == "priorizar_exploracion":
            show erika hablando at center with Dissolve(0.5)
            k "Necesitamos toda la ayuda que podamos conseguir, es la decisión correcta."
        elif decision_cueva == "ignorar":
            show erika ceño_fruncido at center with Dissolve(0.5)
            k "¿No quieres que volvamos a enterrar la caja, ya que estamos?"
        else:
            show erika seria at center with Dissolve(0.5)
            k "Está bien. Pero no nos demoremos demasiado."
        hide erika with Dissolve(0.5)

    elif "bob" in grupo_jugador:
        if decision_cueva == "priorizar_exploracion":
            show bob parado hablando at center with Dissolve(0.5)
            b "Sea lo que sea que haya allí, más te vale que sirva para algo o todo esto será una pérdida de tiempo."
        elif decision_cueva == "ignorar":
            show bob parado hablando at center with Dissolve(0.5)
            b "Por suerte contamos con alguien con los pies en la tierra."
        else:
            show bob parado hablando at center with Dissolve(0.5)
            b "No es la peor idea. Pero espero que lo digas en serio. Nada de locas escapadas hasta terminar aquí."
        hide bob with Dissolve(0.5)

    "{i}El desayuno termina en silencio. Algunos tienen dudas. El día espera, y no va a ser fácil.{/i}"
    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)

    jump cap10_asignacion_tareas

label cap10_asignacion_tareas:

    "{i}El día comienza. El refugio aún necesita reparaciones, y hay tareas por hacer.{/i}"
    "{i}Nadie lo dice, pero todos esperan señales de organización.{/i}"

    if jugador_es_lider:
        if "marina" in grupo_jugador:
            if marina > 1:
                show marina sonriendo at left with Dissolve(0.4)
                m "Todos estamos esperando tus indicaciones, [nombre_personaje]."
            elif marina < -1:
                show marina hablando at left with Dissolve(0.4)
                m "Perfecto.... Otra jornada bajo tus órdenes. Qué emoción..."
            else:
                show marina hablando at left with Dissolve(0.4)
                m "Bueno, [nombre_personaje]. ¿Cómo quieres que nos organicemos hoy?"
            hide marina with Dissolve(0.4)
        elif "erika" in grupo_jugador:
            show erika parada at center with Dissolve(0.4)
            k "¡Vamos, [nombre_personaje]! Contamos con tu liderazgo para que este lugar aguante un día más."
            hide erika with Dissolve(0.4)
        else:
            show bob parado serio at center with Dissolve(0.4)
            b "Bueno. Tu dirás. ¿Qué quieres que hagamos?"
            hide bob with Dissolve(0.4)

        "{i}Revisas mentalmente lo que hace falta y das algunas indicaciones.{/i}"
        "{i}Decides qué tareas realizarás tu personalmente, y por cuál de ellas vas a empezar.{/i}"

        menu:
            "Recolectar leña seca en la zona oeste, que tiene árboles caídos.":
                $ tarea_jugador1 = "leña"
                jump cap10_tarea_leña_1
            "Buscar troncos gruesos en el barranco cercano, para reforzar el refugio.":
                $ tarea_jugador1 = "troncos"
                jump cap10_tarea_troncos_1
            "Revisar los recipientes de agua pluvial que tienen al norte del refugio, donde el terreno es rocoso.":
                $ tarea_jugador1 = "agua"
                jump cap10_tarea_agua_1

    else:  # Jugador no es líder
        if erika_es_lider:
            show erika conversando at center with Dissolve(0.4)
            k "Las tareas no están sujetas a negociación, pero te doy la opción de elegir en qué orden hacer las tres que te tocan."
            hide erika with Dissolve(0.4)
        elif bob_es_lider:
            show bob parado hablando at center with Dissolve(0.4)
            b "Hoy hay que moverse. Te daré a elegir cuál de las tres tareas que te tocan quieres hacer primero."
            hide bob with Dissolve(0.4)

        menu:
            "Recolectar leña seca en la zona oeste, que tiene árboles caídos.":
                $ tarea_jugador1 = "leña"
                jump cap10_tarea_leña_1
            "Buscar troncos gruesos en el barranco cercano, para reforzar el refugio.":
                $ tarea_jugador1 = "troncos"
                jump cap10_tarea_troncos_1
            "Revisar los recipientes de agua pluvial que tienen al norte del refugio, donde el terreno es rocoso.":
                $ tarea_jugador1 = "agua"
                jump cap10_tarea_agua_1

label cap10_tarea_troncos_1:

    scene bg barranco with fade
    show screen combined_ui

    "{i}El terreno aquí es más irregular. Los troncos caídos están cubiertos de líquenes, y el suelo de barro es muy resbaloso.{/i}"
    "{i}Mientras eliges uno de los troncos menos pesados para arrastrar hacia el sendero, oyes una voz que no esperabas.{/i}" 
    
    if "charles" not in grupo_jugador:
        $ cruce1 = "charles"
        show charles brazos cruzados at center with Dissolve(0.5)
        c "Qué casualidad encontrarte aquí. ¿Buscando troncos o un rato de soledad?"
    elif "ingrid" not in grupo_jugador:
        $ cruce1 = "ingrid"
        show ingrid relajada at center with Dissolve(0.5)
        i "Hola, [nombre_personaje]. Que bueno que te encuentro. Tal vez puedas sacarme una duda."
        i "Algunos en mi grupo dicen que ustedes encontraron algo interesante en esa caja."
    elif "laura" not in grupo_jugador:
        $ cruce1 = "laura"
        show laura tranquila at center with Dissolve(0.5)
        l "Hola, [nombre_personaje]. Supongo que no soy la única a la que mandaron lejos del refugio hoy, ¿no?"

    "{i}Luego de unos instantes, clava su mirada en ti de forma inquisidora... y algo en su tono cambia.{/i}"

    if cruce1 == "charles":
        c "Escuché algo entre los de mi grupo. Dicen que ustedes encontraron papeles y mapas en la caja. ¿Te suena familiar?"

    elif cruce1 == "ingrid":
        i "Me dijeron que habían encontrado coordenadas. ¿Hay algo que deberíamos saber los demás?"

    elif cruce1 == "laura":
        l "¡Escuché que tienen una caja que habla! ¿Es cierto lo que dicen? ¿Que encontraron rastros de una misteriosa historia?"

    $ choice_position = "default"
    menu:
        "Contarle la verdad sobre lo que había en la caja.":
            $ compartio_info_caja = True
            if cruce1 == "charles":
                c "Sabía que algo estaban ocultando. Gracias por tu honestidad."
                $ charles += 1
            elif cruce1 == "ingrid":
                if ingrid > 1:
                    i "Gracias por confiar en mí. Me alegra saber que todo lo que vivimos no quedó en el pasado."                   
                elif ingrid < -1:
                    i "¡No esperaba que lo confesaras todo! Para ser sincera, estaba probándote, ¡pero gracias!"
                else:
                    i "Agradezco tu sinceridad. No lo olvidaré."
                    $ ingrid += 1
            elif cruce1 == "laura":
                if laura > 1:
                    l "Me imaginaba que era algo así. Confío en ti, y agradezco que me lo confirmaras."
                elif laura < -1:
                    l "Al menos no insistes en esconderlo."
                else:
                    l "Gracias, de verdad. Mejor ir a la fuente antes que seguir con chismes."
                    $ laura += 1

        "Ocultar y minimizar lo hallado.":
            $ compartio_info_caja = False
            if cruce1 == "charles":
                c "No soy tonto, ¿sabes? No parece ser tan insignificante como lo pintas."
                $ charles -= 1
            elif cruce1 == "ingrid":
                if ingrid < -1:
                    i "Esa no me la trago. No se qué esperaba de ti, de todas formas."
                elif ingrid > 1:
                    i "No suena muy convincente, pero elijo creerte. Al menos por ahora."
                else:
                    i "Qué curioso que te guardes lo más jugoso. Pero está bien, entiendo lo que hacen."
            elif cruce1 == "laura":
                if laura < -1:
                    l "Nos subestimas, ¿sabes? Mejor guárdate tus mentiras."
                elif laura > 1:
                    l "Si estás ocultando algo, lo sabré. Pero te mereces el beneficio de la duda."
                else:
                    l "Esperaba un poco más de transparencia. Pero bueno..."

    hide charles
    hide ingrid
    hide laura
    with Dissolve(0.5)

    "{i}El silencio vuelve mientras sigues arrastrando el tronco. El aire está tenso.{/i}"
    "{i}Cada un[e] sigue su camino sin decir más.{/i}"

    jump cap10_tareas_segunda_ronda

label cap10_tarea_agua_1:

    scene bg jungle_pool with fade
    show screen combined_ui

    "{i}La caminata hacia las pendientes del norte es corta, pero empinada.{/i}"
    "{i}Los recipientes improvisados de agua siguen en su sitio, llenos de hojas húmedas y barro filtrado.{/i}"
    "{i}Mientras buscas algo para limpiarlos, sientes que no estás solo.{/i}"
    
    if "charles" not in grupo_jugador:
        $ cruce1 = "charles"
        show charles brazos cruzados at center with Dissolve(0.5)
        c "Qué casualidad encontrarte aquí. ¿Buscando leña o un rato de soledad?"
    elif "ingrid" not in grupo_jugador:
        $ cruce1 = "ingrid"
        show ingrid relajada at center with Dissolve(0.5)
        i "Hola, [nombre_personaje]. Que bueno que te encuentro. Tal vez puedas sacarme una duda."
        i "Algunos en mi grupo dicen que ustedes encontraron algo interesante en esa caja."
    elif "laura" not in grupo_jugador:
        $ cruce1 = "laura"
        show laura tranquila at center with Dissolve(0.5)
        l "Hola, [nombre_personaje]. Supongo que no soy la única a la que mandaron lejos del refugio hoy, ¿no?"

    "{i}Luego de unos instantes, clava su mirada en ti de forma inquisidora... y algo en su tono cambia.{/i}"

    if cruce1 == "charles":
        c "Escuché algo entre los de mi grupo. Dicen que ustedes encontraron papeles y mapas en la caja. ¿Te suena familiar?"

    elif cruce1 == "ingrid":
        i "Me dijeron que habían encontrado coordenadas. ¿Hay algo que deberíamos saber los demás?"

    elif cruce1 == "laura":
        l "¡Escuché que tienen una caja que habla! ¿Es cierto lo que dicen? ¿Que encontraron rastros de una misteriosa historia?"

    $ choice_position = "default"
    menu:
        "Contarle la verdad sobre lo que había en la caja.":
            $ compartio_info_caja = True
            if cruce1 == "charles":
                c "Sabía que algo estaban ocultando. Gracias por tu honestidad."
                $ charles += 1
            elif cruce1 == "ingrid":
                if ingrid > 1:
                    i "Gracias por confiar en mí. Me alegra saber que todo lo que vivimos no quedó en el pasado."                   
                elif ingrid < -1:
                    i "¡No esperaba que lo confesaras todo! Para ser sincera, estaba probándote, ¡pero gracias!"
                else:
                    i "Agradezco tu sinceridad. No lo olvidaré."
                    $ ingrid += 1
            elif cruce1 == "laura":
                if laura > 1:
                    l "Me imaginaba que era algo así. Confío en ti, y agradezco que me lo confirmaras."
                elif laura < -1:
                    l "Al menos no insistes en esconderlo."
                else:
                    l "Gracias, de verdad. Mejor ir a la fuente antes que seguir con chismes."
                    $ laura += 1

        "Ocultar y minimizar lo hallado.":
            $ compartio_info_caja = False
            if cruce1 == "charles":
                c "No soy tonto, ¿sabes? No parece ser tan insignificante como lo pintas."
                $ charles -= 1
            elif cruce1 == "ingrid":
                if ingrid < -1:
                    i "Esa no me la trago. No se qué esperaba de ti, de todas formas."
                elif ingrid > 1:
                    i "No suena muy convincente, pero elijo creerte. Al menos por ahora."
                else:
                    i "Qué curioso que te guardes lo más jugoso. Pero está bien, entiendo lo que hacen."
            elif cruce1 == "laura":
                if laura < -1:
                    l "Nos subestimas, ¿sabes? Mejor guárdate tus mentiras."
                elif laura > 1:
                    l "Si estás ocultando algo, lo sabré. Pero te mereces el beneficio de la duda."
                else:
                    l "Esperaba un poco más de transparencia. Pero bueno..."

    hide charles
    hide ingrid
    hide laura
    with Dissolve(0.5)

    "{i}El silencio vuelve mientras limpias los recipientes y, sin decir más, te deja sol[e].{/i}"

    jump cap10_tareas_segunda_ronda

label cap10_tarea_leña_1:

    scene bg jungle explore 1 with fade
    show screen combined_ui

    "{i}Te alejas hacia la zona este, donde los árboles caídos aún conservan ramas secas.{/i}"
    "{i}El suelo está cubierto de hojas húmedas y ruido de insectos.{/i}"

    "{i}Mientras levantas algunas ramas livianas, escuchás pasos en dirección opuesta. Alguien más vino por estos lados.{/i}"

    if "charles" not in grupo_jugador:
        $ cruce1 = "charles"
        show charles brazos cruzados at center with Dissolve(0.5)
        c "Qué casualidad encontrarte aquí. ¿Buscando leña o un rato de soledad?"
    elif "ingrid" not in grupo_jugador:
        $ cruce1 = "ingrid"
        show ingrid relajada at center with Dissolve(0.5)
        i "Hola, [nombre_personaje]. Que bueno que te encuentro. Tal vez puedas sacarme una duda."
        i "Algunos en mi grupo dicen que ustedes encontraron algo interesante en esa caja."
    elif "laura" not in grupo_jugador:
        $ cruce1 = "laura"
        show laura tranquila at center with Dissolve(0.5)
        l "Hola, [nombre_personaje]. Supongo que no soy la única a la que mandaron lejos del refugio hoy, ¿no?"

    "{i}Luego de unos instantes, clava su mirada en ti de forma inquisidora... y algo en su tono cambia.{/i}"

    if cruce1 == "charles":
        c "Escuché algo entre los de mi grupo. Dicen que ustedes encontraron papeles y mapas en la caja. ¿Te suena familiar?"

    elif cruce1 == "ingrid":
        i "Me dijeron que habían encontrado coordenadas. ¿Hay algo que deberíamos saber los demás?"

    elif cruce1 == "laura":
        l "¡Escuché que tienen una caja que habla! ¿Es cierto lo que dicen? ¿Que encontraron rastros de una misteriosa historia?"

    $ choice_position = "default"
    menu:
        "Contarle la verdad sobre lo que había en la caja.":
            $ compartio_info_caja = True
            if cruce1 == "charles":
                c "Sabía que algo estaban ocultando. Gracias por tu honestidad."
                $ charles += 1
            elif cruce1 == "ingrid":
                if ingrid > 1:
                    i "Gracias por confiar en mí. Me alegra saber que todo lo que vivimos no quedó en el pasado."                   
                elif ingrid < -1:
                    i "¡No esperaba que lo confesaras todo! Para ser sincera, estaba probándote, ¡pero gracias!"
                else:
                    i "Agradezco tu sinceridad. No lo olvidaré."
                    $ ingrid += 1
            elif cruce1 == "laura":
                if laura > 1:
                    l "Me imaginaba que era algo así. Confío en ti, y agradezco que me lo confirmaras."
                elif laura < -1:
                    l "Al menos no insistes en esconderlo."
                else:
                    l "Gracias, de verdad. Mejor ir a la fuente antes que seguir con chismes."
                    $ laura += 1

        "Ocultar y minimizar lo hallado.":
            $ compartio_info_caja = False
            if cruce1 == "charles":
                c "No soy tonto, ¿sabes? No parece ser tan insignificante como lo pintas."
                $ charles -= 1
            elif cruce1 == "ingrid":
                if ingrid < -1:
                    i "Esa no me la trago. No se qué esperaba de ti, de todas formas."
                elif ingrid > 1:
                    i "No suena muy convincente, pero elijo creerte. Al menos por ahora."
                else:
                    i "Qué curioso que te guardes lo más jugoso. Pero está bien, entiendo lo que hacen."
            elif cruce1 == "laura":
                if laura < -1:
                    l "Nos subestimas, ¿sabes? Mejor guárdate tus mentiras."
                elif laura > 1:
                    l "Si estás ocultando algo, lo sabré. Pero te mereces el beneficio de la duda."
                else:
                    l "Esperaba un poco más de transparencia. Pero bueno..."

    hide charles
    hide ingrid
    hide laura
    with Dissolve(0.5)

    "{i}El silencio vuelve mientras siguen recogiendo ramas. El aire está tenso.{/i}"
    "{i}Por ahora, cada uno carga lo que puede sin decir más.{/i}"

    jump cap10_tareas_segunda_ronda

label cap10_tareas_segunda_ronda:

    if tarea_jugador1 == "agua":
        "{i}Luego de llevar el agua al refugio, te detienes a decidir con qué tarea seguirás ahora.{/i}"
        menu:
            "Recolectar leña seca en la zona oeste.":
                $ tarea_jugador2 = "leña"
                jump cap10_tarea_leña_2
            "Buscar troncos gruesos en el barranco cercano":
                $ tarea_jugador2 = "troncos"
                jump cap10_tarea_troncos_2
            
    elif tarea_jugador1 == "leña":
        "{i}Luego de llevar la leña al refugio, te detienes a decidir con qué tarea seguirás ahora.{/i}"
        menu:
            "Buscar troncos gruesos en el barranco cercano":
                $ tarea_jugador2 = "troncos"
                jump cap10_tarea_troncos_2
            "Revisar los recipientes de agua pluvial que tienen al norte del refugio.":
                $ tarea_jugador2 = "agua"
                jump cap10_tarea_agua_2

    elif tarea_jugador1 == "troncos":
        "{i}Luego de llevar algunos troncos rodando al refugio, te detienes a decidir con qué tarea seguirás ahora.{/i}"
        menu:
            "Recolectar leña seca en la zona oeste.":
                $ tarea_jugador2 = "leña"
                jump cap10_tarea_leña_2
            "Revisar los recipientes de agua pluvial que tienen al norte del refugio.":
                $ tarea_jugador2 = "agua"
                jump cap10_tarea_agua_2

label cap10_tarea_leña_2:

    scene bg jungle explore 1 with fade
    show screen combined_ui

    "{i}Te alejas hacia la zona este, donde los árboles caídos aún conservan ramas secas.{/i}"
    "{i}El suelo está cubierto de hojas húmedas y ruido de insectos.{/i}"
    
    if "tomas" not in grupo_jugador:
        $ cruce2 = "tomas"
        show tomas serio at center with Dissolve(0.5)
        t "A esta altura, negarlo sería insultante. Alguien habló, [nombre_personaje]. ¿Qué encontraron en la caja?"

    elif "marina" not in grupo_jugador:
        $ cruce2 = "marina"
        show marina preocupada at center with Dissolve(0.5)
        m "¿En serio pensaban que podían ocultar algo así? Ya todos sabemos que algo había en esa caja."

    elif "laura" not in grupo_jugador and cruce1 != "laura":
        $ cruce2 = "laura"
        show laura desconfiada at center with Dissolve(0.5)
        l "No voy a jugar a los misterios. Quiero saber qué encontraron ayer antes de que esto se vuelva una guerra fría."

    elif "ingrid" not in grupo_jugador and cruce1 != "ingrid":
        $ cruce2 = "ingrid"
        show ingrid cintura at center with Dissolve(0.5)
        i "Vamos, [nombre_personaje]... Dime qué fue lo que encontraron en esa caja."

    elif "charles" not in grupo_jugador and cruce1 != "charles":
        $ cruce2 = "ingrid"
        show charles brazos cruzados at center with Dissolve(0.5)
        c "¿Por qué tanto secretismo? ¿Acaso no quieren que sepamos qué fue lo que encontraron?"

    # Elección del jugador
    $ choice_position = "default"
    menu:
        "Revelar todo lo que había en la caja: el dibujo, los símbolos y el recorte de diario.":
            $ compartio_info_caja = True

            if cruce2 == "tomas":
                t "¡Suena verdaderamente increíble! Gracias por contármelo, [nombre_personaje]"
                $ tomas += 1

            elif cruce2 == "marina":
                if marina > 1:
                    m "Sabía que podía contar contigo para llegar al fondo de esto."
                elif marina < -1:
                    m "No se en qué estaban pensando, ocultando información que podría ayudarnos a todos."
                else:
                    m "Me llevo una grata sorpresa, con tu sinceridad y apertura."
                    $ marina += 1

            elif cruce2 == "laura":
                if laura > 1:
                    l "Gracias. Te costó... pero me quedo con el gesto."
                elif laura < -1:
                    l "Tarde. Pero al menos no lo seguís escondiendo."
                else:
                    l "Está bien. A veces hace falta hablar, aunque incomode."
                    $ laura += 1

            elif cruce2 == "ingrid":
                if ingrid > 1:
                    i "Gracias por ser direct[e]. Eso ayuda más de lo que imaginas."
                elif ingrid < -1:
                    i "Bueno. Al menos ahora no estás actuando como si estuviésemos en una película de espías."
                else:
                    i "Te creo. Pero me gustaría haberlo sabido antes."
                    $ ingrid += 1
            
            elif cruce2 == "charles":
                if charles > 1:
                    c "¿Joyas robadas? ¿Una cueva? Esto se pone cada vez más digno de una novela."
                elif charles < -1:
                    c "¿Y cuándo pensaban decirnos, si yo no te preguntaba?"
                else:
                    c "Lo sabía. Gracias por confirmarlo, pero esto olía a gato encerrado."
                    $ charles += 1

        "Negarlo o decir que eran solo papeles sin sentido.":
            $ compartio_info_caja = False

            if cruce2 == "tomas":
                t "No sigas, [nombre_personaje]. Claramente no quieres decirme la verdad."
                $ tomas -= 1

            elif cruce2 == "marina":
                if marina > 1:
                    m "Duele ver que ya no confías en mi, [nombre_personaje]."
                elif marina < -1:
                    m "¿Por qué asumí que serías honesto?"
                else:
                    m "No es lo que escuché... Pero está bien, si no quieres sincerarte, no voy a obligarte."
                    

            elif cruce2 == "laura":
                if laura < -1:
                    l "No me mientas en la cara. Ya hablaremos."
                elif laura > 1:
                    l "No insistiré, pero ojalá no te arrepientas de no haber dicho la verdad, cuando sea demasiado tarde."
                else:
                    l "No me termina de convencer. Pero no voy a sacártelo a la fuerza."

            elif cruce2 == "ingrid":
                if ingrid > 1:
                    i "Me cuesta creerte. Pero supongo que tendrás tus motivos."
                elif ingrid < -1:
                    i "Sabés que esto solo empeora las cosas entre nosotros, ¿no?"
                else:
                    i "No tengo forma de comprobarlo... pero suena a que estás tratando de minimizar el hallazgo."

            elif cruce2 == "charles":
                if charles < -1:
                    c "¿Seguimos jugando a los secretos? Después no esperen ayuda."
                elif charles > 1:
                    c "No te creo, pero respeto tu derecho a jugar con las cartas pegadas al pecho. Espero que sea por buen motivo."
                else:
                    c "Te dejas muchas cosas bajo la lengua, [nombre_personaje]."            

    hide ingrid
    hide charles
    hide laura
    hide tomas
    hide marina
    with Dissolve(0.5)

    "{i}El silencio vuelve mientras siguen recogiendo ramas. El aire está tenso.{/i}"
    "{i}Por ahora, cada uno carga lo que puede sin decir más. Pero al menos queda claro: las noticias ya alcanzaron a todos.{/i}"

    jump cap10_tareas_tercera_ronda

label cap10_tarea_agua_2:

    scene bg jungle_pool with fade
    show screen combined_ui

    "{i}La caminata hacia las pendientes del norte es corta, pero empinada.{/i}"
    "{i}Los recipientes improvisados de agua siguen en su sitio, llenos de hojas húmedas y barro filtrado.{/i}"
    "{i}Mientras buscas algo para limpiarlos, sientes que no estás solo.{/i}"
    
    if "tomas" not in grupo_jugador:
        $ cruce2 = "tomas"
        show tomas serio at center with Dissolve(0.5)
        t "A esta altura, negarlo sería insultante. Alguien habló, [nombre_personaje]. ¿Qué encontraron en la caja?"

    elif "marina" not in grupo_jugador:
        $ cruce2 = "marina"
        show marina preocupada at center with Dissolve(0.5)
        m "¿En serio pensaban que podían ocultar algo así? Ya todos sabemos que algo había en esa caja."

    elif "laura" not in grupo_jugador and cruce1 != "laura":
        $ cruce2 = "laura"
        show laura desconfiada at center with Dissolve(0.5)
        l "No voy a jugar a los misterios. Quiero saber qué encontraron ayer antes de que esto se vuelva una guerra fría."

    elif "ingrid" not in grupo_jugador and cruce1 != "ingrid":
        $ cruce2 = "ingrid"
        show ingrid cintura at center with Dissolve(0.5)
        i "Vamos, [nombre_personaje]... Dime qué fue lo que encontraron en esa caja."

    elif "charles" not in grupo_jugador and cruce1 != "charles":
        $ cruce2 = "ingrid"
        show charles brazos cruzados at center with Dissolve(0.5)
        c "¿Por qué tanto secretismo? ¿Acaso no quieren que sepamos qué fue lo que encontraron?"

    # Elección del jugador
    $ choice_position = "default"
    menu:
        "Revelar todo lo que había en la caja: el dibujo, los símbolos y el recorte de diario.":
            $ compartio_info_caja = True

            if cruce2 == "tomas":
                t "¡Suena verdaderamente increíble! Gracias por contármelo, [nombre_personaje]"
                $ tomas += 1

            elif cruce2 == "marina":
                if marina > 1:
                    m "Sabía que podía contar contigo para llegar al fondo de esto."
                elif marina < -1:
                    m "No se en qué estaban pensando, ocultando información que podría ayudarnos a todos."
                else:
                    m "Me llevo una grata sorpresa, con tu sinceridad y apertura."
                    $ marina += 1

            elif cruce2 == "laura":
                if laura > 1:
                    l "Gracias. Te costó... pero me quedo con el gesto."
                elif laura < -1:
                    l "Tarde. Pero al menos no lo seguís escondiendo."
                else:
                    l "Está bien. A veces hace falta hablar, aunque incomode."
                    $ laura += 1

            elif cruce2 == "ingrid":
                if ingrid > 1:
                    i "Gracias por ser direct[e]. Eso ayuda más de lo que imaginas."
                elif ingrid < -1:
                    i "Bueno. Al menos ahora no estás actuando como si estuviésemos en una película de espías."
                else:
                    i "Te creo. Pero me gustaría haberlo sabido antes."
                    $ ingrid += 1
            
            elif cruce2 == "charles":
                if charles > 1:
                    c "¿Joyas robadas? ¿Una cueva? Esto se pone cada vez más digno de una novela."
                elif charles < -1:
                    c "¿Y cuándo pensaban decirnos, si yo no te preguntaba?"
                else:
                    c "Lo sabía. Gracias por confirmarlo, pero esto olía a gato encerrado."
                    $ charles += 1

        "Negarlo o decir que eran solo papeles sin sentido.":
            $ compartio_info_caja = False

            if cruce2 == "tomas":
                t "No sigas, [nombre_personaje]. Claramente no quieres decirme la verdad."
                $ tomas -= 1

            elif cruce2 == "marina":
                if marina > 1:
                    m "Duele ver que ya no confías en mi, [nombre_personaje]."
                elif marina < -1:
                    m "¿Por qué asumí que serías honesto?"
                else:
                    m "No es lo que escuché... Pero está bien, si no quieres sincerarte, no voy a obligarte."
                    

            elif cruce2 == "laura":
                if laura < -1:
                    l "No me mientas en la cara. Ya hablaremos."
                elif laura > 1:
                    l "No insistiré, pero ojalá no te arrepientas de no haber dicho la verdad, cuando sea demasiado tarde."
                else:
                    l "No me termina de convencer. Pero no voy a sacártelo a la fuerza."

            elif cruce2 == "ingrid":
                if ingrid > 1:
                    i "Me cuesta creerte. Pero supongo que tendrás tus motivos."
                elif ingrid < -1:
                    i "Sabés que esto solo empeora las cosas entre nosotros, ¿no?"
                else:
                    i "No tengo forma de comprobarlo... pero suena a que estás tratando de minimizar el hallazgo."

            elif cruce2 == "charles":
                if charles < -1:
                    c "¿Seguimos jugando a los secretos? Después no esperen ayuda."
                elif charles > 1:
                    c "No te creo, pero respeto tu derecho a jugar con las cartas pegadas al pecho. Espero que sea por buen motivo."
                else:
                    c "Te dejas muchas cosas bajo la lengua, [nombre_personaje]."            

    hide ingrid
    hide charles
    hide laura
    hide tomas
    hide marina
    with Dissolve(0.5)

    "{i}El silencio vuelve mientras limpias los recipientes. Pero al menos queda claro: las noticias ya alcanzaron a todos.{/i}"

    jump cap10_tareas_tercera_ronda

label cap10_tarea_troncos_2:

    scene bg barranco with fade
    show screen combined_ui

    "{i}El terreno aquí es más irregular. Los troncos caídos están cubiertos de líquenes, y el suelo de barro es muy resbaloso.{/i}"
    "{i}Mientras eliges uno de los troncos menos pesados para arrastrar hacia el sendero, oyes una voz que no esperabas.{/i}"
    
    if "tomas" not in grupo_jugador:
        $ cruce2 = "tomas"
        show tomas serio at center with Dissolve(0.5)
        t "A esta altura, negarlo sería insultante. Alguien habló, [nombre_personaje]. ¿Qué encontraron en la caja?"

    elif "marina" not in grupo_jugador:
        $ cruce2 = "marina"
        show marina preocupada at center with Dissolve(0.5)
        m "¿En serio pensaban que podían ocultar algo así? Ya todos sabemos que algo había en esa caja."

    elif "laura" not in grupo_jugador and cruce1 != "laura":
        $ cruce2 = "laura"
        show laura desconfiada at center with Dissolve(0.5)
        l "No voy a jugar a los misterios. Quiero saber qué encontraron ayer antes de que esto se vuelva una guerra fría."

    elif "ingrid" not in grupo_jugador and cruce1 != "ingrid":
        $ cruce2 = "ingrid"
        show ingrid cintura at center with Dissolve(0.5)
        i "Vamos, [nombre_personaje]... Dime qué fue lo que encontraron en esa caja."

    elif "charles" not in grupo_jugador and cruce1 != "charles":
        $ cruce2 = "ingrid"
        show charles brazos cruzados at center with Dissolve(0.5)
        c "¿Por qué tanto secretismo? ¿Acaso no quieren que sepamos qué fue lo que encontraron?"

    # Elección del jugador
    $ choice_position = "default"
    menu:
        "Revelar todo lo que había en la caja: el dibujo, los símbolos y el recorte de diario.":
            $ compartio_info_caja = True

            if cruce2 == "tomas":
                t "¡Suena verdaderamente increíble! Gracias por contármelo, [nombre_personaje]"
                $ tomas += 1

            elif cruce2 == "marina":
                if marina > 1:
                    m "Sabía que podía contar contigo para llegar al fondo de esto."
                elif marina < -1:
                    m "No se en qué estaban pensando, ocultando información que podría ayudarnos a todos."
                else:
                    m "Me llevo una grata sorpresa, con tu sinceridad y apertura."
                    $ marina += 1

            elif cruce2 == "laura":
                if laura > 1:
                    l "Gracias. Te costó... pero me quedo con el gesto."
                elif laura < -1:
                    l "Tarde. Pero al menos no lo seguís escondiendo."
                else:
                    l "Está bien. A veces hace falta hablar, aunque incomode."
                    $ laura += 1

            elif cruce2 == "ingrid":
                if ingrid > 1:
                    i "Gracias por ser direct[e]. Eso ayuda más de lo que imaginas."
                elif ingrid < -1:
                    i "Bueno. Al menos ahora no estás actuando como si estuviésemos en una película de espías."
                else:
                    i "Te creo. Pero me gustaría haberlo sabido antes."
                    $ ingrid += 1
            
            elif cruce2 == "charles":
                if charles > 1:
                    c "¿Joyas robadas? ¿Una cueva? Esto se pone cada vez más digno de una novela."
                elif charles < -1:
                    c "¿Y cuándo pensaban decirnos, si yo no te preguntaba?"
                else:
                    c "Lo sabía. Gracias por confirmarlo, pero esto olía a gato encerrado."
                    $ charles += 1

        "Negarlo o decir que eran solo papeles sin sentido.":
            $ compartio_info_caja = False

            if cruce2 == "tomas":
                t "No sigas, [nombre_personaje]. Claramente no quieres decirme la verdad."
                $ tomas -= 1

            elif cruce2 == "marina":
                if marina > 1:
                    m "Duele ver que ya no confías en mi, [nombre_personaje]."
                elif marina < -1:
                    m "¿Por qué asumí que serías honesto?"
                else:
                    m "No es lo que escuché... Pero está bien, si no quieres sincerarte, no voy a obligarte."
                    

            elif cruce2 == "laura":
                if laura < -1:
                    l "No me mientas en la cara. Ya hablaremos."
                elif laura > 1:
                    l "No insistiré, pero ojalá no te arrepientas de no haber dicho la verdad, cuando sea demasiado tarde."
                else:
                    l "No me termina de convencer. Pero no voy a sacártelo a la fuerza."

            elif cruce2 == "ingrid":
                if ingrid > 1:
                    i "Me cuesta creerte. Pero supongo que tendrás tus motivos."
                elif ingrid < -1:
                    i "Sabés que esto solo empeora las cosas entre nosotros, ¿no?"
                else:
                    i "No tengo forma de comprobarlo... pero suena a que estás tratando de minimizar el hallazgo."

            elif cruce2 == "charles":
                if charles < -1:
                    c "¿Seguimos jugando a los secretos? Después no esperen ayuda."
                elif charles > 1:
                    c "No te creo, pero respeto tu derecho a jugar con las cartas pegadas al pecho. Espero que sea por buen motivo."
                else:
                    c "Te dejas muchas cosas bajo la lengua, [nombre_personaje]."            

    hide ingrid
    hide charles
    hide laura
    hide tomas
    hide marina
    with Dissolve(0.5)

    "{i}La carga del tronco parece más liviana que esa conversación. Pero al menos queda claro: las noticias ya alcanzaron a todos.{/i}"

    jump cap10_tareas_tercera_ronda

label cap10_tareas_tercera_ronda:

    if tarea_jugador1 == "leña" and tarea_jugador2 == "troncos":
        "{i}Luego de rodar algunos troncos hasta el refugio, te diriges al norte, para revisar los recipientes de agua pluvial{/i}"
        jump cap10_tarea_agua_3

    elif tarea_jugador1 == "leña" and tarea_jugador2 == "agua":
        "{i}Luego de llevar el agua al refugio, te diriges al barranco, a ver si queda algún tronco que pueda servir.{/i}"
        jump cap10_tarea_troncos_3

    elif tarea_jugador1 == "troncos" and tarea_jugador2 == "leña":
        "{i}Luego de llevar la leña al refugio, te diriges al norte, para revisar los recipientes de agua pluvial{/i}"
        jump cap10_tarea_agua_3

    elif tarea_jugador1 == "troncos" and tarea_jugador2 == "agua":
        "{i}Luego de llevar el agua al refugio, te diriges al oeste, para buscar leña.{/i}"
        jump cap10_tarea_lena_3

    elif tarea_jugador1 == "agua" and  tarea_jugador2 == "troncos":
        "{i}Luego de rodar algunos troncos hasta el refugio, te diriges al oeste, para buscar leña.{/i}"
        jump cap10_tarea_lena_3

    elif tarea_jugador1 == "agua" and tarea_jugador2 == "leña":
        "{i}Luego de llevar la leña al refugio, te diriges al barranco, a ver si queda algún tronco que pueda servir.{/i}"
        jump cap10_tarea_troncos_3

label cap10_tarea_troncos_3:

    scene bg barranco with fade
    show screen combined_ui

    "{i}El terreno aquí es más irregular. Los troncos caídos están cubiertos de líquenes, y el suelo de barro es muy resbaloso.{/i}"
    "{i}Mientras eliges uno de los troncos menos pesados para arrastrar hacia el sendero, oyes una voz que no esperabas.{/i}"

    # Seleccionamos un personaje del otro grupo que no haya aparecido aún
    if "charles" not in grupo_jugador and cruce1 != "charles" and cruce2 != "charles":
        $ cruce3 = "charles"
        show charles serio at center with Dissolve(0.5)
        c "No sé tu, [nombre_personaje], pero a mí me gustan más los secretos cuando salen a la luz, que escondidos en cajas oxidadas."
    elif "laura" not in grupo_jugador and cruce1 != "laura" and cruce2 != "laura":
        $ cruce3 = "laura"
        show laura seria at center with Dissolve(0.5)
        l "Ya todos sabemos que había algo valioso en esa caja. La pregunta es: ¿qué vamos a hacer con eso, todos?"
    elif "ingrid" not in grupo_jugador and cruce1 != "ingrid" and cruce2 != "ingrid":
        $ cruce3 = "ingrid"
        show ingrid cintura at center with Dissolve(0.5)
        i "Lo de la caja no me sorprende. Lo que me sorprende es que nadie de ustedes haya hablado antes."
    elif "marina" not in grupo_jugador and cruce 2 != "marina":
        $ cruce3 = "marina"
        show marina preocupada at center with Dissolve(.5)
        m "Esto se está poniendo realmente incómodo, [nombre_personaje]. Quiero que te sinceres conmigo sobre esa caja."
    elif "tomas" not in grupo_jugador and cruce 2 != "tomas":
        $ cruce3 = "tomas"
        show tomas serio at center with Dissolve(0.5)
        t "No te andes con rodeos conmigo, [nombre_personaje]."
        t "Ya es hora que me cuentes lo que sabes sobre la caja. Se que la abrieron."
        

    "{i}Percibes que no vino aquí para discutir... sino para medirte. Quiere saber en qué punto estás parado con respecto al resto.{/i}"

    $ choice_position = "default"
    menu:
        "Decir que no sabes qué pensar y que te desconcierta todo lo que encontraron.":
            $ interpretacion_personal_caja = "confundido"

            if cruce3 == "charles":
                c "¿No será que simplemente no te atreves tomar partido?"

            elif cruce3 == "laura":
                if laura > 1:
                    l "Al menos admites que encontraron algo. Eso ya es algo."
                elif laura < -1:
                    l "Hmm... ¿Esperaba algo más de ti?"
                else:
                    l "No sos el único que está confundido, si sirve de consuelo."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Aprecio que no me inventes algo para conformarme. Esto es un rompecabezas gigante."
                elif ingrid < -1:
                    i "Al menos intenta actuar como si dijeras la verdad..."
                else:
                    i "No te culpo. Esto parece salido de otra vida."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Gracias, entiendo, si. Primero el jabalí, luego esto. Puede ser abrumador para cualquiera."
                elif marina < -1:
                    m "Después de todo lo que hemos pasado desde que nos encontramos en la playa, ¿me ocultas esto?"
                else:
                    m "No es sencillo, eso está claro."

            elif cruce3 == "tomas":
                t "Hmm... ya veo. ¿Pensaron que quizá sería útil que uno de nosotros le eche un vistazo?"                

        "Decir que todo es una trampa y que no deberíamos seguir ese mapa.":
            $ interpretacion_personal_caja = "temor"

            if cruce3 == "charles":
                c "Yo, la verdad, pierdo el miedo cada vez más con cada día que pasamos aquí."

            elif cruce3 == "laura":
                if laura > 1:
                    l "¿En serio? No esperaba esta cautela de ti. Es prudente, después de todo."
                elif laura < -1:
                    l "Eso es fácil de decir cuando manejas toda la información y la repartes a cuentagotas."
                else:
                    l "La isla entera es una trampa, pero puedes tener razón."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Si es una trampa, prefiero saber quién la puso y porqué."
                elif ingrid < -1:
                    i "Y si no lo es, estamos dejando pasar algo que bien podría significar nuestra salvación."
                else:
                    i "No descarto nada. Pero quedarnos quietos también puede ser un error."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Bueno, ahora que lo pones así... No lo había pensado, pero tienes razón."
                elif marina < -1:
                    m "Y a ti desde cuándo te detienen los riesgos? Me había hecho otra imagen de ti."
                else:
                    m "Puede ser, pero sin duda es algo que deberíamos decidir entre todos."

            elif cruce3 == "tomas":
                t "Tal vez, pero... ¿no te da nada de curiosidad?"

        "Admitir que quieres seguir las pistas y que quizás haya algo importante ahí.":
            $ interpretacion_personal_caja = "curioso"

            if cruce3 == "charles":
                c "¿Es ese el famoso espíritu de aventura? O tal vez sea solo ambición."

            elif cruce3 == "laura":
                if laura > 1:
                    l "Estoy segura de que todos en mi grupo opinarían lo mismo si les dieras la oportunidad de escucharte."
                elif laura < -1:
                    l "Apareció el detective... Estoy segura de que no puede ser tan complicado."
                else:
                    l "No me sorprende. Sólo ten cuidado con lo que puedas encontrar."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Entonces cuenta conmigo. Me empiezo a aburrir en esta isla."
                elif ingrid < -1:
                    i "Sería mejor que manejes tus expectativas de una forma un poco más madura."
                else:
                    i "De todo corazón: espero que tengas razón."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Ya sabes que te apoyaremos si eso es lo que quieres hacer."
                elif marina < -1:
                    m "Esto debe ser otro juego para ti. Hagamos lo que hagamos, lo haremos para sobrevivir."
                else:
                    m "Esa curiosidad nos ha dado buenos frutos en el pasado."

            elif cruce3 == "tomas":
                t "Bueno, si no regresas, ya sabremos que efectivamente... era una trampa."

    hide charles
    hide laura
    hide ingrid
    hide marina
    hide tomas
    with Dissolve(0.5) 

    "{i}Mientras haces rodar un tronco hacia el camino, te das cuenta de que ya no hay marcha atrás.{/i}"
    "{i}La información circula en ambos grupos. Y las posturas, serán variadas.{/i}"

    jump cap10_preparacion_reunion_general

label cap10_tarea_lena_3:

    scene bg jungle explore 1 with fade
    show screen combined_ui

    "{i}La caminata hacia las pendientes del norte es corta, pero empinada. Los recipientes improvisados de agua siguen en su sitio, llenos de hojas húmedas y barro filtrado.{/i}"
    "{i}Mientras removés un madero para limpiarlos, sientes que no estás solo.{/i}"

    # Seleccionamos un personaje del otro grupo que no haya aparecido aún
    if "charles" not in grupo_jugador and cruce1 != "charles" and cruce2 != "charles":
        $ cruce3 = "charles"
        show charles serio at center with Dissolve(0.5)
        c "No sé tu, [nombre_personaje], pero a mí me gustan más los secretos cuando salen a la luz, que escondidos en cajas oxidadas."
    elif "laura" not in grupo_jugador and cruce1 != "laura" and cruce2 != "laura":
        $ cruce3 = "laura"
        show laura seria at center with Dissolve(0.5)
        l "Ya todos sabemos que había algo valioso en esa caja. La pregunta es: ¿qué vamos a hacer con eso, todos?"
    elif "ingrid" not in grupo_jugador and cruce1 != "ingrid" and cruce2 != "ingrid":
        $ cruce3 = "ingrid"
        show ingrid cintura at center with Dissolve(0.5)
        i "Lo de la caja no me sorprende. Lo que me sorprende es que nadie de ustedes haya hablado antes."
    elif "marina" not in grupo_jugador and cruce 2 != "marina":
        $ cruce3 = "marina"
        show marina preocupada at center with Dissolve(.5)
        m "Esto se está poniendo realmente incómodo, [nombre_personaje]. Quiero que te sinceres conmigo sobre esa caja."
    elif "tomas" not in grupo_jugador and cruce 2 != "tomas":
        $ cruce3 = "tomas"
        show tomas serio at center with Dissolve(0.5)
        t "No te andes con rodeos conmigo, [nombre_personaje]."
        t "Ya es hora que me cuentes lo que sabes sobre la caja. Se que la abrieron."
        

    "{i}Percibes que no vino aquí para discutir... sino para medirte. Quiere saber en qué punto estás parado con respecto al resto.{/i}"

    $ choice_position = "default"
    menu:
        "Decir que no sabes qué pensar y que te desconcierta todo lo que encontraron.":
            $ interpretacion_personal_caja = "confundido"

            if cruce3 == "charles":
                c "¿No será que simplemente no te atreves tomar partido?"

            elif cruce3 == "laura":
                if laura > 1:
                    l "Al menos admites que encontraron algo. Eso ya es algo."
                elif laura < -1:
                    l "Hmm... ¿Esperaba algo más de ti?"
                else:
                    l "No sos el único que está confundido, si sirve de consuelo."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Aprecio que no me inventes algo para conformarme. Esto es un rompecabezas gigante."
                elif ingrid < -1:
                    i "Al menos intenta actuar como si dijeras la verdad..."
                else:
                    i "No te culpo. Esto parece salido de otra vida."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Gracias, entiendo, si. Primero el jabalí, luego esto. Puede ser abrumador para cualquiera."
                elif marina < -1:
                    m "Después de todo lo que hemos pasado desde que nos encontramos en la playa, ¿me ocultas esto?"
                else:
                    m "No es sencillo, eso está claro."

            elif cruce3 == "tomas":
                t "Hmm... ya veo. ¿Pensaron que quizá sería útil que uno de nosotros le eche un vistazo?"                

        "Decir que todo es una trampa y que no deberíamos seguir ese mapa.":
            $ interpretacion_personal_caja = "temor"

            if cruce3 == "charles":
                c "Yo, la verdad, pierdo el miedo cada vez más con cada día que pasamos aquí."

            elif cruce3 == "laura":
                if laura > 1:
                    l "¿En serio? No esperaba esta cautela de ti. Es prudente, después de todo."
                elif laura < -1:
                    l "Eso es fácil de decir cuando manejas toda la información y la repartes a cuentagotas."
                else:
                    l "La isla entera es una trampa, pero puedes tener razón."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Si es una trampa, prefiero saber quién la puso y porqué."
                elif ingrid < -1:
                    i "Y si no lo es, estamos dejando pasar algo que bien podría significar nuestra salvación."
                else:
                    i "No descarto nada. Pero quedarnos quietos también puede ser un error."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Bueno, ahora que lo pones así... No lo había pensado, pero tienes razón."
                elif marina < -1:
                    m "Y a ti desde cuándo te detienen los riesgos? Me había hecho otra imagen de ti."
                else:
                    m "Puede ser, pero sin duda es algo que deberíamos decidir entre todos."

            elif cruce3 == "tomas":
                t "Tal vez, pero... ¿no te da nada de curiosidad?"

        "Admitir que quieres seguir las pistas y que quizás haya algo importante ahí.":
            $ interpretacion_personal_caja = "curioso"

            if cruce3 == "charles":
                c "¿Es ese el famoso espíritu de aventura? O tal vez sea solo ambición."

            elif cruce3 == "laura":
                if laura > 1:
                    l "Estoy segura de que todos en mi grupo opinarían lo mismo si les dieras la oportunidad de escucharte."
                elif laura < -1:
                    l "Apareció el detective... Estoy segura de que no puede ser tan complicado."
                else:
                    l "No me sorprende. Sólo ten cuidado con lo que puedas encontrar."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Entonces cuenta conmigo. Me empiezo a aburrir en esta isla."
                elif ingrid < -1:
                    i "Sería mejor que manejes tus expectativas de una forma un poco más madura."
                else:
                    i "De todo corazón: espero que tengas razón."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Ya sabes que te apoyaremos si eso es lo que quieres hacer."
                elif marina < -1:
                    m "Esto debe ser otro juego para ti. Hagamos lo que hagamos, lo haremos para sobrevivir."
                else:
                    m "Esa curiosidad nos ha dado buenos frutos en el pasado."

            elif cruce3 == "tomas":
                t "Bueno, si no regresas, ya sabremos que efectivamente... era una trampa."

    hide charles
    hide laura
    hide ingrid
    hide marina
    hide tomas
    with Dissolve(0.5)    

    "{i}Mientras recoges las últimas ramas, te das cuenta de que ya no hay marcha atrás.{/i}"
    "{i}La información circula en ambos grupos. Y las posturas, serán variadas.{/i}"

    jump cap10_preparacion_reunion_general

label cap10_tarea_agua_3:

    scene bg jungle_pool with fade
    show screen combined_ui

    "{i}La caminata hacia las pendientes del norte es corta, pero empinada. Los recipientes improvisados de agua siguen en su sitio, llenos de hojas húmedas y barro filtrado.{/i}"
    "{i}Mientras removés un madero para limpiarlos, sientes que no estás solo.{/i}"

    # Seleccionamos un personaje del otro grupo que no haya aparecido aún
    if "charles" not in grupo_jugador and cruce1 != "charles" and cruce2 != "charles":
        $ cruce3 = "charles"
        show charles serio at center with Dissolve(0.5)
        c "No sé tu, [nombre_personaje], pero a mí me gustan más los secretos cuando salen a la luz, que escondidos en cajas oxidadas."
    elif "laura" not in grupo_jugador and cruce1 != "laura" and cruce2 != "laura":
        $ cruce3 = "laura"
        show laura seria at center with Dissolve(0.5)
        l "Ya todos sabemos que había algo valioso en esa caja. La pregunta es: ¿qué vamos a hacer con eso, todos?"
    elif "ingrid" not in grupo_jugador and cruce1 != "ingrid" and cruce2 != "ingrid":
        $ cruce3 = "ingrid"
        show ingrid cintura at center with Dissolve(0.5)
        i "Lo de la caja no me sorprende. Lo que me sorprende es que nadie de ustedes haya hablado antes."
    elif "marina" not in grupo_jugador and cruce 2 != "marina":
        $ cruce3 = "marina"
        show marina preocupada at center with Dissolve(.5)
        m "Esto se está poniendo realmente incómodo, [nombre_personaje]. Quiero que te sinceres conmigo sobre esa caja."
    elif "tomas" not in grupo_jugador and cruce 2 != "tomas":
        $ cruce3 = "tomas"
        show tomas serio at center with Dissolve(0.5)
        t "No te andes con rodeos conmigo, [nombre_personaje]."
        t "Ya es hora que me cuentes lo que sabes sobre la caja. Se que la abrieron."        

    "{i}Percibes que no vino aquí para discutir... sino para medirte. Quiere saber en qué punto estás parado con respecto al resto.{/i}"

    $ choice_position = "default"
    menu:
        "Decir que no sabes qué pensar y que te desconcierta todo lo que encontraron.":
            $ interpretacion_personal_caja = "confundido"

            if cruce3 == "charles":
                c "¿No será que simplemente no te atreves tomar partido?"

            elif cruce3 == "laura":
                if laura > 1:
                    l "Al menos admites que encontraron algo. Eso ya es algo."
                elif laura < -1:
                    l "Hmm... ¿Esperaba algo más de ti?"
                else:
                    l "No sos el único que está confundido, si sirve de consuelo."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Aprecio que no me inventes algo para conformarme. Esto es un rompecabezas gigante."
                elif ingrid < -1:
                    i "Al menos intenta actuar como si dijeras la verdad..."
                else:
                    i "No te culpo. Esto parece salido de otra vida."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Gracias, entiendo, si. Primero el jabalí, luego esto. Puede ser abrumador para cualquiera."
                elif marina < -1:
                    m "Después de todo lo que hemos pasado desde que nos encontramos en la playa, ¿me ocultas esto?"
                else:
                    m "No es sencillo, eso está claro."

            elif cruce3 == "tomas":
                t "Hmm... ya veo. ¿Pensaron que quizá sería útil que uno de nosotros le eche un vistazo?"                

        "Decir que todo es una trampa y que no deberíamos seguir ese mapa.":
            $ interpretacion_personal_caja = "temor"

            if cruce3 == "charles":
                c "Yo, la verdad, pierdo el miedo cada vez más con cada día que pasamos aquí."

            elif cruce3 == "laura":
                if laura > 1:
                    l "¿En serio? No esperaba esta cautela de ti. Es prudente, después de todo."
                elif laura < -1:
                    l "Eso es fácil de decir cuando manejas toda la información y la repartes a cuentagotas."
                else:
                    l "La isla entera es una trampa, pero puedes tener razón."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Si es una trampa, prefiero saber quién la puso y porqué."
                elif ingrid < -1:
                    i "Y si no lo es, estamos dejando pasar algo que bien podría significar nuestra salvación."
                else:
                    i "No descarto nada. Pero quedarnos quietos también puede ser un error."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Bueno, ahora que lo pones así... No lo había pensado, pero tienes razón."
                elif marina < -1:
                    m "Y a ti desde cuándo te detienen los riesgos? Me había hecho otra imagen de ti."
                else:
                    m "Puede ser, pero sin duda es algo que deberíamos decidir entre todos."

            elif cruce3 == "tomas":
                t "Tal vez, pero... ¿no te da nada de curiosidad?"

        "Admitir que quieres seguir las pistas y que quizás haya algo importante ahí.":
            $ interpretacion_personal_caja = "curioso"

            if cruce3 == "charles":
                c "¿Es ese el famoso espíritu de aventura? O tal vez sea solo ambición."

            elif cruce3 == "laura":
                if laura > 1:
                    l "Estoy segura de que todos en mi grupo opinarían lo mismo si les dieras la oportunidad de escucharte."
                elif laura < -1:
                    l "Apareció el detective... Estoy segura de que no puede ser tan complicado."
                else:
                    l "No me sorprende. Sólo ten cuidado con lo que puedas encontrar."

            elif cruce3 == "ingrid":
                if ingrid > 1:
                    i "Entonces cuenta conmigo. Me empiezo a aburrir en esta isla."
                elif ingrid < -1:
                    i "Sería mejor que manejes tus expectativas de una forma un poco más madura."
                else:
                    i "De todo corazón: espero que tengas razón."

            elif cruce3 == "marina":
                if marina > 1:
                    m "Ya sabes que te apoyaremos si eso es lo que quieres hacer."
                elif marina < -1:
                    m "Esto debe ser otro juego para ti. Hagamos lo que hagamos, lo haremos para sobrevivir."
                else:
                    m "Esa curiosidad nos ha dado buenos frutos en el pasado."

            elif cruce3 == "tomas":
                t "Bueno, si no regresas, ya sabremos que efectivamente... era una trampa."

    hide charles
    hide laura
    hide ingrid
    hide marina
    hide tomas
    with Dissolve(0.5)

    "{i}Mientras limpias los recipientes, te das cuenta de que ya no hay marcha atrás.{/i}"
    "{i}La información circula en ambos grupos. Y las posturas, serán variadas.{/i}"

    jump cap10_preparacion_reunion_general

label cap10_preparacion_reunion_general:

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)
    show screen combined_ui

    "{i}Ya de regreso, luego de las tareas, el refugio huele a humo y humedad.{/i}"
    "{i}Pero algo se siente raro. ALgo está fuera de lugar.{/i}"

    if "tomas" in grupo_jugador:
        show tomas enojado at center with Dissolve(0.5)
        t "¿Alguien movió el cuaderno? Lo dejé en la caja envuelto con la manta. Y ahora no está."
        hide tomas with Dissolve(0.5)
    elif "erika" in grupo_jugador:
        show erika enojada at center with Dissolve(0.5)
        k "Esperen... ¿y el cuaderno? Yo misma lo vi ahí esta mañana."
        hide erika with Dissolve(0.5)
    else:
        show bob parado enojado at center with Dissolve(0.5)
        b "No encuentro el cuaderno. Ni la manta que lo cubría. ¿Alguien lo movió sin avisar?"
        hide bob with Dissolve(0.5)

    "{i}Revisan cada rincón. Nada. Sólo cenizas del fuego de la noche, y ropa colgada. El cuaderno desapareció.{/i}"
    
    y "Tenemos que llamar a los del otro grupo. Si alguien lo agarró, más vale que lo diga ahora mismo."
    
    pause 1    

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)

    "{i}Un rato después, la persona que fue a buscarlos vuelve con ellos.{/i}"
    "{i}Sus rostros son serios, como juzgándolos a ustedes por ocultar información.{/i}"
    "{i}Sin embargo, falta gente.{/i}"
   
    jump cap10_reunion_doble_grupo

label cap10_reunion_doble_grupo:    

    y "Faltan dos personas. ¿Dónde están Laura y Charles?"
    y "¿Y ustedes... alguno tomó el cuaderno que estaba en esta caja?"

    "{i}Ninguno de ellos parece saber de qué hablas. En cuestión de segundos, todos llegan a la misma conclusión.{/i}"
    "{i}La explicación más lógica es que Laura y Charles se hayan ido solos a seguir las pistas.{/i}"
    "{i}Todos se sienten traicionados. Ellos, y ustedes. Al menos esto distrae a los demás del enojo con el que llegaron.{/i}"
    
    if "erika" in grupo_jugador:
        show erika enojada at left with Dissolve(0.5)
        k "¿Quién me va a explicar qué es lo que está pasando aquí?"
        "{i}Erika se voltea hacia ti y el resto de los de tu grupo.{/i}"
        k "Si uno de ellos tomó el cuaderno, es porque uno de nosotros abrió la boca. Y yo se que no fui yo."

        show bob parado enojado at right with Dissolve(0.5)
        b "¿De qué sirve eso ahora? Si alguien desapareció, tal vez tenga que ver con que entre ustedes hubiesen tantos secretos."
        b "Claramente decidió contactar a alguien de nuestro grupo. Solo lamento que hayan decidido ir solos."

    elif "bob" in grupo_jugador:
        show bob parado enojado at right with Dissolve(0.5)
        b "Bueno, si no saben nada sobre la desaparición del cuaderno, tal vez nos puedan decir cómo fue que se enteraron de su existencia."
        b "A esta altura está claro que toda la información sobre la caja se filtró y desparramó muy rápidamente."

        show erika enojada at left with Dissolve(0.5)
        k "¿Y nosotros qué culpa tenemos?"
        k "Aunque estemos separados, todos hemos forjado vínculos que no se romperán de un día para el otro."
        k "Alguien en tu grupo decidió compartir la información, [nombre_personaje]. Yo celebro que lo haya hecho."

    show marina preocupada at centerleft with Dissolve(0.5)
    m "Lo sabíamos y no les dijimos nada."
    m "Eso probablemente sea lo más doloroso para ustedes."
    m "Fue una mala idea. Ojalá puedan perdonarnos."
    hide marina with Dissolve(0.5)
    
    show ingrid cintura at centerright with Dissolve(0.5)
    i "Si alguien decidió filtrarlo, ya se habrán dado cuenta de que los demás lo sabíamos y eligimos ocultarlo."
    i "Eso quizá sea más problemático, pero espero que decidan perdonarnos por eso. No debimos hacerlo."
    hide ingrid with Dissolve(0.5)
    
    show tomas serio at center with Dissolve(0.5)        
    t "Yo vi a Laura y Charles hablando con disimulo esta mañana."
    t "Ahora solo puedo imaginar que se trataba de algo relacionado a la caja."
    t "No se cuál de los dos le contó al otro, pero no puede haber pasado mucho tiempo antes de que los rumores comenzaran a volar."
    hide tomas with Dissolve(0.5)

    "{i}El silencio es incómodo. Todos lo sabían.{/i}"

    # Participación del jugador: cómo enfrenta el conflicto
    menu:
        "Intentas calmar la situación con argumentos prácticos.":
            $ enfoque_jugador = "practico"
            y "No importa quién filtró la información. Lo que importa ahora es que los que se fueron pueden estar en peligro."

        "Intentas negociar para que se retome la calma y se piense en conjunto.":
            $ enfoque_jugador = "negociador"
            y "Si queremos encontrarlos, tenemos que restaurar la confianza."
            y "Tal vez no sea justo pedírselos luego de lo que pasó, pero ellos dependen de que trabajemos juntos."

        "Acusas al otro grupo de haber robado el cuaderno y/o facilitado la huida.":
            $ enfoque_jugador = "acusador"
            y "Me pregunto cuánta ayuda habrán tenido desde dentro. Tal vez no todos ustedes estén libres de culpa."

    "{i}El clima de la conversación es nefasto, pero lo inevitable ya está dicho y no pueden quedarse esperando.{/i}"
    y "Dos personas salieron en dirección al mar. Tal vez hacia esa playa con los acantilados."
    y "Hay que salir a buscarles... aunque no podamos hacer de cuenta que aca no ha pasado nada."

    hide bob 
    with Dissolve(0.5)
    hide erika
    with Dissolve(0.5)
    "{i}Deciden dividirse en dos equipos para buscar a Laura y Charles.{/i}"

    jump cap10_formacion_equipo_exploracion

label cap10_formacion_equipo_exploracion:

    if not equipo_exploracion:
        $ equipo_exploracion = []


    "{i}Tienes que elegir con quién te vas a aventurar hacia la playa.{/i}"
    "{i}Solo aceptarán ir contigo si confían en ti o si ya son parte de tu grupo y al menos te soportan...{/i}"

    $ choice_position = "superior"

    menu:
        "Invitar a Marina" if not invitar_marina:
            jump cap10_invitar_marina
        "Invitar a Bob" if not invitar_bob:
            jump cap10_invitar_bob
        "Invitar a Erika" if not invitar_erika:
            jump cap10_invitar_erika
        "Invitar a Ingrid" if not invitar_ingrid:
            jump cap10_invitar_ingrid
        "Invitar a Tomás" if not invitar_tomas:
            jump cap10_invitar_tomas
        "No parece que nadie quiera ir contigo" if (invitar_marina and invitar_bob and invitar_erika and invitar_ingrid and invitar_tomas and len(equipo_exploracion) == 0):
            jump cap10_soledad_post_fallo
        "Solo una persona aceptó sumarse" if (invitar_marina and invitar_bob and invitar_erika and invitar_ingrid and invitar_tomas and len(equipo_exploracion) == 1):
            jump cap10_soledad_post_fallo

label cap10_soledad_post_fallo:

    scene bg refugio_exterior with fade
    show screen combined_ui

    "{i}Tus intentos de conformar un grupo no tuvieron mucho éxito.{/i}"

    if jugador_es_lider:
        "{i}Eres el líder de unos grupos, pero empiezas a entender que a veces el liderazgo no significa apoyo ciego en todo.{/i}"
        "{i}Sobredimensionaste la confianza que te tienen los demás.{/i}"
    else:
        "{i}Quizá no seas el líder de ninguno de los grupos, pero aún así sientes la frustración de haber querido hacer algo y no haber podido contar con nadie.{/i}"

    "{i}¿Habrás hecho algo mal? ¿O simplemente tus decisiones dejaron marcas más hondas de lo que imaginabas?{/i}"

    if len(equipo_exploracion) == 1:

        "{i}Sientes una mano en el hombro que trata de confortarte.{/i}"

        if "bob" in equipo_exploracion:
            show bob parado hablando at center with Dissolve(.5)
            b "Iré a ver si puedo convencer a alguien más."
            pause .5
            "{i}Bob vuelve a los pocos minutos.{/i}"
            "{i}Marina lo acompaña.{/i}"
            $ equipo_exploracion.append("marina")

        elif "erika" in equipo_exploracion:
            show erika parada at center with Dissolve(.5)
            k "Iré a ver si puedo convencer a alguien más."
            pause .5
            "{i}Erika vuelve a los pocos minutos.{/i}"
            "{i}Tomás la acompaña.{/i}"
            $ equipo_exploracion.append("tomas")

        elif "marina" in equipo_exploracion:
            show marina hablando at center with Dissolve(.5)
            m "Iré a ver si puedo convencer a alguien más."
            pause .5
            "{i}Marina vuelve a los pocos minutos.{/i}" 
            "{i}Ingrid la acompaña.{/i}"
            $ equipo_exploracion.append("ingrid")

        elif "ingrid" in equipo_exploracion:
            show ingrid cintura at center with Dissolve(.5)
            i "Iré a ver si puedo convencer a alguien más."
            pause .5
            "{i}Ingrid vuelve a los pocos minutos.{/i}"
            "{i}Tomás la acompaña.{/i}"
            $ equipo_exploracion.append("tomas")                        

        elif "tomas" in equipo_exploracion:
            show tomas hablando at center with Dissolve(.5)
            t "Iré a ver si puedo convencer a alguien más."
            pause .5
            "{i}Tomás vuelve a los pocos minutos.{/i}"
            "{i}Marina lo acompaña.{/i}"
            $ equipo_exploracion.append("marina")

    else:
        "{i}Reflexionas sobre esa idea y reconoces que hay cosas por las que nunca pediste perdón.{/i}"

        menu:
            "Volver y explicarle a todos que no te habías detenido a pensar en todas las veces que les has fallado.":
                "{i}Ellos sonríen, asienten, y alguno hasta te abraza, agradecido.{/i}"
                "{i}Ingrid y Tomás dan un paso adelante y acceden a ir contigo.{/i}"
                $ equipo_exploracion.append("tomas")
                $ equipo_exploracion.append("ingrid")

            "No es tiempo de autocrítica. Si nadie quiere acompañarte, tendrás que ir sol[e].":
                "{i}Miras el cielo para orientarte y te propones emprender la marcha hacia la costa.{/i}"
                "{i}De repente escuchas pasos detrás tuyo. Volteas, al parecer alguien está tratando de alcanzarte.{/i}"

                "{i}Ingrid se te acerca en silencio, y se posiciona a tu lado, mostrando su apoyo y voluntad de seguirte.{/i}"
                $ equipo_exploracion.append("ingrid")
                pause .5
                "{i}Escuchas nuevamente movimiento detrás de ustedes.{/i}"                    
                "{i}Parece que alguien más se acerca.{/i}"

    jump cap10_exploracion_inicio           
      
label cap10_invitar_marina:

    $ invitar_marina = True

    if ("marina" in grupo_jugador and marina >= 0) or ("marina" not in grupo_jugador and marina > 0):
        show marina sonriente at center with Dissolve(0.4)
        m "¿Que si quiero ir contigo? ¡Claro!"
        m "Si encontraron algo raro, quiero estar ahí."
        $ equipo_exploracion.append("marina")
    else:
        show marina preocupada at center with Dissolve(0.4)
        m "No. No confío en ti, tus métodos y tus prioridades. Lo lamento."

    hide marina with Dissolve(0.4)

    if len(equipo_exploracion) == 2:
        jump cap10_exploracion_inicio
    else:
        jump cap10_formacion_equipo_exploracion

label cap10_invitar_bob:

    $ invitar_bob = True

    if ("bob" in grupo_jugador and bob >= 0) or ("bob" not in grupo_jugador and bob > 0):
        show bob parado hablando at center with Dissolve(0.4)
        b "Bien. Salgamos rápido, y mantengamos los ojos abiertos."
        $ equipo_exploracion.append("bob")
    else:
        show bob parado serio at center with Dissolve(0.4)
        b "No. Ya no es lo mismo. Si alguna vez te ganaste una pizca de mi confianza, la has perdido."
        b "Elige a alguien más."

    hide bob with Dissolve(0.4)

    if len(equipo_exploracion) == 2:
        jump cap10_exploracion_inicio
    else:
        jump cap10_formacion_equipo_exploracion

label cap10_invitar_erika:

    $ invitar_erika = True

    if ("erika" in grupo_jugador and erika >= 0) or ("erika" not in grupo_jugador and erika > 0):
        show erika parada at center with Dissolve(0.4)
        k "Acepto. Puede ser que necesites de mis habilidades para superar esta crisis después de todo."
        $ equipo_exploracion.append("erika")
    else:
        show erika enojada at center with Dissolve(0.4)
        k "La verdad es que no has demostrado gran capacidad para la resolución de problemas desde que nos conocimos."
        k "Lo siento, pero la respuesta es no."
        hide erika with Dissolve(0.4)

    if len(equipo_exploracion) == 2:
        jump cap10_exploracion_inicio
    else:
        jump cap10_formacion_equipo_exploracion

label cap10_invitar_ingrid:

    $ invitar_ingrid = True

    if ("ingrid" in grupo_jugador and ingrid >= 0) or ("ingrid" not in grupo_jugador and ingrid > 0):
        show ingrid sonriente at center with Dissolve(0.4)
        i "¡Por supuesto! Necesito saber qué está pasando allá abajo."
        $ equipo_exploracion.append("ingrid")
    else:
        show ingrid cintura at center with Dissolve(0.4)
        i "Me cuesta creer que tendrás la seguridad y salud de Laura y Charles como tu primera prioridad."
        i "Tendrás que encontrar a alguien más."
        hide ingrid with Dissolve(0.4)

    if len(equipo_exploracion) == 2:
        jump cap10_exploracion_inicio
    else:
        jump cap10_formacion_equipo_exploracion 

label cap10_invitar_tomas:

    $ invitar_tomas = True

    if ("tomas" in grupo_jugador and tomas >= 0) or ("tomas" not in grupo_jugador and tomas > 0):
        show tomas hablando at center with Dissolve(0.4)
        t "Cuenta conmigo. Quiero respuestas, al misterio, y a qué hizo que pensaran que ir tras sus pistas era buena idea."
        $ equipo_exploracion.append("tomas")
    else:
        show tomas enojado at center with Dissolve(0.4)
        t "Prefiero quedarme a garantizar el bienestar de los que no hemos decidido unilateralmente correr riesgos innecesarios."
        hide tomas with Dissolve(0.4)

    if len(equipo_exploracion) == 2:
        jump cap10_exploracion_inicio
    else:
        jump cap10_formacion_equipo_exploracion

label cap10_exploracion_inicio:

    scene bg beach sunny at truecenter
    with Dissolve(0.5)

    "{i}El mar está en calma y la orilla está retirada por la marea baja.{/i}"
    "{i}El grupo camina bordeando la costa. La arena está húmeda.{/i}"
    "{i}En ella hay dos pares de huellas frescas.{/i}"    

    # Uno del grupo señala las huellas
    if "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "¿Ya sabes lo que significa eso, verdad [nombre_personaje]?"
        y "Estas huellas fueron hechas luego de que la marea bajara."
        y "No pueden llevarnos mucha ventaja."
        hide ingrid with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "Mira eso, [nombre_personaje]."
        y "Estas huellas fueron hechas luego de que la marea bajara."
        y "No pueden llevarnos mucha ventaja."
        hide bob with Dissolve(0.4)

    elif "tomas" in equipo_exploracion:
        show tomas cruzado at left with Dissolve(0.4)
        t "Dos pares de huellas. ¡Seguro son Laura y Charles!"
        y "Estas huellas fueron hechas luego de que la marea bajara."
        y "No pueden llevarnos mucha ventaja."
        hide tomas with Dissolve(0.4)

    elif "erika" in equipo_exploracion:
        show erika preocupada at left with Dissolve(0.4)
        k "Las huellas van en una dirección clara. Tienen que ser ellos."
        y "Estas huellas fueron hechas luego de que la marea bajara."
        y "No pueden llevarnos mucha ventaja."
        hide erika with Dissolve(0.4)

    elif "marina" in equipo_exploracion:
        show marina alerta at center with Dissolve(0.4)
        m "Uff... miren lo profundas que son esas huellas. Caminar en esta arena si que es duro."
        y "Estas huellas fueron hechas luego de que la marea bajara."
        y "No pueden llevarnos mucha ventaja."
        hide marina with Dissolve(0.4)

    "{i}Mientras siguen la línea de huellas, alguien más en el equipo rompe el silencio.{/i}"

    if "marina" in equipo_exploracion:
        show marina alerta at center with Dissolve(0.4)
        m "Cuidemos nuestras energías, ¿si? No sabemos qué nos espera cuando los encontremos."
        hide marina with Dissolve(0.4)

    elif "erika" in equipo_exploracion:
        show erika preocupada at left with Dissolve(0.4)
        k "¿Y si fue uno de ellos quien convenció al otro?"
        hide erika with Dissolve(0.4)

    elif "tomas"in equipo_exploracion:
        show tomas cruzado at left with Dissolve(0.4)
        t "No me gusta esto. Si se fueron sin decir nada, ¿cómo podemos confiar en ellos?"
        hide tomas with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "Espero que los encontremos antes de que hagan alguna locura."       
        hide bob with Dissolve(0.4)

    elif "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "No tenemos cómo perder este rastro, siempre y cuando no perdamos el tiempo."        
        hide ingrid with Dissolve(0.4)
    
    $ choice_position = "alta"
    menu:
        "Sentenciar que probablemente se fueron por puro egoísmo o falta de criterio. No se los puede justificar.":
            $ postura_jugador_desaparecidos = "critico"
            y "Quisieron ser los únicos en encontrar el secreto y ahora nosotros estamos aquí de todas formas, buscándolos."

        "Sugerir que tal vez tenían razones válidas. No es justo juzgar sin saber.":
            $ postura_jugador_desaparecidos = "comprensivo"
            y "No sabemos lo que pensaban. Tal vez solo querían hacer lo correcto y solamente fueron impulsivos."

        "Admitir que tu también hubieras sentido la tentación de ser el primero en ir a descubrir el misterio.":
            $ postura_jugador_desaparecidos = "autocritico"
            y "Yo también sentí que había que moverse rápido. No lo apruebo, pero los entiendo."

    "{i}Caminan en silencio tratando de no darle más vueltas al asunto.{/i}"
    "{i}La jungla, a un lado, forma un muro que enfrenta el viento salado.{/i}"
    "{i}El mar, del otro lado, se impone como una frontera insondable.{/i}" #GOTY

    scene bg costa_bifurcacion with fade

    "{i}Llegan al punto donde el paisaje cambia.{/i}"
    "{i}Una extensa zona de rocas antes ocultas por el mar se abre como una lengua gris entre espuma y mejillones.{/i}"
    "{i}Detrás de ella, un complejo de grutas que podría esconder una entrada al escondite, o algo similar.{/i}"

    #condicionales segun quienes estan en el grupo de exploracion

    if "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "Si vamos por las rocas, avanzaremos más rápido, pero si la marea sube antes de que volvamos, quedaremos atrapados."
        hide ingrid with Dissolve(0.4)

    if "bob" in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "Por la selva es más seguro... en teoría."
        hide bob with Dissolve(0.4)

    if "tomas" in equipo_exploracion:
        show tomas cruzado at left with Dissolve(0.4)
        t "En la selva avanzaremos más lento, y además corremos el riesgo de perdernos. La vegetación está muy densa."        
        hide tomas with Dissolve(0.4)

    if "erika" in equipo_exploracion:
        show erika preocupada at left with Dissolve(0.4)
        k "No sabemos exactamente qué tan larga es la ventana de tiempo que nos permite la marea."
        hide erika with Dissolve(0.4)

    if "marina" in equipo_exploracion:
        show marina alerta at center with Dissolve(0.4)
        m "También hay que pensar que por las rocas terminaremos ensopados, con las olas estrellándose frente a nosotros"
        m "Eso hará todo un poco más difícil..."
        hide marina with Dissolve(0.4)  
    
    menu:
        "Avanzar por las rocas. El camino es más rápido, pero potencialmente peligroso si sube la marea.":
            $ ruta_elegida = "rocas"
            jump cap10_exploracion_rocas

        "Dar un rodeo por la selva. Es más seguro, pero más lento y cansador.":
            $ ruta_elegida = "jungla"
            jump cap10_exploracion_jungla

label cap10_exploracion_jungla:

    scene bg selva_densa with fade
    show screen combined_ui

    "{i}El follaje se cierra sobre sus cabezas. El sol queda atrapado entre ramas trenzadas.{/i}"
    "{i}Avanzar se vuelve una lucha contra raíces, humedad y caminos casi impenetrables.{/i}"

    if "marina" in equipo_exploracion:
        show marina molesta at center with Dissolve(0.4)
        m "Creo que después de todo hubiese preferido mojarme..."
        hide marina with Dissolve(0.4)

    elif "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "¿Estamos seguros de que esto no es un laberinto vegetal que nunca se termina?"
        hide ingrid with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "No dejemos que la espesura nos desanime. ¡A redoblar fuerzas!"
        hide bob with Dissolve(0.4)

    elif "tomas" in equipo_exploracion:
        show tomas cruzado at left with Dissolve(0.4)
        t "La única razón por la que no nos hemos perdido es que es tan densa la espesura que vamos dejando un zurco en la vegetación."        
        hide tomas with Dissolve(0.4)

    elif "erika" in equipo_exploracion:
        show erika preocupada at left with Dissolve(0.4)
        k "Me quedó la espina en el ojo con lo de la marea. ¿Nos habría dado el tiempo, después de todo?"
        hide erika with Dissolve(0.4)

    "{i}Mientras avanzan, las ramas les raspan la piel y los pies se les hunden en el barro."
    "{i}No poder ver el sol entre las ramas no ayuda nada a su orientación, pero siguen marchando.{/i}"

    $ update_stat("hambre", hambre - 1)
    $ show_variable_changed_popup("El hambre ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}En determinado momento llegan a un zurco en la vegetación muy parecido al que vienen dejando ustedes.{/i}"
    "{i}Lo examinan, esperanzados por encontrar un rastro de Laura o Charles.{/i}"
    "{i}Pero rápidamente se dan cuenta de algo terrible. Este es su propio rastro. Han estado caminando en círculos.{/i}"

    if "tomas" in equipo_exploracion:
        show tomas frustrado at left with Dissolve(0.4)
        t "Esto es ridículo. No estamos explorando, estamos transpirando... ¡y sin rumbo!"
        hide tomas with Dissolve(0.4)

    elif "marina" in equipo_exploracion:
        show marina molesta at center with Dissolve(0.4)
        m "Creo... Creo que ya pasamos por aquí..."
        hide marina with Dissolve(0.4)

    elif "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "Lo que temíamos. Nos perdimos y nos fuimos desviando."
        hide ingrid with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "A este paso nunca los encontraremos. Asegurémonos de dejar marcas para que esto no vuelva a pasar."
        hide bob with Dissolve(0.4)

    elif "erika" in equipo_exploracion:
        show erika preocupada at left with Dissolve(0.4)
        k "Después de todo, la que nos atrapó fue la marea verde. Esta espesura es realmente un laberinto."
        hide erika with Dissolve(0.4)

    "{i}Luego de tomar medidas para no desviarse, llegan a una zona donde la luz del sol sí atraviesa las copas de los árboles.{/i}"
    "{i}Esta área es mucho menos densa y con árboles más altos, alzándose como columnas.{/i}"
    "{i}Transformando el bosque en una catedral natural, con rayos de sol colándose entre el manto vegetal, como vitrales.{/i}"
    "{i}El silencio de todos evidencia lo impactados que quedan.{/i}"

    scene bg manglar_inicial with fade
    $ update_stat("sed", sed - 1)
    $ show_variable_changed_popup("La sed ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Pasando la alta arbolada encuentran un manglar.{/i}"
    "{i}Con ramas saliendo del barro negro, las sombras dibujan figuras siniestras en la superficie del agua estancada.{/i}" # GOTY

    if "erika" in equipo_exploracion:
        show erika preocupada at right with Dissolve(0.4)
        k "No me encanta esto. Si nos hundimos ahí adentro, no hay vuelta."
        hide erika with Dissolve(0.4)

    elif "tomas" in equipo_exploracion:
        show tomas frustrado at left with Dissolve(0.4)
        t "Esto se está poniendo cada vez más peligroso. Espero que los demás no hayan venido por aquí también."
        hide tomas with Dissolve(0.4)

    elif "marina" in equipo_exploracion:
        show marina molesta at center with Dissolve(0.4)
        m "En este tipo de pantanos tropicales... ¿no hay serpientes?"
        hide marina with Dissolve(0.4)

    elif "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "Encontrar un camino seguro a través de la ciénaga será todo un desafío."
        hide ingrid with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "Debo admitir que la selva quizá no era la opción más segura después de todo."
        hide bob with Dissolve(0.4)

    $ update_stat("hambre", hambre - 1)
    $ show_variable_changed_popup("El hambre ha aumentado", rojo)
    hide screen combined_ui
    show screen combined_ui

    "{i}Avanzar por el manglar les resulta mas dificil de lo esperado.{/i}"
    "{i}Alguien propone decidir si seguir adelante o volver sobre sus pasos.{/i}"
    menu:
        "Volver a la costa y tomar el camino de las rocas, si todavía es viable.":
            $ decision_tras_manglar = "retroceder"            
            jump cap10_transicion_rocas_tardia

        "Seguir por el manglar, avanzando con extrema precaución":
            $ decision_tras_manglar = "seguir_manglar"
            jump cap10_manglar_decisiones

label cap10_transicion_rocas_tardia:

    scene bg costa_bifurcacion with fade
    show screen combined_ui
    $ reloj_marea +=1

    "{i}Retroceden desde el manglar, pasando por los altos árboles y volviendo por el camino que dejaron entre la maleza.{/i}"
    "{i}Cuando por fin emergen nuevamente a la costa, la vista los detiene en seco.{/i}"

    pause .5

    "{i}Las rocas que antes parecían abiertas como un sendero ya están parcialmente cubiertas.{/i}"
    "{i}El mar ruge con una nueva cadencia y las olas son bastante más altas.{/i}"

    if "marina" in equipo_exploracion:
        show marina seria at left with Dissolve(0.4)
        m "Tendríamos que haber ido por las rocas desde un principio."
        hide marina with Dissolve(0.4)

    if "bob" in equipo_exploracion:
        show bob tenso at center with Dissolve(0.4)
        b "Tenemos dos opciones: cruzar ya y arriesgarnos a resbalar... o esperar y ver qué tan rápido está subiendo."
        b "Corremos el riesgo de perder la última chance de atravesar al otro lado."
        hide bob with Dissolve(0.4)

    if "ingrid" in equipo_exploracion:
        show ingrid seria at center with Dissolve(0.4)
        i "Si nos hubiésemos detenido a ver qué tan rápido subía la marea, nos habríamos dado cuenta de que había tiempo de sobra."
        i "Ahora puede que ya sea demasiado tarde."
        hide ingrid with Dissolve(0.4)   

    if "tomas" in equipo_exploracion:
        show tomas cruzado at left with Dissolve(0.4)
        t "Perdimos demasiado tiempo dando vueltas en esa condenada selva."        
        hide tomas with Dissolve(0.4)

    if "erika" in equipo_exploracion:
        show erika preocupada at left with Dissolve(0.4)
        k "No me gusta esto. En una hora ese sendero, que ahora apenas vemos, va a estar bajo un metro de agua."
        hide erika with Dissolve(0.4)

    menu:
        "Intentar atravesar las rocas ahora, antes de que la marea suba más.":
            $ decision_rocas_tardia = "cruzar"
            jump cap10_exploracion_rocas

        "Esperar unos minutos y observar el comportamiento de la marea antes de decidir.":
            $ decision_rocas_tardia = "esperar"
            jump cap10_espera_en_rocas

label cap10_espera_en_rocas:

    scene bg playa_gruta_entrada with fade
    show screen combined_ui

    "{i}Se quedan junto a las rocas, observando el movimiento del agua, como si la respuesta fuera un suspiro entre olas.{/i}"
    "{i}El sol está más bajo. La línea húmeda en la roca no llega al medio metro.{/i}"

    if "erika" in equipo_exploracion:
        show erika observando at left with Dissolve(0.4)
        k "Si medio metro más, nos quedamos afuera..."
        k "Laura y Charles estarán atrapados allí un día entero."
        hide erika with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        show bob ceño_fruncido at left with Dissolve(0.4)
        b "Esperar demasiado no es buena idea. Cruzar sin saber no me gusta demasiado, pero ya estamos aquí, y no hay opción."
        hide bob with Dissolve(0.4)

    "{i}No hay más tiempo que perder. Tienen que seguir, y tiene que ser ya.{/i}"
    "{i}Esperar más significaría arriesgar la única oportunidad que tienen de cruzar.{/i}"

    jump cap10_exploracion_rocas

label cap10_exploracion_rocas:

    scene bg zona_rocas with fade
    show screen combined_ui

    if decision_rocas_tardia == "cruzar" or $ decision_rocas_tardia = "esperar":
        "{i}El mar se escucha distinto: más cerca, más violento.{/i}"
        "{i}Las rocas, que mas temprano estaban secas, ahora son salpicadas por las olas. No hay margen para titubear.{/i}"
    else:
        "{i}Mejillones rotos crujen bajo sus pasos. La marea aún no ha empezado a subir del todo.{/i}"

    "{i}Avanzar con cuidado y sin enlentencer la marcha se les hace muy difícil.{/i}"
    "{i}El ruido de las olas es interumpido por un grito de dolor.{/i}"

    if "erika" in equipo_exploracion:    
        "{i}Erika dió un paso en falso y cayó. La ayudas a levantarse, y parece no haber sufrido más que un rasguño.{/i}"
        show erika preocupada at right with Dissolve(0.4)
        menu:
            "Pedirle que tenga más cuidado.":
                y "Erika, ten cuidado. Si uno de nosotros se lastima, esta misión de rescate está acabada."
            "Guardarte tus palabras para más tarde.":
                "{i}Ella se encuentra bien, que es lo que importa. Discutir ahora solo los haría perder más tiempo.{/i}"
        hide erika with Dissolve(0.4)
        
    elif "tomas" in equipo_exploracion:
        "{i}Tomás dió un paso en falso y cayó. Lo ayudas a levantarse, y parece no haber sufrido más que un rasguño.{/i}"
        show tomas frustrado at left with Dissolve(0.4)
        menu:
            "Pedirle que tenga más cuidado.":
                y "Tomás, ten cuidado. Si uno de nosotros se lastima, esta misión de rescate está acabada."
            "Guardarte tus palabras para más tarde.":
                "{i}El se encuentra bien, que es lo que importa. Discutir ahora solo los haría perder más tiempo.{/i}" 
        hide tomas with Dissolve(0.4)

    elif "marina" in equipo_exploracion:        
        "{i}Marina dió un paso en falso y cayó. La ayudas a levantarse, y parece no haber sufrido más que un rasguño.{/i}"
        show marina molesta at center with Dissolve(0.4)
        menu:
            "Pedirle que tenga más cuidado.":
                y "Marina, ten cuidado. Si uno de nosotros se lastima, esta misión de rescate está acabada."
            "Guardarte tus palabras para más tarde.":
                "{i}Ella se encuentra bien, que es lo que importa. Discutir ahora solo los haría perder más tiempo.{/i}"        
        hide marina with Dissolve(0.4)

    elif "ingrid" in equipo_exploracion:
        "{i}Ingrid dió un paso en falso y cayó. La ayudas a levantarse, y parece no haber sufrido más que un rasguño.{/i}"
        show ingrid seria at center with Dissolve(0.4)
        menu:
            "Pedirle que tenga más cuidado.":
                y "Ingrid, ten cuidado. Si uno de nosotros se lastima, esta misión de rescate está acabada."
            "Guardarte tus palabras para más tarde.":
                "{i}Ella se encuentra bien, que es lo que importa. Discutir ahora solo los haría perder más tiempo.{/i}"
        hide ingrid with Dissolve(0.4)

    elif "bob" in equipo_exploracion:
        "{i}Bob dió un paso en falso y cayó. Lo ayudas a levantarse, y parece no haber sufrido más que un rasguño.{/i}"        
        show bob parado hablando at center with Dissolve(0.4)
        menu:
            "Pedirle que tenga más cuidado.":
                y "Bob, ten cuidado. Si uno de nosotros se lastima, esta misión de rescate está acabada."
            "Guardarte tus palabras para más tarde.":
                "{i}El se encuentra bien, que es lo que importa. Discutir ahora solo los haría perder más tiempo.{/i}"        
        hide bob with Dissolve(0.4)

    "{i}Avanzan con más cuidado y lentamente, pero finalmente llegan a una pequeña playa escondida.{/i}"
 
    scene bg playa_gruta_entrada with fade
    
    "{i}La entrada a una cueva es visible entre dos riscos de piedra cubierta cubierta de musgo.{/i}"
    "{i}Las marcas de agua llegan a la altura de tu pecho.{/i}"
    "{i}En marea alta, todo esto quedará sumergido.{/i}"
    "{i}Pero por ahora la entrada sigue libre. Y hay dos pares de huellas en la arena que se dirigen hacia allí.{/i}"    

    menu:
        "Entrar en la cueva antes de que el agua bloquee la entrada.":
            "{i}El tiempo apremia y ya perdieron demasiado.{/i}"
            jump cap10_inicio_cueva

        "Esperar para ver si la marea sube o si los desaparecidos regresan por su cuenta.":
            "{i}Antes de que puedas comenzar a plantearle tu punto a los demás, un sonido llama tu atención.{/i}"
            jump cap10_inicio_cueva

label cap10_manglar_decisiones:

    scene bg manglar_interior with fade
    show screen combined_ui

    "{i}Avanzan entre raíces retorcidas y el agua estancada. El aire es espeso, y los mosquitos no dan tregua.{/i}"

    "{i}Frente a ustedes, un arbol caído, cubierto de líquenes, atraviesa la parte más angosta de una pequeña laguna.{/i}"
    "{i}Evitar cruzar la laguna significaría un gran rodeo.{/i}"
    "{i}El tronco es bastante ancho, pero un mal paso puede significar caer al agua.{/i}"

    menu:
        "Apurarse y cruzar en equilibrio antes de pensarlo demasiado":
            $ decision_tronco = "rapido"
            "{i}Se lanzan hacia el tronco con gran agilidad{/i}"
            "{i}Resbalan un poco, pero logran mantener el equilibrio y logran atravesar con éxito.{/i}"
        "Tantear cada paso y cruzar lento, asegurando el equilibrio agarrándose de las ramas":
            $ decision_tronco = "precavido"
            "{i}Avanzan despacio. Las botas crujen, pero la travesía es segura. Todos llegan sin problemas.{/i}"
        "Rodear la laguna y no correr riesgos.":
            $ decision_tronco = "evita"
            $ update_stat("cansancio", cansancio - 1)
            $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
            hide screen combined_ui
            show screen combined_ui
            "{i}Dan un rodeo que los agota más de lo esperado, pero evitan el tronco resbaladizo.{/i}"

    "{i}Más adelante, algo parece moverse sobre la superficie del pantano.{/i}"
    "{i}Una sombra alargada, inmóvil, apenas sumergida entre juncos. No hay certeza de lo que es.{/i}"

    menu:
        "Acercarse lentamente para observar mejor":
            $ decision_sombra = "observar"
            "{i}Te acercas despacio, sin hacer ruido. Resulta no ser más que un tronco podrido y cubierto de hongos.{/i}"
        "Lanzar algo hacia la sombra para medir su reacción":
            $ decision_sombra = "provocar"
            "{i}Una piedra cae al lado de la figura, levantando agua turbia.{/i}"
            "{i}Las ondas sacuden la figura, hasta que ven que solo se trata de un tronco podrido y cubierto de hongos.{/i}"
        "Retroceder sin hacer ruido y rodear la zona":
            $ decision_sombra = "retroceder"
            $ update_stat("hambre", hambre - 1)
            $ show_variable_changed_popup("El hambre ha aumentado", rojo)
            hide screen combined_ui
            show screen combined_ui
            "{i}El desvío es largo y cansador. Pierden tiempo y energía, pero al menos nadie corre riesgos.{/i}"

    "{i}Cuando ya divisan el fin del manglar, una vibración mínima alerta tus sentidos.{/i}"
    "{i}Entre dos troncos caídos, enroscada como un ramal, una serpiente se camufla perfectamente. Respiras profundamente.{/i}"

    menu:
        "Retroceder con calma y trazar un rodeo, sin sobresaltos":
            $ decision_serpiente = "evita"
            "{i}La dejan atrás sin alertarla. Caminan despacio hasta perderla de vista.{/i}"
        "Hacer ruido para espantarla y abrir el paso":
            $ decision_serpiente = "ruido"
            "{i}La serpiente se alza, sisea... pero pronto voltea y se escurre hacia el pantano.{/i}"
            "{i}Sus corazones tardan unos segundos en calmarse.{/i}"
        "Avanzar ignorándola, con cuidado de no pisarla":
            $ decision_serpiente = "ignorar"
            $ update_stat("cansancio", cansancio - 1)
            $ show_variable_changed_popup("El cansancio ha aumentado", rojo)
            hide screen combined_ui
            show screen combined_ui
            "{i}Pasan cerca de ella, conteniendo la respiración.{/i}"
            "{i}La serpiente se mantiene alerta, pero no se mueve.{/i}"

    scene bg playa_gruta_entrada with fade

    "{i}Finalmente, el follaje se abre y emergen a una pequeña playa oculta, acorralada por rocas y la espuma de las olas.{/i}"
    "{i}Frente a ustedes se alza la entrada a una oscura y húmeda gruta invadida por algas.{/i}"
    "{i}En las piedras hay marcas recientes de la subida de la marea y dos pares de huellas en la arena que se pierden dentro de la cueva.{/i}"

    jump cap10_inicio_cueva
     
label cap10_inicio_cueva:

    "{i}Escuchan crujidos detrás de ustedes, cada vez más fuerte.{/i}"
    "{i}Voltean para ver y reconocen los rostros agotados de los integrantes del otro grupo de búsqueda.{/i}"
    "{i}Se acercan jadeando, y se detienen a contemplar la entrada a la cueva.{/i}"

    if "bob" not in equipo_exploracion:
        show bob parado hablando at center with Dissolve(0.4)
        b "¡Qué suerte que están todos bien, [nombre_personaje]!"
        b "El camino hasta aquí resultó ser bastante más accidentado de lo que esperábamos, ¿eh?"
        show erika preocupada at right with Dissolve(0.4)
        k "Lo importante es que encontramos la cueva antes de que la marea lo hiciera imposible."
        k "Ahora tenemos que entrar..."
        hide bob with Dissolve(0.4)
        hide erika with Dissolve(0.4)

    else:
        show erika preocupada at right with Dissolve(0.4)
        k "Veo que llegaron sanos y salvos. ¡Excelente!"
        k "Nosotros nos demoramos porque encontrar el camino resultó todo un desafío. Imagino que habrán pasado por lo mismo."
        show bob parado hablando at center with Dissolve(0.4)
        b "La marea fue lo que hizo difícil tomar una decisión. Cuando entendimos que debíamos apurarnos, decidimos cruzar."
        b "Supongo que ahora lo único que resta es entrar..."
        hide bob with Dissolve(0.4)
        hide erika with Dissolve(0.4)
    
    if jugador_es_lider:
        "{i}Todas las miradas se posan en ti con mucha expectativa. Todos esperan que des el primer paso.{/i}"
        "{i}Asientes con la cabeza y te adentras en la profundidad, con los demás siguiéndote en fila.{/i}"

    else:
        "{i}Todos intercambian miradas, buscando coraje en los demás.{/i}"    
        "{i}Suspiran al unísono y se adentran hacia la profundidad.{/i}"

    jump cap10_end

label cap10_end:
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
        #$ desicion_intro = calcular_decisiones_intro(lista_decisiones_intro)
                    
        # Generar contenido para los pop-ups de decisiones
        #$ decisiones_contenido = generar_lista_popup("DECISIONES", lista_decisiones_intro, desicion_intro)

        # Mostrar los pop-ups
        show screen relaciones_popup(contenido=relaciones_contenido)
        # show screen decisiones_popup(contenido=decisiones_contenido)
                    
        "Aquí termina el capitulo 10, con dos sobrevivientes dentro de la cueva y la marea subiendo."
        "¿Podrá el grupo rescatar a sus compañeros a tiempo o los dejará a su suerte por haberse ido en secreto?"
        # Ocultar los pop-ups con dissolve
        hide screen relaciones_popup with dissolve
        # hide screen decisiones_popup with dissolve
        jump continuar10

label continuar10:
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump final_cap10
                #jump chapter_9_start
            "VOLVER A VER EL RESÚMEN":
                jump cap10_end
                #jump chapter_8_end

label final_cap10:
    if renpy.android:
        jump chapter_11_start
    else:
        # call pedir_codigo_capitulo from _call_pedir_codigo_capitulo10
        jump chapter_11_start


#######################################################################################   #####   ######  ##############################################################
##########################################################################################  ##  ########  ##############################################################
## Aca comienza la PARTE 11 ##############################################################  ##  ########  ##############################################################
########################################################################################   ####   ######  ##############################################################

label chapter_11_start:
    
    $ persistent.cantidad_capitulos +=1

    scene bg gruta_entrada with fade
    show screen combined_ui

    "{i}Lo primero que notan al entrar a la cueva es que en algún lugar hay una fuente de luz{/i}"
    
    show bob parado hablando at right with Dissolve(0.4)
    b "Es probable que haya alguna apertura en el techo de la gruta."

    show ingrid parada  at center with Dissolve(0.4)
    i "¡Por suerte! Si no, no se cómo haríamos para ver dónde pisamos."
    i "Lo único que nos falta es que alguien se tropiece entre las rocas y se tuerza el tobillo."

    show marina at left with Dissolve(0.4)
    m "¡Ingrid! Ni lo menciones... necesitamos a la suerte de nuestro lado, no la tientes."

    hide marina with Dissolve(0.4)        
    hide bob with Dissolve(0.4)
    hide ingrid with Dissolve(0.4)
    
    "{i}El eco de sus pasos se extingue rápido. El musgo que cubre las paredes de roca parece tragar los sonidos.{/i}"
    "{i}El aire está cargado de sal pero hay una corriente fresca.{/i}"
    "{i}Luego de avanzar un poco más, ven algunos haces de luz solar filtrados por raíces que se cuelan entre grietas en el techo.{/i}"
    
    show erika seria at left with Dissolve(0.4)
    k "Mira eso, Bob. Parece que por una vez, tenías razón."

    show ingrid parada  at center with Dissolve(0.4)
    i "Al menos ahora sabemos que el complejo de cavernas no es cerrado."
    i "Será útil recordarlo si nos atrapa la marea."

    hide ingrid with Dissolve(0.4)
    hide erika with Dissolve(0.4)   

    if jugador_es_lider:
        if marina > 0:
            show marina at left with Dissolve(0.4)
            m "Bien. Eso me deja más tranquila. Debo admitir que no estaba muy segura de entrar..."
            hide marina with Dissolve(0.4)
        elif marina < 0:
            show marina molesta at left with Dissolve(0.4)
            m "Ingrid, ¿otra vez?"
            m "Creo que ya tengo suficientes pensamientos pesimistas sabiendo quién nos lidera..."
            hide marina with Dissolve(0.4)

        if tomas > 0:
            show tomas firme at center with Dissolve(0.4)
            t "No podíamos quedarnos esperando. Por suerte [nombre_personaje] tomó la iniciativa, y ahora vemos que no era tan peligroso."
            hide tomas with Dissolve(0.4)
        elif tomas < 0:
            show tomas cruzado at center with Dissolve(0.4)
            t "Esperemos que si sucede una emergencia, todos estemos a la altura."
            "{i}Algo en su tono de voz te hace sospechar que eso fue dirigido hacia ti.{/i}"
            hide tomas with Dissolve(0.4)
    else:
        if marina > 0:
            show marina seria at left with Dissolve(0.4)
            m "La verdad, [nombre_personaje], es que ya no tengo miedo."
            m "Me has ayudado a darme cuenta de que soy capaz de más de lo que creía."
            hide marina with Dissolve(0.4)

        if tomas > 0:
            show tomas analizando at center with Dissolve(0.4)
            t "A mi me alegra mucho que hayamos tenido la oportunidad de entrar juntos a la cueva después de todo."
            t "Necesitábamos un recordatorio de cuánto más fuertes somos si estamos unidos."
            hide tomas with Dissolve(0.4)
    
    "{i}Continúan adentrándose en la cueva y pronto el suelo se vuelve más arenoso, y es entonces cuando detectan las huellas nuevamente.{/i}"
    "{i}Parece que uno de los dos venía rengueando y arrastrándose un poco.{/i}"

    show marina preocupada at left with Dissolve(0.4)
    m "¿Creen que uno de ellos esté herido?."    

    show ingrid parada  at center with Dissolve(0.4)   
    i "A juzgar por el tamaño de las huellas, es Laura la que rengueaba."

    hide marina with Dissolve(0.4)
    hide ingrid with Dissolve(0.4)
    
    show bob parado hablando at right with Dissolve(0.4)
    b "¡Miren! ¡Allí!"
    hide bob with Dissolve(0.4)    

    "{i}Unos pasos más adelante hay algo en el piso que llama su atención.{/i}"
    "{i}No es una piedra, y tampoco una planta.{/i}"
    "{i}Se acercan y descubren que se trata de un trozo de tela.{/i}"
    "{i}Como si alguien hubiera arrancado la manga de una camisa.{/i}"
    
    menu:
        "Minimizar el hallazgo, evitando sugerir escenarios pesimistas.":
            y "Esta tela es de la camisa de Charles..."
            y "¡Vamos! Ya casi los alcanzamos."
        "Mencionar que seguramente se detuvieron para atender las heridas de Laura.":
            y "Deben de haber usado la manga de la camisa de Charles para hacer vendas o un cabestrillo."
            y "¡Estas son buenas noticias! Significa que Laura consiguió seguir adelante."
        "Admitir que el hallazgo te preocupa.":
            y "Esto solo confirma que efectivamente, Laura está herida."
            y "No hay sangre, pero de todas formas creo que deberíamos apurar la marcha."

    "{i}Siguen avanzando, ansiosos y con la expectativa de encontrar a Laura y Charles pronto.{/i}"    

    jump cap11_dialogos_en_marcha

label cap11_dialogos_en_marcha:

    scene bg gruta_pasillo with fade
    show screen combined_ui

    "{i}Los caminos entre las rocas de la gruta serpentean como si no quisieran que ningún intruso llegue al corazón de la cueva.{/i}"
    
    show marina preocupada at right with Dissolve(.4)
    m "Laura tuvo ideas raras desde que llegamos, pero arriesgarse así, con la marea subiendo, es lo más impulsivo que ha hecho."
    show tomas serio at left with Dissolve(.4)
    t "Charles por otro lado siempre fue impulsivo, pero esto es distinto. Poner en riesgo a alguien más, es algo que no me esperaba de el."
    show bob_parado_enojado at centerright with Dissolve(.4)
    b "Creo que hay un ángulo que no estamos considerando."
    b "Quizá creyeron que podían escapar de la isla con el tesoro."
    b "Repartirlo entre dos es mejor que repartirlo entre ocho."
    show show erika parada at centerleft with Dissolve(.4)
    k "Estoy de acuerdo con que no estamos considerando todos los enfoques, pero tiene que haber algo más."

    hide erika
    hide bob
    with Dissolve(.4)

    "{i}Hay unos segundos de silencio, como si esperaran tu opinión. Te detienes y volteas hacia ellos.{/i}"

    menu:
        "Defender a Laura.":
            y "Quizás se equivocó, pero no creo que se trate de un tema de egoísmo."
            $ laura += 1
            $ marina += 1
            "{i}Marina asiente de forma muy sutil.{/i}"
            "{i}Pareces haberla tranquilizado un poco.{/i}"

        "Criticar a Charles.":
            y "Laura no es la que siempre hace cosas impredecibles, es Charles. Temo que el la haya convencido de hacer una locura."
            $ charles -= 1
            $ tomas += 1
            "{i}Tomás aprieta los labios. No lo dice, pero en el fondo sabe que tienes razón.{/i}"
        "Enfocarse en el rescate.":
            y "No importa por qué lo hicieron. Hay que sacarlos de aquí. Y rápido."
            $ bob += 1
            $ erika += 1
            "{i}El ritmo del grupo se acelera. El resto parece haberse haberse contagiado de tu sentido de urgencia.{/i}"

    "{i}Empiezan a notar humedad en el piso, luego algunos charcos, y pronto caminan con el agua cubriéndoles la planta de los pies.{/i}"
    
    show tomas serio at left with Dissolve(.4)
    t "¿Sienten un cambio en el olor del aire, o soy solo yo? Está como... estancado."
    t "No se si esta parte de la cueva tiene tanta ventilación como había en la entrada."
    show ingrid gr seria at center with Dissolve(.4)
    i "Eso... eso puede significar que estamos empezando a bajar. También explicaría el agua en el piso."
    i "Debemos tener cuidado. Si hemos subido y bajado sin darnos cuenta, podríamos estar yendo hacia una trampa mortal."
    show marina preocupada at right with Dissolve(.4)
    m "¿A qué te refieres?"
    i "Si estamos en un 'codo' del sendero, seremos los últimos en enterarnos si la cueva se inunda."

    hide ingrid
    hide marina
    hide tomas
    with Dissolve(.4)

    "{i}El grupo avanza lentamente, cada vez más consciente de lo traicionera que es la gruta, y tratando de no pensar en la marea.{/i}"
    "{i}Bob parece querer decir algo. Se nota la duda en su rostro, pero finalmente rompe el silencio.{/i}"

    b "Esto definitivamente es una trampa mortal. Miren esa grieta... es aún peor de lo que Ingrid imaginaba."
    "{i}Bob señala unas grietas en la pared de la cueva por las que se filtra agua.{/i}"
    k "Entra agua, pero no aire..."    
    
    hide bob
    hide erika
    with Dissolve(0.4)

    "{i}El pasadizo entre las rocas se vuelve más angosto, como si quisiera reflejar lo angustiante de la situación.{/i}"
    "{i}El sonido del mar parece escucharse más cerca, y el agua ya les llega a los tobillos.{/i}"

    jump cap11_marca_de_la_marea

label cap11_marca_de_la_marea:

    scene bg gruta_marca_agua with fade
    show screen combined_ui

    "{i}El pasaje vuelve a ensancharse y casi tropiezas cuando el suelo baja en unos escalones naturales.{/i}"
    "{i}A tu izquierda, una línea salina cubre la pared rocosa, bastante por encima de la altura de tus ojos.{/i}"
    "{i}Recta y brillante, parece una señal ominosa, una sentencia inevitable.{/i}"

    show erika seria at left with Dissolve(0.4)
    k "Esta es la primera vez que veo una marca como esta. Es posible que marque el punto máximo de crecida."
    k "Si nos demoramos mucho, todo esto quedará bajo agua."
    hide erika with Dissolve(0.4)

    show bob parado serio at center with Dissolve(0.4)
    b "Claramente solo seguirá subiendo. Si seguimos, lo hacemos a riesgo de quedarnos encerrados."
    hide bob with Dissolve(0.4)
    
    show marina preocupada at right with Dissolve(0.4)
    if marina >= 0:
        m "¿Y si entramos y después no encontramos salida?"
    else:
        m "Este es el rescate más peligroso e improvisado de la historia..."
    hide marina with Dissolve(0.4)

    "{i}Una ola que se estrella no muy lejos los sorprende a todos con su imponente furia.{/i}"
    "{i}Pueden ver cómo esto provoca que el agua suba lo suficiente como para que se note en tiempo real.{/i}"
    "{i}Su situación se vuelve más complicada, segundo a segundo.{/i}"    

    menu:
        "Intentar calmarlos a todos.":
            y "Tranquilos, los encontraremos pronto."
            $ marina += 1
            $ bob -= 1
            "{i}Marina parece reconfortarse con tus plabras, pero Bob se nota que Bob no comparte tu confianza.{/i}"
        "Pedirle a todos que se mantengan alerta.":
            y "Claramente la situación está cambiando minuto a minuto. Por favor, mantengan los ojos abiertos y tengan cuidado."
            $ bob += 1
            $ erika += 1
            "{i}Erika te observa y asiente. En su mirada ves que sabe que el pánico puede ser más peligroso que el agua.{/i}"
            "{i}A Bob se le hincha el pecho. ¿Acaso está orgulloso de ti? Después de todo, te ha enseñado alguna cosa sobre liderar.{/i}"
        "Ofrecer regresar por donde vinieron.":
            y "¿Creen que deberíamos volver? Si es así, decidámoslo ahora."
            $ marina -= 1
            "{i}Marina sacude la cabeza incrédula y pasa a tu lado, adelantándose unos metros.{/i}"
            "{i}Bob se encoje de hombros y el resto te evita con su mirada.{/i}"
            "{i}Tal vez sea demasiado tarde como para proponer regresar.{/i}"    

    jump cap11_entrada_cueva

label cap11_entrada_cueva:

    scene bg cueva_humedad_profunda with fade
    show screen combined_ui

    "{i}Luego de un par de vueltas más, el pasaje se abre a una amplia caverna.{/i}"
    "{i}Acurrucada detrás de una roca caída, con el pie vendado, está a Laura, que sonríe al verlos{/i}"

    show laura dolorida at center with Dissolve(0.4)
    l "Me torcí el pie. Charles me ayudó como pudo, pero siguió solo."
    l "Está convencido de que hay una cámara más profunda."
    hide laura with Dissolve(0.4)

    show marina triste at right with Dissolve(0.4)
    m "¡Laura! ¡No sabes lo preocupados que estábamos!"
    hide marina with Dissolve(0.4)

    show ingrid seria at left with Dissolve(0.5)
    i "Se fue solo, ¿eh?"
    i "Hasta ahora este lugar solo nos ha dado muestras de lo implacable que es."

    "{i}Laura apenas puede moverse, pero les señala el pasadizo por el que se fue Charles.{/i}"
    "{i}Las gotas, que caen desde el techo de forma rítmica, parecen marcar la cuenta regresiva.{/i}"

    menu:
        "Ir solo tras Charles.":
            y "Bob, Tomás, ustedes dos carguen a Marina. Igrid, Marina, Erika, ustedes vayan adelante para ver que sea seguro."
            $ charles += 1
            $ erika += 1
            $ bob += 1
            $ laura += 1
            $ ingrid += 1
            $ marina += 1
            $ tomas += 1
            "{i}Laura te mira con una cierta admiración. Sabe que tendrás los segundos contados.{/i}"
            "{i}Bob y Erika asienten, y todos te desean suerte mientras te internas en el corazón de la gruta.{/i}"
            jump cap11_busqueda_charles

        "Quedarte a ayudar a Laura.":

            y "Yo me encargo de Laura, pero necesitaré que alguien me ayude a cargarla."
            show bob parado serio at right with Dissolve(.4)
            b "Yo te ayudaré a hacerlo."
            hide bob with Dissolve(.4)
            show tomas serio at left with Dissolve(.4)
            t "Yo iré a buscar a Charles entonces. ¡Deseénme suerte!"
            hide tomas with Dissolve(.4)
            $ laura += 2
            $ marina += 2
            $ tomas += 1
            "{i}Tu y Bob ayudan a Laura a levantarse. Tomás agarra la antorcha y se interna en la oscuridad.{/i}"
            jump cap11_regreso_con_laura

label cap11_regreso_con_laura:

    scene bg cueva_retorno_con_laura with fade
    show screen combined_ui

    "{i}Regresando sobre sus pasos, encuentran el aire más denso. Laura respira con dificultad mientras se apoya en sus hombros.{/i}"    

    show marina hablando at left with Dissolve(0.4)
    m "¡Fíjense! Esa raíz estaba seca cuando pasamos por aquí. Ahora gotea."
    hide marina with Dissolve(0.4)

    show laura dolorida at center with Dissolve(0.4)
    l "(jadeando) No puedo apoyar el pie, y el agua está aflojándome las vendas.."
    hide laura with Dissolve(0.4)

    "{i}Se detienen un momento a ajustarle los vendajes mientras deciden qué hacer.{/i}"

    menu:
        "Cargar a Laura en brazos":
            $ laura += 1
            "{i}Levantas a Laura con cuidado y ella cruza sus brazos alrededor de tu cuello.{/i}"
            "{i}Puedes sentir lo débil que está, apenas puede sostenerse sobre tu pecho.{/i}"

        "Hacer un esfuerzo para que sus pies no toquen el agua ni el piso.":
            $ laura += 1
            "{i}Se aseguran de agarrarla firmemente de la cintura y la levantan junto a Bob en el aire.{/i}"
            "{i}Coordinan el ritmo de la marcha como si lo hubieran ensayado.{/i}"

        "Proponer separarse.":
            y "Marina, Ingrid, Erika... No hay necesidad de que ustedes nos esperen."            
            "{i}Las tres te miran con desaprobación, sabiendo lo que eso implicaría.{/i}"
            "{i}Parecen determinadas a quedarse con Laura, porque te ignoran sin decir palabra alguna.{/i}"

    "{i}Se escuchan pasos chapoteando tras ustedes.Voltean y ven a Tomás, alcanzándolos." 

    show tomas serio at center with Dissolve(0.4)
    t "¡Pensé que ya estarían fuera! Charles viene atrás. Lo encontré justo a tiempo."
    hide tomas with Dissolve(0.4)

    show charles triste at right with Dissolve(0.4)
    c "Se que querrán oírlo todo acerca del tesoro, pero por favor, salgamos de aquí primero."
    hide charles with Dissolve(0.4)

    "{i}El agua ya les llega a las rodillas, y hay pequeñas ondas que indican que el flujo de agua es cada vez mayor.{/i}"

    jump cap11_salida_media_abertura

label cap11_salida_media_abertura:

    scene bg pasillo_agua_altura_pecho with fade
    show screen combined_ui

    "{i}Llegan a la abertura, los demás les gritan que se apuren. Está cayendo mucha agua formando una pequeña cascada.{/i}"

    show marina triste at left with Dissolve(0.4)
    m "La abertura está cerca. Pero el agua cae fuerte, hay que tener cuidado."

    hide marina with Dissolve(0.4)

    show laura triste at center with Dissolve(0.4)
    l "(susurrando) Estoy agotada. Pero si alguien me guía… creo que puedo llegar."

    hide laura with Dissolve(0.4)

    show tomas hablando at right with Dissolve(0.4)
    t "Esa piedra sobresale. Podemos usarla como escalón. Pero hay que moverse ya..."

    hide tomas with Dissolve(0.4)

    menu:
        "Subís primero por la roca y abrís paso desde arriba":
            $ tomas += 1
            "{i}Tomás te impulsa con fuerza. Desde la piedra seca extendés la mano a Marina. La cadena se forma sin palabras, pero firme.{/i}"

        "Sostenés a Laura mientras Marina se adelanta por la pendiente":
            $ laura += 1
            $ marina += 1
            "{i}El agua golpea los muslos. Marina trepa con precisión. Laura se apoya contra vos, temblando. Entre los tres logran que avance.{/i}"

        "Te quedás al final y vigilás que nadie se quede atrás":
            $ bob += 1
            "{i}Esperás, mirando cada sombra. Bob te extiende la mano, con gesto grave. Haces fuerza para trepar poco a poco con el agua cayendo y empujando hacia abajo. El último escalón cede.{/i}"
            "{i}Quedas un instante colgado del brazo de Bob pero con un ultimo impulso logras llegar arriba.{/i}"

    "{i}Una corriente más fuerte se filtra entre los pies. La salida no parece más cercana… hay que darse prisa.{/i}"

    jump cap11_salida_media_tension

label cap11_busqueda_charles:

    scene bg gruta_excavacion_inicio with fade
    show screen combined_ui

    "{i}El pasadizo baja entre piedras resbaladizas y charcos con fondo de barro mezclado con arena arena.{/i}"

    "{i}Al fondo, ves una silueta agachada escarbando bajo el agua.{/i}"
    "{i}Cuando voltea, confirmas que es Charles, que te mira con una sonrisa de oreja a oreja.{/i}"

    show charles boca abierta at center with Dissolve(0.4)
    c "Sabía que estaban aquí. Mira el símbolo tallado... es el mismo del dibujo. Las joyas fueron escondidas aquí mismo.{/i}"

    "{i}En el fondo del pozo hecho por Charles una losa cubre una pequeña abertura.{/i}"
    "{i}Charles la retira con gran esfuerzo revelando un atado de cuero casi destruído.{/i}"
    "{i}Entre los retazos, brillan unas pocas joyas.{/i}"

    c "¡Te lo dije! El resto debe estar enterrado más abajo."

    hide charles with Dissolve(0.4)

    "{i}Charles escarba con las manos mientras ya escuchas el agua correr pendiente abajo. Pronto el pasaje quedará inundado.{/i}"
    menu:
        "Ayudar a Charles a escarbar. No pueden irse con tan poco, luego de arriesgar tanto.":
            $ charles += 1
            $ reloj_marea +=1
            "{i}Juntos remueven barro y arena hasta que se topan con un cofre de madera podrida, que colapsa sobre sí mismo.{/i}"
            "{i}Hay muchas más joyas aquí, pero también hay mucha más agua cayendo.{/i}"
            "{i}Charles comienza a sacar las gemas del pozo y te las pasa para que las guardes.{/i}"
            jump cap11_joyas_rescate_dificil

        "Hay que irse. Lo encontrado debe bastar o la marea no los perdonará.":
            $ charles -= 1
            "{i}Charles te mira como si le estuvieras robando la navidad. Guarda lo que ya sacó y se levanta.{/i}"
            jump cap11_regreso_desde_excavacion


label cap11_joyas_rescate_dificil:

    scene bg cueva_desborde with fade
    show screen combined_ui

    "{i}Al sacar la última, una roca se desploma y le cae en la mano, pasando a centímetros de su cabeza.{/i}"

    show charles triste at center with Dissolve(0.4)
    c "(gritando de dolor) No... no puedo seguir. ¡Salgamos ya!"

    hide charles with Dissolve(0.4)

    "{i}Logran subir con dificultad hasta la caverna donde tu y los demás encontraron a Laura.{/i}"
    "{i}Con el agua al nivel de la rodilla, una corriente inesperada los empuja desde atrás, sumergiéndolos brevemente.{/i}"
    "{i}Los revuelca un poco hasta que se vuelve a nivelar, y siguen avanzando tan rápido como sus piernas se los permiten.{/i}"
    "{i}Luego de una curva ven a Bob y a Tomás levantando a Laura. Un poco más adelante están Marina, Erika e Ingrid.{/i}"

    show marina preocupada at left with Dissolve(0.4)
    m "¡Pensamos que no salían! ¿Por qué demoraron tanto?"

    menu:
        "Sacar un puñado de joyas relucientes de tu bolsillo.":
            $ marina -= 1
            $ tomas -= 1
            "{i}Todos miran incrédulos, y por un segundo, parece que su ánimo mejora.{/i}"
            jump cap11_salida_final
        "No decir nada por ahora. Lo importante era sobrevivir.":
            $ charles += 1
            y "Ya tendramos tiempo de hablar de eso, ahora hay que salir de aqui, ¡y rápido!"
            jump cap11_salida_final

label cap11_regreso_desde_excavacion:

    scene bg cueva_tension_retorno with fade
    show screen combined_ui

    "{i}Charles camina detrás tuyo, con un trapo con las pocas joyas recogidas apretado entre sus dedos.{/i}"
    "{i}No dice mucho, pero se nota que aún está lidiando con la frustración de no haber podido rescatar algo más.{/i}"
    "{i}El agua, que ahora alcanza sus rodillasm hace que cada paso requiera un gran esfuerzo, y es dificil ver donde pisar.{/i}"

    show charles frustrado at center with Dissolve(0.4)
    c "Podríamos haber sacado el resto. Pero entiendo... era arriesgado. Tal vez podamos vuelver cuando baje la marea."
    hide charles with Dissolve(0.4)

    "{i}Las voces del grupo llegan desde más adelante. Laura se apoya en Bob y Tomás. Erika les hace señas con su antorcha.{/i}"

    show erika sorprendida at right with Dissolve(0.4)
    k "¡Menos mal que lograron salir de ahí! Nos imaginábamos lo peor..."
    y "Logré sacarlo de ahí justo a tiempo."
    k "Entonces... ¿valió la pena, o no?"

    "{i}Charles pasa junto a ella con la cabeza gacha. Su rostro es una mezcla de frustración y culpa.{/i}"
    "{i}Sus ojos delatan que comienza a entender que puso a todos en peligro.{/i}"

    y "Ya habrá tiempo para detalles cuando salgamos de aquí."

    jump cap11_salida_final

label cap11_salida_final:

    if reloj_marea == 0:
        jump cap11_salida_rapida_abertura
    elif reloj_marea == 1:
        jump cap11_salida_media_abertura
    else:
        jump cap11_salida_tardia_abertura

label cap11_salida_rapida_abertura:

    scene bg gruta_entrada_encharcada with fade
    show screen combined_ui

    "{i}La abertura por la que habían entrado está inundada. El agua se sacude dentro de la caverna con cada embate de las olas afuera.{/i}"
    "{i}La grieta en el techo de la gruta, por la que cuelgan raíces del manglar, es la única salida visible.{/i}"

    y "Allí arriba, ¡sigan la luz!"

    "{i}Pruebas trepar, pero en seguida te das cuenta de que las rocas están húmedas y la pendiente ahora requiere usar manos y piernas.{/i}"
    "{i}Cualquiera de ustedes podría hacerlo, pero Laura no lo logrará sin ayuda.{/i}"

    show bob nervioso at left with Dissolve(0.4)    

    if bob < 0:
        b "Vamos, [nombre_personaje]. Demuéstranos que no eres tan mal líder como yo creí. ¿Qué hacemos?"
    else:
        b "Lo que sea que tengas en mente, hagámoslo rápido."
    hide bob with Dissolve(0.4)

    show ingrid parada  at center with Dissolve(0.4)
    i "Laura, vamos a ayudarte, como cuando me ayudaron ustedes a mi, ¿recuerdas?. Tu tranquila."
    hide ingrid with Dissolve(0.4)

    "Laura extiende la mano, sin hablar. En sus ojos ves que el miedo y la culpa la distraen del dolor."

    menu:
        "La sujetas con fuerza, ayudándola a trepar.":
            $ laura += 1
            "{i}Avanzan lentamente, ella primero, usando sus brazos, y tu empujándola detrás."
            "{i}El musgo se desprende un poco, pero tu agarre es firme.{/i}"
            "{i}El de ella sin embargo, no tanto. Se suelta poco antes de llegar arriba, y se resbala, cayendo.{/i}"
            menu:
                "Tratar de atajarla.":
                    "{i}No llegas a atajarla, pero logras frenar un poco su caída, y el agua hace el resto.{/i}"
                "Alertar a Charles.":
                    "{i}Abajo, a nivel de suelo, Charles logra atraparla y amortigua el impacto tirándose de espaldas hacia atrás, al agua.{/i}"

        "Le haces señas a Charles para que la asista, mientras tu abres camino, tanteando la firmeza de las rocas y apartando raíces.":
            "{i}Los musgos y raíces están más resbalosas de lo que creías.{/i}"
            "{i}Laura avanzan lentamente, ella primero, usando sus brazos, y Tomás empujándola detrás.{/i}"
            "{i}De repente, ella resbala y su agarre en el musgo se desprende, poco antes de llegar arriba, y se resbala, cayendo.{/i}"
            menu:
                "Alertar a Tomás.":
                    "{i}Tomás, no llega a atajarla, pero logra frenar un poco su caída, y el agua hace el resto.{/i}"
                "Alertar a Charles.":
                    "{i}Abajo, a nivel de suelo, Charles logra atraparla y amortigua el impacto tirándose de espaldas hacia atrás, al agua.{/i}"

        "Vigilas desde arriba mientras los demás la ayudan. La coordinación es clave.":
            $ bob -= 1
            "{i}Bob gruñe, pero sostiene a Laura como puede mientras sube cargándola.{/i}"
            "{i}De repente, Bob resbala y Laura no logra sostenerse en sus brazos.{/i}"
            "{i}Bob logra agarrarse de una roca en el último segundo, pero Laura Cae.{/i}"
            menu:
                "Alertar a Tomás.":
                    "{i}Tomás, detrás que venía detrás de ellos, no llega a atajarla, pero logra frenar un poco su caída, y el agua hace el resto.{/i}"
                "Alertar a Charles.":
                    "{i}Abajo, a nivel de suelo, Charles logra atraparla y amortigua el impacto tirándose de espaldas hacia atrás, al agua.{/i}"
            
    "{i}Luego de asegurarse de que Laura no está lastimada, vuelven a intentarlo.{/i}"
    "{i}Se posicionan en distintos puntos del trayecto de escalada, y la van ayudando con más cuidado, hasta que logra emerger al exterior.{/i}"
    "{i}El resto sube detrás de ella.{/i}"
    jump cap11_salida_rapida_salida

label cap11_salida_rapida_salida:

    scene bg manglar_luz_gris with fade
    show screen combined_ui

    "{i}La salida los recibe con luz ceniza. Las raíces del manglar los acogen y protegen, pero el aire está pesado.{/i}"
   
    show erika exhausta at left with Dissolve(0.4)
    k "Están todos... temía que alguno fuera a quedarse atrás. Cada vez entra mas agua."
    hide erika with Dissolve(0.4)

    show charles triste at center with Dissolve(0.4)    
    if charles >= 2:
        c "Lo lamento, no queria ponerlos a todos en peligro."
    else:
        c "Me pregunto cuantas joyas abrán quedado enterradas en el fondo de la cueva."
    hide charles with Dissolve(0.4)

    "{i}El grupo se toma unos minutos para recuperar el aliento.{/i}"
    "{i}Algunos se sientan en la arena mojada. Laura se revisa el vendaje. Bob se aparta, sin hablar.{/i}"

    menu:
        "Pese a todo, logramos salir. Y que eso es lo único que importa.":
            $ laura += 1
            $ tomas += 1
            $ charles += 1
            $ marina += 1
            $ bob += 1
            $ erika += 1
            "{i}Nadie te contradice. Todos están agradecidos de haber sobrevivido.{/i}"
        "Finalmente terminamos salvándonos nosotros, y parte del tesoro.":
            $ charles += 1
            if charles >= 2:
                "{i}Charles te sorníe. Sabes que le hubiese gustado recuperar el resto del tesoro, pero que valora más su vida.{/i}"
            else:
                "{i}Charles cruza miradas contigo. Claramente no está contento con las pocas joyas que pudieron recuperar.{/i}"
        "Te sientas a mirar la entrada ya sumergida, en silencio.":
            $ bob += 1
            "{i}Bob se acerca sin hablar. Parece querer alejarse del resto. Resopla un poco, sin duda conteniendo el enojo.{/i}"
            "{i}No quisieras estar en las botas de Laura y Charles si el capitán les pide una explicación.{/i}"

    jump cap11_post_salida_rapida

label cap11_salida_media_tension:

    scene bg cueva_corriente_alta with fade
    show screen combined_ui

    "{i}El agua te llega al pecho. Cada paso que das requiere un esfuerzo tremendo.{/i}"
    "{i}No llegan a ver dónde pisan, sólo sienten el roce de rocas resbalozas debajo de sus pies.{/i}"

    show erika sorprendida at center with Dissolve(0.4)
    k "¡Me quedé! ¡El pie... entre dos piedras! ¡No lo puedo mover!"

    "{i}Se gira hacia ti. El agua ya le llega a los hombros. El agua podría cubrirle el rostro si no se libera pronto.{/i}"
    "{i}El grupo se reúne alrededor de Erika, pero no ven sus pies y no saben qué hacer.{/i}"
    menu:
        "Te quedas dudando, una mala desicion puede causar mas problemas":
            $ tomas += 1
            $ erika += 1
            "{i}Tomás actúa de prisa. Logra empujar la piedra más liviana y liberar el pie de Erika.{/i}"
            "{i}Ella se cae, pero Marina la sujeta justo a tiempo Para evitar que quede sumergida.{/i}"
        "Das instrucciones rápidas, organizando al resto para que aflojen las rocas del fondo, o tiren de Erika para liberarla.":
            $ erika += 1
            $ ingrid += 1
            "{i}Ingrid logra patear la piedra más liviana. Erika se libera justo cuando una corriente empieza a crear pequeñas olas.{/i}"
        "Esperas a que Bob tome la iniciativa.":            
            "{i}Como buen marino, Bob se zambuye y afloja las piedras que sujetan el pie de Erika y ella se libera.{/i}"

    hide erika with Dissolve(0.4)

    "{i}El grupo sigue avanzando, cada segundo con más dificultad.{/i}"
    "{i}La corriente los empuja en la dirección opuesta, y pronto tienen que armar una cadena humana para poder avanzar.{/i}"
    "{i}La luz del manglar aparece entre los reflejos líquidos en las paredes rocosas.{/i}"
    "{i}La abertura por la que habían entrado está inundada, así como gran parte de la caverna.{/i}"
    "{i}La grieta en el techo de la gruta, por la que cuelgan raíces del manglar, es la única salida visible.{/i}"

    y "Vamos, ¡tenemos que subir!"

    show ingrid triste at left with Dissolve(0.4)
    i "Al menos ahora el agua nos ayudará un poco. La cueva está tan inundada que nos ahorraremos los primeros peldaños."
    i "Ayudemos a Ingrid y salgamos de aquí de una vez."

    "{i}Miras a tu alrededor pensando en cómo lograr que Laura pueda trepar hasta la salida.{/i}"

    menu:
        "Repetir la cadena humana hasta la cima, asegurándose de que Laura tenga en quién sostenerse durante todo el camino.":
            "{i}Organizas a todos para que en cada nivel alguien pueda sostenerla.{/i}"
            "{i}En unos pocos minutos logran salir todos.{/i}"
        "Esperar a que el agua suba un poco más y los eleve hacia el manglar.":
            y "Todos sabemos nadar, ¿o no? Déjen que el agua nos ayude, al menos esta vez."
            y "Con cada nuevo embate de las olas, aprovecharemos el impulso para subir un poco más."
        "Cargar a Laura hasta la cima.":
            "{i}Laura extiende la mano, sin hablar. En sus ojos ves que el miedo y la culpa la distraen del dolor.{/i}"                
            "La sujetas con fuerza, ayudándola a colgarse de ti."
            $ laura += 1
            "{i}Avanzan lentamente y con cuidado, pero de repente el musgo se desprende de una roca cuando afirmas el pié, y resbalas.{/i}"
            "{i}Logras agarrarte de una roca, pero Laura comienza a caer.{/i}"
            menu:
                "Tratar de atajarla.":
                    "{i}No llegas a atajarla, pero logras frenar un poco su caída y evitar que golpee contra las rocas. El agua hace el resto.{/i}"
                "Alertar a Charles.":
                    "{i}Abajo, a nivel de suelo, Charles desvía su caída para evitar que se golpee contra las rocas y el agua hace el resto.{/i}"
            "Finalmente deciden esperar a que el agua suba un poco más, para que las caídas no sean tan peligrosas si resbalan."
    
    jump cap11_salida_media_salida

label cap11_salida_media_salida:

    scene bg manglar_claro_turquesa with fade
    show screen combined_ui    

    "{i}La salida los recibe con luz ceniza. Las raíces del manglar los acogen y protegen, pero el aire está pesado.{/i}"

    show ingrid triste at left with Dissolve(0.4)
    i "¡Pensé que no salíamos más! ¿Están todos bien?"

    show tomas enojado at center with Dissolve(0.4)
    t "Aunque todo esto fue una pésima idea, lo que importa es que salimos todos de esa condenada cueva."

    show charles brazos cruzados at right with Dissolve(0.4)
    if charles <= 0:
        c "Yo no les pedí que vinieran a rescatarnos."
        "{i}Los demás lo miran, incrédulos de su ingratitud. Está claro que el no iba a poder cargar con Laura sin ayuda.{/i}"

    hide ingrid
    hide charles
    hide tomas
    with Dissolve(0.4)

    "{i}Laura se recuesta en una raíz baja. Marina le revisa el vendaje. Bob resopla con la cabeza baja.{/i}"

    menu:
        "Agradecer que estén juntos y que lo hayan logrado.":
            $ marina += 1
            $ tomas += 1
            $ ingrid += 1
            "{i}Nadie te contradice, pero todos parecen aún muy agitados como para reflexiones.{/i}"
            "{i}Comienzan a prepararse para regresar al refugio.{/i}"
        "Acompañar a Tomás en el reproche. Fue una pésima idea que vinieran solos.":
            $ tomas += 1            
            "{i}Laura desvía la vista. Charles te mira como si lo hubieses insultado.{/i}"
            "{i}Comienzan a prepararse para regresar al refugio.{/i}"
        "Esperas a que todos recuperen energías, y comienzas a caminar hacia el refugio sin decir más.":
            $ bob += 1
            "{i}Bob te sigue en silencio. El resto, de a tandas, los sigue desde atrás.{/i}"

    jump cap11_post_salida_media

label cap11_salida_tardia_abertura:

    scene bg cueva_corriente_alta with fade
    show screen combined_ui

    "{i}El agua le llega al mentón a los de menor estatura, y avanzar es una combinación de caminata y nado.{/i}"
    "{i}La fuerza de la corriente solo lo hace más difícil, y empiezan a dudar si llegarán a salir a tiempo.{/i}"
    "{i}Cuando llegan a la última caverna, está totalmente inundada. El agua se sacude dentro de la caverna con cada embate de las olas afuera.{/i}"
    "{i}La grieta en el techo de la gruta, por la que cuelgan raíces del manglar, es la única salida visible.{/i}"

    y "Allí, ¡miren! ¡Tendremos que nadar hasta las raíces!"
    jump cap11_salida_tardia_tension

label cap11_salida_tardia_tension:

    scene bg cueva_tiburon_alerta with fade
    show screen combined_ui

    "{i}Bob y tu ayudan a Laura primero, y el resto los sigue nadando.{/i}"

    "{i}Una sombra corta el agua. La superficie se parte como una herida. Una aleta asoma sobre la superficie.{/i}"
    "{i}Un tiburón de unos dos metros sacude el agua violentamente, intentando abrirse paso hacia ustedes entre una red de raíces.{/i}"

    show marina triste at left with Dissolve(0.4)
    m "¡Tiburón!"
    hide marina with Dissolve(0.4)
    "{i}No puede llegar hasta ustedes todavía, pero la el nivel ascendente del agua le permitirá alcanzarlos si no se apuran.{/i}"

    menu:
        "Coordinas el grupo en cadena para que cada uno que alcance las rocas cercanas a la salida pueda ayudar al siguiente.":          
            "{i}Suben uno a uno. El tiburón golpea una raíz con la aleta.{/i}"
            "{i}Abre la boca y destruye las raíces, nadando a toda prisa, pero ustedes ya están fuera de alcance.{/i}"
        "Empujas a Charles primero, luego trepas tú para ayudar a Laura.":            
            "{i}Charles trepa y agarra a Laura una vez que llega a la cima. Tu trepas detrás de ella y ayudas al resto.{/i}"
            "{i}Segundos después de que sube el último, el tiburón destruye las raíces y comienza a buscarlos furioso.{/i}"
        "Dejas que Bob suba primero con Laura, y luego cubres al resto mientras trepa.":            
            "{i}Nadas lo más rápido que tu cuerpo te lo permite hasta llegar a las rocas.{/i}"
            "{i}Mientras trepas fuera del agua, la nariz del tiburón roza tu pierna, pero cuando abre su boca, ya estás fuera.{/i}"

    jump cap11_salida_tardia_salida

label cap11_salida_tardia_salida:

    scene bg saliente_aislada_noche with fade
    show screen combined_ui

    "{i}La salida los recibe con luz ceniza. Las raíces del manglar los acogen y protegen, pero el aire está pesado.{/i}"

    show bob agotado at left with Dissolve(0.4)
    b "Eso... estuvo cerca. Bien hecho, [nombre_personaje]. Ese tiburón no tenía chances contra tu madera de líder."
    hide bob with Dissolve(0.4)

    show charles triste at center with Dissolve(0.4)
    c "Estas joyas... no son tan valiosas como ustedes. Lamento haberlos expuesto a semejantes peligros."
    hide charles with Dissolve(0.4)  

    jump cap11_post_salida_tardia

    ##########
    # LUNES LLEGUÉ HASTA ACÁ
    ##########

label cap11_post_salida_tardia:

    scene bg rocas_marea_baja_amanece with fade
    show screen combined_ui

    "{i}El mar retrocedió, rápidamente. El grupo desciende de la saliente. Nadie celebra. Nadie habla. El cuerpo duele. La cabeza más.{/i}"

    "{i}Avanzan por las rocas. Sin comida. Sin agua. El sol nace como una promesa hueca. El cansancio arrastra los pies como cadenas invisibles.{/i}"

    $ hambre += 2
    $ sed += 2
    $ cansancio += 3

    show bob parado enojado at left with Dissolve(0.4)
    b "¿Valió la pena? Lo pregunto en serio. ¿Todo ese riesgo por unas piedras mojadas?"

    show marina triste at center with Dissolve(0.4)
    m "La cueva casi nos ahoga… porque alguien quiso ir más profundo. Esto no fue grupo… fue egoismo."

    show charles triste at right with Dissolve(0.4)
    c "Tomé una decisión. Pero no empujé a nadie. Cada uno eligió seguir."

    hide bob
    hide marina
    hide charles
    with Dissolve(0.4)

    "{i}El tono sube. Las palabras cortan. Las culpas flotan como si buscaran a quién pegarse.{/i}"

    menu:
        "Recriminás a Charles por haber puesto en riesgo a todos":
            $ charles -= 1
            $ marina += 1
            "{i}Charles baja la vista. Marina asiente. Nadie contradice.{/i}"
        "Defendés que las decisiones fueron compartidas, no impuestas":
            $ bob += 1
            $ charles += 1
            "{i}Bob se cruza de brazos. No acepta del todo, pero no discute. Charles te mira con cierto alivio.{/i}"
        "Pedís que dejen de culparse. Lo importante es que todos están vivos":
            $ marina -= 1
            $ tomas += 1
            "{i}Marina resopla con fastidio. Tomás te da una palmada muda en el hombro.{/i}"

    "{i}El sonido interrumpe. Lejano. Agudo. Un motor en el aire. Un punto metálico cruza el cielo. Un avión. El grupo grita. Agitan los brazos. Saltan.{/i}"

    "{i}El avión gira...  y se aleja entre nubes bajas, tragado por la bruma costera. El silencio que deja atrás es distinto. Es la esperanza rota.{/i}"

    "{i}¿Esperar el rescate? ¿O tratar de saloir de la isla? Esas preguntas están en la mente de todos.{/i}"

    jump cap11_end

label cap11_post_salida_media:

    scene bg costa_bote_oleaje with fade
    show screen combined_ui

    "{i}El bote golpea contra la arena. Los cuerpos duelen, los brazos tiemblan. El mar ruge detrás, la marea y las olas cada mes mas grandes.{/i}"

    $ hambre += 1
    $ sed += 2
    $ cansancio += 2

    show erika enojada at center with Dissolve(0.4)
    k "Los traje. Pero esto no fue un rescate. Fue un parche. No se puede repetir."

    show tomas enojado at left with Dissolve(0.4)
    t "Si no se hubiera escarbado más, no hubiéramos corrido tanto riesgo."

    show charles brazos abiertos at right with Dissolve(0.4)
    c "No fue por codicia. Era una oportunidad. Y ustedes decidieron venir detras mio."

    hide erika
    hide tomas
    hide charles
    with Dissolve(0.4)

    "{i}Las voces se cruzan. Cada uno defiende su pedazo de razón. El grupo eleva el tono, aún bajo el impacto de lo vivido.{/i}"

    menu:
        "Defendés a Erika por haber actuado cuando otros dudaban":
            $ erika += 1
            $ tomas -= 1
            "{i}Erika te mira sin decir nada. Tomás aprieta los dientes.{/i}"
        "Culpás a Charles por haber insistido más allá de lo prudente":
            $ charles -= 1
            "{i}Charles te observa sin emoción. La herida va más allá del orgullo.{/i}"
        "Proponés enfocarse en cómo seguir, no en quién falló":
            $ marina += 1
            "{i}Marina asiente. Ingrid murmura algo que suena como ‘por fin’.{/i}"

    "{i}Un zumbido en el cielo. El grupo gira la cabeza. Un avión. Bajo. Gris. Se acerca… hace un giro. Las voces explotan. Gritos. Brazos al aire. Un silbido de esperanza.{/i}"

    "{i}Pero no baja. No gira hacia ellos. Lo ven alejarse como un recuerdo que nunca fue suyo.{/i}"

    "{i}¿Y ahora qué? Esperar sentados. O buscar una alternativa. La isla no da certezas. Sólo opciones duras.{/i}"

    jump cap11_end

label cap11_post_salida_rapida:

    scene bg costa_orilla_clara with fade
    show screen combined_ui

    "{i}La arena está húmeda. Las rocas escupen espuma. El grupo llega justo a tiempo. El mar ya lame la entrada con fuerza. Si hubieran tardado más, estarían encerrados.{/i}"

    $ hambre += 1
    $ sed += 1
    $ cansancio += 2

    show marina preocupada at left with Dissolve(0.4)
    m "Fue suerte. No decisión. Y la suerte... no se recicla."

    show bob parado enojado at center with Dissolve(0.4)
    b "La imprudencia va a terminar con uno de nosotros muerto... o varios."

    show laura triste at right with Dissolve(0.4)
    l "Lo siento, me tento la aventura. No pretendía ponerlos en riesgo"

    hide marina
    hide bob
    hide laura
    with Dissolve(0.4)

    "{i}La discusión es suave, pero punzante. Nadie grita. Pero se dicen las cosas con claridad.{/i}"

    menu:
        "Ya no podemos actuar sin plan. Hay que decidir juntos.":
            $ tomas += 1
            $ marina += 1
            "{i}Tomas asiente. Marina murmura: ‘Era hora’.{/i}"
        "El problema fue la falta de liderazgo claro.":
            $ bob += 1
            $ marina -= 1
            "{i}Bob no habla, pero se mantiene más cerca que antes. Marina se aleja hacia una roca.{/i}"
        "Lo importante es haber llegado. El resto se verá después.":
            $ laura += 1
            "{i}Laura sonríe, muy apenas. Nadie contradice… por ahora.{/i}"

    "{i}El cielo cruje. Un ruido. Una línea metálica en el horizonte. Un avión. Las manos se alzan. Los gritos rompen el aire.{/i}"

    "{i}Pero no desciende. Da media vuelta. Se va. Como si nunca los hubiera visto. El silencio pesa sobre todos.{/i}"

    "{i}¿Esperar otro día? ¿O buscar otras opciones? Hay que decidir que hacer.{/i}"

    jump cap11_end


label cap11_end:
        $ choice_position = "default" # default alta superior
        menu:
            "CONTINUAR":
                jump chapter_12_start
                #jump chapter_9_start
            "VOLVER A VER EL RESÚMEN":
                jump cap11_end
                #jump chapter_8_end



#######################################################################################   #####   ######  #####  #########################################################
##########################################################################################  ##  ########  #####  #########################################################
## Aca comienza la PARTE 11 ##############################################################  ##  ########  #####  #########################################################
########################################################################################   ####   ######  #####  #########################################################

label chapter_12_start:
    "ACA EMPIEZA EL CAP 12"
    jump cap12_avion_visto

label cap12_avion_visto:

    scene bg costa_amplia_con_niebla with fade
    show screen combined_ui

    "{i}El grupo descansa sobre la arena húmeda. Las voces son pocas. El cansancio y la tensión cae sobre el grupo como un mazazo.{/i}"

    show marina mirando_cielo at left with Dissolve(0.4)
    m "¿Eso es…? ¡Mirá arriba!"

    show ingrid parada at center with Dissolve(0.4)
    i "¡Un avión! ¡Está girando!"

    show tomas levantandose at right with Dissolve(0.4)
    t "¡Agiten los brazos! ¡Griten! ¡Que nos vean!"

    hide marina
    hide ingrid
    hide tomas
    with Dissolve(0.4)

    "{i}Todos se levantan. Saltan. Gritan. Erika intenta prender fuego una tela pero todo esta mojado. Bob lanza una rama al aire. El avión gira... y se aleja entre nubes bajas.{/i}"

    show laura decepcionada at center with Dissolve(0.4)
    l "(susurrando) No nos vieron. No fue suficiente."

    hide laura with Dissolve(0.4)

    "{i}El grupo queda quieto. El sonido del motor se aleja. La esperanza se convierte en pregunta. ¿Y ahora qué?{/i}"

    jump cap12_discusion_rescate

label cap12_discusion_rescate:

    scene playa_tarde with Dissolve(0.5)

    show laura molesta at left
    l "¡Era un avión de búsqueda! ¡Lo vi claramente! Dio una curva y se fue."

    show charles despreocupado at centerright
    c "Sí, pero no bajó ni hizo señales. Sin duda ni nos vió."

    show erika seria at centerleft
    k "No podemos quedarnos esperando. Hay que hacer algo visible. Algo que grite 'estamos acá'."

    show bob firme at center
    b "No nos desesperemos, pensemos. Ya demostramos que podemos hacer cosas juntos. ¿Se acuerdan del jabalí?"

    show marina preocupada at right
    m "Sí, pero después cada uno se fue por su lado. Y mirá cómo terminamos."

    show ingrid cansada at centerleft
    i "Lo que pasó con la caja fue grave. Todos sabíamos que había algo importante ahí."

    show tomas callado at center
    t "Y cuando volvimos... el mapa y el cuaderno ya no estaban."

    show erika enojada at centerleft
    k "¿Y ustedes? ¿Van a explicar por qué se fueron solos a la cueva?"

    show laura a_la_defensiva at left
    l "No teníamos que pedir permiso. Vimos una oportunidad y la tomamos."

    show charles bromista at centerright
    c "Además, conseguimos algo. No todo, pero algo. ¿No cuenta?"

    show bob serio at center
    b "¿Y si no los encontrábamos? ¿Y si la marea los atrapaba?"

    show marina juzgadora at right
    m "Fue egoísta. Y peligroso. No es la primera vez que actúan por su cuenta."

    show ingrid reflexiva at centerleft
    i "La caja, el mapa, las notas... eran pistas. Pero no para que dos se metan solos en una cueva inundada."

    menu:
        "Defender a Laura y Charles":
            $ cap12_choice = "Defender a Laura y Charles"
            $ laura += 1
            $ charles += 1
            y "Tomaron una decisión arriesgada, sí. Pero también actuaron con iniciativa."
            l "Gracias. No todo se puede resolver en asamblea."
            c "¡Al fin alguien que lo entiende!"

        "Recriminar su actitud":
            $ cap12_choice = "Recriminar su actitud"
            $ marina += 1
            $ erika += 1
            y "Lo que hicieron fue imprudente. Pusieron en riesgo al grupo."
            m "Exactamente. No podemos permitir que cada uno haga lo que quiera."
            k "Gracias por decirlo."

        "Intentar mediar entre ambos lados":
            $ cap12_choice = "Intentar mediar entre ambos lados"
            $ bob += 1
            $ ingrid += 1
            y "Lo que importa ahora es que estamos todos vivos. Aprendamos de esto."
            b "Bien dicho. Lo que viene va a requerir más unidad."
            i "Sí. No podemos repetir errores."

        "Quedarse en silencio":
            $ cap12_choice = "Quedarse en silencio"
            y "{i}Preferís observar. Las palabras vuelan, pero las miradas pesan más.{/i}"

    jump cap12_reacciones_jugador

label cap12_reacciones_jugador:

    if cap12_choice == "Defender a Laura y Charles":
        show laura agradecida at left
        l "No todos entienden lo que es actuar bajo presión. Gracias por no juzgarnos."

        show charles relajado at centerright
        c "Sabía que ibas a ver el lado práctico. No todo es democracia en la selva."

        show marina molesta at right
        m "¿En serio? ¿Eso es lo que valoramos ahora?"

        show erika decepcionada at centerleft
        k "Pensé que tenías más criterio..."

    elif cap12_choice == "Recriminar su actitud":
        show marina satisfecha at right
        m "Gracias por poner las cosas en su lugar. Ya era hora."

        show erika firme at centerleft
        k "Tu voz pesa. Y hoy la usaste bien."

        show laura herida at left
        l "No esperaba eso de vos..."

        show charles incómodo at centerright
        c "Bueno, ya entendí el mensaje."

    elif cap12_choice == "Intentar mediar entre ambos lados":
        show bob tranquilo at center
        b "Eso es lo que necesitamos. Cabeza fría."

        show ingrid serena at centerleft
        i "Tu forma de ver las cosas ayuda a que no nos rompamos."

        show laura pensativa at left
        l "Tal vez nos apresuramos..."

        show charles reflexivo at centerright
        c "Sí... pudo haber salido mal."

    elif cap12_choice == "Quedarse en silencio":
        show marina desconfiada at right
        m "¿Nada que decir? A veces el silencio también toma partido."

        show bob observador at center
        b "Estás pensando. Lo respeto."

        show laura confundida at left
        l "¿Estás de acuerdo o no?"

        show charles curioso at centerright
        c "Tu cara dice más que tus palabras."

    show erika decidida at centerleft
    k "Sea como sea, tenemos que volver. El refugio es lo único que tenemos seguro."

    show bob asintiendo at center
    b "Y tenemos que pensar qué hacemos con lo que se recuperó. Las joyas fueron robadas y las están buscando."

    show ingrid mirando al horizonte at centerleft
    i "¿Cómo que hacemos, las entregamos a la policía. Es lo más lógico."

    "Algunos no parecen estar muy de acuerdo, está claro que podría haber otros destinos para esas joyas."

    scene bosque_atardecer with fade
    "El grupo comienza a caminar de regreso. Las tensiones no se han resuelto del todo, pero algo ha cambiado."

    jump cap12_regreso_refugio

label cap12_regreso_refugio:

    scene bosque_atardecer with fade

    "Las ramas crujen bajo los pies. El sol cae lento, tiñendo el bosque de naranja y sombras largas."

    show laura caminando at left
    l "Cuando vi el mapa, pensé... tal vez era una señal. Algo que nos podía sacar de acá."

    show charles caminando at centerright
    c "Y si no lo hacíamos nosotros, alguien más lo iba a hacer. No quería que se perdiera."

    show marina caminando at right
    m "¿Y pensaron en nosotros? En lo que íbamos a sentir al ver que no estaban."

    show bob caminando at center
    b "La confianza se construye. Y se rompe fácil."

    show ingrid caminando at centerleft
    i "Pero también se puede reparar. Si hay voluntad."

    menu:
        "Preguntar a Laura por qué no confió en el grupo":
            $ laura += 1
            y "¿Por qué no lo hablaste con nosotros? Podíamos haber ido juntos."
            l "No sé... pensé que si lo discutíamos, nunca íbamos a decidir nada."

        "Preguntar a Charles si pensó en el peligro":
            $ charles += 1
            y "¿Y si la marea los atrapaba? ¿Pensaste en eso?"
            c "Sí. Pero también pensé que si no lo intentábamos, nos íbamos a arrepentir."

        "Reflexionar sobre lo que significa confiar":
            $ bob += 1
            $ ingrid += 1
            y "Confiar no es estar de acuerdo en todo. Es saber que el otro no te va a dejar atrás."
            b "Eso. Eso es lo que tenemos que recuperar."
            i "Y cuidar."

        "No decir nada, solo seguir caminando":
            y "{i}Caminás en silencio. Las palabras flotan entre los árboles, pero vos elegís el peso del momento.{/i}"

    show erika mirando al cielo at centerleft
    k "¿Y ahora qué? ¿Guardamos las joyas? ¿Las usamos? ¿Las escondemos?"

    show bob pensativo at center
    b "No sabemos si alguien más las está buscando. El recorte hablaba de ladrones, no de tesoros."

    show marina inquieta at right
    m "Y si ese avión vuelve... ¿qué vamos a contar?"

    show charles firme at centerleft
    c "Aún hay tiempo para decidir eso, no? Aún estamos atrapados en esta isla."

    scene refugio_tarde with fade
    "El refugio aparece entre los árboles. No es perfecto, pero es suyo. Y por ahora, es hogar."

    jump cap12_cena_refugio

label cap12_cena_refugio:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)

    "El grupo se acomoda en el refugio. Se apoyan contra los troncos, las piernas se estiran, y el aire huele a leña y humedad."

    show bob cocinando at center
    b "No es gourmet, pero calienta el alma. Sopa de raíces y unas zanahorias silvestres."

    show marina sirviendo agua at right
    m "Y agua fresca. No como la de la cueva..."

    show laura sentada at left
    l "Todavía me duelen las piernas. Pero estoy viva. Y eso ya es mucho."

    show charles comiendo at centerright
    c "¿Qué habrá pasado con quién enterró las joyas? Se tomó un buen trabajo para ocultarlas."

    show erika pensativa at centerleft
    k "Quizás algo le pasó y nunca puedo regresar a recuperarlas."

    show ingrid tomando sopa at center
    i "LO nunca logró salir de la isla... hay muchos peligros. Un jabalí furioso, serpientes venenosas..."

    "Comen en silencio por un momento. El calor de la sopa contrasta con el frío de la noche que se acerca."

    jump cap12_conversaciones_jugador

label cap12_conversaciones_jugador:

    menu:
        "Hablar con Laura sobre lo que sintió en la cueva":
            $ laura += 1
            show laura cerca at left
            l "Pensé que no salía. Que me iba a quedar ahí. Pero Charles no me dejó rendirme."

        "Hablar con Charles sobre las joyas":
            $ charles += 1
            show charles cerca at centerright
            c "No sé si valen tanto como dicen. Pero verlas ahí... fue como tocar una historia olvidada."

        "Hablar con Erika sobre el grupo":
            $ erika += 1
            show erika cerca at centerleft
            k "Estamos rotos. Pero no destruidos. Si aprendemos de esto, podemos ser más fuertes."

        "Hablar con Ingrid sobre el futuro":
            $ ingrid += 1
            show ingrid cerca at center
            i "Mañana tenemos que decidir. Qué hacer con las joyas, con el mapa, con nosotros."

        "No hablar con nadie":
            y "{i}Te quedás observando. Las palabras flotan, pero vos elegís el silencio como compañía.{/i}"

    "La comida se termina. Las miradas se cruzan. Algunos se acomodan para dormir, otros vigilan el entorno."

    jump cap12_noche

label cap12_noche:

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)

    "La noche cae como un manto espeso. El fuego se reduce a brasas. Los cuerpos se acomodan en mantas improvisadas."

    "El silencio no es total. Se oyen respiraciones, algún suspiro, el crujir de ramas lejanas."

    "Dormís. Y aunque el suelo es duro, el cansancio vence."

    jump cap12_amanecer

label cap12_amanecer:

    scene expression fondos_refugios[refugio]["interior"] with Dissolve(0.5)

    "El sol se filtra al interior del refugio. El aire es fresco. El cuerpo, aunque adolorido, se siente más liviano."

    show bob estirando at center
    b "Dormí como roca. Hoy hay que pensar. No podemos seguir improvisando."

    show marina preparando algo at right
    m "Tenemos comida para un par de días. Pero no más."

    show erika anotando en su cuaderno at centerleft
    k "Voy a hacer una lista. Lugares, recursos, riesgos."

    show laura mirando el mapa at left
    l "Este mapa... tiene más marcas. No vimos todo."

    show charles sacando el cuaderno de notas at centerright
    c "Y este cuaderno tiene claves. Nombres, fechas. Algo más hay."

    jump cap12_inicio_plan

label cap12_inicio_plan:

    scene expression fondos_refugios[refugio]["exterior"] with Dissolve(0.5)

    "Salen del refugio. El sol se levanta entre las ramas. El aire es fresco, pero la tensión se siente antes que el calor."

    show bob firme at center
    b "La huerta está casi vacía. Los hongos de la cueva no son seguros. Y los huevos que encontramos ya no están."

    show marina preocupada at right
    m "Podemos intentar pescar, pero no es fácil. No tenemos los implementos mínimos."

    show ingrid reflexiva at centerleft
    i "Sobrevivir sin hacer nada no es opción. No por mucho tiempo."

    show erika seria at left
    k "Entonces decidamos. ¿Qué hacemos para salir de acá?"

    jump cap12_plan_discusion

label cap12_plan_discusion:

    scene playa_reunion with fade

    "El grupo se acomoda en círculo, algunos sentados en troncos, otros de pie. El silencio pesa."

    show bob decidido at center
    b "Podemos construir una balsa. Usar el bote inflable como base, sumar troncos, hojas de palma, lo que flote."

    b "Vi una silueta en el horizonte. Podría ser otra isla. El avión pasó en esa dirección."

    show erika firme at right
    k "O podemos hacer una hoguera gigante. Algo que se vea desde kilómetros. Si pasa un barco o avión, que nos vean."

    show charles pensativo at left
    c "Ambas ideas tienen sentido... pero también riesgos."

    "Las miradas se cruzan. Nadie quiere decidir solo. Es momento de hablar."

    jump cap12_plan_opciones_jugador

label cap12_plan_opciones_jugador:

    menu:
        "Construir la balsa y arriesgarse":
            $ jugador_postura = "balsa"
            "Crees que vale la pena arriesgarse. Quedarse no es opción."

        "Hacer la hoguera y esperar ayuda":
            $ jugador_postura = "hoguera"
            "Prefieres apostar a que alguien los vea. Irse podría ser peor."

        "Ambas ideas tienen problemas...":
            $ jugador_postura = "duda"
            "No estás convencido de ninguna. Hay que pensar más."

    jump cap12_plan_intercambio_personajes

label cap12_plan_intercambio_personajes:

    if jugador_postura == "balsa":
        show bob animado at center
        b "¡Eso! Si nos movemos, hay una chance real. No podemos quedarnos esperando."

        show erika escéptica at right
        k "¿Y si esa silueta no es nada? ¿Y si la balsa se rompe? No hay segunda oportunidad."

        show charles dudando at left
        c "Mmm... lo de la balsa suena bien, pero Erika tiene razón. Es arriesgado."

    elif jugador_postura == "hoguera":
        show erika esperanzada at right
        k "Gracias. No podemos lanzarnos al mar sin saber. Una señal fuerte puede salvarnos."

        show bob frustrado at center
        b "¿Y si nadie pasa? ¿Cuánto tiempo más podemos aguantar acá?"

        show charles pensativo at left
        c "La hoguera es más segura... pero también más pasiva. No sé..."

    elif jugador_postura == "duda":
        show bob impaciente at center
        b "¡Pero hay que decidir! No podemos quedarnos en la indecisión."

        show erika firme at right
        k "Pensar no es perder tiempo. Es evitar errores."

        show charles confundido at left
        c "Estoy igual que tú. No sé cuál es peor... o mejor."

    "El grupo se enreda en argumentos. Cada uno defiende su idea, pero también escucha."

    jump cap12_plan_posturas

label cap12_plan_posturas:

    scene playa_reunion_tension with dissolve

    "Las voces se elevan. Cada propuesta empieza a tomar forma, pero también a mostrar sus grietas."

    # Postura a favor de la hoguera
    show erika explicando at right
    k "La hoguera puede arder por días. Si usamos aceite de alguna planta, madera seca, ropa... será visible desde lejos."

    k "No arriesgamos vidas. No nos alejamos. Solo necesitamos que alguien nos vea."

    show ingrid asintiendo at centerleft
    i "Y podemos mantenerla encendida por turnos. No es tan difícil."

    # Postura a favor de la balsa
    show bob señalando el horizonte at center
    b "Pero si nadie pasa... ¿qué hacemos? ¿Morir esperando?"

    b "La silueta en el horizonte está ahí. No es imaginación. Podemos llegar en un día si el clima ayuda."

    show marina dudando at right
    m "¿Y si hay corriente? ¿Y si no hay isla? ¿Y si no volvemos?"

    # Charles empieza a cambiar de opinión
    show charles pensativo at left
    c "Lo de la hoguera suena más seguro... pero si Bob tiene razón, podríamos estar a un paso de salir."

    c "No sé. Cada vez que escucho a uno, cambio de idea."

    "Charles se gira hacia ti, buscando tu opinión."

    menu:
        "La balsa es nuestra mejor oportunidad. Hay que arriesgarse.":
            $ influencia_charles += 1
            "Le hablas con convicción. Charles asiente, aunque aún duda."

        "La hoguera es más sensata. No podemos lanzarnos al mar a ciegas.":
            $ influencia_charles -= 1
            "Le explicas los riesgos. Charles parece inclinarse hacia tu lógica."

        "Ambas ideas tienen sentido. Lo importante es que el grupo esté unido.":
            $ influencia_charles = 0
            "Charles sonríe. 'Eso también es verdad', dice, aunque sigue sin decidirse."

    "La discusión continúa. Algunos personajes cambian de postura, otros se aferran a su plan."

    jump cap12_plan_charles_decide

label cap12_plan_charles_decide:

    "Charles se queda en silencio unos segundos. Mira a Erika, luego a Bob. Finalmente te mira a ti."

    if influencia_charles > 0:
        show charles decidido at left
        c "Podría ir con ustedes. Si hay una posibilidad de salir, hay que tomarla."

        $ charles_grupo = "balsa"

    elif influencia_charles < 0:
        show charles firme at left
        c "Podría quedarme con Erika. Prefiero esperar ayuda que arriesgarme al mar."

        $ charles_grupo = "hoguera"

    else:
        if charles >= 1:
            show charles sonriente at left
            c "Confío en ti. Podría sumarme a tu grupo."

            $ charles_grupo = jugador_postura
        else:
            show charles neutral at left
            c "No lo sé... pero creo que Erika tiene razón."

            $ charles_grupo = "hoguera"

    "La indecisión de Charles marca el cierre de la discusión. El grupo empieza a dividirse."
    jump cap12_plan_division

label cap12_plan_division:
##### este no va, quedo por las dudas
    scene playa_decision with fade
    "Después de una larga discusión, el grupo decide dividirse en dos proyectos: construir una balsa para buscar ayuda o mantener una hoguera encendida para ser vistos desde el aire."

    "Algunos ya han tomado partido."

    show bob at centerleft
    show marina at left
    show erika at centerright
    show tomas at right


    "Bob, Tomas y Marina se inclinan por construir la balsa. Erika, Ingrid y Laura creen que mantener la hoguera encendida es más seguro. Charles aún no ha decidido."

    menu:
        "Unirme al equipo que construye una balsa con Bob, Laura y Marina":
            $ proyecto = "balsa"
            $ equipo_actual = ["jugador", "Bob", "Marina", "Laura"]
            #$ posibles_reclutas = ["Charles", "Tomas"]
            jump cap12_plan_division2

        "Unirme al equipo de la hoguera con Erika, Ingrid y Tomas":
            $ proyecto = "hoguera"
            $ equipo_actual = ["jugador", "Erika", "Tomas", "Ingrid"]
            #$ posibles_reclutas = ["Charles", "Tomas"]
            jump cap12_plan_division2

label cap12_plan_division2:

    scene playa_separacion with fade

    "El grupo se divide en dos zonas de la playa. Algunos se acercan a Bob, otros a Erika."

    if proyecto == "balsa":
        show bob motivado at center
        b "Vamos a necesitar hojas de palma para trensar cuerdas, troncos, ramas... y el bote inflable. ¡Manos a la obra!"

        show marina decidida at right
        m "Yo puedo ayudar con los nudos. Aprendí algo en los campamentos."

        show charles sonriente at centerleft
        c "Estoy contigo. Vamos a hacer que esto funcione."
        $ equipo_actual.append("Charles")

        "Te sumas al grupo de la balsa. El trabajo comienza con energía y urgencia."
        jump cap12_balsa_inicio

    elif proyecto == "hoguera":
        show erika concentrada at center
        k "Necesitamos madera seca, algo de aceite de alguna planta, telas... y una estructura que aguante el viento."

        show ingrid práctica at right
        i "Hay ramas gruesas cerca del acantilado. Podemos empezar por ahí."

        show charles sonriente at centerleft
        c "Estoy contigo. Vamos a hacer que esto funcione."
        $ equipo_actual.append("Charles")

        "Te unes al grupo de la hoguera. El plan es claro, pero requiere precisión."
        jump cap12_hoguera_inicio

label cap12_balsa_inicio:

    scene playa_balsa_construccion with Dissolve(0.5)

    show bob organizando at center
    b "Vamos a dividir tareas. Necesitamos troncos, cuerdas, bidones, y revisar el bote inflable."

    show marina activa at right
    m "Yo puedo buscar los bidones. Vi algunos cerca del arroyo."

    "Te toca decidir cómo organizar el equipo. Todos esperan tu palabra."

    menu:
        "Asignar tareas según habilidades":
            $ liderazgo += 1
            "El grupo se organiza con eficiencia. Cada uno sabe qué hacer."

        "Dejar que cada uno elija qué hacer":
            $ liderazgo -= 1
            "Algunos se dispersan. Hay confusión, pero también autonomía."

        "Tomar el control y dar órdenes claras":
            $ liderazgo += 2
            "El grupo responde con rapidez. Aunque algunos se sienten presionados."

    "La construcción comienza. El sonido de ramas cortadas y nudos apretados llena el aire."

    jump cap12_balsa_encuentro_1

label cap12_balsa_encuentro_1:

    scene bosque_madera with dissolve

    "Mientras buscás ramas gruesas cerca del límite del bosque, te cruzás con Erika. Lleva una pila de madera seca en los brazos."

    show k molesta at center
    k "¿Qué hacés acá? Esta zona la estamos usando para la hoguera."

    y "Necesitamos madera para reforzar la balsa. No podemos navegar con algo que se desarme en el primer oleaje."

    k "Y nosotros no podemos quedarnos sin fuego. Si pasa un avión y no tenemos con qué encenderlo, perdemos nuestra única oportunidad."

    menu:
        "Insistir en llevarse la madera":
            $ erika -= 1
            "Erika te mira con dureza."
            k "Hacelo. Pero no esperes que te cubra si algo sale mal."

        "Negociar y dividir los recursos":
            $ erika += 1
            "Proponés repartir la madera. Erika duda, pero acepta."
            k "Está bien. Pero que no se repita."

        "Ceder y dejar que Erika se lleve todo":
            $ erika += 1
            "Erika queda sorprendida por tu actitud."
            menu:
                "Invitar a Erika a sumarse al proyecto de la balsa":
                    if erika > 2:
                        $ equipo_actual.append("Erika")
                        #$ proyecto_reclutas += 1
                        "Erika te observa con atención, luego asiente lentamente."
                        k "Aún creo que la hoguera es una buena opción pero si tu haces la balsa puede funcionar."
                        "Erika y tu vuelven con la madera al sitio de construccion de la balsa"
                    else:
                        "Erika te observa con atención, luego sacude la cabeza lentamente."
                        k "Claramente no me conoces, [nombre_jugador]. No voy a abandonar a mi grupo."
                "No quiero problemas entre nosotros, hay mas madera en la isla.":
                    "Erika se interna molesta en la jungla cargando la madera."   

    "El bosque queda en silencio, pero la tensión persiste."

    jump cap12_balsa_crisis_1

label cap12_balsa_crisis_1:

    scene balsa_construccion with fade

    "La construcción avanza, pero el ambiente está tenso. Marina se sienta sola, mirando el agua con expresión apagada."

    show marina triste at center
    m "No sé si quiero seguir con esto..."

    y "¿Qué pasó?"

    m "Desde que empezamos, nadie me pregunta nada. Tomas y Laura deciden todo, vos estás siempre ocupado. Me siento invisible."

    "La balsa cruje con el peso de los materiales. El silencio se vuelve incómodo."

    menu:
        "Decirle que no hay tiempo para dramas":
            $ marina -= 1
            y "Marina, aquí todos hacemos lo que podemos. No hay tiempo para hacerse la víctima."
            "Marina se pone de pie, dolida."
            m "Entonces no cuenten conmigo."
            $ equipo_actual.remove("Marina")
            "Marina abandona el grupo y se dirige a donde se está haciendo la hoguera."
            "La tensión aumenta y la balsa aún no está lista."

        "Reconocer su esfuerzo y proponerle que se encargue de una tarea clave":
            $ marina += 1
            y "¿Que te parece liderar la organización de los suministros?"
            m "¿En serio? Bueno... lo voy a intentar."
            "Te acercás y le agradecés por todo lo que ha hecho."
            m "Gracias... No quiero rendirme. Pero necesito sentir que importo."
            "La tensión baja, pero queda claro que el grupo necesita más comunicación."

    jump cap12_balsa_encuentro_2

label cap12_balsa_encuentro_2:

    scene playa_orilla with dissolve

    "Mientras inspeccionás la orilla, escuchás una voz familiar cantando desafinadamente."

    show c relajado at center
    c "¡Ahoy! Mirá lo que encontré. Una vela vieja, pero todavía sirve."

    y "¿Dónde la conseguiste?"

    c "Estaba enterrada cerca de los restos del bote que usamos al principio. No sé si usarla para hacer humo en la hoguera o dársela a ustedes para la balsa."

    "Charles sonríe, pero se nota que está esperando que tomes una postura."

    menu:
        "Pedirle la vela para la balsa":
            $ charles += 1
            y "Esa vela podría ser clave para navegar mejor y no terminar flotando en el mar."
            c "Bueno, si lo decís así... acá tenés."

        "Decirle que la use como quiera":
            "Decidís no presionarlo. Charles se encoge de hombros."
            c "Gracias por no hacerme sentir culpable."
            "Charles se aleja, con cara pensativa. Es dificil entender como piensa Charles."
            if charles > 1:
                c "Si, mejor sigo en el equipo. Aqui está la vela."
            else:
                c "En la hoguera me van a recibir bien cuando lleve esta vela."
                c "Me voy con el otro equipo."
                $ equipo_actual.remove("Charles")

        "Burlarte de su indecisión":
            $ charles -= 1
            y "¿Sigues con idas y vueltas? Pareces un niño eligiendo un dulce."
            "Charles frunce el ceño."
            c "¿Sabés qué? Me la llevo, seguro que en la hoguera me reciben mejor."
            $ equipo_actual.remove("Charles")

    "Charles se aleja, tarareando una melodía inventada."

    jump cap12_balsa_encuentro_3

label cap12_balsa_encuentro_3:

    scene laboratorio_improvisado with dissolve

    "Te acercás al refugio donde Ingrid ha estado trabajando con algunos materiales recuperados."

    show i seria at center
    i "Estuve haciendo cálculos. La balsa no va a resistir si no se adhiere el bote a las ramas que están poniendo poe debajo."

    y "¿Qué proponés?"

    i "Se puede sacar una resina pegajosa de unos arboles que vi en la isla. Pero solo encontré dos de esos árboles."
    i "Es la misma resina que pensabamos usar para acelerar el encendido del fuego de la hoguera."

    "Ingrid te mira con seriedad. No hay sarcasmo ni enojo, solo lógica."

    menu:
        "Pedirle que te lleve hasta esos árboles":
            y "Realmente sin la balsa, no hay salida. Además el fuego va a prender de todas maneras."
            y "Y tú misma dices que sin eso nos vamos a hundir en medio del mar"
            i "Entiendo. Pero esto pone en riesgo a mi grupo."
            i "Pero tienes razón, tampoco puedo dejar que se ahoguen."
            y "¿Que tal si te sumas al proyecto de la balsa? Tu podrías guiar para hacer buen uso de la resina."
            if ingrid > 1:
                $ equipo_actual.append("Ingrid")
                #$ proyecto_reclutas += 1
                "Ingrid te observa con atención."
                i "Si voy con ustedes, quiero tener voz en las decisiones técnicas. ¿Está claro?"
            else:
                i "No, el otro equipo me necesita. No deberías pedir ni la resina ni que los traicione."
                $ ingrid -= 1

        "Negociar una solución intermedia":
            $ ingrid += 1
            "Podriamos usar un poco para dar mas solidez a la balsa y ustedes usar el resto para encender el fuego.."
            i "No es ideal, pero podría funcionar. Acepto."

        "Respetar su decisión y no pedir el recurso":
            $ ingrid += 1
            "Decidís no presionar. Ingrid asiente con respeto."
            i "Gracias. No todos entienden lo que está en juego."

    "Ingrid vuelve a sus cálculos. La decisión que tomaste podría cambiar el rumbo del proyecto."

    jump cap12_balsa_crisis_2

label cap12_balsa_crisis_2:

    scene balsa_construccion_tarde with fade

    "Volvés al campamento y notás que Laura ha reorganizado todo el plan de construcción sin consultar a nadie."

    show l molesta at center
    l "No podíamos seguir esperando. Tomé decisiones. Si no te gusta, podés irte."

    y "¿No pensás que deberíamos decidir esto juntos?"

    l "¿Decidir? Cada vez que debatimos perdemos tiempo. Yo quiero que esto funcione, no que sea democrático."

    "El resto del equipo observa en silencio. La tensión es palpable."

    menu:
        "Confrontarla y exigir que respete al grupo":
            $ laura -= 1
            y "¿Otra vez tomando decisiones por tu lado sin importar los demas?"
            y "Hay que escuchar a los demás. No puedes cambiar el plan sin consultar."
            l "Yo me bajo. Tampoco te voy a consultar esto. Me voy con el otro equipo."
            $ equipo_actual.remove("Laura")

        "Cederle el liderazgo del proyecto":
            $ laura += 1
            y "No es la manera adecuada pero lo importante es hacer las cosas."
            y "Explica lo que quieres hacer y nos repartimos esas tareas con el grupo."
            l "Al menos ahora vamos a avanzar."

        "Proponer una estructura compartida de decisiones":
            y "Al grupo le viene bien tu ánimo y determinación."
            y "Separemos las tareas, tu coordina algunas y otros decidiran sobre las demas."
            l "Está bien. Pero si esto se vuelve un caos, no me culpes."

    "La crisis deja huellas. El grupo sigue adelante, pero la dinámica ha cambiado."

    jump cap12_balsa_evaluacion

label cap12_balsa_evaluacion:

    scene playa_balsa_finalizada with fade

    "La balsa está lista. El grupo se reúne en la orilla, observando el horizonte."

    $ cantidad_equipo = len(equipo_actual)

    if cantidad_equipo >= 5:
        "El equipo es sólido. Hay suficientes manos para navegar y enfrentar imprevistos."
        "Los reclutas del otro proyecto aportan nuevas perspectivas y recursos."
        "La tensión interna se ha reducido, aunque quedan heridas abiertas."

        menu:
            "Confirmar el proyecto de la balsa":
                "El grupo se prepara para zarpar. El proyecto está completo."
                jump cap12_balsa_completa

    elif cantidad_equipo == 4:
        "El equipo está incompleto. No hay suficientes personas para garantizar el éxito del proyecto."
        "Tampoco el grupo de la hoguera tiene los recursos ni el personal necesario para sostener su plan."
        "Ambos equipos se ven obligados a reunirse y tomar una decisión conjunta."

        menu:
            "Convocar a todos para decidir qué proyecto seguir":
                "Se organiza una reunión entre los ocho personajes. El futuro depende de lo que decidan juntos."
                jump cap12_decision_grupal

    else:
        "El equipo es insuficiente. La balsa no puede zarpar en estas condiciones."
        "La falta de colaboración y las decisiones conflictivas debilitaron el proyecto."
        "Algunos miembros dudan, otros se han ido. El grupo de la hoguera sigue activo."

        menu:
            "Aceptar que el proyecto de la balsa ha fallado":
                "El grupo se repliega. El liderazgo pasa al equipo de la hoguera."
                jump cap12_hoguera_completa

label cap12_hoguera_inicio:

    scene campamento_hoguera_dia
    with fade

    show erika neutral at left with Dissolve(0.5)
    show ingrid annoyed at centerright with Dissolve(0.5)
    show tomas annoyed at centerleft with Dissolve(0.5)
    show charles relaxed at right with Dissolve(0.5)

    k "Si queremos que esto funcione, necesitamos una base sólida. Troncos grandes abajo, ramas intermedias, hojas secas en la cima. Si se cae antes de prenderla, perdimos todo."

    c "¿Y cómo pensás cortar troncos sin hachas? ¿Vamos a abrazarlos hasta que se rompan?"

    c "Yo digo que juntemos todo lo que encontremos y lo apilemos. Si parece una montaña, ya está. ¿No?"

    k "Eso no va a prender bien. Y si se cae, no hay segunda oportunidad."

    t "Lo que no hay, no hay. Busquemos opciones."

    "Todos te miran, esperando tu opinión."

    menu:
        "Apoyar a Erika":
            $ erika += 1
            $ charles -= 1
            $ enfoque_hoguera = "estructurado"
            y "La estructura es clave. Si se cae antes de prenderla, perdimos todo."
            k "Gracias. Alguien entiende lo que está en juego."
            c "Claro, sigamos planeando como si tuviéramos herramientas mágicas."

        "Apoyar a Tomas":
            $ tomas += 1
            $ erika -= 1
            $ enfoque_hoguera = "adaptativo"
            y "No podemos planear como si tuviéramos herramientas. Hay que adaptarse."
            t "¡Exacto! Por fin alguien con los pies en la tierra."
            k "Adaptarse no significa dejar de planear con cuidado."

        "Apoyar a Charles":
            $ charles += 1
            $ erika -= 1
            $ enfoque_hoguera = "improvisado"
            y "Si juntamos suficiente material, podemos ajustar la forma después."
            c "¡Esa es la actitud! Montaña de ramas, allá vamos."
            k "Esto no es un juego, Charles."

        "Proponer una síntesis":
            $ erika += 1
            $ tomas += 1
            $ enfoque_hoguera = "hibrido"
            y "Podemos empezar con lo que tenemos, pero seguir el diseño de Erika en lo posible."
            k "Me parece razonable."
            t "Mientras no nos pasemos el día dibujando planos, va bien."
            c "¿Y mi montaña de ramas? Nadie la quiere..."

    "Con la decisión tomada, el grupo comienza a trabajar. Las tensiones no desaparecen, pero hay una dirección clara."

    hide erika with Dissolve(0.5)
    hide tomas with Dissolve(0.5)
    hide charles with Dissolve(0.5)
    hide ingrid with Dissolve(0.5)

    jump cap12_hoguera_encuentro_1

label cap12_hoguera_encuentro_1:

    scene campamento_hoguera_dia
    with fade

    show erika neutral at left with Dissolve(0.5)
    show bob neutral at right with Dissolve(0.5)

    b "Buen día. Vine a ver cómo va el proyecto de la pira. Desde la balsa parece que están avanzando."

    k "Avanzando sí, pero no improvisando. Estamos siguiendo una estructura clara. No queremos que se venga abajo cuando más lo necesitemos."

    b "Entiendo. Aunque a veces, si uno espera a tener todo perfecto, se le pasa la oportunidad."

    k "Prefiero perder tiempo que perder la oportunidad del rescate."

    "La tensión entre Erika y Bob es evidente. Ambos tienen estilos de liderazgo distintos. Te miran, esperando tu opinión."

    menu:
        "Defender el enfoque estructurado":
            $ erika += 1
            $ bob -= 1
            y "La estructura es clave. Si se cae antes de prenderla, perdimos todo."
            k "Gracias. Alguien entiende lo que está en juego."
            b "Solo espero que no se les pase el momento por estar midiendo ramas."

        "Cuestionar el enfoque estructurado":
            $ bob += 1
            $ erika -= 1
            y "Tal vez deberíamos ser más flexibles. No sabemos cuándo va a pasar el avión."
            b "Exacto. A veces hay que actuar con lo que se tiene."
            k "Y a veces actuar sin pensar es lo que te deja sin fuego cuando más lo necesitas."

        "Intentar mediar":
            $ bob += 1
            $ erika += 1
            y "Podemos mantener la estructura, pero tener algo listo para encender rápido si aparece el avión."
            b "Eso suena razonable."
            k "Mientras no se comprometa la estabilidad, me parece bien."

        "Evitar intervenir":
            y "..."
            b "Bueno, seguiré observando."
            k "..."

    "Bob observa el trabajo un rato más, intercambia algunas palabras con Charles y Laura, y luego se despide."

    hide erika with Dissolve(0.5)
    hide bob with Dissolve(0.5)

    scene bg hoguera with fade
    "El día continúa, y el equipo de la hoguera sigue trabajando con la visita de Bob en mente."

    jump cap12_hoguera_crisis_1

label cap12_hoguera_crisis_1:

    scene campamento_hoguera_tarde
    with fade

    show erika annoyed at left with Dissolve(0.5)
    show charles neutral at right with Dissolve(0.5)

    k "¿En serio estuviste toda la mañana buscando ramas secas y no trajiste ni una decente?"

    c "¿Decente según quién? Las que encontré no estaban mojadas, ¿eso no cuenta?"

    k "¡No si son del tamaño de mi brazo! Necesitamos troncos, no souvenirs."

    c "Bueno, perdón por no tener superpoderes para partir árboles con la mente."

    "La discusión sube de tono. Charles se burla, Erika se exaspera. El ambiente se vuelve tenso. Ambos te miran, esperando que digas algo."

    menu:
        "Defender a Erika":
            $ erika += 1
            $ charles -= 1
            y "Charles, necesitamos materiales que realmente sirvan. Esto no es un juego."
            l "Gracias. Alguien que entiende la urgencia."
            c "Claro, sigamos gritando hasta que aparezcan troncos mágicos."
            c "No vine para que me griten o me pidan imposibles,"
            c "Suerte con su hoguera, me voy con el grupo de la balsa"
            $ equipo_actual.remove("Charles")
            hide charles with Dissolve(0.5)
            "Charles se interna en la jungla enojado."

        "Defender a Charles":
            $ charles += 1
            $ erika -= 1
            y "Erika, está haciendo lo que puede. No tenemos herramientas."
            c "¡Gracias! Al menos alguien ve la realidad."
            k "Sí, claro. Y mientras tanto, seguimos perdiendo tiempo."

        "Intentar mediar":
            $ erika += 1
            $ charles += 1
            y "Entiendo los dos puntos. Tal vez podemos reorganizar tareas para que cada uno haga lo que mejor se le da."
            k "Eso... podría funcionar."
            c "Mientras no me manden a abrazar troncos, estoy dentro."

        "Evitar intervenir":
            y "..."
            k "¿Nada? Genial. Silencio útil."
            c "Bueno, me voy a seguir buscando ramitas."

    "La tensión no desaparece del todo, y esas palabras dejan una marca en la dinámica del grupo."

    hide laura with Dissolve(0.5)
    hide charles with Dissolve(0.5)

    scene bg hoguera with fade
    "La tarde avanza, y el trabajo continúa con una energía distinta."

    jump cap12_hoguera_encuentro_2

label cap12_hoguera_encuentro_2:

    scene campamento_hoguera_tarde
    with fade

    if "Charles" in equipo_actual:
        jump cap12_hoguera_charles_mariana
    else:
        jump cap12_hoguera_encuentro_3

label cap12_hoguera_charles_mariana:
    show charles neutral at left with Dissolve(0.5)
    show marina nervous at right with Dissolve(0.5)

    m "Hola... vine a ver si necesitaban algo. Tenemos algunas sogas que no estamos usando."

    c "¿Sogas? ¿Para atar la pira o para atarnos nosotros cuando nos frustremos?"

    m "Pensé que podían servir para estabilizar la base. No sé si es buena idea..."

    c "Ey, no te preocupes. Es mejor que lo que yo traje esta mañana."

    m "¿Realmente les sirve? No quiero molestar..."

    c "¿Por qué eres tan mojigata? Marina, si todos fueran como vos, esto sería un spa."

    "Marina baja la mirada. Charles sonríe, pero no parece notar lo incómoda que está."

    menu:
        "Proteger a Marina":
            $ marina += 1
            $ charles -= 1
            y "Marina, tu ayuda es valiosa. No tenés que justificarte."
            m "Gracias... eso significa mucho."
            c "Uy, perdón. No quise hacerte sentir mal."

        "Presionar a Marina":
            $ marina -= 1
            y "Si vas a ofrecer algo, hacelo con seguridad. No estamos para dudas."
            m "Lo siento... no quería incomodar."
            c "Che, tampoco para retarla así."

        "Evitar intervenir":
            y "..."
            m "Bueno... me voy entonces."
            c "¿Es por algo que dije?"

    "Marina se despide con una sonrisa tímida. Charles se queda mirando la pira, pensativo."

    hide charles with Dissolve(0.5)
    hide marina with Dissolve(0.5)

    scene black with fade
    "La noche se acerca, y el grupo reflexiona sobre lo que significa colaborar entre equipos."

    jump cap12_hoguera_crisis_2

label cap12_hoguera_encuentro_3:
    #hay que ajustar este label y reconectarlo
    scene campamento_hoguera_noche
    with fade

    show laura neutral at left with Dissolve(0.5)
    show tomas neutral at right with Dissolve(0.5)

    l " Hola Tomas, el silencioso constructor de hogueras."

    t "..."

    l "¿No hablás o estás guardando energía?"

    t "..."

    l "Bueno, al menos trajiste algo útil. ¿Eso es corteza seca?"

    t "Sí."

    l "¡Milagro! Una palabra completa."

    "Tomas sigue trabajando en silencio. Laura lo observa con curiosidad, mezclada con impaciencia. El jugador puede intervenir."

    menu:
        "Valorar el silencio de Tomas":
            $ tomas += 1
            $ laura -= 1
            y "No hace falta hablar mucho para aportar. Tomas está haciendo más que muchos."
            t "Gracias."
            l "Sí, claro. Y mientras tanto, yo tengo que adivinar qué piensa."

        "Presionar a Tomas":
            $ tomas -= 1
            y "Si vas a colaborar, estaría bueno que te comuniques. Esto es un equipo."
            t "..."
            l "¡Por fin alguien que lo dice!"

        "Apoyar a Laura":
            $ laura += 1
            $ tomas -= 1
            y "Laura tiene razón. No podemos trabajar con alguien que no habla."
            l "Gracias. Pensé que era la única que lo notaba."
            t "..."

        "Intentar mediar":
            $ laura += 1
            $ tomas += 1
            y "Tomas trabaja bien, y Laura necesita claridad. Tal vez podemos encontrar un punto medio."
            l "Mientras no tenga que leerle la mente, me sirve."
            t "Haré lo posible."

    "Tomas termina de acomodar la corteza y se despide con un gesto. Laura se queda mirando la pira, pensativa."

    hide laura with Dissolve(0.5)
    hide tomas with Dissolve(0.5)

    scene black with fade
    "La noche cae, y el grupo reflexiona sobre lo que significa trabajar con estilos distintos."

    jump cap12_hoguera_crisis_2

label cap12_hoguera_crisis_2:

    scene campamento_hoguera_noche
    with fade

    show erika neutral at left with Dissolve(0.5)
    show ingrid annoyed at right with Dissolve(0.5)

    i "¿Sabés qué? Estoy harta de tus planes rígidos. Esto no es una simulación controlada, Erika."

    k "Y yo estoy harta de tu constante análisis. Si no seguimos una estructura, esto se desmorona."

    i "¡Se desmorona igual si nadie entiende ni comparte tus decisiones!"

    k "No vine a caerle bien a nadie. Vine a hacer que esto funcione."

    "La discusión escala. El tono se hace mas fuerte. El grupo pende de un hilo"

    menu:
        "Apoyar a Erika con firmeza":
            $ erika += 2
            $ ingrid -= 2
            y "Erika tiene razón. Necesitamos orden, aunque no sea perfecto."
            k "Gracias. Esto no es una competencia de lógica, es supervivencia."
            i "Entonces hacelo sola. No voy a seguir a alguien que descarta el análisis."
            $ equipo_actual.remove("Ingrid")
            hide ingrid with Dissolve(0.5)
            "Ingrid se aleja rumbo al lugar donde el otro equipo está haciendo la balsa."

        "Apoyar a Ingrid con firmeza":
            $ ingrid += 2
            $ erika -= 2
            y "Ingrid tiene razón. No podemos seguir un plan que no se cuestiona."
            i "Por fin alguien lo ve."
            k "Entonces que lo hagan sin mí. No voy a liderar un grupo que no confía."
            $ equipo_actual.remove("Erika")
            hide erika with Dissolve(0.5)
            "Erika se aleja rumbo al lugar donde el otro equipo está haciendo la balsa."

        "Intentar reconciliar":
            $ ingrid += 1
            $ erika += 1
            y "Las dos tienen puntos válidos. Si no se escuchan, esto no va a funcionar."
            k "Escuchar no significa ceder en todo."
            i "Y liderar no significa imponer sin evidencia."
            y "Estamos todos de acuerdo con eso. Repasemos lo que estamos haciendeo y busquemos que esto funcione."
            "Ambas bajan la voz. No hay acuerdo total, pero siguen en el proyecto."

        "Evitar intervenir":
            y "..."
            k "Silencio no es liderazgo."
            i "Perfecto. Otro que no dice lo que piensa."
            i "Yo no sigo en esto. Me voy."
            $ equipo_actual.remove("Ingrid")
            hide ingrid with Dissolve(0.5)
            "Ingrid se aleja rumbo al lugar donde el otro equipo está haciendo la balsa."

    "La situación está resuelta. El proyecto sigue, pero no será igual."

    hide erika with Dissolve(0.5)
    hide ingrid with Dissolve(0.5)

    jump cap12_hoguera_evaluacion

label cap12_hoguera_evaluacion:

    scene campamento_hoguera_amanecer
    with fade

    y "La hoguera está avanzando. Pero lo que importa ahora es quién sigue comprometido."

    # Recuento de personajes en el proyecto de la hoguera
    $ hoguera_equipo = 0
    $ equipo_actual.remove("jugador")

    $ hoguera_equipo = len(equipo_actual) 
    $ hoguera_equipo += 1

    "Ahora hay [hoguera_equipo] personas que siguen en el equipo de la hoguera."
    "[', '.join(equipo_actual)] y tú"

    if hoguera_equipo >= 5:
        y "Con este equipo, podemos completar la hoguera sin problemas."
        jump cap12_hoguera_completa

    elif hoguera_equipo == 4:
        y "Cuatro personas no son suficientes para asegurar el éxito."
        y "Necesitamos decidir como grupo qué hacer."
        jump cap12_decision_grupal_dialogos

    else:
        y "Con tan poca gente, no hay forma de continuar este proyecto."
        y "La única opción viable es construir la balsa."
        "Todos se miran, han puesto mucho esfuerzo cargando troncos, ramas, extrayendo aceite de plantas..."
        "Pero no es suficiente, quizás uniendo con esos recursos y su apoyo pueda completarse la balsa."
        "Cargan lo que pueden y se dirigen a donde está el grupo de la balsa"
        $ abandonar_hoguera = True
        jump cap12_balsa_completa

label cap12_decision_grupal_dialogos:

    scene campamento_decision_grupal
    with fade

    show charles neutral at center with Dissolve(0.5)

    c "No podemos seguir así. No hay suficiente gente en ningún proyecto. Hay que hablarlo."

    # Personajes que pudieron cambiar de proyecto: Bob, Marina, Tomás, Ingrid

    ## Erika
    if "Erika" in equipo_actual:
        show erika neutral at left
        k "Me quedé en la hoguera porque pensé que era lo correcto. Pero no sé si fue la mejor decisión."
    else:
        show erika neutral at left
        k "Me cambié a la balsa. No podía seguir en un grupo que no se escuchaba."

    menu:
        "Responder con empatía":
            $ erika += 1
            y "Entiendo lo que sentís. Fue una decisión difícil."
        "Responder con neutralidad":
            y "Es bueno que lo digas. Ya veremos qué hacemos."
        "Responder con crítica":
            $ erika -= 1
            y "No era momento de cambiar de grupo por inseguridad."

    ## Charles
    if "Charles" in equipo_actual:
        show charles neutral at left
        c "Me quedé en la hoguera porque no quería decepcionar a nadie. Pero tengo dudas de si va a funcionar."
    else:
        show charles neutral at left
        c "Me cambié a la balsa. Necesitaba estar con gente que no me cuestionara."

    menu:
        "Responder con apoyo":
            $ charles += 1
            y "Tu decisión fue valiente. Lo importante es que sigas adelante."
        "Responder con distancia":
            y "Lo entiendo. No todos pueden con tanta presión."
        "Responder con juicio":
            $ charles -= 1
            y "No podés esperar que nadie cuestione si hay pobre desempeño."

    ## Tomás
    if "Tomas" in equipo_actual:
        show tomas neutral at left
        t "Me quedé en la hoguera. No soy de hablar mucho, pero se que podemos lograrlo."
    else:
        show tomas neutral at left
        t "Me cambié a la balsa. No me gusta el conflicto, y allá hay más calma."

    menu:
        "Reconocer su esfuerzo":
            $ tomas += 1
            y "Tu constancia es valiosa. Gracias por seguir apostando."
        "Responder con neutralidad":
            y "Está bien. Cada uno busca lo que necesita."
        "Cuestionar su decisión":
            $ tomas -= 1
            y "No podés evitar los problemas cambiando de grupo."

    ## Ingrid
    if "Ingrid" in equipo_actual:
        show ingrid neutral at left
        i "Me quedé en la hoguera. Aunque no me sienta cómoda, creo que puedo aportar algo técnico."
    else:
        show ingrid neutral at left
        i "Me cambié a la balsa. No confío en la forma en que se manejan las cosas en la hoguera."

    menu:
        "Valorar su aporte":
            $ ingrid += 1
            y "Tu conocimiento puede marcar la diferencia. Gracias por quedarte."
        "Responder con cautela":
            y "Tus opiniones tienen peso. Espero que sean aportes."
        "Desconfiar abiertamente":
            $ ingrid -= 1
            y "No sirve aportar si no confías en el equipo."

    ## Cierre del jugador
    hide bob
    hide marina
    hide tomas
    hide ingrid
    hide charles
    with fade

    scene campamento_decision_grupal_noche
    show jugador neutral at center

    y "No podemos seguir así. Divididos, sin rumbo. Hay que tomar una decisión clara."

    y "Propongo que elijamos uno de los dos proyectos y nos comprometamos todos."

    menu:
        "Proponer continuar con la hoguera":
            $ jugador_proyecto = "hoguera"
            jump cap12_decision_grupal_reasignacion

        "Proponer continuar con la balsa":
            $ jugador_proyecto = "balsa"
            jump cap12_decision_grupal_reasignacion

label cap12_decision_grupal_reasignacion:

    scene campamento_decision_grupal_noche
    with fade

    $ proyecto_jugador = jugador_proyecto
    $ proyecto_opuesto = "balsa" if jugador_proyecto == "hoguera" else "hoguera"

    $ equipo_jugador = 1  # jugador incluido
    $ equipo_opuesto = 0

    ## Charles
    if charles > 1:
        show charles neutral at center
        c "Estoy con vos. Me quedo en el proyecto de la [proyecto_jugador]."
        $ equipo_jugador += 1
    else:
        show charles neutral at center
        c "Prefiero irme al otro grupo. No me convence tu propuesta."
        $ equipo_opuesto += 1
    hide charles

    ## Laura
    if laura > 1:
        show laura neutral at center
        l "Voy con vos. No me importa lo que digan los demás."
        $ equipo_jugador += 1
    else:
        show laura neutral at center
        l "No confío en tu forma de liderar. Me voy al otro proyecto."
        $ equipo_opuesto += 1
    hide laura

    ## Erika
    if erika > 1:
        show erika neutral at center
        k "Trabajemos juntos. Si vamos a hacer esto, que sea con decisión."
        $ equipo_jugador += 1
    else:
        show erika neutral at center
        k "No me convence tu propuesta. Me voy al otro grupo."
        $ equipo_opuesto += 1
    hide erika

    ## Bob
    if bob > 1:
        show bob neutral at center
        b "Contá conmigo. Prefiero el proyecto de la [proyecto_jugador]."
        $ equipo_jugador += 1
    else:
        show bob neutral at center
        b "No me parece lo mejor. Me voy al otro grupo."
        $ equipo_opuesto += 1
    hide bob

    ## Marina
    if marina > 1:
        show marina neutral at center
        m "Voy con vos. Me preocupa, pero confío en vos."
        $ equipo_jugador += 1
    else:
        show marina neutral at center
        m "Prefiero irme al otro grupo. No me siento segura acá."
        $ equipo_opuesto += 1
    hide marina

    ## Tomás
    if tomas > 1:
        show tomas neutral at center
        t "Estoy con vos."
        $ equipo_jugador += 1
    else:
        show tomas neutral at center
        t "Me voy al otro grupo."
        $ equipo_opuesto += 1
    hide tomas

    ## Ingrid (desempate)
    if ingrid > 1:
        if equipo_jugador == 4 and equipo_opuesto == 4:
            show ingrid neutral at center
            i "No quiero que esto siga en empate. Me sumo a tu proyecto."
            $ equipo_jugador += 1
        else:
            show ingrid neutral at center
            i "Voy con vos. Creo que puedo aportar algo."
            $ equipo_jugador += 1
    else:
        if equipo_jugador == 4 and equipo_opuesto == 4:
            show ingrid neutral at center
            i "No quiero que esto quede en empate. Me sumo a tu proyecto."
            $ equipo_jugador += 1
        else:
            show ingrid neutral at center
            i "Me voy al otro grupo. No confío en tu liderazgo."
            $ equipo_opuesto += 1

    hide charles
    hide laura
    hide erika
    hide bob
    hide marina
    hide tomas
    hide ingrid
    with fade

    ## Resultado final
    if equipo_jugador > equipo_opuesto:
        "La mayoria se compromete con tu proyecto de la [proyecto_jugador]."
        if proyecto_jugador == "hoguera":
            jump cap12_hoguera_completa
        else:
            jump cap12_balsa_completa
    else:
        "La mayoría se compromete con el proyecto de la [proyecto_opuesto]."
        if proyecto_opuesto == "hoguera":
            jump cap12_hoguera_completa
        else:
            jump cap12_balsa_completa

label cap12_hoguera_completa:

    scene campamento_hoguera_final
    with fade
    "Los ocho se ponen manos a la obra, entre todos el proceso se hace mas sencillo."
    "Se traen los troncos, cuerdas y demas materiales de la balsa, lo que acelera mucho la construccion de la hoguera."
    "Finalmente..."

    scene bg hoguera_pronta
    with fade
    "La pira está armada. Alta, sólida, y ubicada en una zona protegida por rocas naturales. Si llega una tormenta, resistirá."

    "Las capas de ramas y troncos están bien distribuidas. En la cima, hojas secas y resina lista para encender."

    "Al costado, un pequeño depósito con elementos para generar humo denso: corteza húmeda, aceites vegetales, y restos de tela."

    "El grupo observa en silencio. No hay fuego aún, pero hay esperanza."

    menu:
        "Dar una última indicación técnica":
            y "Asegúrense de que el depósito de ressina esté cubierto pero accesible. No podemos perder tiempo si aparece el avión."
            "El grupo asiente. Tu liderazgo técnico refuerza la confianza."

        "Compartir una reflexión emocional":
            y "No sé si esto va a funcionar. Pero lo hicimos juntos. Y eso ya es algo."
            "Algunos bajan la mirada. Otros sonríen. Hay algo más fuerte que el miedo: el vínculo."

    "La hoguera queda atrás. Alta, silenciosa, esperando su momento."

    jump cap_final_hoguera_avion_aparece

label cap12_balsa_completa:

    scene playa_balsa_final
    with fade

    "Los ocho se ponen manos a la obra, entre todos el proceso se hace mas sencillo."
    "Se traen los troncos, resina y demas materiales de la hoguera, lo que acelera mucho la construccion de la balsa."
    "Finalmente..."

    scene bg balsa_pronta
    with fade
    "La balsa está terminada. Amplia, equilibrada, con una base reforzada por sogas y troncos entrelazados."

    "En el centro, un compartimento improvisado con reservas de agua y comida. No es mucho, pero puede durar unos días."

    "Han construido remos con ramas gruesas y un timón rudimentario con una tabla rota y cuerda vegetal."

    "El grupo la rodea. No hay viento aún, pero hay decisión."

    menu:
        "Dar una última indicación técnica":
            y "Aseguren las reservas con doble nudo. Si se cae algo al agua, no hay segunda oportunidad."
            "El grupo ajusta las sogas. Tu atención al detalle marca la diferencia."

        "Compartir una reflexión emocional":
            y "No sé si esto va a funcionar. Pero lo hicimos juntos. Y eso ya es algo."
            "Algunos bajan la mirada. Otros sonríen. Hay algo más fuerte que el miedo: el vínculo."

    "La balsa queda en la orilla. Lista para partir, esperando el momento justo."

    jump cap_final_balsa_lanzamiento

label cap_final_hoguera_avion_aparece:

    scene cielo_nublado
    with fade

    "Una figura metálica aparece entre las nubes. Es un avión."
    "Pero la visibilidad es mala. Empieza a caer una Llovizna fina y el viento parece ir en aumento."

    show laura irascible at left
    l "¡Ahí está! ¡Lo vi! ¡Es ahora o nunca!"

    show charles despreocupado at centerleft
    c "¿Y si no nos ve? ¿Y si es solo una nube con forma de esperanza?"

    show erika decidida at center
    k "¡No es momento para bromas! Hay que encender la pira ya."

    show marina nerviosa at centerright
    m "¿Y si el viento la apaga? ¿Y si no funciona?"
    hide charles
    show bob firme at right
    b "Calma. Tenemos una oportunidad. Pero hay que actuar con cabeza."

    "El grupo se agita. Algunos discuten, otros dudan. La tensión escala."

    show ingrid pensativa at centerright

    l "Las ramas están húmedas. No prenderán fácil."

    i "Si usamos corteza de palma y resina, podríamos lograr una combustión más estable."

    "La situacion es un caos, muchas voces y poco tiempo para resaolver el problema."
    $ caos = 0
    menu:
        "Tomar el liderazgo y asignar tareas":
            y "Erika, dirige el encendido. Ingrid, prepara la mezcla. Tomás, protege la base. Bob, vigila el avión. Laura y Charles, ayuden sin discutir."
            "El grupo se reorganiza. Hay tensión, pero obedecen."
            $ liderazgo += 1

        "Intentar mediar entre las posturas":
            y "Todos quieren lo mejor. Pero si no nos escuchamos, vamos a fallar. Ingrid, ¿puedes explicar tu propuesta?"
            i "Sí. Si usamos resina y corteza seca, el fuego resistirá el viento."
            k "Entonces vamos con eso. Pero rápido."
            $ liderazgo += 1

        "Dejar que el grupo actúe sin intervenir":
            y "No voy a meterme. Que cada uno haga lo que crea mejor."
            "El grupo se dispersa. Hay caos. Algunos siguen a Erika, otros a Ingrid. Charles se distrae. Marina entra en pánico."
            $ caos += 1

    "El avión parece girar lentamente. ¿Está alejándose?"

    hide laura
    hide charles
    hide erika
    hide marina
    hide bob
    hide tomas
    hide ingrid

    jump cap_final_hoguera_intento_fallido

label cap_final_hoguera_intento_fallido:

    scene campamento_lluvia
    with fade

    "Intentan encender la pira. Las hojas prenden, pero el viento las apaga. El avión gira lentamente, alejándose."

    show erika frustrada at center
    show charles exaltado at centerleft
    show marina llorando at left
    show bob evaluando at right
    show laura molesta at centerright

    k "¡No prende! ¡El viento lo arruina todo!"

    c "¡Pongan toda la resina de una! ¡No hay tiempo!"

    m "¡No, no! ¡Eso es peligroso! Puede explotar y desarmar toda la pira."

    b "Podríamos agregar mas con cuidado. Pero hay que decidir ya."

    l "¡Esto es un desastre! Nadie escucha. Nadie manda."

    show tomas concentrado at centerleft
    show ingrid analizando at centerright

    t "Tengo ramas gruesas. Pero necesitamos calor constante."

    i "La resina está lista. Pero necesitamos proteger el fuego del viento."

    "Hay que actuar. Hay múltiples frentes abiertos."

    menu:
        "Usar toda la resina disponible para encender la pira":
            y "No hay tiempo. Usamos la resina. Bob, tú controlas que no se ponga mucha de una sola vez."
            "Charles corre a buscarla. Erika prepara la base. Marina se aleja, temblando. Ingrid analiza el mejor lugar para agregar la resina."
            $ liderazgo += 1

        "Buscar otra fuente de combustible menos riesgosa":
            y "No arriesgaremos todo. Tomas, busca corteza seca. Ingrid, mezcla hojarasca con resina. Laura, ayuda a proteger la base."
            "Erika protesta, pero acepta. Charles se impacienta. Bob observa en silencio."
            $ liderazgo += 1

        "Calmar a Marina y reorganizar al grupo":
            y "Marina, respira. No estás sola. Bob, toma el control del encendido. Erika, apóyalo. Charles, sin bromas."
            m "Gracias... estoy bien. Lo intentaré."
            "El grupo se reorganiza. El avión aún no se ha ido del todo."
            $ liderazgo += 1

        "Imponer órdenes con firmeza":
            y "¡Basta de dudas! Resina, ramas gruesas y predemos el fuego ya! ¡Vamos, sin peros!"
            "El grupo obedece, pero hay tensión. Laura lanza una mirada dura. Marina se aleja."

    "La tensión es máxima. El fuego aún no prende. El avión parece dudar en su trayectoria."

    hide erika
    hide charles
    hide marina
    hide bob
    hide laura
    hide tomas
    hide ingrid

    jump cap_final_hoguera_reaccion_grupal

label cap_final_hoguera_reaccion_grupal:

    scene campamento_lluvia_intensa
    with fade

    "La lluvia arrecia. El viento sopla con fuerza. El avión parece girar para alejarse. El grupo entra en frenesí."

    show erika decidida at center
    k "¡Vamos! ¡No se detengan! ¡Protejan la base!"
    hide erika

    show bob calculador at centerleft
    b "Si usamos la lona del refugio como cortaviento, podríamos estabilizar el fuego."
    hide bob

    show ingrid tensa at centerright
    i "La mezcla está lista. Pero hay que encenderla con algo más potente."
    hide ingrid

    show tomas concentrado at center
    t "Está el frasco de alcohol de la caja enterrada."
    hide tomas

    show laura alterada at left
    l "¡No hay tiempo! ¡Tiren toda la resina y ya!"
    hide laura

    show marina colapsando at center
    m "¡No quiero morir aquí! ¡No quiero!"
    hide marina

    show charles improvisando at center
    c "¡Alcohol y resina! ¿Y si las usamos para prender todo de golpe?"
    hide charles

    "El jugador debe elegir entre dos planes contradictorios:"

    menu:
        "Plan A: método seguro y técnico (lona + proteger entre todos la base)":
            show bob firme at centerleft
            show tomas concentrado at center
            show ingrid decidida at centerright

            y "Vamos con el plan técnico. Bob, Tomas, coloquen la lona. Los demás a proteger la base del viento y la lluvia."

            b "Entendido. La lona va contra el viento."
            t "Espero que funcione."
            i "¡Sujeten bien la base!"

            hide bob
            hide tomas
            hide ingrid

            $ estrategia_final += 1

        "Plan B: método rápido y riesgoso (alcohol + resina)":
            show charles exaltado at centerleft
            show laura decidida at centerright

            y "No hay tiempo. Charles, trae el alcohol. Laura, Bob preparen el resto de la resina. Erika, enciende esas hojas secas."

            c "¡Esto va a ser épico o fatal!"
            l "¡Ya está! ¡Prende!"

            hide charles
            hide laura

    "Mientras se ejecuta el plan, Marina tiene una crisis emocional."

    show marina temblando at center

    menu:
        "Ayudar a Marina a recuperar la calma":
            y "Marina, mírame. Respira. Estamos cerca. No te rindas ahora."
            m "Lo intento... gracias..."
            hide marina
            $ liderazgo += 1

        "Ignorar la crisis y enfocarse en el fuego":
            y "No hay tiempo para emociones. ¡Concéntrense!"
            m "..."
            hide marina

    "Finalmente, el fuego prende. Una columna de humo negro se eleva. El grupo contiene la respiración."

    jump cap_final_hoguera_encendido

label cap_final_hoguera_encendido:

    scene campamento_hoguera_encendida
    with fade

    "La pira finalmente prende. Las llamas crecen. Una columna de humo negro se eleva hacia el cielo gris."

    show erika aliviada at center
    k "Lo logramos... ahora depende de ellos."
    hide erika

    show bob observando at centerleft
    b "El humo es denso. Si están atentos, lo verán."
    hide bob

    "El grupo se reúne en silencio. Todos miran al cielo. El avión parece girar... ¿está regresando?"

    show marina esperanzada at center
    m "¿Está volviendo? ¿Lo logramos?"
    hide marina

    show laura emocionada at right
    l "¡Sí! ¡Está girando! ¡Nos vio!"
    hide laura

    show charles eufórico at centerleft
    c "¡Nos vio! ¡Nos vio! ¡Estamos salvados!"
    hide charles

    show tomas sonriendo at centerright
    t "Nunca pensé que me alegraría tanto de ver un avión."
    hide tomas

    show ingrid reflexiva at center
    i "La ciencia y el caos... funcionaron juntos."
    hide ingrid

    "El avión pasa sobre sus cabezas, bajo y lento. Desde la cabina, alguien saluda con la mano. Luego gira y se aleja por donde había llegado."

    show erika emocionada at center
    k "Van a volver. El rescate es inminente."
    hide erika

    "El grupo estalla en gritos, abrazos, risas. Algunos lloran. Otros simplemente se sientan, agotados pero aliviados."

    menu:
        "Celebrar con el grupo":
            y "¡Lo logramos! ¡Juntos!"
            "Te unes a los abrazos y festejos. La tensión se disuelve en alegría compartida."


        "Quedarse en silencio, observando":
            y "..."
            "Observas desde la distancia. El humo aún se eleva. El cielo comienza a despejarse."

        "Buscar a alguien en particular":
            menu:
                "Buscar a Marina":
                    y "¿Estás bien?"
                    show marina emocionada at center
                    m "Sí... gracias a ti."
                    hide marina
                    $ marina += 1

                "Buscar a Erika":
                    y "Buen trabajo, líder."
                    show erika agradecida at center
                    k "No habría funcionado sin todos."
                    hide erika
                    $ erika += 1

                "Buscar a Charles":
                    y "No estuvo tan mal tu idea."
                    show charles orgulloso at center
                    c "¿Viste? El caos tiene estilo."
                    hide charles
                    $ charles += 1

    jump epilogo_isla

label cap_final_balsa_lanzamiento:

    scene playa_balsa
    with fade

    "La balsa está lista. Hecha con troncos, cuerdas y esperanza. El grupo la empuja al agua y sube con cuidado."

    show bob al mando at center
    b "Charles, vigila el equilibrio. Marina, cuida el agua y la comida. Tomás, Laura, Ingrid y Erika en los remos. Yo voy al timón."

    b "¿[nombre_jugador], dónde crees que puedes aportar más?"

    menu:
        "Tomar el timón":
            y "Yo dirijo. Bob, tú puedes estar atento a la corriente."
            b "Bien, si crees que puedes hacerlo, yo me fijo en las corrientes."
            $ rol_timon = True

        "Remar junto a Erika, Tomás y el resto":
            y "Voy a remar. Necesitamos fuerza."
            b "Buena elección."
            $ rol_remo = True

        "Encargarse del equilibrio y provisiones":
            y "Me ocupo de que nada se pierda. Marina, ayúdame."
            show marina at left
            m "Sí... haré lo que pueda."
            $ rol_soporte = True

    hide bob
    hide erika

    show charles incómodo at center
    c "¿Y yo por qué tengo que vigilar el equilibrio? ¡No soy un contrapeso humano!"

    show laura molesta at centerleft
    l "Porque si te caes, nos hundimos. ¿Querés remar?"

    show marina nerviosa at centerright
    m "Por favor, no peleen. Ya estamos en el agua..."

    "La situacion escala y distrae a todos. La balsa toma una ola un poco en diagonal, haciendo que todo cruja y se sacuda."

    menu:
        "Reasignar tareas":
            if rol_soporte:
                y "Charles, ven aqui a ayudar con las provisiones a Marina."
                y "Yo me encargo de equilibrar la balsa."
                $ rol_soporte = False
                $ rol_equilibrio = True
            else:
                y "Laura, vigila el equilibrio. Charles, agarra un remo y ayuda."
                l "Está bien. Pero estoy cansada de que actúe como un niño."

        "Imponer orden":
            y "Charles, hacé lo que te toca. No estamos en un crucero."
            c "Ok, ok..."
            $ liderazgo += 1

        "Ignorar el conflicto":
            y "..."
            "Laura y Charles siguen discutiendo. Marina se pone más nerviosa."
            $ caos += 1

    hide charles
    hide laura
    hide marina

    jump cap_final_balsa_olas

label cap_final_balsa_olas:

    scene mar_rompiente
    with fade

    "La balsa avanza lentamente. Las olas crecen cerca de la rompiente. El grupo se tensa."

    show bob concentrado at center
    b "¡Mantengan el ritmo! ¡No se detengan!"

    if rol_timon:
        b "¡[nombre_jugador]! Cuidado, hay que tomar esa corriente de a poco. Si entramos de frente nos va a dar vuelta."
    else:
        show bob concentrado at centerleft
        b "La corriente se cruza. Voy a tener que girar un poco y tomar la corriente con suavidad.."

    show ingrid analítica at centerright
    i "No. Si giramos, perdemos fuerza. Hay que atravesar recto."

    "El grupo se divide. Hay que decidir decidir si seguir el plan de Ingrid o tomar la corriente con un giro."

    menu:
        "Atravesar recto la corriente para mantener impulso":
            y "Vamos recto. No perdamos impulso."
            k "Bien. Todos, mantengan el ritmo."
            t "¡A remar!"
            $ caos -= 1


        "Girar un poco la balsa para tomar la corriente de a poco":
            y "Giramos un poco. Tomás, marca el ángulo."
            show tomas at left
            t "Entendido."
            show erika at right
            k "Espero que funcione..."
            $ caos -= 1

        "No decidir, dejar que el grupo actúe":
            y "..."
            "Erika y Tomás discuten. Bob toma el mando. La balsa se sacude."
            $ caos += 1

    hide bob
    hide tomas
    hide erika
    hide ingrid

    show marina asustada at center
    m "¡Nos vamos a volcar! ¡No puedo...!"

    menu:
        "Calmar a Marina":
            y "Respira. Estamos bien. Confía en nosotros."
            m "Lo intento..."
            $ liderazgo += 1

        "Ignorarla y concentrarse en remar":
            y "¡Remen! No hay tiempo para distracciones."
            m "..."
            $ caos += 1


    hide marina

    "La balsa supera la rompiente. El grupo respira aliviado, pero el mar sigue agitado."

    jump cap_final_balsa_corriente

label cap_final_balsa_corriente:

    scene mar_abierto
    with dissolve
    "Luego de varias horas de esfuerzo y sobresaltos, la balsa está bastante cerca de la costa a la que se dirigían,"
    "Parece una isla pequeña o quizas la punta de de alguna lengua de tierra de una isla mas grande. Aún es dificil de decir a la sitancia."
    "La balsa se acerca de la costa. El grupo se da cuenta de que una corriente los arrastra hacia mar abierto."

    show tomas tenso at centerleft
    t "Esto no está bien. Nos está llevando mar adentro."

    show erika calculando at centerright
    k "La corriente es fuerte. Si desmontamos la balsa, podríamos nadar en partes."

    show bob frustrado at center
    b "¡No! Si saltamos, nos dispersamos. Hay que resistir y esperar que cambie."

    show marina desesperada at right
    m "¡No quiero morir aquí!"

    "El grupo se divide. El jugador debe tomar una decisión."
    jump cap_final_balsa_corriente_desicion

label cap_final_balsa_corriente_desicion:
    "El tiempo se acaba y hay que tomar una desicion...ya."

    menu:
        "Estrellar la balsa hacia una roca cercana, y luego nadar hasta la costa.":
            y "Erika, Bob, todos a los remos. Ttratemos de golpear contra esa roca a medio camino. Tomás, ayuda a Marina."
            k "Es muy arriesgado pero puede funcionar."
            i "Es probable que alguno se lastime cuando se rompa la balsa"
            l "Nos vamos a quedar sin agua, ni nada..."
            m "No se si puedo nadar tanto..."
            $ liderazgo += 1
            jump resolucion_corriente_nado_check

        "Resistir en la balsa y remar hasta que la corriente ceda":
            y "Nos quedamos juntos. Bob, guia la balsa. Los demás...rememos todos."
            b "Buena decisión. No nos separemos."
            c "No hay remos para todos."
            i "Si fallamos no hay manera de volver a ninguna isla."
            $ liderazgo += 1
            jump resolucion_corriente_resistencia_check

        "Tomar una acción impulsiva y saltar sin consenso":
            y "¡Salten! ¡Ahora!"
            "El grupo entra en caos. Algunos dudan, otros obedecen."
            $ caos += 1
            jump resolucion_corriente_impulsiva

label resolucion_corriente_nado_check:
    "Todos opinan, el tiempo se acaba."
    menu:
        "Mantener el plan de ir contra la roca y nadar a la orilla desde ahi":
            y "¡Prepárense! Vamos a estrellarnos contra la roca"
            y "Todos listos para nadar cuando eso pase"
            jump resolucion_corriente_nado
        "Quizas no es un buen plan, mejor pensar otra opcion.":
            jump cap_final_balsa_corriente_desicion

label resolucion_corriente_resistencia_check:
    "La corriente cada vez es mas fuerte, hay que decidir."
    menu:
        "Mantener el plan de remar rumbo a la isla contra la corriente":
            y "¡Remen! Con lo que tengan, saquen partes de la balsa si es necesario"
            y "Podemos tomar turnos para remar con los que no consigan remos"
            jump resolucion_corriente_resistencia
        "Quizas no es un buen plan, mejor pensar otra opcion.":
            jump cap_final_balsa_corriente_desicion

label resolucion_corriente_nado:

    scene mar_nado
    with fade
    "¡CRASHHH! La balsa se estrella contra la roca, agua, espuma y troncos vuelan por el aire."
    "El grupo cae al gua y se dispersa. La balsa se desarma. Erika guía a los demás con señales."
    $ salvados = 0
    jump resolucion_corriente_nado_grupo

label resolucion_corriente_nado_grupo:
    $ salvados += 1
    menu:
        "Esperas a que todos estén nadando hacia la orilla" if salvados < 3:
            "El cansancio hace que pesen los brazos y las piernas"
            "No estas segur[e] de cuanto más puedes mantenerte a flote entre las olas."
            "Ayudas a quienes están mas rezagados y con mas dificultades para nadar"
            jump resolucion_corriente_nado_grupo

        "Decides asegurarte de llegar tú tambien a la orilla" if salvados < 3:
            "La última ola te hizo tragar agua salada, hay gritos por todos lados."
            "Nadas con determinación hacia la orilla, esperas que los demás puedan llegar a salvo..."
            "...pero decides que es momento de cuidarte primero."
            $ todos_salvados = False
        "Parece que todos están ya nadando a la orilla" if salvados == 3:
            "Observas y a tu alrededor ya no hay nadie necesitando ayuda"
            "Nadas entre las olas rumbo a la orilla... "
            "...pero los brazos te pensan más y más, las olas te cubren."
            b "¡Aquí! Toma mi mano, [nombre_jugador]"
            "Bob te ayuda los últimos metros, mientras escupes agua y toses."
            b "Debes cuidarte, casi te ahogas por salvar los demas."
            $ todos_salvados = True
        "Te aseguras que todos estén a salvo." if salvados == 3:
            "Observas y a tu alrededor ya no hay nadie necesitando ayuda"
            "Nadas entre las olas rumbo a la orilla... "
            "...pero los brazos te pensan más y más, las olas te cubren."
            b "¡Aquí! Toma mi mano, [nombre_jugador]"
            "Bob te ayuda los últimos metros, mientras escupes agua y toses."
            b "Debes cuidarte, casi te ahogas por salvar los demas."
            $ todos_salvados = True


    "Tras mucho esfuerzo, logran llegar a una costa desconocida."

    show tomas agotado at center
    t "No sé cómo lo logramos..."

    show erika aliviada at centerright
    k "Las olas cerca de la orilla ayudaron un poco. Pero fue arriesgado."

    jump cap_final_balsa_rescate

label resolucion_corriente_resistencia:

    scene mar_espera
    with fade

    "El grupo permanece unido en la balsa. Bob refuerza el timón con cuerdas improvisadas."

    "Todos reman con fuerza, Bob gruñe al timón tratando de mantener el curso. Ingrid delante tuyo rema con determinación."

    "Una ola golpea la balsa de costado. Ingrid deja caer su remo al agua y al intentar recuperarlo trastabilla y pierde el equilibrio."
    menu: 
        "Tratar de ayudarla para que no caiga de la balsa":
            "Te estiras y tratas de impularla al interior de la balsa"
            i "¡Me caigo! ¡Ayudaaaaaa!"
            menu:
                "Empujarla al interior de la balsa a como de lugar":
                    "La empujas por el hombro, pero ella ya está cayendo."
                    "Su peso te arrastra al borde la balsa."
                    menu: 
                        "Salvar a Ingrid":
                            "Empujas a Ingrid y mientras ella cae al interior de la balsa, tú te caes de cabeza al agua."
                            b "¡Nooooo, [nombre_personaje] se cayó al agua!"
                            c "Yo puedo agarrarl[e]"
                            "Charles se inclina y te agarra del brazo"
                            "Sientes como hace fuerza y te saca de debajo del agua. Varias manos te agarran y te suben a la balsa."
                            "Escupiendo agua y jadeando, te recuperas boca arriba en el piso de la balsa."
                            $ salvar_ingrid_cae_player = True
                        "Salvarte a ti":
                            "Te agarras del bolde de la balsa y logras volver a tu posicion."
                            "Mientras te recuperas, ves como Ingrid se cae de cabeza al agua."
                            $ salvar_ingrid_cae_ingrid = True
                            b "¡Nooooo, Ingrid se cayó al agua!"
                            c "Yo puedo agarrarla"
                            "Charles se inclina y la agarra del brazo"
                            "SiLe saca de debajo del agua. Varias manos la agarran y la suben a la balsa."
                            "Escupiendo agua y jadeando, Ingrid se recupera boca arriba en el piso de la balsa."
                "Mantenerte firme en tu posición y ayudar en lo posible.":
                    "Tratas de empujarla al interior de la balsa pero ya está muy al borde y no puedes sujetarla bien"
                    "Ves como cae por el borde del bote y se hunde."
                    $ salvar_ingrid_cae_ingrid = True
                    b "¡Nooooo, Ingrid se cayó al agua!"
                    c "Yo puedo agarrarla"
                    "Charles se inclina y la agarra del brazo"
                    "Con esfeurzo la saca de debajo del agua. Varias manos la agarran y la suben a la balsa."
                    "Escupiendo agua y jadeando, Ingrid se recupera boca arriba en el piso de la balsa."   
        "Dejar de remar para recuperar el remo que Ingrid dejó caer al agua.":
            "Aseguras tu remo con las piernas y te inclinas para recoger el remo."
            $ salvar_ingrid_remo = True
            "Recoges el remo y se lo pasas a Charles que no tiene uno"
            y ¡"Rema! ¡O vamos a terminar a la deriva!"
            "Le tiras el remo a Charles al mismo tiempo que Ingrid cae al agua."
            b "¡Nooooo, Ingrid se cayó al agua!"
            c "Yo puedo agarrarla... ¡ufff!"
            "El remo que le tiraste lo distrae y falla el intento. Ingrid pasa de largo y la balsa sigue de largo."
            "Bob en el ultimo momento se inclina y logra agarrarla cuando la la balsa la dejaba atras."
            "Una ola terminó ayudando dandole un impulso que terminó con ambos escupiendo agua en el piso de la balsa."

        "Mantienes la intensidad de tu remo para compensar que Ingrid no está remando":
            "Agarras con fuerza el remo y redoblas tus esfuerzos para vencer la corriente"
            $ salvar_ingrid_ignorar = True
            y "¡No dejen de remar! Estamos en el medio de la corriente, si paramos ahora estamos perdidos"
            "Ingrid es golpeada por una ola y termina cayendo al agua"
            b "¡Nooooo, Ingrid se cayó al agua!"
            c "Yo puedo agarrarla"
            "Charles se inclina y la agarra del brazo"
            "Con esfuerzo la saca de debajo del agua. Varias manos la agarran y la suben a la balsa."
            "Escupiendo agua y jadeando, Ingrid se recupera boca arriba en el piso de la balsa." 

    show bob at left
    b "¡Es ahora o nunca! Voy a cruzar la balsa en la corriente, o salimos o nos arrastra."
    show erika at right
    k "¡A remar!"
    "Todos toman sus remos, se acomodan ràpido en sus posiciones y comienzan a remar con todo."
    "La corriente cambia lentamente, las olas los levantan y empujan hacia la orilla."

    show bob orgulloso at center
    b "Sabía que aguantar era lo correcto."

    show marina emocionada at right
    m "¡Tierra! ¡Lo logramos!"

    jump cap_final_balsa_rescate

label resolucion_corriente_impulsiva:

    scene mar_caos
    with fade

    "El grupo se lanza al agua sin coordinación. Algunos se separan, otros se aferran a restos de la balsa."
    $ salvados = 0
    jump resolucion_corriente_impulsiva_check

label resolucion_corriente_impulsiva_check:
    $ salvados += 1
    menu:
        "Esperas a que todos estén nadando hacia la orilla" if salvados < 3:
            "El cansancio hace que pesen los brazos y las piernas"
            "No estas segur[e] de cuanto más puedes mantenerte a flote entre las olas."
            "Ayudas a quienes están mas rezagados y con mas dificultades para nadar"
            jump resolucion_corriente_impulsiva_check

        "Decides asegurarte de llegar tú tambien a la orilla" if salvados < 3:
            "La última ola te hizo tragar agua salada, hay gritos por todos lados."
            "Nadas con determinación hacia la orilla, esperas que los demás puedan llegar a salvo..."
            "...pero decides que es momento de cuidarte primero."
            $ todos_salvados = False
        "Parece que todos están ya nadando a la orilla" if salvados == 3:
            "Observas y a tu alrededor ya no hay nadie necesitando ayuda"
            "Nadas entre las olas rumbo a la orilla... "
            "...pero los brazos te pensan más y más, las olas te cubren."
            b "¡Aquí! Toma mi mano, [nombre_jugador]"
            "Bob te ayuda los últimos metros, mientras escupes agua y toses."
            b "Debes cuidarte, casi te ahogas por salvar los demas."
            $ todos_salvados = True
        "Te aseguras que todos estén a salvo." if salvados == 3:
            "Observas y a tu alrededor ya no hay nadie necesitando ayuda"
            "Nadas entre las olas rumbo a la orilla... "
            "...pero los brazos te pensan más y más, las olas te cubren."
            b "¡Aquí! Toma mi mano, [nombre_jugador]"
            "Bob te ayuda los últimos metros, mientras escupes agua y toses."
            b "Debes cuidarte, casi te ahogas por salvar los demas."
            $ todos_salvados = True

    "La corriente los arrastra, y por suerte, los conduce a una costa rocosa."

    show erika molesta at center
    k "Eso fue una locura. Pero funcionó... de algún modo."

    show tomas distante at centerleft
    t "No todos están bien. Algunos casi se ahogan, otros se lastimaron con las rocas."
    t "Esto fue muy insensato"
    menu:
        "Actué y ahora estamos a salvo":
            "Soluciones no problemas, Tomas. No iba a ser fácil de ninguna manera. Yo decidí y actué"
            "Tomas te mira con intensidad, parece estar por decir algo, pero sigue caminando y te ignora."
            $ tomas -= 1
        "Lamento la impulsividad":
            y "La verdad, tienes razon Tomas. Afortunadamente salió bien."
            t "Afortunadamente. Disculpas aceptadas."


    jump cap_final_balsa_rescate

label cap_final_balsa_rescate:

    scene isla_pequena
    with fade

    "El grupo llega a la costa de una isla diminuta. La vegetación es escasa, y una colina rocosa se alza en el centro."

    show bob observador at center
    b "No parece haber mucho aquí..."

    show erika decidida at centerright
    k "Subamos esa colina. Desde arriba podremos ver mejor."

    show marina at right
    m "¿Que vamos a hacer ahora? Estamos peor que antes"

    show charles at centerleft
    c "Algo se nos ocurrirá, Marina. Al menos acá no parece haber jabalíes."

    show marina sonriente 
    m "Solo podría haber uno, parado en la punta de la colina."
    "Algunos se sonrien, pero todos alegran el semblante. Ese toque de humor de Charles y Marina les devuelve un poco de esperanza."

    "El grupo asciende con esfuerzo. El sol golpea fuerte, y el viento trae olor a sal y combustible quemado."

    scene cima_colina
    with dissolve

    "Desde la cima, el grupo observa el otro lado de la isla. Un pequeño bote de pesca se balancea cerca de la costa."

    show marina emocionada at center
    m "¡Un bote! ¡Un bote de verdad!"

    show tomas euforico at centerleft
    t "¡Griten! ¡Que nos vean!"

    "Todos gritan con fuerza. Uno de los pescadores en el bote se gira, los ve, y responde con un grito."

    p "¡Los vimos! ¡Vamos a pedir ayuda!"

    "El grupo se queda en silencio por un momento. Luego, estalla en festejos."

    show bob sonriendo at right
    b "Lo logramos..."

    show erika aliviada at left
    k "Estamos a salvo."

    show marina llorando at center
    m "Pensé que no saldríamos de esta..."

    "El sol comienza a descender. El grupo se abraza, exhausto pero esperanzado. El rescate es inminente."

    jump epilogo_isla

label epilogo_isla:

    scene costa_isla
    with fade

    "Horas después, un barco de rescate llega a la isla. Un grupo de médicos y rescatistas baja con rapidez."

    show rescatista at center
    r "Tranquilos, estamos aquí para ayudarlos. ¿Hay heridos?"

    "El grupo es atendido, hidratado, y guiado al barco. La tensión comienza a disiparse."

    scene cubierta_barco
    with dissolve

    "Ya en la cubierta, mientras el barco se aleja de la isla, el grupo se reúne. El viento es suave, y el mar tranquilo."

    ## Diálogos según relación con el jugador

    if bob >= 2:
        show bob reflexivo at left
        b "Nunca pensé que confiar en vos me iba a salvar la vida. Gracias por no rendirte."

    elif bob <= -2:
        show bob distante at left
        b "No sé si fue suerte o qué, pero no vuelvo a seguir tus decisiones."

    else:
        show bob neutral at left
        b "Fue duro. No siempre estuve de acuerdo con vos, pero salimos adelante."

    if erika >= 2:
        show erika serena at center
        k "Tu forma de pensar nos mantuvo unidos. Me alegra haber compartido esto con vos."

    elif erika <= -2:
        show erika fría at center
        k "Tomaste decisiones que casi nos cuestan todo. No lo voy a olvidar."

    else:
        show erika pensativa at center
        k "Aprendí mucho. No sé si lo hicimos bien, pero sobrevivimos."

    if tomas >= 2:
        show tomas sonriente at right
        t "Sos de los que no se quiebran. Me alegra haber estado con vos en esto."

    elif tomas <= -2:
        show tomas serio at right
        t "No me gustó cómo manejaste las cosas. Pero al menos estamos vivos."

    else:
        show tomas tranquilo at right
        t "Fue una locura. No sé si lo hicimos bien, pero funcionó."

    if marina >= 2:
        show marina emocionada at center
        m "Nunca me sentí tan protegida. Gracias por cuidarme."

    elif marina <= -2:
        show marina distante at center
        m "No quiero hablar de lo que pasó. No contigo."

    else:
        show marina vulnerable at center
        m "Todavía estoy procesando todo. Pero gracias por estar ahí."

    ## Reflexión final del jugador

    "Mientras el barco se aleja, el jugador observa el horizonte. El grupo guarda silencio por un momento."

    menu:
        "Fue una experiencia transformadora":
            y "No somos los mismos. Algo cambió en todos nosotros."
            $ reflexion = "transformadora"

        "Solo quiero olvidar lo que pasó":
            y "Prefiero no pensar más en esto. Que quede atrás."
            $ reflexion = "evasiva"

        "Sobrevivimos, y eso es suficiente":
            y "No sé qué aprendí. Pero sobrevivimos. Eso basta."
            $ reflexion = "pragmática"

    "El sol cae sobre el mar. El barco sigue su curso. El grupo, marcado por la experiencia, comienza a imaginar lo que vendrá."

    "El juego termina aqui!!!!"

    return

