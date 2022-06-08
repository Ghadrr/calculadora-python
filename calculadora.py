from asyncio import sleep
from re import X
while True:    
        
    decisao=int(input('\nescolha a operação\n1 - adição\n2 - subtração\n3 - divisão\n4 - multiplicação\n5 - sair\nescolha: '))
    if decisao==5:
        print('finalizando...')
        break
    elif decisao > 5:
        print('\nvalor invalido...\nfinalizando...')    
        quit()
    elif decisao== 1 or 2 or 3 or 4:
        v1=float(input('insira o primeiro valor: '))
        v2=float(input('insira o segundo valor: '))
        
    if decisao==1:
        print(f'{v1} + {v2} = {v1+v2}')
        dec2=int(input('\n1 - fazer outra operação de adição\n2 - voltar para o menu inicial\nescolha: '))
        if dec2>2:
            print('----valor invalido----')            
        while dec2 == 1: 
            if dec2==1:
                v1=float(input('insira o primeiro valor: '))
                v2=float(input('insira o segundo valor: '))
                print(f'{v1} + {v2} = {v1+v2}')
                dec2=int(input('\n1 - fazer outra operação de adição\n2 - voltar para o menu inicial\nescolha: '))
                if dec2>2:
                    print('----valor invalido----')
    elif decisao==2:
        print(f'{v1} - {v2} = {v1-v2}')
        dec2=int(input('\n1 - fazer outra operação de subtração\n2 - voltar para o menu inicial\nescolha: '))
        if dec2>2:
            print('----valor invalido----')
        while dec2 == 1:  
            if dec2==1:                
                v1=float(input('insira o primeiro valor: '))
                v2=float(input('insira o segundo valor: '))
                print(f'{v1} - {v2} = {v1-v2}')
                dec2=int(input('\n1 - fazer outra operação de subtração\n2 - voltar para o menu inicial\nescolha: '))       
                if dec2>2:
                    print('----valor invalido----')
    
    elif decisao==3:
        print(f'{v1} / {v2} = {v1/v2}')
        dec2=int(input('\n1 - fazer outra operação de divisão\n2 - voltar para o menu inicial\nescolha: '))
        if dec2>2:
            print('----valor invalido----')
        while dec2 == 1:     
            if dec2==1:
                v1=float(input('insira o primeiro valor: '))
                v2=float(input('insira o segundo valor: '))
                print(f'{v1} / {v2} = {v1/v2}')
                dec2=int(input('\n1 - fazer outra operação de divisão\n2 - voltar para o menu inicial\nescolha: '))    
                if dec2>2:
                    print('----valor invalido----')
                    
    elif decisao==4:
        print(f'{v1} X {v2} = {v1*v2}')
        dec2=int(input('\n1 - fazer outra operação de multiplicação\n2 - voltar para o menu inicial\nescolha: '))    
        if dec2>2:
            print('----valor invalido----')
        while dec2 == 1:     
            if dec2==1:
                v1=float(input('insira o primeiro valor: '))
                v2=float(input('insira o segundo valor: '))
                print(f'{v1} X {v2} = {v1*v2}')
                dec2=int(input('\n1 - fazer outra operação de multiplicação\n2 - voltar para o menu inicial\nescolha: '))            
                if dec2>2:
                    print('----valor invalido----')
                