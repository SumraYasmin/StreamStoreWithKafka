import json
import uuid

from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})
order = {
    "order_id": str(uuid.uuid4()),
    "user_id": "Faiza",
    "product_name": "pizza",
    "quantity": "1",
}

def delivery_report(err, _msg):
    if err:
        print("Failed to deliver message: {}".format(err))
    else:
        print("Successfully delivered message")

value = json.dumps(order).encode("utf-8")
producer.produce(topic="orders", value=value,callback= delivery_report)

producer.flush()