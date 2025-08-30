import email_service

def cadastrar_usuario(nome, email, senha):

    if not nome or not email or not senha:
        return False

    print(f"Cadastrando o usuário '{nome}' no banco de dados...")

    email_foi_enviado = email_service.enviar_email_boas_vindas(email)

    if email_foi_enviado:
        print("Cadastro finalizado com sucesso, e-mail enviado!")
    else:
        print("Usuário cadastrado, mas houve uma falha ao enviar o e-mail de boas-vindas.")

    return True