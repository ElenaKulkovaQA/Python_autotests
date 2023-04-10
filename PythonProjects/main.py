import requests

# создание покемона
token = 'e2a0833f6026eaba0f6b8fe277d96f2d' # создание переменной токен= токену, полученному из котика
response_add_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', # имя переменной = requests.тип зпроса(здесь post)
json={                                      # body запроса в формате json
    "name": "Бульбик",
    "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/008.png&size=200"
}, 
headers= {'trainer_token': token}           # headers запроса в формате json
)
print(response_add_pokemon.text)            # напечатать ответ переменной


 # Убить покемона 

response_kill_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons/kill', # имя переменной = requests.тип зпроса(здесь post)
json={                                      # body запроса в формате json
    "pokemon_id": "8816"
}, 
headers= {'trainer_token': token}           # headers запроса в формате json
)
print(response_kill_pokemon.text)            # напечатать ответ переменной



# создание покемона2
base_url = 'https://pokemonbattle.me:9104' # создание переменной base_url
response_add_pokemon2 = requests.post(f'{base_url}/pokemons',
json={                                     # body запроса в формате json
    "name": "Бука",
    "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/028.png&size=200"
}, 
headers= {'trainer_token': token}           # headers запроса в формате json
)
print(response_add_pokemon2.text)           # напечатать ответ переменной



# получение списка моих покемонов
response_my_pokemons = requests.get(f'{base_url}/pokemons', # создание переменной "response_my_pokemons"
 params= {'trainer_id' : 3493}                              # квери параметры для сортировки: trainer_id
)
print(response_my_pokemons.text)            # напечатать ответ переменной


 
  # Убить покемона 

response_kill_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons/kill', # имя переменной = requests.тип зпроса(здесь post)
json={                                      # body запроса в формате json
    "pokemon_id": "8815"
}, 
headers= {'trainer_token': token}           # headers запроса в формате json
)
print(response_kill_pokemon.text)            # напечатать ответ переменной


# смена имени покемона
response_put_name = requests.put('https://pokemonbattle.me:9104/pokemons',
json= {
       "pokemon_id": "8817",
       "name":"Цветок",
       "photo": "https://dolnikov.ru/pokemons/albums/004.png",
      }, 
headers= {'trainer_token': token})
print (response_put_name.text)

# поймать покемона в покебол

response_add_pokebol = requests.post(f'{base_url}/trainers/add_pokeball', # имя переменной = requests.тип зпроса(здесь post)
json={                                      # body запроса в формате json
    "pokemon_id": "8346"
}, 
headers= {'trainer_token': token}           # headers запроса в формате json
)
print(response_add_pokebol.text)  









                                    
