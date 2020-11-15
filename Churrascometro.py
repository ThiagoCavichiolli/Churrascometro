def pacote(f,l,p):
    """
    Define o pacote (items) escolhido pelo cliente
    :param f: Se o cliente deseja frango
    :param l: Se o cliente deseja linguica
    :param p: Se o cliente deseja pao de alho
    :return: n = numero do pacote
    """
    if f and l and p == 'S':
        n = 1
    if f and p == 'S' and l == 'N':
        n = 2
    if l and f == 'S' and p == 'N':
        n = 3
    if l and p == 'S' and f == 'N':
        n = 4
    if l == 'S' and f and p == 'N':
        n = 5
    if f == 'S' and l and p == 'N':
        n = 6
    return n

def items(escolha):
    """
    Calcula a quantidade de items do pacote escolhido
    :param escolha: numero do pacote
    :return: nada
    """
    carne = frango = linguica = pao_alho = 0
    if escolha == 1:
        carne = (adultos + criancas) * 0.1
        frango = (adultos + criancas) * 0.1
        linguica = (adultos + criancas) * 0.1
        pao_alho = (adultos + criancas) * 0.1
    if escolha == 2:
        linguica = 0
        carne = (adultos + criancas) * 0.2
        frango = (adultos + criancas) * 0.15
        pao_alho = (adultos + criancas) * 0.15
    if escolha == 3:
        carne = (adultos + criancas) * 0.2
        linguica = (adultos + criancas) * 0.15
        frango = (adultos + criancas) * 0.15
        pao_alho = 0
    if escolha == 4:
        carne = (adultos + criancas) * 0.2
        linguica = (adultos + criancas) * 0.15
        pao_alho = (adultos + criancas) * 0.15
        frango = 0
    if escolha == 5:
        carne = (adultos + criancas) * 0.4
        linguica = (adultos + criancas) * 0.25
        pao_alho = 0
        frango = 0
    if escolha == 5:
        carne = (adultos + criancas) * 0.4
        linguica = 0
        pao_alho = 0
        frango = (adultos + criancas) * 0.25
    total_carnes = carne + frango + linguica + pao_alho
    carvao = total_carnes/2
    print(f'\033[0:30:44mCom {adultos + criancas} pessoas sera necessario comprar: \033[m')
    print(f'\033[0:30:44m{carne:.2f}kg de carne, {frango:.2f}kg de frango, {linguica:.2f}kg de linguica, {pao_alho:.2f}kg de pao de alho.\033[m')
    print(f'\033[0:30:44m{cerveja:.2f} litros de cerveja e {refri:.2f} litros de refrigerante.\033[m')
    print(f'\033[0:30:44m{carvao:.1f}kg de carvao.\033[m')


print('-=' * 20)
print('           Churrascometro!')
print('-=' * 20)
adultos=int(input('Quantos adultos estarao no churrasco? '))
while adultos not in range (0,1000):
    print('Entrada invalida! Tente novamente')
    adultos = int(input('Quantos adultos estarao no churrasco? '))
criancas =int(input('Quantas criancas estarao no churrasco? '))
while criancas not in range(0,1000):
    print('Entrada invalida! Tente novamente')
    criancas = int(input('Quantas criancas estarao no churrasco? '))
adultos_bebem =int(input('Quantos adultos consomem cerveja? '))
while adultos_bebem not in range (0,1000):
    print('Entrada invalida! Tente novamente')
    adultos_bebem = int(input('Quantos adultos consomem cerveja? '))
f = str(input('Churrasco tera frango? [S/N] ')).upper().strip()
while f not in 'SN':
    print('Entrada invalida! Tente novamente')
    f = str(input('Churrasco tera frango? [S/N] ')).upper().strip()
l = str(input('Churrasco tera linguica? [S/N] ')).upper().strip()
while l not in 'SN':
    print('Entrada invalida! Tente novamente')
    l = str(input('Churrasco tera linguica? [S/N] ')).upper().strip()
p = str(input('Churrasco tera pao de alho? [S/N] ')).upper().strip()
while p not in 'SN':
    print('Entrada invalida! Tente novamente')
    p = str(input('Churrasco tera pao de alho? [S/N] ')).upper().strip()
cerveja = adultos_bebem * 0.35 * 8
refri = ((adultos - adultos_bebem) + criancas) * 0.6

pacote(f,l,p)
items(pacote(f,l,p))
