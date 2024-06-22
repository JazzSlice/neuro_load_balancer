import pandas as pd

# Чтение лог-файлов Nginx
nginx_logs = pd.read_csv("nginx_logs.csv")  # Содержит колонки: timestamp, request, response_time, server_id

# Чтение данных о производительности серверов
server_metrics = pd.read_csv("server_metrics.csv")  # Содержит колонки: timestamp, server_id, cpu_usage, memory_usage, active_connections

# Объединение данных для последующей обработки
data = pd.merge(nginx_logs, server_metrics, on=["timestamp", "server_id"])
