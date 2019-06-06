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
        self.channel.basic_publish(exchange='', routing_key='worker_queue', body=message)
        print(f"Inviato messaggio '{message}'")

    def consume_messages(self, callback):
        self.channel.basic_consume(on_message_callback=callback, queue='worker_queue', auto_ack=True)
        self.channel.start_consuming()

    def terminate(self):
        self.connection.close()
