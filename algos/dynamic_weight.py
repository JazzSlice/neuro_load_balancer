import requests

def get_server_load_features():
    # Функция для получения текущих метрик серверов
    # Возвращает массив с текущими значениями метрик серверов
    pass

def choose_server():
    features = get_server_load_features()
    response = requests.post('http://localhost:5000/predict', json={'input': features})
    load_prediction = response.json()['prediction']
    
    # Логика выбора сервера на основе предсказания нагрузки
    # В данном примере предположим, что выбирается сервер с наименьшей предсказанной нагрузкой
    chosen_server = min(load_prediction)
    return chosen_server

# Интеграция с логикой балансировки Nginx (например, через перезапись конфигурации)
chosen_server = choose_server()
update_nginx_config(chosen_server)
