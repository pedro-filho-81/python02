from time import sleep

print('\nA função sleep(número inteiro) suspende (atrasa) \na execução do programa  atual pelo número de segundos fornecido.')

print('\n\tÍnicio 5 segundos antes.')

print('\tsleep(5) #espera 5 segundos')

for i in range(5):
   print(f'\tcontando: {i + 1}')
   sleep(5)

print('\taparece depois de 5 segundos.')

print()
