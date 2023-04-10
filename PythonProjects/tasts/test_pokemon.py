import requests
import pytest

TOKEN = 'e2a0833f6026eaba0f6b8fe277d96f2d'
base_url = 'https://pokemonbattle.me:9104'

def test_status_code():                                                # тест.статус код
    response = requests.post(f'{base_url}/pokemons', # Oтвет = запрос post()
    headers={'trainer_token': TOKEN},
    json={                                      
    "name": "Бука",
    "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/028.png&size=200"
})
    assert response.status_code == 400                    # утверждаю, что Oтвет на тест.статус код = 



def test_part_of_body():                            # тест.на содержание текста в боди
    response = requests.get('https://pokemonbattle.me:9104/trainers',  # Ответ= запрос get()
    params= {'trainer_id' : 3493}
                       )                   # квери параметры 
    assert response.json()['trainer_name'] == 'Silvia' #утверждаю,в формате Json,что имя тренера = Сильвия


# вводим маркер по параметру, чтобы получить сразу несколько ответов по заданным параметрам (имя, город)
@pytest.mark.parametrize('key, value', [('trainer_name', 'Silvia'), ('city', 'Tokyo')]) # тест маркер параметры (в формате ключ, значение), а именно:[('trainer_name', 'Silvia'), ('city', 'Tokyo')])

# далее подставляем в ответ на наш запрос данный маркер:
def test_part_of_body(key, value):
    response = requests.get('https://pokemonbattle.me:9104/trainers', # Ответ= запрос get()
    params= {'trainer_id' : 3493})                                    # квери параметры 
    assert response.json()[key] == value                               # подставляем в наш ответ данный маркер
