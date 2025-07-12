# import the time module
import time
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

print('\nA função time.ctime() recebe os segundos passados ​​desde a EPOCH \ncomo argumento e retorna uma string representando a hora local.')

seconds = time.ctime()
print('\n\tseconds = time.ctime()')

# print local time
print(f'Em seguida imprimimos o valor de seconds:\n\tseconds2 = {seconds}\n')

print('Usamos a função time.ctime() para converter o tempo em segundos \ndesde a época EPOCH para um formato legível STRING \ne, então, imprimimos o resultado.')

print()