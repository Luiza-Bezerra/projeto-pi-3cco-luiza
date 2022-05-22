import random
import pandas as pd
import modules.sprint3.constants as CONST

def generate_data_to_csv(identificador):
    idade_atual = random.randint(12, 64) # Foco jovens e adultos com autismo 
    idade_descoberta = random.randint(0, idade_atual) 

    return {
        'id_paciente': identificador,
        'idade_atual': idade_atual, # Idade da pessoa autista
        'idade_descoberta': idade_descoberta, # Idade que descobriou o autismo
        'genero': random.choice(['M','M','M','M','F']), # F-feminino | M-Masculino | (1 F a cada 4 M possui autismo)
        'grau': random.choice(['leve', 'moderado', 'severo']),
        'sensibilidade_sentidos': random.choice([True, False]),
        'agressivo': random.choice([True, False]),
        'hiperativo': random.choice([True, False]),
        'movimentos_repetitivos': random.choice([True, False]),
        'baixa_concentracao': random.choice([True, False]),
        'hiperfoco': random.choice([True, False]),
        'necessidade_rotina': random.choice([True, False]),
        'dificuldade_imaginacao': random.choice([True, False]),
        'introvertido': random.choice([True, False]),
        'tipo_autismo': random.choice(CONST.TIPOS_AUTISMO)
    }
    
def generate_data_to_xml(identificador):
    return {
        'identificador': identificador,
        'pais': identificador,
        'regiao': random.choice(CONST.REGIOES)
    }

def generate_data_to_json(identificador):
    return {
        'id_paciente': identificador,
        'classe': random.choice(['A', 'B', 'C', 'D', 'E']),
        'quantidade_familia': random.choice([1, 6]),
        'total_salario': random.randrange(1_212, 10_000),
        'empregado': random.choice([True, False])
    }

def generate_file_csv(data_list):
    df = pd.DataFrame(data_list)
    df.to_csv('modules\sprint3\data\\autismo_csv.csv', index=False)

def generate_file_xml(data_list):
    df = pd.DataFrame(data_list)
    df.to_xml('modules\sprint3\data\\autismo_xml.xml', index=False)

def generate_file_json(data_list):
    df = pd.DataFrame(data_list)
    df.to_json('modules\sprint3\data\\autismo_json.json', orient="records")

def execute(entradas):
    # -m - é o nome do module
    # -s - é o número de entradas
    # python main.py -m 'generate_csv' -s 10
    
    data_list_csv = []
    data_list_xml = []
    data_list_json = []

    for id in range(1, entradas):
        data_list_csv.append(generate_data_to_csv(identificador=id))
        data_list_xml.append(generate_data_to_xml(identificador=id))
        data_list_json.append(generate_data_to_json(identificador=id))

    generate_file_csv(data_list_csv)
    generate_file_xml(data_list_xml)
    generate_file_json(data_list_json)
