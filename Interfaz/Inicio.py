print('::::Inicio del Programa:::::')

from tkinter import *   # Importacion de la Clase de la Interfaz Grafica
import random
import threading
import time
import requests

#************************ CONSTRUCCION DE LA VENTANA

raiz=Tk()                           # Construccion de la Raiz llamamos a TK
raiz.title("Simulador De Trafico")  # Titulo de la Ventana
raiz.resizable(True,True)           # Redimencionar alto y ancho
raiz.geometry("800x500")            # Tamaño de la Ventana

#************************ VARIABLES GLOBALES

caja_url=StringVar()
caja_concurrencia=StringVar()
caja_solicitudes=StringVar()
caja_parametros=StringVar()
caja_timeout=StringVar()
caja_resumen=StringVar()

global BanderaContador

global contador2
BanderaContador=True
global t


#************************ METODOS GLOBALES

def CambiarGlobalTrue():
    BanderaContador = True


def CambiarGlobalFalse():
    BanderaContador = False

def Envio_Paquetes (lineas2, Numhilo, Identificador):

    print("::::::::::::::::::Ejecuta Hilo # ->"+str(Numhilo))

    usuarios = [
    "herbertreyes13@gmail.com",
    "xavilima12@gmail.com",
    "jeannirasic@gmail.com",
    "lestermaz.96@gmail.com",
    "matalejandro18@gmail.com",
    "luisrobles2408@gmail.com",
    "bcfiusac@gmail.com",
    "herberaegueta4@gmail.com",
    "checha18964@gmail.com",
    "nery016s@gmail.com",
    "ayau15@gmail.com",
    "0108moralesluis@gmail.com",
    "alfonso.melgar97@gmail.com",
    "carloscampaneros@gmail.com",
    "mada.salgui@gmail.com",
    "richimenen@gmail.com",
    "velandreas@gmail.com",
    "mindi.ajpop@gmail.com",
    "yimmiss305@gmail.com",
    "franklinvelasquez35@gmail.com",
    "csazo171@gmail.com",
    "canchemolinas@gmail.com",
    "elielbarrios97@gmail.com",
    "sebastiansancheztuchez@gmail.com",
    "aroche.brayan@gmail.com",
    "brayanch1297@gmail.com",
    "mynormolina1@gmail.com",
    "alejothegame@gmail.com",
    "sandymeridah@gmail.com",
    "sandraeujim@gmail.com",
    "hellenlacan1994@gmail.com",
    "davidligo@gmail.com",
    "geovanni.fly@gmail.com",
    "bcoronado.morales@gmail.com",
    "alexixva@gmail.com",
    "carloscante@gmail.com",
    "cobolatrix@gmail.com",
    "edushowy@gmail.com",
    "davidgmz79@gmail.com",
    "christsoldier92@gmail.com",
    "carlosorantes77@gmail.com",
    "keosme@gmail.com",
    "luisito1811@gmail.com",
    "vanessa.oajaca@gmail.com",
    "danniel.santos924@gmail.com",
    "gonibal15@gmail.com",
    "totoday72@gmail.com",
    "trapavoided22@gmail.com",
    "willialberto.125@gmail.com",
    "SuperSpeed52@gmail.com",
    "zruiz89@gmail.com",
    "apuntapuess@gmail.com",
    "metalcrowley@gmail.com",
    "ebenja42@gmail.com",
    "bryaned44@gmail.com",
    "cuentaroja11@gmail.com",
    "kevgoz11@gmail.com",
    "dolmix.xd@gmail.com",
    "guayof.r9@gmail.com",
    "jmcque123@gmail.com",
    "walkter@gmail.com",
    "marr1708@gmail.com"
    ]

    nombres=[
    "Herbert Rafael Reyes Portillo",
    "Javier Estuardo Lima Abrego",
    "Jeannira Del Rosario Sic Menéndez",
    "Lester Fernando Mazariegos Navarro",
    "Manuel Alejandro De Mata Mayen",
    "Juan Luis Robles Molina",
    "Byron David Cermeño Juárez",
    "Herberth Josué Argueta Aragón",
    "César Alejandro Sazo Quisquinay",
    "Nery Antonio Alvizures Sologaistoa",
    "Carlos Mauricio Ayau Romero",
    "Luis Fernando Morales García",
    "Luis Alfonso Melgar Arizpe",
    "Carlos Antonio Campaneros Benito",
    "Maynor David Salguero Guillen",
    "Ricardo Antonio Menéndez Tobías",
    "Escarleth Andrea Velasco Campos",
    "Mindi Guisela Ajpop Aguilar",
    "Yimmi Daniel Ruano Pernillo ",
    "Franklin Estuardo Velásquez Fuentes",
    "Cesar Dionicio Sazo Mayen",
    "Jorge David Espina Molina ",
    "Miamin Eliel Barrios Arrivillaga",
    "Sebastián Sánchez Túchez",
    "Brayan Mauricio Aroche Boror",
    "Brayan Alberto Chinchilla Ramos",
    "Mynor Joel Lombardo Molina Guevara",
    "Oscar Alejandro Rodríguez Calderon",
    "Sandy Fabiola Mérida Hernández",
    "Sandra Eunice Jiménez Rodas",
    "Hellen Alexandra Lacan Hernandez",
    "David Estuardo Ligorría Taracena",
    "Byron geovanni chicoj perez",
    "Bruno Marco Jose Coronado Morales",
    "Raymundo Alexander Ixvalan Pacheco",
    "Carlos Enrique Cante López",
    "Edwin Antonio López Ordóñez",
    "José Eduardo Morales Garcia ",
    "David Jonathan González Gámez",
    "Ramon Osvaldo Patzan Caballeros",
    "Carlos Rene Orantes Lara",
    "Kevin Oswaldo Mejía Lemus",
    "Luis Enrique López Urbina",
    "Vanessa Dayanara Oajaca Ruiz",
    "Daniel Enrique Santos Godoy",
    "Aníbal Roberto Gómez Morales",
    "Erick Daniel Hernández Tó",
    "Augusto German Mazariegos Salguero",
    "Willians Alberto Lemus López",
    "Ozmar René Escobar Avila",
    "Edwin Estuardo Ruíz",
    "Mario Najarro",
    "Carlos Anibal Rafael Loarca",
    "Erick Benjamin López Xajil ",
    "Bryan Eduardo Chacón López ",
    "Edwar Everaldo Zacarias ",
    "Kelvin Vásquez Gómez",
    "Dolmo Flores Mateo Pedro",
    "Julio César Eduardo Flores Tubac",
    "José Miguel Celiz Quevedo ",
    "Walter Roberto Morales Quiñonez",
    "Fredy Estuardo Marroquin Alvarez"
    ]

    mensaje=[
    "Nunca le doy la mano a un pistolero zurdo",
    "No existen preguntas sin respuesta solo preguntas mal formuladas",
    "La única vez que el éxito viene antes que el trabajo es en el diccionario",
    "Enterramos nuestros pecados lavamos nuestras conciencias",
    "Siempre digo la verdad incluso cuando miento digo la verdad",
    "Mantén cerca a tus amigos pero aún más cerca a tus enemigos",
    "El dinero nunca duerme",
    "Carpe diem aprovechen el día hagan sus vidas extraordinarias",
    "Mi respeto no se pide se gana",
    "Soy el rey del mundo",
    "Hoy me considero a mí mismo el hombre más afortunado sobre la tierra",
    "No me pidas la luna nosotros tenemos las estrellas",
    "Que yo recuerde desde que tuve uso de razón quise ser un gángster",
    "Creo en América América hizo mi fortuna",
    "Esta es la diferencia entre tú y yo tú quieres perder poco yo quiero ganar mucho",
    "Hasta el infinito y más allá",
    "Si quieres un amigo cómprate un perro",
    "El pasado puede doler pero tal como lo veo puedes: o huir de él o aprender",
    "Tenía 12 años casi 13 la primera vez que vi un cadáver",
    "Si quieren ser billonarios algún día muestren agallas tomen una decisión",
    "¿Sabes? mucha gente viene a Las Vegas para perder yo no",
    "Lo siento jefe. Solo confío en dos personas. Uno soy yo y el otro no eres tú",
    "Me niego a responder con el argumento de que no quiero",
    "Si sabes lo que vales ve y consigue lo que mereces pero tendrás que aguantar golpes",
    "Hay personas por las que vale la pena derretirse",
    "El juego consiste en pasar el dinero del bolsillo de tu cliente a tu bolsillo y ya",
    "¿Por qué tan serio?",
    "El pueblo no debería temer a sus gobernantes los gobernantes deberían temer al pueblo",
    "Siempre deja que tu conciencia sea tu guía",
    "Estoy en contra de tener emociones no de utilizarlas",

    "El que lee mucho y anda mucho, ve mucho y sabe mucho",
    "Escribir es fácil. Lo único que tienes que hacer es cruzar las palabras erróneas",
    "No basta con saber, se debe también aplicar. No es suficiente querer, se debe también hacer",
    "El primer paso de la ignorancia es presumir de saber",
    "El futuro tiene muchos nombres. Para los débiles es lo inalcanzable. Para los temerosos, lo desconocido. Para los valientes es la oportunidad",
    "Es mejor ser rey de tu silencio que esclavo de tus palabras",
    "Buscamos la felicidad, pero sin saber dónde, como los borrachos buscan su casa, sabiendo que tienen una",
    "La raza humana se encuentra en la mejor situación cuando posee el más alto grado de libertad",
    "El alma que hablar puede con los ojos, también puede besar con la mirada",
    "Cuando creíamos que teníamos todas las respuestas, de pronto, cambiaron todas las preguntas",
    "El verdadero amor no es otra cosa que el deseo inevitable de ayudar al otro para que sea quien es",
    "El vínculo que une a tu auténtica familia no es de sangre, sino de respeto y alegría mutua",
    "Afortunado es el hombre que tiene tiempo para esperar",
    "Todo fracaso es el condimento que da sabor al éxito",
    "Puedes llegar a cualquier parte, siempre que andes lo suficiente",
    "Los hombres son como los vinos: la edad agria los malos y mejora los buenos",
    "Daría todo lo que sé, por la mitad de lo que ignoro",
    "Nada es más nocivo para la creatividad que el furor de la inspiración",
    "El éxito consiste en obtener lo que se desea. La felicidad, en disfrutar lo que se obtiene",
    "Un corazón es una riqueza que no se vende ni se compra, pero que se regala",
    "La ciencia moderna aún no ha producido un medicamento tranquilizador tan eficaz como lo son unas pocas palabras bondadosas",
    "Al fin y al cabo, somos lo que hacemos para cambiar lo que somos",
    "Donde funciona un televisor, seguro que hay alguien que no está leyendo",
    "Si es bueno vivir, todavía es mejor soñar, y lo mejor de todo, despertar",
    "La desvalorización del mundo humano crece en razón directa de la valorización del mundo de las cosas",
    "Se viaja no para buscar el destino sino para huir de donde se parte",
    "No hay cosa más fácil que dar consejo ni más difícil que saberlo tomar",
    "Sólo en soledad se siente la sed de la verdad",
    "Como todos los soñadores, confundí el desencanto con la verdad",
    "Como no me he preocupado de nacer, no me preocupo de morir",

    "Hay pocas razones para decir la verdad, pero para mentir el número es infinito.  La Sombra del Viento- Carlos Ruiz Zafón",
    "Soy como todas las personas: veo el mundo tal como desearía que sucedieran las cosas y no como realmente sucede. El Alquimista- Paulo Coelho",
    "Cuando deseas alguna cosa, todo el universo conspira para que puedas realizarla.  El Alquimista - Paulo Coelho",
    "El verdadero amor cambia con el tiempo y crece y descubre nuevas maneras de expresarse. Veronika decide morir-Paulo Coelho",
    "Amor y deseo son dos cosas diferentes; que no todo lo que se ama se desea, ni todo lo que se desea se ama.Don Quijote de la Mancha- Miguel",
    "Deja de preocuparte por envejecer y piensa en crecer. El animal moribundo-Philip Roth",
    "¡Qué maravilloso es que nadie necesite esperar ni un solo momento antes de comenzar a mejorar el mundo! El Diario de Ana Frank-Ana Frank",
    "El hombre llega mucho más lejos para evitar lo que teme que para alcanzar lo que desea. El Código da Vinci- Dan Brown",
    "Nuestras vidas se definen por las oportunidades, incluso las que perdemos. El curioso caso de Benjamin Button -F. Scott Fitzgerald",
    "No todo lo que es de oro reluce, ni toda la gente errante anda perdida. El Señor de los Anillos- J.R.R. Tolkien",
    "Es mejor mirar al cielo que vivir allí. Desayuno con diamantes-Truman Capote",
    "La vida es demasiado importante como para tomarla en serio. -Oscar Wilde ",
    "El que lee mucho y anda mucho, ve mucho y sabe mucho. Miguel de Cervantes ",
    "Tus pensamientos son semillas, y lo que cosechas dependerá de las semillas que plantas. El secreto – Rhonda Byrne",
    "Sabes que es amor cuando todo lo que deseas es estar a todas horas con la otra persona y de alguna manera sabes que la otra persona siente lo mismo",
    "No puedo volver al pasado porque antes era una persona diferente Lewis Carroll-Alicia en el País de las Maravillas",
    "Si quieres saber como es un hombre, observa como trata a sus inferiores, no a sus iguales J.K. Rowling ,Harry Potter y el Cáliz de Fuego",
    "El mundo era tan reciente que muchas cosas carecian de nombre Gabriel García Marquez, Cien años de soledad",
    "Las personas mayores nunca pueden comprender algo por si solas, y es muy aburrido para los niños tener que darles explicaciones. El principito",
    "A pesar de ti, de mi y del mundo que se dequebraja, yo te amo  Margareth Mitchell, Lo que el viento se llevó",
    "No sé a lo que pueda llegar pero sea lo que sea, iré hacia ello riéndome  Herman Melvill, Moby Dick ",
    "No todos los que vagan, están perdidos El Hobbit-J. R. R. Tolkien",
    "Puedo escribir los versos mas tristes esta noche. Yo la quise, y a veces ella también me quiso. (Pablo Neruda) ",
    "Estar sin ti es como vivir en una eterna noche sin estrellas. El infierno de Gabriel",
    "Me estás enseñando a amar. yo no sabía. Amar es no pedir, es dar. Mi alma, vacía. (Gerardo Diego) ",
    "Te amo por encima de todo aquello que no podemos ver, por encima de lo que no podemos conocer. (Federico Moccia) ",
    "Amar es destruir, y ser amado es ser destruido. (Cazadores de sombras: Ciudad de hueso) ",
    "Son nuestras elecciones las que muestran lo que somos, mucho más que nuestras habilidades. Harry Potter –  J. K. Rowling",
    "La memoria del y magnifica los buenos, y que gracias a ese artilugio logramos sobrellevar el pasado. El amor en los tiempos del cólera – Gabriel",
    "Es mejor mirar al cielo que vivir allí. Desayuno con diamantes-Truman Capote",

    "hola",
    "como estas",
    "porfavor",
    "gracias",
    "espero que te mejores",
    "saludos.",
    "feliz cumpleaños"
    ]

    categoria=["amor", "pelicula", "escritores", "libros", "lugares", "cosas", "vida", "desamor", "saludos","amigos"]

    salidita=""

    print("USERS::: " + str(len(usuarios)) + "")
    print("NOMBRES::: " + str(len(nombres)) + "")
    print("MENSAJES::: " + str(len(mensaje)) + "")
    print("CATEGORIAS::: " + str(len(categoria)) + "")
    print("CATEGORIAS::: " + str(Identificador) + "\n")

    print("URL::: " + caja_url.get() + "")
    salidita+="URL::: " + caja_url.get() + "\n"
    numero_solicitudes=int(caja_solicitudes.get())
    print("NUM SOLICITUDES::: " + str(numero_solicitudes) + "")
    salidita +="NUM SOLICITUDES::: " + str(numero_solicitudes) + "\n"
    numero_concurrencia = int(caja_concurrencia.get())
    print("NUM CONCURRENCIA::: " + str(numero_concurrencia) + "")
    salidita +="NUM CONCURRENCIA::: " + str(numero_concurrencia) + "\n"
    print("ARCHIVO PARAMETRO::: " + caja_parametros.get() + "\n")
    salidita +="ARCHIVO PARAMETRO::: " + caja_parametros.get() + "\n"

    numero_timeout=int(caja_timeout.get())

    print("***** CADENAS GENERADAS ***** " + "\n")

    global SALIDOTA
    SALIDOTA=salidita

    for i in range(numero_solicitudes):

        random_users=random.randint(0, len(usuarios)-1)
        random_mensaje = random.randint(0, len(mensaje)-1)
        random_categoria = random.randint(0, len(categoria)-1)

        if ((len(usuarios)-1) < random_users):
            random_users=random.randint(0, len(usuarios)-1)

        if ((len(mensaje)-1) < random_mensaje):
            random_mensaje=random.randint(0, len(mensaje)-1) + Identificador

        if ((len(categoria)-1) < random_categoria):
            random_categoria=random.randint(0, len(categoria)-1) + Identificador

        mensaje_saliente = "usr="
        mensaje_saliente+=usuarios[random_users]+"&"
        mensaje_saliente+= "nom="
        mensaje_saliente+=nombres[random_users]+"&"
        mensaje_saliente += "txt="
        mensaje_saliente += mensaje[random_mensaje]+" "
        mensaje_saliente += "%23"
        mensaje_saliente += categoria[random_categoria] + "\n"
        lineas2.append(mensaje_saliente)

    print("Tamaño del Archivo::: " + str(len(lineas2)) + "\n")
    for elemento in lineas2:

        global segundos

        if(segundos==numero_timeout):
            break
        else:
            url = caja_url.get()+"/api/tweet?"+elemento.replace("\n","")
            print(url)
            #r = requests.get(url)


    #*********************************************************** ARRIBA SE ENVIA EL TRAFICO







    numero_concurrencia = int(caja_concurrencia.get())
    if(Numhilo==numero_concurrencia):
        print("************************************ENTRO Y SACO LA BANDERA")
        global ContadorTiempo
        ContadorTiempo = 1


