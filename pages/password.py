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
        st.image("denied.jpg", width=300)  
    else:
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
        st.success("Mot de passe correct, bravo ")  
        st.snow()
        st.balloons()
        st.image("image.png", width=300)  