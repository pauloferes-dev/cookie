if nome:
    if nome in ["pamela", "pamela patricia", "pamela matos", "pamelinha", "paty", "pam"]:
        st.write("É você mesmo que eu procuro. Vamos continuar.")

        resposta = st.text_input("Você é o que do Paulo?").strip().lower()

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
