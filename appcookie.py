
import streamlit as st

st.title("Quizz teste.")

if "etapa_cookie" not in st.session_state:
    st.session_state.etapa_cookie = False

nome = st.text_input("Qual é o seu nome?").strip().lower()

if nome in ["pamela", "pam", "pamelinha", "pamela matos", "pamela patricia", "paty", "pamela patricia de almeida matos", "pamelao"]:

    st.write("É você mesmo que eu procuro. Vamos continuar.")

resposta = st.text_input("Você é o que do Paulo?").strip().lower()

if resposta == "namorada":
    st.success("Muito bem, é isso mesmo!")
    st.session_state.etapa_cookie = True

elif resposta == "ficante":
    st.write("Não é bem isso. Talvez só por um momento, mas vamos continuar.")
    st.session_state.etapa_cookie = True

elif resposta != "":
    st.error("Resposta incorreta. Tente novamente.")

if st.session_state.etapa_cookie:

    cookie = st.radio(
        "Você gostaria de um cookie hoje?",
        ["Sim! 😍", "Não, obrigado."]
    )

    if st.button("Confirmar escolha"):
        if cookie == "Sim! 😍":
            st.success("Então está certo! Me aguarde que receberá o seu produto pós aula. 🍪")
        else:
            st.write("Você não tem escolha, só estou testando a programação. Você vai receber seu cookie de qualquer maneira. Obrigado, beijos e tchau!")