
import streamlit as st

st.title("Quizz teste 🍪")

# Inicialização
if "etapa" not in st.session_state:
    st.session_state.etapa = 1

# ETAPA 1 - Nome

if st.session_state.etapa == 1:

    nome = st.text_input("Qual é o seu nome?").strip().lower()

    if nome = "":
        nomes = [
            "pamela", "pam", "pamelinha",
            "pamela matos", "pamela patricia",
            "paty", "pamela patricia de almeida matos",
            "pamelao"
        ]

        if nome in nomes:
            st.success("É você mesmo que eu procuro. Vamos continuar!")

            if st.button("Continuar"):
                st.session_state.etapa = 2
                st.rerun()

        else:
            st.error("Esse código não é pra você. Até mais. 😊")


# ETAPA 2 - Relacionamento

if st.session_state.etapa == 2:

    resposta = st.text_input("Você é o que do Paulo?").strip().lower()

    if resposta == "namorada":
        st.success("Muito bem, é isso mesmo!")

        if st.button("Próxima pergunta"):
            st.session_state.etapa = 3
            st.rerun()

    elif resposta == "ficante":
        st.write("Não é bem isso. Talvez por enquanto, mas vamos continuar.")

        if st.button("Próxima pergunta"):
            st.session_state.etapa = 3
            st.rerun()

    elif resposta != "":
        st.error("Repense sua resposta, Pamela.")


# ETAPA 3 - Cookie

if st.session_state.etapa == 3:

    cookie = st.radio(
        "Você gostaria de um cookie hoje?",
        ["Sim! 😍", "Não, obrigado."]
    )

    if st.button("Confirmar escolha"):

        if cookie == "Sim! 😍":
            st.success(
                "Então está certo! Me aguarde que receberá "
                "o seu produto pós aula. 🍪"
            )
        else:
            st.write("Você não tem escolha. Estou testando o código mesmo. Continue me aguardando após a aula.")

        st.session_state.etapa = 4


# ETAPA FINAL

if st.session_state.etapa == 4:
    st.balloons()
    st.title("Ihuuu! Cookie hoje ❤️")
