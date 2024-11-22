from pickle import load
import streamlit as st

model = load(open("/workspaces/proyecto_final_estefanico/models/random_forest.sav", "rb"))

st.markdown(
    """
    <style>
    .stApp {
        background-color: #dbd9d9; /* Color gris claro */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Título
st.markdown(
    """
    <style>
    .stApp h1 {
        color: #010369; /* Cambia este valor al color que desees */
        font-weight: bold; /* Opcional: pone el título en negrita */
        text-align: center; /* Opcional: centra el título */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal de la aplicación
st.title('TIP: Perfila al usuario por sus ingresos económicos')

st.markdown(
    """
    <style>
    /* Cambiar el color y formato de los labels de los radios */
    .stRadio label {
        color: #010369; /* Color del texto */
        font-size: 30px; /* Tamaño del texto */
        font-weight: bold; /* Negrita */
        font-family: 'Arial', sans-serif; /* Fuente */
        text-align: left; /* Alineación */
    }

    /* Cambiar el color y formato de los labels de los sliders */
    .stSlider label {
        color: #010369; /* Color del texto */
        font-size: 30px; /* Tamaño del texto */
        font-weight: bold; /* Negrita */
        font-family: 'Helvetica', sans-serif; /* Fuente */
        text-align: center; /* Alineación */
    }

    /* Cambiar el color de fondo y texto de los labels */
    .stCheckbox label {
        color: #008080; /* Color del texto */
        font-size: 30px; /* Tamaño del texto */
        font-weight: normal; /* Negrita */
        text-align: center; /* Alineación */
    }

#Variables
st.subheader("Región: ")
st.markdown(

    /* Cambiar el color de los botones seleccionados */
    .stRadio > div > div > div > label {
        background-color: #010369; /* Color de fondo de las opciones seleccionadas */
        border-radius: 5px;
    }

    /* Cambiar el color del texto al pasar el mouse por encima */
    .stRadio > div > div > div > label:hover {
        background-color: #010369; /* Color cuando el cursor pasa por encima */
        color: white; /* Color del texto cuando se selecciona */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Cambiar el color de fondo y el color del texto en el slider */
    .stSlider div {
        background-color: ##d9dadb; /* Color de fondo del slider */
        color: #010369; /* Color del texto */
        font-size: 16px; /* Tamaño del texto */
    }

    /* Personalizar el color del track y el botón del slider */
    .stSlider > div > div > div {
        background-color: #fffff; /* Color del track */
        height: 8px; /* Altura del track */
    }

    .stSlider > div > div > input {
        background-color: #010369; /* Color de la barra del slider */
        width: 20px; /* Ancho del slider */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader("Pertenencia a zona urbana o rural")
area =  st.radio(
    "Seleccione el área al cual pertenece",
    ['Urbano','Rural'],
    index = None)

st.subheader("Nivel socioeconómico")
nsoceco = st.selectbox(
    "Seleccione su nivel socioeconómico",
    ['Bajo', 'Bajo-medio', 'Bajo-medio-alto', 'Bajo-alto', 'Medio','Medio-alto','Alto'],
    index = None)

st.subheader("¿Cuántas personas viven en el hogar?")
personas_x_hogar = st.slider('Seleccione un número', min_value=1, max_value=11, step=1)

st.subheader("Nivel educacional:")
educ = st.selectbox(
    "Seleccione nivel educacional",
    ['Sin educación formal', 'Básica incompleta', 'Básica completa', 'Media humanista incompleta','Media humanista completa', 'Media técnica profesional incompleta',  'Media técnica profesional completa', 'Técnico nivel superior incompleta', 'Técnico nivel superior completo', 'Profesional incompleto', 'Profesional completo', 'Posgrado incompleto', 'Posgrado completo'],
     index= None)

st.subheader("Afiliación a sistema previsional de salud")
sprev_salud =  st.radio(
    "Seleccione sistema previsional de salud",
    ['FONASA','Isapre','FF.AA. y del Orden','Ninguno (particular)','Otro sistema'],
    index = None
)

st.subheader("Condición laboral")
activ = st.radio(
    "Seleccione condición laboral actual",
    ['Ocupado(a)', 'Desocupado(a) (busca empleo)', 'Inactivo(a) (no busca empleo)'],
    index = None
)

st.subheader("Propiedad de la vivienda actual")
ten_viv = st.radio(
  "Seleccione propiedad de la vivienda",
  ['Propia', 'Arrendada', 'Cedida', 'Poseedor/ocupante irregular, usufructo u otro'],
  index = None
)

#Diccionarios

area_dic = {'Urbano': 1, 'Rural': 2}

nsoceco_dic = {'Bajo': 1,
 'Medio': 2,
 'Alto': 3,
 'Bajo-medio': 4,
 'Bajo-alto': 5,
 'Bajo-medio-alto': 6,
 'Medio-alto': 7}

educ_dic = {'Sin educación formal': 0,
 'Básica incompleta': 1,
 'Básica completa': 2,
 'Media humanista incompleta': 3,
 'Media técnica profesional incompleta': 4,
 'Media humanista completa': 5,
 'Media técnica profesional completa': 6,
 'Técnico nivel superior incompleta': 7,
 'Técnico nivel superior completo': 8,
 'Profesional incompleto': 9,
 'Posgrado incompleto': 10,
 'Profesional completo': 11,
 'Posgrado completo': 12}

sprev_salud_dic= {'FONASA': 1,
 'Isapre': 2,
 'FF.AA. y del Orden': 3,
 'Ninguno (particular)': 4,
 'Otro sistema': 5}

ten_viv_dic={'Propia': 1,
 'Arrendada': 2,
 'Cedida': 3,
 'Poseedor/ocupante irregular, usufructo u otro': 4}

activ_dic = {'Ocupado(a)': 1,
 'Desocupado(a) (busca empleo)': 2,
 'Inactivo(a) (no busca empleo)': 3}

#Botón final
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #010369; /* Color de fondo del botón (Azul) */
        color: white; /* Color del texto */
        font-size: 30px; /* Tamaño de la fuente */
        font-weight: bold; /* Negrita */
        border-radius: 10px; /* Bordes redondeados */
        border: none; /* Sin borde */
        padding: 15px 25px; /* Espaciado interno */
        transition: background-color 0.3s ease; /* Efecto de transición para el color de fondo */
    }

    .stButton>button:hover {
        background-color: #010369; /* Color de fondo cuando se pasa el mouse*/
    }
    </style>
    """, 
    unsafe_allow_html=True
)

if st.button('Haz clic aquí'):
    prediccion = model.predict([
        [area_dic[area], nsoceco_dic[nsoceco], personas_x_hogar,  educ_dic[educ],
        sprev_salud_dic[sprev_salud], activ_dic[activ], ten_viv_dic[ten_viv]]
    ])
    st.write('Ingreso estimado:', prediccion)

