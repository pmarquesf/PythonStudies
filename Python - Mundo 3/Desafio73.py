tupla = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Goiás', 'Botafogo', 'Santos', 'Bragantino', 'São Paulo', 'Fortaleza', 'Ceará SC', 'Coritiba', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude')

print(f'Libertadores: {tupla[0:6]}')
print(f'Zona de Rebaixamento: {tupla[-4:]}')
print(sorted(tupla))
print('São Paulo está na {} posição'.format(tupla.index('São Paulo')+1))