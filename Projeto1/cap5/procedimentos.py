def saudacao(hora):
    if hora < 12:
        msg = "Bom dia."
    elif hora < 18:
        msg = "Boa tarde."
    else:
        msg = "Boa noite."
    print(msg, "Seja Bem-Vindoa FIAP!")

saudacao(20)