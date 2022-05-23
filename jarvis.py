import speech_recognition as sr
import pyttsx3

name = 'alexa'
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(message):
    engine.say(message)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            voice = listener.listen(source)
            try:
                rec = listener.recognize_google(voice, language="es-CO")
            except sr.UnknownValueError:
                engine.say("undestand")
            rec = rec.lower()
            # if name in rec:
            print(rec)

    except:
        pass
    return rec

def run():
    talk('que quieres que haga por ti hoy?');
    rec = listen()
    if 'llamar lista' in rec:
        # music = rec.replace("llamar lista" , '')
        talk('llamando lista...');
        talk('Obteniendo datos...');
        getDataCourses();


def getDataCourses(): 
    dataCourses = [2125,2223,3235,3653];
    talk("¿Cual es tu numero de curso?");
    rec = listen();
    curso ='undefined'
    if dataCourses[0] in rec:
        curso = "metodologia de desarrollo"
    elif dataCourses[1] in rec:
        curso = "ingenieria de software 2"
    elif dataCourses[2] in rec:
        curso = "desarrollo web"
    elif dataCourses[3] in rec:
        curso = "desarrollo avanzado"
    
    if curso == 'undefined':
        talk("lo siento curso no encontrado")

    talk("el curso es" + curso + "correcto?");
  
    isCourseCorrect()



def isCourseCorrect():
  rec = listen();
  if 'si' in rec:
    talk('Obteniendo estudiantes...')
    llamarLista()
  else:
    getDataCourses()



def llamarLista():
    estudiantes = ["juan diego", "andres camilo", "julian enrique"]
    for i in estudiantes:
        talk(i);
        rec = listen()
        if 'presente' in rec:
            talk("gracias " + i)
        if 'aqui' in rec:
            talk("gracias " + i)
        if 'yo' in rec:
            talk("gracias " +i)
        else:
            continue


run()