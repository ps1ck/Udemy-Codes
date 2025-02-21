user = input('Digite seu usuário: ')
senha = input('Digite a senha: ')

if user == 'admin' and senha == '123456':
    print('Login OK!')
else:
    print('Usuário ou senha incorretos.')
