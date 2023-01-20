cidade = input('Digite uma cidade: ').strip()

cidade = cidade.upper();

if(cidade.find('SANTO')==0):
    print('A sua cidade começa com Santo')
else:
    print('Não começa com Santo')

# FORMA ALTERNATIVA

print(cidade[0:5] == 'SANTO')

