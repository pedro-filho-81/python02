from time import localtime

data = localtime()

print(f'\nPasso 01 -> data = localtime()\n{data}')

print('\nPasso 02 -> variáveis recebem valores da struct_time')

dia = data.tm_mday
mes = data.tm_mon
ano = data.tm_year

print("""
dia = data.tm_mday
mes = data.tm_mon
ano = data.tm_year
      """)

print('Passo 3 -> exibir a data de hoje e o horário.')

print(f'Data de hoje: {dia}/{mes}/{ano}')
print(f"Horas: {data.tm_hour}:{data.tm_min}:{data.tm_sec}")

print()
