# Import the time module
import time

# display
print('\nEm Python, a função time() retorna o número de segundos\ndecorridos desde a época (EPOCH) (dia 1/01/1970 às 00:00:00).')

# get the current time in seconds since the epoch
seconds = time.time  ()

print("\nseconds = time.time()\nSeconds since epoch =", seconds)	

print('\nNo exemplo acima, usamos a função time.time() \npara obter o tempo atual em segundos desde a época e, \nem seguida, imprimimos o resultado.')

# Output: Seconds since epoch = 1672214933.6804628

print()
