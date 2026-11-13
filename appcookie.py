
import streamlit as st

st.title("Quizz teste 🍪")

# Inicialização das etapas
if "nome_validado" not in st.session_state:
    st.session_state.nome_validado = False

if "etapa_cookie" not in st.session_state:
    st.session_state.etapa_cookie = False

if "finalizado" not in st.session_state:
    st.session_state.finalizado = False


# ETAPA 1 - Perguntar o nome

if not st.session_state.nome_validado:

    nome = st.text_input("Qual é o seu nome?").strip().lower()

    if nome != "":

        if nome in [
            "pamela",
            "pam",
            "pamelinha",
            "pamela matos",
            "pamela patricia",
            "paty",
            "pamela patricia de almeida matos",
            "pamelao"
        ]:

            st.session_state.nome_validado = True
            st.rerun()

        else:
            st.error("Esse código não é pra você. Até mais. 😊")


# ETAPA 2 - Perguntar o relacionamento

if st.session_state.nome_validado and not st.session_state.etapa_cookie:

    st.success("É você mesmo que eu procuro. Vamos continuar!")

    resposta = st.text_input("Você é o que do Paulo?").strip().lower()

    if resposta == "namorada":

        st.success("Muito bem, é isso mesmo!")
        st.session_state.etapa_cookie = True
        st.rerun()

    elif resposta == "ficante":

        st.write("Não é bem isso. Talvez por enquanto sim, mas vamos continuar.")
        st.session_state.etapa_cookie = True
        st.rerun()

    elif resposta != "":

        st.error("Repense sua resposta, Pamela.")


# ETAPA 3 - Pergunta do cookie

if st.session_state.etapa_cookie and not st.session_state.finalizado:

    st.success("Vamos continuar!")

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

        st.session_state.finalizado = True


# ETAPA FINAL

if st.session_state.finalizado:

    st.balloons()
    st.title("Ihuuu! Cookie hoje ❤️")
