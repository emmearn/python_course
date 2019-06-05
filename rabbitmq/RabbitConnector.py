import pika


class RabbitConnector:
    def __init__(self):
        print("Collegamento a RabbitMQ...")

        params = pika.ConnectionParameters(host="localhost")
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='worker_queue')

        print("..eseguito")

    def publish_message(self, message):
        self.channel.basic_publish(exchange='', rounting_key='worker_queue', body=message)
        print("Inviato messaggio %s", message)

    def terminate(self):
        self.connection.close()