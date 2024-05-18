from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загрузка данных
train_df = pd.read_csv('train/train_data.csv')
test_df = pd.read_csv('test/test_data.csv')

# Предобработка данных
scaler = StandardScaler()
train_df['Temperature'] = scaler.fit_transform(train_df[['Temperature']])
test_df['Temperature'] = scaler.transform(test_df[['Temperature']])

# Сохранение обработанных данных
train_df.to_csv('train/preprocessed_train_data.csv', index=False)
test_df.to_csv('test/preprocessed_test_data.csv', index=False)