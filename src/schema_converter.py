from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Нормализация данных
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data[["response_time", "cpu_usage", "memory_usage", "active_connections"]])

# Разделение данных на входные признаки и метки
X = data_scaled[:, :-1]  # Входные признаки
y = data_scaled[:, -1]   # Метки (например, активные соединения)

# Разделение данных на обучающую и тестовую выборки
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
