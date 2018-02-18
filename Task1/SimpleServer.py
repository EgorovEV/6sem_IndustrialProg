#!/usr/bin/env python
#По умолчанию RabbitMQ будет отправлять каждое сообщение следующему абоненту в последовательности.
# В среднем каждый потребитель получает одинаковое количество сообщений.
# Этот способ распространения сообщений называется round-robin.
import pika
import time
import psycopg2
import codecs

def open_db():  #Затирает старую бд, открывает новую
    try:
        connect_str = "dbname='my_postgres_db' user='evgeniy' host='localhost' " + \
                      "password='admin'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

    try:
        cursor.execute("""DROP TABLE task1_opp""")
    except:
        print("I can't drop our test database!")

    try:
        cursor.execute("""CREATE TABLE task1_opp (id serial PRIMARY KEY,data varchar);""")
    except Exception as e:
        print("Can't create new db:")
        print(e)

    #cursor.execute("""INSERT INTO task1_opp (data) VALUES ('test_msg');""")
    #cursor.execute("""SELECT * from task1_opp""")
    conn.commit()

def write_to_db(msg):   #Логгирует сообщения, записывая в уже открытую базу данных
    try:
        connect_str = "dbname='my_postgres_db' user='evgeniy' host='localhost' " + \
                      "password='admin'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    try:
        cursor.execute("""INSERT INTO task1_opp (data) VALUES (%s);""", [msg])
    except Exception as e:
        print("Can't insert into DB:")
        print(e)

    cursor.execute("""SELECT * from task1_opp""")
    conn.commit()
    rows = cursor.fetchall()
    print(rows)

#def counter(func):
#    """
#    Декоратор, считающий и выводящий количество вызовов
#    декорируемой функции.
#    """
#    def wrapper(*args, **kwargs):
#        wrapper.count += 1
#        res = func(*args, **kwargs)
#        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
#        return res
#    wrapper.count = 0
#    return wrapper
#
#@counter


def callback(ch, method, properties, body):
    try:
        callback.called += 1
    except AttributeError:
        callback.called = 0

    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    if callback.called == 0:
        print("_____1_____")
        open_db()

    print("_____2_____")
    a = codecs.decode(body, 'unicode_escape')
    print("%s", a)
    print(body)
    write_to_db(a)
    print(" [x] Done")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  # open channel
    channel = connection.channel()  # chech avaliability of channel

    channel.queue_declare(queue='hello')  # declare name of queue
    channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)      # tell RabbitMQ that this particular callback function should receive messages from our hello queue:

    print(' [*] Waiting for messages. To exit press CTRL+C')    # finally, we enter a never-ending loop that waits for data and runs
                                                            # callbacks whenever necessary.
    channel.start_consuming()

if __name__ == "__main__":
    main()