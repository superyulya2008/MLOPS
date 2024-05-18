
import numpy as np
import pandas as pd
import os

# Генерация данных
np.random.seed(0)
dates = pd.date_range(start='2023-01-01', periods=365)
temperatures = 15 + 8 * np.random.randn(365)

# Добавление аномалий
anomalies = [50, 60, -10]
for a in anomalies:
    idx = np.random.randint(0, 365)
    temperatures[idx] = a

# Создание DataFrame
df = pd.DataFrame(data={'Date': dates, 'Temperature': temperatures})

# Разделение на тренировочный и тестовый наборы
train_df = df.sample(frac=0.8, random_state=1)
test_df = df.drop(train_df.index)

# Сохранение данных
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)
train_df.to_csv('train/train_data.csv', index=False)
test_df.to_csv('test/test_data.csv', index=False)