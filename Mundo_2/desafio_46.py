# Contagem regressiva

from time import sleep

for i in range(10, -1, -1):
    print(f'\33[1;36;40m{i:^5}\33[m')
    sleep(0.5)

print('\33[1;33;40mFELIZ ANO NOVO!!!\33[m')
