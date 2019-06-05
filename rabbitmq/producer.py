from rabbitmq import RabbitConnector

connector = RabbitConnector()

for i in range(0, 100_000):
    connector.publish_message(str(i))

connector.terminate()
