
import streamlit as st

st.title("Quizz teste.")

nome = st.text_input("Qual é o seu nome?").strip().lower()

if nome in ["pamela", "pam", "pamelinha"]:

    st.write("É você mesmo que eu procuro. Vamos continuar.")

    resposta = st.text_input("Você é o que do Paulo?").strip().lower()

    if resposta == "namorada":
        st.write("Muito bem, é isso mesmo!")

    elif resposta == "ficante":
        st.write("Não é bem isso, mas vamos continuar.")

    elif resposta != "":
        st.write("Está errado, repense suas respostas.")

    cookie = st.radio(
        "Você gostaria de um cookie hoje?",
        ["Sim! 😍", "Não, obrigado."]
    )

    if cookie == "Sim! 😍":
        st.write("Então temos um encontro marcado! 🍪")
    else:
        st.write("Tudo bem, fica para a próxima!")

elif nome != "":
    st.write("Esse código não é pra você. Até mais. 😊")
