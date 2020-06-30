#!/bin/bash
# Automação do processo de deployment docker All in One
# Automation Team - Jabil Belo
# Outubro de 2019

bold=$(tput bold)
normal=$(tput sgr0)

image_name="docker.corp.jabil.org/automation-bel/aio:beta"
hostname="BRBELRASP124"
dns_search="corp.jabil.org"
volume="/run/dbus:/host/run/dbus"

# Docker build
printf "\n${bold}Realizando build da imagem beta do All in One${normal}\n"
printf "${image_name}\n\n"
docker image build -t ${image_name} .


# Docker run
printf "\n${bold}Executando container beta do All in One${normal}\n"
printf "  - privileged\n  - hostname: ${hostname}\n  - dns_search: ${dns_search}\n  - volumes:\n    - ${volume}\n\n"

if read -r -s -n 1 -t 5 -p "Ao mudar de tty, pressione ${bold}Ctrl+Alt+F7${normal} para retornar, para continuar pressione qualquer tecla em 20 segundos" key 
then
    printf "\nScript encerrado\n\n"
else
    echo ""
    docker run --privileged -p 6080:80 --hostname=${hostname} --dns-search=${dns_search} --volume=${volume} ${image_name} 
fi


