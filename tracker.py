from confluent_kafka import Consumer
# import

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'consumer_group_1',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(["orders"])
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        value = msg.value().decode('utf-8')
        print(value)

except KeyboardInterrupt:
   print("Closing Kafka consumer")
   consumer.close()
finally:
  consumer.close()