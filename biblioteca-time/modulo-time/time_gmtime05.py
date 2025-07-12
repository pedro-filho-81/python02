from time import gmtime, localtime

print('\nA função gmtime() recebe o número de segundos decorridos \ndesde a época EPOCH como argumento e retorna struct_time em UTC.')

hora_mundial = gmtime()
hora_local = localtime()

print(f'\n\thora_mundial = gmtime()\n{hora_mundial}')

print(f'\n\thora_local = localtime()\n{hora_local}')

print()
