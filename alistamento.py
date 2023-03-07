from datetime import date
atual = date.today().year
sexo = input('Qual seu sexo? (Digite F para Feminino ou M para Masculino) ')
if sexo == 'F':
    print('Você não precisa se alistar')
    exit();
elif sexo == 'M':
    print('Siga para o próximo passo')

ano1 = int(input('Qual seu ano de nascimento? '))
idade = (atual - ano1)
print(f'Sua idade é {atual - ano1}')
alistamento = 18
if idade > alistamento:
    saldo1 = idade - 18
    print(f'Você não se alistou, você deveria ter se alistado há {saldo1} anos')
elif idade == alistamento:
        print('Corra para se alistar')
elif idade < alistamento:
    saldo = 18 - idade
    print(f'Você ainda não precisa se alistar, somente daqui {saldo} anos')
