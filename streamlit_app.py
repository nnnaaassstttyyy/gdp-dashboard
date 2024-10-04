import streamlit as st
import pandas as pd
import math
from pathlib import Path
import csv
from PIL import Image

st.title("Титаник!")

st.header("Титаник до и после:")
image = Image.open('641aee6d9d7f730aa0810f53d9323b51.jpg')
st.image(image, caption = 'Фото из архива', use_column_width=True)

def count_by_class_and_sex(filename):
    class_counts = {
        1: {'male': 0, 'female': 0},
        2: {'male': 0, 'female': 0},
        3: {'male': 0, 'female': 0}
    }

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        pclass_idx = header.index('Pclass')
        sex_idx = header.index('Sex')

        for row in reader:
            try:

                pclass = int(row[pclass_idx])
                sex = row[sex_idx].lower()
                if pclass in class_counts and sex in class_counts[pclass]:
                    class_counts[pclass][sex] += 1
            except (ValueError, IndexError):
                continue

    return class_counts
file_path = "titanic_train 2.csv"
results = count_by_class_and_sex(file_path)

st.sidebar.header("Выберите класс и пол")

pclass = st.sidebar.selectbox("Выберите класс:", [1, 2, 3])
sex = st.sidebar.selectbox("Выберите пол:", ["male", "female"])

st.header(f"Статистика для {pclass} класса, {sex}:")
st.write(f"Количество пассажиров: {results[pclass][sex]}")

df = pd.DataFrame(results).T
df = df.rename(columns = {'male':'Мужчины','female':'Женщины'})
st.header("Полная статистика:")
st.table(df)
