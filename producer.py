import json
import logging
import time
import uuid
import requests
from kafka import KafkaProducer
from kafka.errors import TopicAlreadyExistsError
from kafka.admin import KafkaAdminClient, NewTopic

# Configurações
#BOOTSTRAP_SERVERS = ['localhost:9092', 'localhost:9093', 'localhost:9094']
BOOTSTRAP_SERVERS = ['broker-1:9092', 'broker-2:9093', 'broker-3:9094']
TOPIC_NAME = 'user_topic'
ENDPOINT = "https://randomuser.me/api/"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_topic():
    admin_client = None
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)
        topic = NewTopic(name=TOPIC_NAME, num_partitions=3, replication_factor=1)
        admin_client.create_topics([topic])
        logging.info(f"Topic {TOPIC_NAME} successfully created")
    except TopicAlreadyExistsError:
        logging.info(f"Topic {TOPIC_NAME} already exists")
    except Exception as ex:
        logging.error(f"Error creating topic: {ex}")
    finally:
        if admin_client:
            admin_client.close()


def get_data_from_api():
    try:
        response = requests.get(ENDPOINT)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Exception occurred while fetching data: {e}")
        return None


def format_user_data(user_data):
    data = user_data['results'][0]
    location = data['location']
    return {
        "uuid": str(uuid.uuid4()),
        "title": data['name']['title'],
        "first_name": data['name']['first'],
        "last_name": data['name']['last'],
        "gender": data['gender'],
        "street": f"{location['street']['number']} {location['street']['name']}",
        "city": location['city'],
        "state": location['state'],
        "country": location['country'],
        "postcode": location['postcode'],
        "email": data['email'],
        "dob": data['dob']['date'],
        "registered_date": data['registered']['date'],
        "registered_age": data['registered']['age'],
        "phone": data['phone'],
        "cell": data['cell'],
        "picture_large": data['picture']['large']
    }


def streaming_producer_data():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    while True:
        data = get_data_from_api()
        if data:
            formatted = format_user_data(data)
            producer.send(TOPIC_NAME, value=formatted)
            logging.info(f"Data sent to topic {TOPIC_NAME}: {formatted['uuid']}")
            producer.flush()
        time.sleep(5)


if __name__ == "__main__":
    create_topic()
    streaming_producer_data()
