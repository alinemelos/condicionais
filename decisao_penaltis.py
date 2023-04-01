time1 = str(input())
time2 = str(input())
gol1 = 0
gol2 = 0
verdade = 0
resto1 = 0
resto2 = 0
#chute 1
entrada1 = str(input())
entrada2  = str(input())
#chute 2
entrada3 = str(input())
entrada4  = str(input())
#chute 3
entrada5 = str(input())
entrada6  = str(input())
#chute 1
if entrada1 == 'Gol' and entrada2 == 'Gol':
    gol1 += 1
    gol2 += 1
    resto1 += 1
    resto2 += 1
elif entrada1  == 'Gol' and entrada2 != 'Gol' :
    gol1  += 1
    resto1 += 1
    resto2 += 1
elif entrada1 != 'Gol' and entrada2 == 'Gol' :
    gol2 += 1
    resto1 += 1
    resto2 += 1
elif entrada1 != 'Gol' and entrada2 != 'Gol' :
    resto1 += 1
    resto2 += 1
#chute 2
if entrada3 == 'Gol'and entrada4 == 'Gol' :
    gol1 += 1
    gol2 += 1
    resto1 += 1
    resto2 += 1
elif entrada3  == 'Gol' and entrada4 != 'Gol' :
    gol1  += 1
    resto1 += 1
    resto2 += 1
elif entrada3 != 'Gol' and entrada4 == 'Gol' :
    gol2 += 1
    resto1 += 1
    resto2 += 1
elif entrada3 != 'Gol' and entrada4 != 'Gol' :
    resto1 += 1
    resto2 += 1
#chute 3
if entrada5 == 'Gol' and entrada6 == 'Gol' :
    gol1 += 1
    gol2 += 1
    resto1 += 1
    resto2 += 1
elif entrada5  == 'Gol' and entrada6 != 'Gol' :
    gol1  += 1
    resto1 += 1
    resto2 += 1
elif entrada5 != 'Gol' and entrada6 == 'Gol' :
    gol2 += 1
    resto1 += 1
    resto2 += 1
elif entrada5 != 'Gol' and entrada6 != 'Gol' :
    resto1 += 1
    resto2 += 1
#acaba o jogo?
if gol1 > gol2 + (5 - resto2) :
    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
elif gol2 > gol1 + (5 - resto1) :
    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
else :
    entrada7 = str(input())
    resto1 += 1
    if entrada7 == 'Gol' :
        gol1 += 1
        if gol1 > gol2 + (5 - resto2) :
            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
            verdade = 0
        elif gol2 > gol1 + (5 - resto1) :
            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
            verdade = 0
        else :
            verdade = 1
            entrada8 = str(input())
            resto2 += 1
            if entrada8 == 'Gol' :
                gol2 += 1
                if gol1 > gol2 + (5 - resto2) :
                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                    verdade = 0
                elif gol2 > gol1 + (5 - resto1) :
                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                    verdade = 0
                else :
                    entrada9 = str(input())
                    resto1 += 1
                    if entrada9 == 'Gol' :
                        gol1 += 1
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                    elif entrada9 != 'Gol':
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
            elif entrada8 != 'Gol' :
                resto2 += 1
                if gol1 > gol2 + (5 - resto2) :
                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                    verdade = 0
                elif gol2 > gol1 + (5 - resto1) :
                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                    verdade = 0
                else :
                    entrada9= str(input())
                    resto1 += 1
                    if entrada9 == 'Gol' :
                        gol1 += 1
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                    elif entrada9 != 'Gol' :
                        if gol1 > gol2 + (5 - resto2) :
                                print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
    elif entrada7 != 'Gol' or verdade == 1:
        if gol1 > gol2 + (5 - resto2) :
            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
            verdade = 0
        elif gol2 > gol1 + (5 - resto1) :
            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
            verdade = 0
        else :
            entrada8 = str(input())
            resto2 += 1
            if entrada8 == 'Gol' :
                gol2 += 1
                if gol1 > gol2 + (5 - resto2) :
                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                    verdade = 0
                elif gol2 > gol1 + (5 - resto1) :
                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                    verdade = 0
                else :
                    entrada9 = str(input())
                    resto1 += 1
                    if entrada9 == 'Gol' :
                        gol1 += 1
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                    elif entrada9 != 'Gol' or verdade == 4 :
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else:
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
            elif entrada8 != 'Gol' :
                if gol1 > gol2 + (5 - resto2) :
                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                    verdade = 0
                elif gol2 > gol1 + (5 - resto1) :
                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                    verdade = 0
                else :
                    entrada9 = str(input())
                    resto1 += 1
                    if entrada9 == 'Gol' :
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                    elif entrada9 != 'Gol' :
                        if gol1 > gol2 + (5 - resto2) :
                            print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                            verdade = 0
                        elif gol2 > gol1 + (5 - resto1) :
                            print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                            verdade = 0
                        else :
                            entrada10 = str(input())
                            resto2 += 1
                            if entrada10 == 'Gol' :
                                gol2 += 1
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')
                            elif entrada10 != 'Gol' :
                                if gol1 > gol2 + (5 - resto2) :
                                    print(f'{time1} vence a disputa de pênaltis por {gol1} a {gol2} e avança de fase!')
                                    verdade = 0
                                elif gol2 > gol1 + (5 - resto1) :
                                    print(f'{time2} vence a disputa de pênaltis por {gol2} a {gol1} e avança de fase!')
                                    verdade = 0
                                elif gol1 == gol2 :
                                    print(f'Ambas as seleções terminaram com {gol1} gols, mas o desempate vai ficar para outro dia.')