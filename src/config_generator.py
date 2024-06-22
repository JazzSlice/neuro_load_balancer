import requests 
import numpy as np 
 
def get_server_load_features(): 
    # Реализация функции для получения текущих метрик серверов 
    # Примерный возврат данных в виде списка метрик 
    return [0.5, 0.3, 0.7, 0.6]  # Это пример, в реальности нужны данные с серверов 
 
def choose_server(): 
    features = get_server_load_features() 
    response = requests.post('http://localhost:5000/predict', json={'input': features}) 
    load_prediction = response.json()['prediction'] 
     
    # Логика выбора сервера на основе предсказания нагрузки 
    chosen_server_index = np.argmin(load_prediction) 
    return chosen_server_index 
 
def update_nginx_config(chosen_server_index): 
    nginx_config_template = """ 
    stream { 
        upstream dynamic_balancer { 
            least_conn; 
 
            server backend1.example.com max_fails=3 fail_timeout=30s; 
            server backend2.example.com max_fails=3 fail_timeout=30s; 
            server backend3.example.com max_fails=3 fail_timeout=30s; 
        } 
 
        server { 
            listen 12345; 
 
            location / { 
                proxy_pass http://dynamic_balancer; 
            } 
        } 
    } 
    """ 
     
    # Пример обновления конфигурации Nginx (псевдокод) 
    with open('/etc/nginx/nginx.conf', 'w') as config_file: 
        config_file.write(nginx_config_template) 
     
    # Перезапуск Nginx для применения новой конфигурации 
    import os 
    os.system('nginx -s reload') 
 
chosen_server_index = choose_server() 
update_nginx_config(chosen_server_index)