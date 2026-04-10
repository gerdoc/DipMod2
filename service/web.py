import logging
from typing import List

import streamlit as st

from archivo.leer_data2 import LeerData2
from config.config import options, FILE_PATH, COLUMNS_FILE, median_house_value, get_pd_by_list, modelos
from regresion.modelo import Modelo


def web( ) -> None:
    st.write("""
    # Módulo 2
    ## Modelo lineal para predicción de precios de viviendas  
    """)
    ###
    #epocas = st.number_input("Épocas", value=1000, placeholder="Número de épocas")
    #batch_size = st.number_input("Batch Size", value=100, placeholder="Batch Size")
    selection = st.segmented_control("Columnas", options, selection_mode="multi",
                                     format_func=lambda option: options[option],)
    with st.form("form_prediccion"):
        longitude = st.number_input(options[0], value=0.0, format="%.2f", placeholder=options[0])
        latitude = st.number_input(options[1], value=0.0,  format="%.2f", placeholder=options[1])
        housing_median_age = st.number_input(options[2], value=0.0, format="%.2f", placeholder=options[2])
        total_rooms = st.number_input(options[3], value=0.0,  format="%.2f", placeholder=options[3])
        total_bedrooms = st.number_input(options[4], value=0.0, format="%.2f", placeholder=options[4])
        population = st.number_input(options[5], value=0.0, format="%.2f", placeholder=options[5])
        households = st.number_input(options[6], value=0.0, format="%.2f", placeholder=options[6])
        median_income = st.number_input(options[7], value=0.0, format="%.4f", placeholder=options[7])
        modelo = st.selectbox("Selecciona modelo",modelos)
        boton_enviar = st.form_submit_button("Enviar")
    if boton_enviar:
        valor: List[float] = [longitude, latitude, housing_median_age, total_rooms, total_bedrooms, population, households, median_income]
        ld: LeerData2 = LeerData2(FILE_PATH, COLUMNS_FILE, median_house_value)
        if not ld.load_train_test_data( ):
            logging.error('error loading data')
            return
        logging.info('data loaded')
        mo: Modelo = Modelo(ld, modelo1=modelo==modelos[0])
        if not mo.procesa_regresion():
            logging.error('error evaluating regression')
            return
        logging.info('regression evaluated')
        mo.prediccion( get_pd_by_list( valor ) )
        if mo.resultado is not None:
            st.success(f"Predicción del precio: {mo.resultado:.10f}")




