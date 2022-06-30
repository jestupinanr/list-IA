import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

fails = 0
course = ''
failsStudent = []
assistantToday = []

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
        talk('llamando lista...');
        talk('Obteniendo datos...');
        return getDataCourses()
    elif 'mostrar fallas' in rec:
        return showFails()
    elif 'mostrar estudiantes con fallas' in rec:
        return showStudentsFail()
    elif 'mostrar lista' in rec:
        return mostrarLista()

       

def getDataCourses(): 
    from data.dataExample import datacourses
    # dataCourses = [2125,2223,3235,3653];
    talk("¿Cual es tu numero de curso?");
    rec = listen();
    talk("Buscando curso" + rec);
    curso ='undefined'
    global course
    if rec in datacourses.clases:
        course = rec
        talk("curso encontrado")
        data = {}
        if rec == '2232':
            data = datacourses.curso2232
        
        elif rec == '2125':
            data = datacourses.curso2125
        elif rec == '2223':
            data = datacourses.curso2223
        elif rec == '3235':
            data = datacourses.curso3235
        elif rec == '3235':
            data = datacourses.curso3653
        isCourseCorrect(data)
    else:
        talk("curso no encontrado por favor intente de nuevo")
        getDataCourses()



def isCourseCorrect(data):
  print(data)
  talk("el curso es" + data['name'] + "correcto?");
  rec = listen();
  if 'correcto' in rec:
    talk('Obteniendo estudiantes...')
    llamarLista(data)
  else:
    getDataCourses()



def llamarLista(data):
    students = data['students']
    global fails
    global assistantToday
    for i in students:
        talk(i);
        try:
            rec = listen()
            if 'presente' in rec:
                assistantToday.append({"name": i, "isThere": "Si"})
                talk("gracias " + i)
            elif 'aqui' in rec:
                assistantToday.append({"name": i, "isThere": "Si"})
                talk("gracias " + i)
            elif 'yo' in rec:
                assistantToday.append({"name": i, "isThere": "Si"})
                talk("gracias " +i)
            else:
                fails = fails+1
                assistantToday.append({"name": i, "isThere": "No"})
                failsStudent.append(i)
               
        except:
           fails = fails+1
           assistantToday.append({"name": i, "isThere": "No"})
           failsStudent.append(i)
           continue
    return 'finalizado'

def showFails():
    global fails
    global course
    talk("El total de fallas para el curso " +course + " es de " + str(fails));
    return "El total de fallas para el curso " +course + " es de " + str(fails)

def showStudentsFail():
    global failsStudent
    text = ''
    talk('Estos son los estudiantes con fallas')
    for i in failsStudent:
        text += i + '\n' 
    return text

def mostrarLista():
    global assistantToday
    text = ''
    talk('Estos son los resultados de la lista de hoy')
    print(assistantToday)
    for i in assistantToday:
        print(i)
        text += i['name'] +"----"+i['isThere'] + '\n' 
    return text