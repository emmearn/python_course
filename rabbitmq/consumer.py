from rabbitmq.rabbit_connector import RabbitConnector

connector = RabbitConnector()


def callback(ch, method, properties, body):
    print(f"Ricevuto {body}")


connector.consume_messages(callback)