def hilo2 (mensaje):

    global ContadorTiempo
    global segundos
    contador2=0

    milisegundos = 0
    segundos = 0

    while True:

        tiempo = str(segundos) + " sg: " + str(milisegundos) + " mlsg"
        time.sleep(10 / 1000)

        milisegundos = milisegundos + 1
        if (milisegundos == 60):
            milisegundos = 0
            segundos = segundos + 1
            caja_resumen.set(str(tiempo))

        if ContadorTiempo == 1:
            break

    print("TIEMPO DE EJECUCION ======== "+str(contador2))
    global SALIDOTA
    caja_resumen.set("Resumen de Tiempo Procesado: " + tiempo + "sg\n"+SALIDOTA)


def codigoBotonEjecutar():

    #Leer el Archivo
    lineas2=leer_lista()
    lineas2.clear()

    numero_concurrencia = int(caja_concurrencia.get())
    print("::::::::::::::::::Concurrencia ->" + str(numero_concurrencia))


    global ContadorTiempo
    ContadorTiempo=0

    t = threading.Thread(target=hilo2, args=("hiloTimer",))
    t.start()

    time.sleep(1)

    for i in range(numero_concurrencia):

        iden = random.randint(2, 9)

        t2 = threading.Thread(target=Envio_Paquetes, args=(lineas2, i+1, iden))
        t2.start()



    #caja_resumen.set("Resumen de Tiempo Procesado: " + str(contador2) + "sg")


