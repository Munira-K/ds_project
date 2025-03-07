import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

st.title("👌Оценка качества моделей")

st.write(''' Метрики, представленные в таблице, помогают оценить качество моделей на тестовых и тренировочных данных. Мы выбрали следующие метрики:
- Recall - чтобы найти всех недовольных пассажиров и минимизировать ложкоположительные случаи (то есть, когда модель ошибочно считает недовольного пассажира удовлетворенным).
- ROC AUC оценивает способность модели различать удовлетворенных и неудовлетворенных пассажиров.

##### 🔹1. Таблица метрик:''')
data = {
    'Model': ['Logistic Regression', 'K-Nearest Neighbors (KNN)', 'Decision Tree', 'LightGBM (LGBM)'],
    'Recall (Test)': [0.80, 0.84, 0.88, 0.89],
    'Recall (Train)': [0.80, 0.89, 0.88, 0.89],
    'ROC AUC (Test)': [0.89, 0.93, 0.95, 0.98],
    'ROC AUC (Train)': [0.89, 0.97, 0.95, 0.98]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.write(''' ---
Кросс-валидация помогает оценить стабильность моделей на разных подвыборках данных.
##### 🔹Результаты на кросс-валидации''')

df2 = {
    'Model': ['KNN', 'Logistic Regression', 'Decision Tree', 'LGBM'],
    'Mean Recall': [0.86, 0.80, 0.86, 0.89],
    'Recall Std Dev': [0.0010, 0.0021, 0.0109, 0.0014]
}

data2 = pd.DataFrame(df2)
st.dataframe(df2)

st.write(''' ---
**🏆 Выбор лучшей модели**
- **Высокая точность и полнота**: LGBM лучше всего справляется с предсказанием удовлетворенности пассажиров.
- **Стабильность**: Низкая дисперсия на кросс-валидации указывает на то, что модель хорошо обобщает данные.
- **Отсутствие переобучения**: Результаты на тренировочных и тестовых данных практически идентичны.
- **Лучшее разделение классов**: ROC AUC (0.98) — максимальное значение среди всех моделей.
''')