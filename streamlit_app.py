import streamlit as st
import joblib
import numpy as np
import datetime

vars1 = ('Ст3пс/Э        ', 'C121TM/ЭТ      ', '25Г2С          ',
       'C091TM.z01/ЭТ  ', '09Г2С          ', 'C071TM.z01/ЭТ  ',
       '3SP.z23/ЭТ     ', '28С.2          ', 'Ст3сп          ',
       'СТ3ПС.6        ', '35ГС           ', '4SP.z08/ЭТ     ',
       'СТ3ГСП.2       ', '09Г2С.16       ', 'СТ3ГПС.8       ',
       '08YU.z02/ЭТ    ', 'Ш2.3           ', 'СТ3ПС.7        ',
       '3SP.z24/ЭТ     ', '5SP.z24/ЭТ     ', 'SC2/ЭТ         ',
       'Ст3сп/Э        ', 'SC2M/ЭТ        ', 'GR60.z06/ЭТ    ',
       'Ст5сп          ', 'Ш2.1           ', 'Ст2пс          ',
       'Ст1пс.z05/ЭТ   ', 'Ст1пс          ', '20             ',
       'Ст3Гпс         ', 'СТ3ГСП.4       ', 'Ст3сп/Т        ',
       'Ст4сп/ЭТ       ', 'Ст4сп          ', 'Ст1кп          ',
       'Ст3сп/ЭТ       ', 'Ст3пс          ', '28С            ')

vars2 = ('Изл', 'МНЛС', 'МНЛЗ')

st.sidebar.title('Введите значения для каждого признака')
f1 = st.sidebar.number_input('Время, затраченное на этап "Продувка" (сек)', value = 1167.0, min_value = 0.0, max_value =  1553.0)
f2 = st.sidebar.number_input('Доля O2 в отх. газах (медиана)', value = 7.52, min_value = 0.0, max_value = 29.0)
f3 = st.sidebar.number_input('Доля H2 в отх. газах (медиана)', value = 0.17, min_value = 0.0, max_value = 2.0)
f4 = st.sidebar.number_input('Доля СО2 в отх. газах', value = 7.53, min_value = 0.0, max_value =12.0)
f5 = st.sidebar.selectbox('Марка заданная', vars1)
f6 = st.sidebar.number_input('Доля СО2 в отх. газах (стандартное отклонение)', value = 8.72, min_value = 0.0, max_value = 13.0)
f7 = st.sidebar.selectbox('Направление разливки', vars2)
f8 = st.sidebar.number_input('Доля О2 в отх. газах (суммарное значение)', value = 26061.0, min_value = 0.0, max_value = 140000.0)
f9 = st.sidebar.number_input("""Время, затраченное на этап "Обрыв горловины" (сек) (если не было, напишите 0)""", value = 138.0, 
	min_value = 0.0, max_value =10000.0)
f10 = st.sidebar.number_input('Температура чугуна', value = 1397.0, min_value = 0.0, max_value = 1470.0)


l = np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]).reshape(1, -1)
model1 = joblib.load("cb_temp.pkl")
model2 = joblib.load("cb_c.pkl")
pred_t = model1.predict(l)
pred_c = model2.predict(l)

temp = np.round(pred_t[0])
c = np.round(pred_c[0], 4)

if c:
       now = datetime.datetime.now() 
       st.write(now.strftime('%Y-%m-%d %H:%M:%S'))
       
st.write('**Температура:** ', temp)
st.write('**Содержание углерода:** ', c)

