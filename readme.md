﻿# All in One - v1.11.0
* nova base image no dockerfile
* FROM docker.corp.jabil.org/raspberry-pi/xwindow
* boas ideias ligado ativado

# All in One - v1.07 1.08 1.09
* Código de ambiente de testes e produção integrados, agora funciona no Rasp e no Windows sem precisar mudar nada
* Full Paper Less - versão inicial
* Hostname buscado a partir do volume caso o request falhe
* botões da sidebar gerados a partir das tags
* classe/arquivo espcífica para login 
* Botões padronizados e responsivos
* correção de bugs
* correção erro ao não encontrar hostname não ligava
* inversão da ordem de login - tela aparece primeiro e informações são carregadas depois
* product name e client são preenchidos na hora do login

# All in One - v1.06a
* correcao temporaria demora do login e boot (jit suporte temporariamente desativado) 

# All in One - v1.05
* nao sei, perdemos

# All in One - v1.04
* Tratamento do erro que acontecia quando o posto não estava cadastrado no e-station e consequentemente não deixava o AIO iniciar
* Mural de anuncios
* POC do JIT support - versão inicial

# All in One - v1.03
* colocar imagens sipat na tela principal

# All in One - v1.02
* Nova tela de login implementada

# All in One - v1.01
* fim da necessidade de alterar hostname no compose.yml

# All in One - v1.00
* Tela principal nova implementada
* resources novos
* reestruturação do código
* código parcialmente compatível com Raspberry e windows
* nova janela e funcionalidades 5s
* resolução do erro que a tela travava na tela de ficha de instrução
* correção de bugs

# All in One - v47
## Features 
* Containerizado;
* Baseado na imagem base: docker.corp.jabil.org/devservices/rpi3-xwindow:strech-1.1.0-alpha
* Leitura de crachás via SPI.
* Botões de: Boas ideias, FI, Listar ferramentais, LPA.
* Metrics implementados: Yield, Produtividade.

## [NEW on V35]
* Remoção dos prints de debug da leitura de crachá. 

## [NEW on V36]
* Adição de prints de debug no console nas exceções importantes.

## [NEW on V37]
* Adicao de Thread para tratar exception de nome do posto

## [NEW on V38]
* Alteração estrutural no script para uma programação orientada a objetos#   a l l - i n - o n e 