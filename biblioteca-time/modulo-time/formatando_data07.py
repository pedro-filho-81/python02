from time import strftime, localtime

print("\nFORmATANDO DATAS")

print('A função strftime() recebe a struct_time como argumento \ne retorna uma string que o representa com base \nno código de formato utilizado.\nPor exemplo:')

print('\nPrimeiro, importamos a biblioteca time.\n\tfrom time import strftime, localtime\nSegundo, atribuimos localtime a uma variável:\n\ttempo_locala = localtime()')

print('Terceiro, em outra variável atribuimos strftime():\n\ttempo_string = strftime(\'%d %m %Y\', tempo_local)')

print('Quarto, exibimos o conteudo formatado:\n\tprint("hoje são: {tempo_string})')

tempo_local = localtime() # get struct_time

tempo_string = strftime('%d %m %Y', tempo_local) 

print(strftime("\thoje são: %d/%m/%y", tempo_local))

print()
