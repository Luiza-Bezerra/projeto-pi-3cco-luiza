PAISES = [
    {
        'id':'BR',
        'description':'Brasil',
        'economics': {
            'PIB': 8_700_000_000_000,
            'populacao': 212_600_000,
            'densidade_demografica': 23.8,
            'area': 3_853_676_948,
            'regioes_geoeconomicas': ['Amazônia', 'Nordeste', 'Centro-Sul'],
            'gentilico': 'brasileiro'
        }
    },

]

REGIOES = [
    {
        'id':'S',
        'description':'Sul',
        'economics': {
            'PIB_percent_BR': 16.4,
            'PIB': 1_195_000_000_000,
            'populacao': 30_192_315,
            'densidade_demografica': 48.8,
            'area':  576_736_819,
            'regiao_geoeconomica': 'Centro-Sul',
            'gentilico': 'sulista',
            'raca_predominante': 'branca'
        }
    },
    {
        'id':'N',
        'description':'Norte',
        'economics': {
            'PIB_percent_BR': 5.3,
            'PIB': 1_195_000_000_000,
            'populacao': 18_672_591,
            'densidade_demografica': 4.12,
            'area': 3_853_676_948,
            'regiao_geoeconomica': 'Amazônia',
            'gentilico': 'nortista',
            'raca_predominante': 'parda'
        }
    },
    {
        'id':'SE',
        'description':'Sudeste',
        'economics': {
            'PIB_percent_BR': 55.9,
            'PIB': 3_460_000_000_000, 
            'populacao': 89_632_912,
            'densidade_demografica': 96.94,
            'area':  924_620_678,
            'regiao_geoeconomica': 'Centro-Sul',
            'gentilico': 'sudestino',
            'raca_predominante': 'branca'
        }
    },
    {
        'id':'NE',
        'description':'Nordeste',
        'economics': {
            'PIB_percent_BR': 13.9,
            'PIB': 15_779_110,
            'populacao': 56_560_081,
            'densidade_demografica': 36.06,
            'area':  576_736_819,
            'regiao_geoeconomica':['Amazônia','Nordeste'],
            'gentilico': 'nordestino',
            'raca_predominante': 'parda'
        }
    },
    {
        'id':'CO',
        'description':'Centro-Oeste',
        'economics': {
            'PIB_percent_BR': 9.4,
            'PIB': 542_632_000_000,
            'populacao': 16_090_000,
            'densidade_demografica': 8.7,
            'area': 1_612_000,
            'regiao_geoeconomica':['Amazônia', 'Centro-Sul'],
            'gentilico': 'centro-oestino',
            'raca_predominante': 'parda'
        }
    },
]

CLASSES = [
    {'id':'F', 'description':'Vulnerável', 'minimo': 324, 'maximo': 1764},
    {'id':'E', 'description':'Baixa classe media', 'minimo': 1764, 'maximo': 2564},
    {'id':'D', 'description':'Media classe media', 'minimo': 2564, 'maximo': 4076},
    {'id':'C', 'description':'Alta classe media','minimo': 4076, 'maximo':9920},
    {'id':'B', 'description':'Baixa classe alta','minimo': 9920, 'maximo': 10_000},
    {'id':'A', 'description':'Alta classe alta','minimo': 10_000, 'maximo':22_000},
]

GRAU = ['leve', 'moderado', 'severo']

GENERO = ['M','M','M','M','F']

RACA = [
    {'id':1,'description':'Branca'},
    {'id':2,'description':'Preta'},
    {'id':3,'description':'Parda'},
    {'id':4,'description':'Indigena'},
    {'id':5,'description':'Amarela'}
]

TIPOS_AUTISMO = [
    {
        'id':1, 
        'title': 'Sindrome de Asperger', 
        'description':'Está extremidade mais branda do espectro autista, pois a inteligência pode ser alta e a capacidade de realizar as atividades diárias é preservada. No entanto, a dificuldade na interação social é muito comum.'
    },
    {
        'id':2, 
        'title': 'Transtorno invasivo do desenvolvimento', 
        'description':'Esse diagnóstico incluía a maioria das crianças com autismo mais grave do que a síndrome de Asperger, mas não tão grave quanto o transtorno autista.'
    },
    {
        'id':3, 
        'title': 'Transtorno desintegrativo da infância', 
        'description':'Esse era o diagnóstico para os casos mais graves do espectro — crianças que se desenvolvem normalmente e depois perdem as habilidades sociais, de linguagem e cognitivas, geralmente entre 2 e 4 anos. '
    },
    {
        'id':4, 
        'title': 'Transtorno do espectro Autista (TEA)', 
        'description':'TEA é agora o termo genérico para o grupo de transtornos de neurodesenvolvimento complexos que constituem o autismo. Os sintomas do autismo costumam estar presentes desde a primeira infância e podem afetar o funcionamento diário. Os sintomas do TEA geralmente aparecem nos primeiros 2 anos de vida.'
    }
]

