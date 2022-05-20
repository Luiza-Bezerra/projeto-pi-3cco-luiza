import random

import constants as CONST

def geracao(entradas):
    data_list = []
    for i in range(1, entradas):
        idade_atual = random.randint(17,64) # Foco jovens e adultos com autismo 
        idade_descoberta = random.randint(0,idade_atual) 


        data_list.append({
            'id_pacinte': i,
            'idade_atual': idade_atual, # Idade da pessoa autista
            'genero': random.choice(['M','M','M','M','F']), # F-feminino | M-Masculino | (1 F a cada 4 M possui autismo)
            'regiao': random.choice(), # Regiões do Brasil
            'idade_descoberta': idade_descoberta, # Idade que descobriou o autismo
        })

"""
identificador	int
grau	alto, medio, baixo
raca	str
genero	M , F
idade_diagnostico	int
idade 	int
sensibilidade_sentidos	bool
agressivo	bool
hiperativo	bool
passivo	bool
baixa_concentracao	bool
movimentos_repetitivos	bool
hiperfoco	bool
agorafobia	bool
introvertido	bool
data de coleta	date
tipo_autismo	string
"""'