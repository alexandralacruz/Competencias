import json
from src import config 



def load_courses():
    with open(config.COURSES_FILE, 'r', encoding='utf-8') as f:
        courses_data = json.load(f)
    return courses_data


def load_competencies_description():
    with open(config.DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
        desc_data = json.load(f)
    return desc_data

def find_course(code):
    with open(config.COMPETENCES_FILE, 'r', encoding='utf-8') as f:
        competencias = json.load(f)
    
    # try:
    #     value = competencias[code]  # Intentar acceder al valor usando la clave
    # except KeyError:
    #     value = None  # Si no existe la clave, asigna un valor por defectoreturn competencias[code]
     
    return competencias.get(code,'El curso no existe')  # Devolver el valor o None si no existe la clave

def get_list_especificas(especificas):

    with open(config.DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
        desc_data = json.load(f)

    list_especificas = []

    for i in especificas:
        list_especificas.append(f'{i}-{desc_data["competencias especificas"][i]}')

    return list_especificas

def get_list_genericas(genericas):

    with open(config.DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
        desc_data = json.load(f)

    list_genericas = []

    for i in genericas:
        list_genericas.append(f'{i}-{desc_data["competencias genericas"][i]}')

    return list_genericas

def get_list_saberpro(saberpro):

    with open(config.DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
        desc_data = json.load(f)

    list_saberpro = []

    for i in saberpro:
        list_saberpro.append(f'{i}-{desc_data["SABER PRO"][i]}')

    return list_saberpro

def get_list_dimension(dimension):

    with open(config.DESCRIPTION_FILE, 'r', encoding='utf-8') as f:
        desc_data = json.load(f)

    list_dimension = []

    if len(dimension)!=0:
        for i in dimension:
            list_dimension.append(f'{i}-{desc_data["dimensiones"][i]}')

    return list_dimension

def get_list_abet(abet):
    with open(config.ABET_ES_FILE, 'r', encoding='utf-8') as f:
        abet_data = json.load(f)
    
    output = {}

    for indicator in abet:
        for objective, d in abet_data.items():
            #print(objective)
            #print(d)
            if indicator in d["indicadores"]:
                if objective not in output:
                    output[objective] = {"description": abet_data[objective]["description"], "indicadores": []}
                output[objective]["indicadores"].append(f"{indicator}: {d['indicadores'][indicator]}")
    return output
    # abet_str = []
    # # Imprimir la salida en el formato requerido
    # for objective, d in output.items():
    #     abet_str.append(f"{objective}: {d['description']}")
    #     for indicator in d["indicadores"]:
    #         abet_str.append(f"  {indicator}")
            

    # return abet_str 