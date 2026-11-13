import streamlit as st

st.title("Quizz teste.")

nome = st.text_input("Qual é o seu nome?").strip().lower()

if nome:
    if nome in ["pamela", "pamela patricia", "pamela matos", "pamelinha", "paty","pam", "pamela patricia de almeida matos"]:
                st.write("É você mesmo que eu procuro. Vamos continuar.")
    else:
        st.write("Esse código não é pra você. Até mais. 😊")

resposta = st.text_imput("Você é o que do Paulo?").strip().lower()

	if resposta:
		if resposta == "namorada":
			st.write("Muito bem, é isso mesmo!")
		elif resposta == "ficante":
			st.write("Não é bem isso, mas vamos continuar.")
		else:
			st.write("Está errado, repense suas respostas.")

convite = st.text_imput("O Paulo gostaria de te fazer um convite")
cookie = st.radio(
    "Você gostaria de ganhar um cookie hoje saindo da faculdade?",
    ["Sim! 😍", "Não, obrigado."]
)

if cookie == "Sim! 😍":
    st.write("Então é só aguardar, que assim será feito! 🍪")
else:
    st.write("Tudo bem, fica para a próxima!")
