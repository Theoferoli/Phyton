while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha != usuario:
        print("Cadastro realizado com sucesso!")
        break
    print("Erro: A senha não pode ser igual ao nome de usuário.")
