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
    
## Aequivo docker-compose.yml
1. zookeeper

    Coordena os brokers Kafka.
    
    Mantém metadados do cluster e ajuda os brokers a se comunicarem.
    
    Porta: 2181.
    
    Tem healthcheck para garantir que está pronto antes dos brokers iniciarem.

2. broker-1, broker-2, broker-3

    São os brokers Kafka, responsáveis por armazenar e distribuir os tópicos/mensagens.
    
    Cada um tem:
    
    KAFKA_BROKER_ID: identificador único do broker.
    
    KAFKA_LISTENERS: porta interna que o broker escuta (0.0.0.0:9092/9093/9094).
    
    KAFKA_ADVERTISED_LISTENERS: o endereço que outros clientes/brokers usam para se conectar (importante para o producer/consumer).
    
    KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: quantas réplicas criar para o tópico interno de offsets.
    
    Cada broker expõe uma porta diferente para fora do container.

3. schema-registry

    Mantém os esquemas de mensagens (usado se você quiser usar Avro ou Protobuf).
    
    Depende do broker-1.
    
    Porta: 8081.

4. control-center

    Interface web da Confluent para monitorar o Kafka (tópicos, brokers, consumidores).
    
    Depende do schema-registry e do broker-1.
    
    Porta: 9021.

5. producer

    Seu script Python que envia mensagens para o Kafka.
    
    Conecta aos brokers pelo network kafka-net.
    
    Construído via Dockerfile.producer.

6. networks: kafka-net

    Rede interna Docker onde todos os containers se comunicam.
    
    Importante porque o producer e os brokers usam os nomes dos serviços (broker-1, broker-2, etc.) para se conectar.


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
