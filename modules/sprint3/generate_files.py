import random
import pandas as pd
import modules.sprint3.constants as CONST

from datetime import date

def generate_data_to_csv(identificador):
    idade_atual = random.randint(12, 64) # Foco jovens e adultos com autismo 
    idade_descoberta = random.randint(0, idade_atual) 

    return {
        'id_paciente': identificador,
        'idade_atual': idade_atual, # Idade da pessoa autista
        'idade_descoberta': idade_descoberta, # Idade que descobriou o autismo
        'genero': random.choice(CONST.GENERO), # F-feminino | M-Masculino | (1 F a cada 4 M possui autismo)
        'grau': random.choice(CONST.GRAU),
        'sensibilidade_sentidos': random.choice([True, False]),
        'agressivo': random.choice([True, False]),
        'hiperativo': random.choice([True, False]),
        'movimentos_repetitivos': random.choice([True, False]),
        'baixa_concentracao': random.choice([True, False]),
        'hiperfoco': random.choice([True, False]),
        'necessidade_rotina': random.choice([True, False]),
        'dificuldade_imaginacao': random.choice([True, False]),
        'introvertido': random.choice([True, False]),
        'tipo_autismo': random.choice(CONST.TIPOS_AUTISMO).get('title'),
        'tipo_autismo_descricao': random.choice(CONST.TIPOS_AUTISMO).get('description')
    }
    
def generate_data_to_xml(identificador):
    nation =  random.choice(CONST.PAISES)
    region = random.choice(CONST.REGIOES)
    economia = region.get('economics')
    return {
        'identificador': identificador,
        'pais': nation.get('description'),
        'PIB_nacional': nation.get('economics').get('PIB'),
        'regiao': region.get('description'),
        'PIB_percent_BR': economia.get('PIB_percent_BR'),
        'PIB_regional': economia.get('PIB'),
        'populacao_regiao': economia.get('populacao'),
        'densidade_demografica_regiao':economia.get('densidade_demografica'),
        'area_regiao': economia.get('area'),
        # 'regiao_geoeconomica': economia.get('regiao_geoeconomica'), #apresenta um erro
        'gentilico_regiao': economia.get('gentilico'),
        'raca_predominante_regiao': economia.get('raca_predominante')
    }

def generate_data_to_json(identificador):
    classe = random.choice(CONST.CLASSES)
    total_salario = random.randrange(classe.get('minimo'), classe.get('maximo'))
    quantidade_familia = random.choice([1, 6])

    return {
        'id_paciente': identificador,
        'classe':classe.get('id'),
        'classe-descricao': classe.get('description'),
        'quantidade_familia':quantidade_familia,
        'total_salario': total_salario,
        'empregado': random.choice([True, False]),
        'per_capita': total_salario/quantidade_familia
    }

def generate_file_csv(data_list, file_date):
    path = f'data\\{file_date}-autismo_csv.csv'
    df = pd.DataFrame(data_list)
    df.to_csv(path, index=False)

def generate_file_xml(data_list, file_date):
    path = f'data\\{file_date}-autismo_xml.xml'
    df = pd.DataFrame(data_list)
    df.to_xml(path, index=False)

def generate_file_json(data_list, file_date):
    path = f'data\\{file_date}-autismo_json.json'
    df = pd.DataFrame(data_list)
    df.to_json(path, orient="records")

def execute(entradas):
    # -m - é o nome do module
    # -s - é o número de entradas
    # python main.py -m 'generate_files' -s 100_000

    data_atual = date.today().strftime('%d-%m-%Y')

    data_list_csv = []
    data_list_xml = []
    data_list_json = []

    for id in range(1, entradas):
        data_list_csv.append( generate_data_to_csv(identificador=id) ) 
        data_list_xml.append( generate_data_to_xml(identificador=id) )
        data_list_json.append( generate_data_to_json(identificador=id) )

    generate_file_csv(data_list_csv, data_atual)
    generate_file_xml(data_list_xml, data_atual)
    generate_file_json(data_list_json, data_atual)
