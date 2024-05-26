bash
#!/bin/bash

#echo "Создание данных для обучения"
python data_creation.py train

#echo "Создание данных для тестирования"
python data_creation.py test

#echo "Предобработка данных"
python model_preprocessing.py

#echo "Обучение модели"
python model_preparation.py

#echo "Тестирование модели"
python model_testing.py

