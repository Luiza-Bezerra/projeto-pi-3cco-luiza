# projeto-pi-3cco-luiza

# ___ Preparacao ______

    apt update
    apt upgrade
    apt install docker docker.io docker-compose net-tools
    systemctl start docker
    systemctl enable docker
    docker info
    usermod -a -G docker ubuntu
    docker --version
    docker-compose --version
    docker pull mysql:latest

    docker images mysql

    docker run --name banco_sprint_2 -p 3306:3306 -v mysql_volume:/var/lib/mysql/ -d -e "MYSQL_ROOT_PASSWORD=temp123" mysql

    docker exec -it banco_sprint_2 bash 

    docker cp bd_sprint_1.sql banco_sprint_2:/tmp
    docker cp bd_sprint_2.sql banco_sprint_2:/tmp

    source /tmp/bd_sprint_1.sql 
    source /tmp/bd_sprint_2.sql 

# ___ Rodar o projeto ______
    sudo su 
    ** User Root

    docker start 6e6

    cd projeto-pi-3cco-luiza

    source ./venv/bin/activate

    python generate_sprint_2.py

# ___ Rodar a sprint 3______
    Verificar se o terminal está na raiz do projeto : /projeto-pi-3cco-luiza
    utilizar ocomando : python main.py -m 'generate_files' -s 100_000 
    parametro -m é o modeulo a ser executado
    parametro -s é a quantidade de dados a ser gerado

# ___ Validar o banco ______

    docker exec -it banco_sprint_2 bash

    mysql -h localhost -P 3306 -u root -p
    ** password: temp123

    use algas_2;

    select * from dados;
