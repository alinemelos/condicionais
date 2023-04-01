nomeA = str(input())
ataqueA = int(input())
defesaA = int(input())
folegoA = int(input())

nomeB = str(input())
ataqueB = int(input())
defesaB = int(input())
folegoB = int(input())

sorte_1 = int(input())
sorte_2 = int(input())
sorte_3 = int(input())
sorte_4 = int(input())

golA = 0
golB = 0
proximo = ''
fator_canseira_A = 1 - ((5 - folegoA)/10)
fator_canseira_B = 1 - ((5 - folegoB)/10)

ataque_a_cansado2 = 0
defesa_a_cansado2 = 0
ataque_b_cansado2 = 0
defesa_b_cansado2 = 0
ataque_a_cansado3 = 0
defesa_a_cansado3 = 0
ataque_a_cansado4 = 0
defesa_a_cansado4 = 0
ataque_b_cansado4 = 0
defesa_b_cansado4 = 0


print('Início de jogo!')
# turno 1
print('1° tempo:')
print(f'{nomeA} [{golA}-{golB}] {nomeB}')
#time A atacando
print(f'O time {nomeA} vem pressionando.')
if sorte_1  == 1 :
    novo_ataque_a = ataqueA + 2
    if novo_ataque_a >= defesaB :
        golA += 1
        print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeA}!!!')
        proximo = 'true'
    elif defesaB > novo_ataque_a :
        print(f'O ataque é interrompido! Ótima defesa do time {nomeB}')
        proximo = 'true'
elif sorte_1 == 2 :
    novo_defesa_b = defesaB + 2
    if ataqueA >= novo_defesa_b :
        golA += 1
        print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeA}!!!')
        proximo = 'true'
    elif novo_defesa_b > ataqueA :
        print(f'O ataque é interrompido! Ótima defesa do time {nomeB}')
        proximo = 'true'
# turno 2
# time B atacando
ataque_a_cansado2 = ataqueA * fator_canseira_A
defesa_a_cansado2 = defesaA * fator_canseira_A
ataque_b_cansado2 = ataqueB * fator_canseira_B
defesa_b_cansado2 = defesaB * fator_canseira_B
print(f'O time {nomeB} vem pressionando.')
if proximo == 'true' :
    if sorte_2  == 1 :
        novo_ataque_b2 = ataque_b_cansado2 + 2
        if novo_ataque_b2 >= defesa_a_cansado2 :
            golB += 1
            print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeB}!!!')
            proximo = 'true'
        elif defesa_a_cansado2 > novo_ataque_b2 :
            print(f'O ataque é interrompido! Ótima defesa do time {nomeA}')
            proximo = 'true'
    elif sorte_2 == 2 :
        novo_defesa_a2 = defesa_a_cansado2 + 2
        if ataque_b_cansado2 >= novo_defesa_a2 :
            golB += 1
            print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeB}!!!')
            proximo = 'true'
        elif novo_defesa_a2 > ataque_b_cansado2 :
            print(f'O ataque é interrompido! Ótima defesa do time {nomeA}')
            proximo = 'true'

# turno 3
print('2° tempo:')
print(f'{nomeA} [{golA}-{golB}] {nomeB}')
# time B atacando
print(f'O time {nomeB} vem pressionando.')
ataque_a_cansado3 = ataque_a_cansado2 * fator_canseira_A
defesa_a_cansado3 = defesa_a_cansado2 * fator_canseira_A
ataque_b_cansado3 = ataque_b_cansado2 * fator_canseira_B
defesa_b_cansado3 = defesa_b_cansado2 * fator_canseira_B
if proximo == 'true' :
    if sorte_3  == 1 :
        novo_ataque_b3 = ataque_b_cansado3 + 2
        if novo_ataque_b3 >= defesa_a_cansado3 :
            golB += 1
            print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeB}!!!')
            proximo = 'true'
        elif defesa_a_cansado3 > novo_ataque_b3 :
            print(f'O ataque é interrompido! Ótima defesa do time {nomeA}')
            proximo = 'true'
    elif sorte_3 == 2 :
        novo_defesa_a3 = defesa_a_cansado3 + 2
        if ataque_b_cansado3 >= novo_defesa_a3 :
            golB += 1
            print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeB}!!!')
            proximo = 'true'
        elif novo_defesa_a3 > ataque_b_cansado3 :
            print(f'O ataque é interrompido! Ótima defesa do time {nomeA}')
            proximo = 'true'

# turno 4
# time A atacando
ataque_a_cansado4 = ataque_a_cansado3 * fator_canseira_A
defesa_a_cansado4 = defesa_a_cansado3 * fator_canseira_A
ataque_b_cansado4 = ataque_b_cansado3 * fator_canseira_B
defesa_b_cansado4 = defesa_b_cansado3 * fator_canseira_B
print(f'O time {nomeA} vem pressionando.')
if proximo == 'true' :
    if sorte_4  == 1 :
        novo_ataque_a4 = ataque_a_cansado4 + 2
        if novo_ataque_a4 >= defesa_b_cansado4 :
            golA += 1
            print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeA}!!!')
            proximo = 'true'
        elif defesa_b_cansado4 > novo_ataque_a4 :
            print(f'O ataque é interrompido! Ótima defesa do time {nomeB}')
            proximo = 'true'
    elif sorte_4 == 2 :
        novo_defesa_b4 = defesa_b_cansado4 + 2
        if ataque_a_cansado4 >= novo_defesa_b4 :
            golA += 1
            print(f'GOOOOOOOOOOOOLLLLLL DO TIME {nomeA}!!!')
            proximo = 'true'
        elif novo_defesa_b4 > ataque_a_cansado4 :
            print(f'O ataque é interrompido! Ótima defesa do time {nomeB}')
            proximo = 'true'

if golA == golB :
    print(f'{nomeA} [{golA}-{golB}] {nomeB}')
    print('Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!')
elif  golA > golB :
    print(f'{nomeA} [{golA}-{golB}] {nomeB}')
    print(f'ACABOOOOU!! O TIME {nomeA} É O CAMPEÃO!!!')
elif golB > golA :
    print(f'{nomeA} [{golA}-{golB}] {nomeB}')
    print(f'Fim de jogo! O time {nomeB} é campeão.')