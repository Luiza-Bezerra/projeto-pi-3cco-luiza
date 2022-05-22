import argparse
import csv

def parse_arguments() -> dict:
    parser = argparse.ArgumentParser(description='')

    parser.add_argument(
        '-s','--samples', 
        action = 'store', 
        dest = 'samples', 
        type=int,
        required = False,
        help = 'O número de amostras.'
    )

    parser.add_argument(
        '-m','--module', 
        required =True,
        help = 'Modulo que será executado execução.'
    )

    parser.add_argument(
        '-c','--config',
        dest='config',
        required =False,
        default= './local.json',
        help = 'Arquivo de configuração.'
    )

    parsed_args = vars(parser.parse_args())

    if len(parsed_args) > 0:
        return parsed_args
    else:
        raise ValueError('Argumentos inválidos!')

if __name__ == "__main__":
    args = parse_arguments()
    module = args['module'].lower()

    if module == 'generate1':
        from modules.sprint1 import execute
        execute(args["samples"]) 
    
    elif module == 'generate2':
        from modules.sprint2 import execute
        execute(args['config'])

    elif module == 'generate_csv':
        from modules.sprint3.generate_csv import execute
        execute(args["samples"])

    else:
        raise ValueError('Argumento inválido!')