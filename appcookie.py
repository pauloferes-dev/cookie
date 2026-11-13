
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
            st.write("Não é bem isso, mas vamos continuar.")
            st.session_state.etapa_cookie = True

        else:
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
                st.write("Tudo bem, fica para a próxima!")

elif nome != "":
    st.write("Esse código não é pra você. Até mais. 😊")
