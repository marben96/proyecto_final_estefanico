from pickle import load
import streamlit as st
model = load(open("/workspaces/proyecto_final_estefanico/models/random_forest.sav", "rb"))

st.title('Cálculo de ingreso')

region =  st.radio(
    "Región a la que pertenece", 
    ['Región de ñuble',
 'Región del biobio',
 'Región metropolitana',
 'Región de tarapaca',
 'Región de los rios',
 'Región del libertador gral bernardo ohiggins',
 'Región de la araucania',
 'Región de valparaiso',
 'Región de los lagos'
 'Región de coquimbo',
 'Región del maule',
 'Región de arica y parinacota',
 'Región de antofagasta',
 'Región de atacama',
 'Región de magallanes y de la antartica chilena',
 'Región de aysen del gral carlos ibañez del campo'],
    index=None)

nivel_socioeconomico = st.radio(
    "Nivel socioeconómico",
    ['Bajo-medio', 'Bajo-medio-alto', 'Medio', 'Bajo', 'Alto', 'Medio-alto', 'Bajo-alto'],
     index= None)

personas_por_hogar = st.slider('¿Cuántas personas viven con usted?', min_value=1, max_value=13, step=1)

edad = st.slider('Edad', min_value=15, max_value=100, step=1)

estado_civil = st.radio(
    "Estado civil",
    ['Casado(a)','Separado(a)','Conviviente sin acuerdo de unión civil', 'Soltero(a)', 'Viudo(a)', 'Divorciado(a)','Anulado(a)', 'Conviviente civil streamlit run src/app.py'],
index= None)


nivel_educacional = st.radio(
    "Nivel educacional",
    ['Básica', 'Técnica nivel superior', 'Media científico humanista', 'Técnica comercial industrial normalista', 'Media técnica profesional', 'Profesional', 'Diferencial', 'Ninguno', 'Magister', 'Doctorado'],
     index= None)

prevision =  st.radio(
    "Previsión",
    ['FONASA','Isapre','FF.AA. y del Orden','Ninguno (particular)','Otro sistema'],
    index = None
)



region_dic = {'Región de ñuble': 0,
 'Región del biobio' : 1,
 'Región metropolitana' : 2,
 'Región de tarapaca' : 3,
 'Región de los rios': 4,
 'Región del libertador gral bernardo ohiggins': 5,
 'Región de la araucania': 6,
 'Región de valparaiso': 7,
 'Región de los lagos': 8,
 'Región de coquimbo':9,
 'Región del maule':10,
 'Región de arica y parinacota': 11,
 'Región de antofagasta': 12,
 'Región de atacama':13,
 'Región de magallanes y de la antartica chilena': 14,
 'Región de aysen del gral carlos ibañez del campo': 15}


nivel_socioeconomico_dic = {
'Bajo-medio': 0,
 'Bajo-medio-alto': 1,
 'Medio': 2,
 'Bajo': 3,
 'Alto': 4,
 'Medio-alto': 4,
 'Bajo-alto': 6}


estado_civil_dic = {'Casado(a)': 0,
 'Separado(a)': 1,
 'Conviviente sin acuerdo de unión civil': 2,
 'Soltero(a)': 3,
 'Viudo(a)': 4,
 'Divorciado(a)': 5,
 'Anulado(a)': 6,
'Conviviente civil': 7}

nivel_educacional_dic= {'Básica': 0,
'Técnica nivel superior': 1,
'Media científico humanista': 2,
'Técnica comercial industrial normalista': 3,
'Media técnica profesional': 4,
'Profesional': 5,
'Diferencial': 6,
'Ninguno': 7,
'Magister': 8,
'Doctorado': 9}

prevision_dic= {
'FONASA': 0,
 'Isapre': 1,
 'FF.AA. y del Orden': 2,
 'Ninguno (particular)': 3,
'Otro sistema': 4}


if st.button('Predecir'):
    prediccion = model.predict([[region_dic[region],nivel_socioeconomico_dic[nivel_socioeconomico], personas_por_hogar, edad, prevision_dic[prevision],estado_civil_dic[estado_civil],nivel_educacional_dic[nivel_educacional]]])
    st.write('Salario', prediccion)