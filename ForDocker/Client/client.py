import sys
import pika

def main():
    #message = ' '.join(sys.argv[1:]) or "Hello World!"
    message = "Hello World"
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))  # We're connected now, to a broker on the local machine - hence the localhost.
    channel = connection.channel()  # Next, before sending we need to make sure the recipient queue exists

    channel.queue_declare(
        queue='hello')  # Our first message will just contain a string Hello World! and we want to send it to our hello queue.

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    print(" [x] Sent %r" % message)

    connection.close()  # Before exiting the program we need to make sure the network buffers
    #  were flushed and our message was actually delivered to RabbitMQ. We can do it by gently closing the connection.

if __name__ == "__main__":
    main()
