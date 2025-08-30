from faker import Faker

fake = Faker('pt_BR')

print("--- Gerando 5 usuários de teste com dados fictícios ---")
for i in range(5):
    nome = fake.name()
    email = fake.email()
    senha = fake.password(length=12)
    print(f"Usuário {i+1}: Nome='{nome}', Email='{email}', Senha='{senha}'")
print("-----------------------------------------------------")