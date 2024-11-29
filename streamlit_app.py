import streamlit as st

st.title("🎈 Yes Bpo")


# Campos del formulario
fecha = st.date_input("Fecha")
nombre = st.text_input("Nombre")
novedad = st.selectbox("Novedad", ["Llegada Tarde", "Incapacidad"])
detalles = st.text_area("Detalles")

# Botón para enviar los datos (en este caso, simplemente imprimimos los datos)
if st.button("Enviar"):
    st.write("Datos ingresados:")
    st.write(f"Fecha: {fecha}")
    st.write(f"Nombre: {nombre}")
    st.write(f"Novedad: {novedad}")
    st.write(f"Detalles: {detalles}")

import streamlit as st
import pandas as pd

st.title(" Yes Bpo")

# Crear un DataFrame vacío para almacenar los datos
data = pd.DataFrame(columns=['Fecha', 'Nombre', 'Novedad', 'Detalles'])

# Campos del formulario
fecha = st.date_input("Fecha")
nombre = st.text_input("Nombre")
novedad = st.selectbox("Novedad", ["Llegada Tarde", 'Incapacidad'])
detalles = st.text_area("Detalles")

# Botón para enviar los datos
if st.button("Enviar"):
    # Crear un nuevo DataFrame con los datos ingresados
    new_data = pd.DataFrame({'Fecha': [fecha],
                             'Nombre': [nombre],
                             'Novedad': [novedad],
                             'Detalles': [detalles]})

    # Agregar los nuevos datos al DataFrame principal
    data = pd.concat([data, new_data], ignore_index=True)

    # Guardar el DataFrame en un archivo CSV
    data.to_csv('novedades.csv', index=False)

    st.write("Datos guardados en el archivo CSV")
