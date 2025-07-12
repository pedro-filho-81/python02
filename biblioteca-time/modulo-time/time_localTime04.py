from time import localtime

print('\nA função localtime() recebe o número de segundos decorridos \ndesde a época EPOCH como argumento e retorna struct_time\n(uma tupla contendo 9 elementos correspondentes a struct_time) \nou seja o horário local .')

hora_local = localtime()

print('\thora_local = localtime()')

print(f'\nExibe a estrutua da hora_local:\n{hora_local}')

print('\nAqui, se nenhum argumento ou None for passado para localtime(), \no valor retornado por time() será usado.')

print()
