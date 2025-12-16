# Kafka Producer Dockerized

Este projeto contém um **Kafka Producer** em Python, dockerizado, que envia dados de usuários gerados aleatoriamente para um tópico Kafka.

---

## Estrutura do projeto

KAFKA-APPS-BROKERS/
├── Dockerfile.producer # Dockerfile do producer
├── docker-compose.yml # Compose para Kafka, Zookeeper e Producer
├── producer.py # Script Python do producer
├── requirements.txt # Dependências Python
└── .gitignore # Arquivos ignorados pelo git


## Tecnologias

- Python 3.12
- Kafka 2.6 (Confluent Platform)
- Zookeeper
- Docker / Docker Compose
- kafka-python

---

## Configuração e execução
  
  1. Clone o repositório:
  
  ```bash
  
  Suba os containers usando Docker Compose:
  
  sudo docker compose up -d --build
  
  sudo docker compose up -d --build
  Verifique os logs do producer:

bash
Copiar código
sudo docker compose logs -f producer
O producer começará a enviar dados para o tópico user_topic em intervalos definidos no script producer.py.



git clone https://github.com/BorgePambo/kafka-producer-docker.git
cd kafka-producer-docker
