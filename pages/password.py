import streamlit as st
import time
pw = "123456"
essais_restants = 3

st.title("My new password app")
st.write("SAISIR VOTRE SUPER MOT DE PASSE CI-DESSOUS")

saisie = st.text_input("Saisir votre mot de passe", type="password")

if(st.button("Vérifier") or saisie):
    with st.spinner('Vérification'):
        time.sleep(3)
    if(saisie!=pw):
        st.error("Mot de passe incorrect")
        st.image("Pinguoin.jpg", width=300)  
    else:
        st.success("Mot de passe correct, bravo ")  
        st.snow()
        st.balloons()
        st.image("Apple and cookie.jpg", width=300)  