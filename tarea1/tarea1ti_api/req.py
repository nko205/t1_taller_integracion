import requests


## saca los episodios con su info
def info_episodios(lista):
    response = []
    for episodio in lista:
        nombre = episodio["name"]
        f_aire = episodio["air_date"]
        code_episode = episodio["episode"]
        id = episodio["id"]
        response.append([nombre, f_aire, code_episode, id])
    return response

def get_all_episodes():

    pag1 = requests.get("https://rickandmortyapi.com/api/episode/?page=1").json()
    pag2 = requests.get("https://rickandmortyapi.com/api/episode/?page=2").json()
    lista_resultado = [pag1, pag2]
    result_final = []
    for pagina in lista_resultado:
        pg = info_episodios(pagina["results"])
        result_final = result_final + pg
    return result_final

## entrega toda la info del episodio con sus personajes ##

def obtener_personajes(episodio):
    lista_personajes = []

    for personaje in episodio["characters"]:
        id_personaje = personaje.rsplit('/', 1)[-1]
        lista_personajes.append(int(id_personaje))

    info_personajes = requests.get("https://rickandmortyapi.com/api/character/"+str(lista_personajes)).json()

    lista_final = []
    for personajes in info_personajes:
        id = personajes["id"]
        nombre = personajes["name"]
        lista_final.append([nombre, id])

    return lista_final





def info_episodio(id):
    episodio = requests.get("https://rickandmortyapi.com/api/episode/"+str(id)).json()
    personajes = obtener_personajes(episodio)
    info_episodio = []
    lista_final = []
    for item in episodio:
        if item != "characters":
             info_episodio.append(episodio[item])
        else:
            pass
    lista_final.append(info_episodio)
    lista_final.append(personajes)
    return lista_final

## info personajes ##

def obtener_episodios_personaje(personaje):
    lista_episodios =[]
    for episodio in personaje["episode"]:
        id_episodio = episodio.rsplit('/', 1)[-1]
        lista_episodios.append(int(id_episodio))
    inf_episodio = requests.get("https://rickandmortyapi.com/api/episode/"+str(lista_episodios)).json()
    lista_final = []
    for episodio in inf_episodio:
        nombre_episodio = episodio["name"]
        id_episodio = episodio["id"]
        lista_final.append([nombre_episodio, id_episodio])
    return lista_final

def info_personaje(id):

    personaje = requests.get("https://rickandmortyapi.com/api/character/"+str(id)).json()
    episodios = obtener_episodios_personaje(personaje)
    resultado = [personaje["id"], personaje["name"], personaje["status"],
    personaje["species"],personaje["type"],
    personaje["gender"], personaje["origin"]["name"],
    personaje["origin"]["url"].rsplit('/', 1)[-1],
    personaje["location"]["name"],
    personaje["location"]["url"].rsplit('/', 1)[-1], personaje["image"], personaje["created"]
    ]
    resultado.append(episodios)
    return resultado


# print(info_personaje(249))




## info lugar ##
def obtener_personajes_lugar(lugar):
    lista_personajes = []

    for personaje in lugar["residents"]:
        id_personaje = personaje.rsplit('/', 1)[-1]
        lista_personajes.append(int(id_personaje))

    info_personajes = requests.get("https://rickandmortyapi.com/api/character/"+str(lista_personajes)).json()

    lista_final = []
    for personajes in info_personajes:
        id = personajes["id"]
        nombre = personajes["name"]
        lista_final.append([nombre, id])

    return lista_final

def info_lugar(id):
    lugar = requests.get("https://rickandmortyapi.com/api/location/"+str(id)).json()
    personajes = obtener_personajes_lugar(lugar)
    info_lugar = []
    for item in lugar:
        if item != "residents":
            info_lugar.append(lugar[item])
        else:
            pass
    info_lugar.append(personajes)
    return info_lugar

# print(info_lugar(7))