def codigoBotonTimeOut():

    global ContadorTiempo
    ContadorTiempo=1
    print("CASASDFASDFASDFASD "+str(ContadorTiempo))


def leer_lista():

    archivo = open(caja_parametros.get(), 'r')
    lineas = archivo.readlines()
    print("\nTamaño del Archivo::: "+str(len(lineas))+"\n")
    archivo.close()
    return lineas


# ************************ COMPONENTES

                                    #Primer Label con texto color de letra  y posicion
Titulo=Label(raiz,text="Ingrese los Parametros y Opciones para Enviar Trafico", fg="black")
Titulo.place(x=10, y=20)


                                    # URL

URL_label=Label(raiz,text="URL: ", fg="black")
URL_label.grid(row=0, column=1, padx=10, pady=80)

URL_entry=Entry(raiz, textvariable=caja_url)
URL_entry.place(x=120, y=80)

                                    # CONCURRENCIA

Con_label=Label(raiz,text="Concurrencia: ", fg="black")
Con_label.place(x=10, y=120)

Con_entry=Entry(raiz,textvariable=caja_concurrencia)
Con_entry.place(x=120, y=120)

                                    # SOLICITUDES

SOLI_label=Label(raiz,text="Solicitudes: ", fg="black")
SOLI_label.place(x=10, y=160)

