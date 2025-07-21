# HandControl

## Objetivo

Este repositório contém um projeto de controle e reconhecimento de gestos por meio do rastreamento da mão utilizando a biblioteca **MediaPipe** em Python. A aplicação captura imagens em tempo real da webcam, detecta e desenha os pontos de referência (landmarks) das mãos, possibilitando o desenvolvimento de interfaces baseadas em gestos.

## Descrição

O sistema realiza a captura contínua da câmera, converte os frames para o formato RGB necessário para o processamento do MediaPipe e detecta até duas mãos simultaneamente. Os landmarks das mãos são desenhados sobre o vídeo, utilizando diferentes cores para os pontos e conexões, para facilitar a visualização.

Além disso, o script imprime no console as coordenadas (x, y) dos pontos de referência de cada mão detectada, o que pode ser utilizado para implementar funcionalidades específicas com base nos gestos reconhecidos.

## Tecnologias Utilizadas

- Python 3.x  
- OpenCV  
- MediaPipe
