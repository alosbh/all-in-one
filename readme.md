﻿
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
* versão definitiva compatível com Raspberry e windows
* nova janela e funcionalidades 5s
* tratamento de erros diversos
* resolução do erro que a tela travava na tela de ficha de instrução

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