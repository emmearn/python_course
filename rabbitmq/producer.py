from rabbitmq.rabbit_connector import RabbitConnector

connector = RabbitConnector()

for i in range(0, 100_000):
    connector.publish_message(str(i))

connector.terminate()
