import time

def enviar_email_boas_vindas(email):
    print(f"Conectando ao servidor de e-mail REAL...")
    time.sleep(2)
    print(f"E-mail de boas-vindas enviado para {email}")
    return True