SOLI_entry=Entry(raiz, textvariable=caja_solicitudes)
SOLI_entry.place(x=120, y=160)

                                    # PARAMETROS

PARAM_label=Label(raiz,text="Parametros: ", fg="black")
PARAM_label.place(x=10, y=200)

PARAM_entry=Entry(raiz, textvariable=caja_parametros)
PARAM_entry.place(x=120, y=200)

PARAM_buton=Button(raiz, text="Buscar", command=codigoBotonTimeOut)
PARAM_buton.place(x=350, y=200)

                                    # TIMEOUT

TIME_label=Label(raiz,text="TimeOut: ", fg="black")
TIME_label.place(x=10, y=240)

TIME_entry=Entry(raiz, textvariable=caja_timeout)
TIME_entry.place(x=120, y=240)

                                    # COMPLETADO

TIME_label=Label(raiz,text="Completado: ", fg="black")
TIME_label.place(x=10, y=280)

TIME_entry=Label(raiz,text="0 %", fg="black")
TIME_entry.place(x=120, y=280)


TIME_buton=Button(raiz,text="Ejecutar", command=codigoBotonEjecutar)
TIME_buton.place(x=200, y=280)

                                    # Resumen

TIME_label=Label(raiz,text="Resumen: ", fg="black")
TIME_label.place(x=10, y=320)

TIME_label=Label(raiz,text="RES ", fg="black", textvariable=caja_resumen)
TIME_label.place(x=10, y=340)


#************************ EJECUCION DE LA VENTANA

raiz.mainloop()         # Metodo Mainloop Para levantar la ventana, para estar en ejecucion debe estar en un
                        # boocle infinito



# http://34.67.161.177:3000/api/tweet?
#http://34.67.161.177:3000/api/tweet?usr=hellenlacan1994@gmail.com&amp;nom=Hellen%20Alexandra%20Lacan%20Hernandez&amp;txt=Como%20no%20me%20he%20preocupado%20de%20nacer,%20no%20me%20preocupo%20de%20morir%20#desamor

# usr=hellenlacan1994@gmail.com&amp;nom=Hellen Alexandra Lacan Hernandez&amp;txt=Como no me he preocupado de nacer, no me preocupo de morir #desamor










#http://34.67.161.177:3000