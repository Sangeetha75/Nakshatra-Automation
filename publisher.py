import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime

student_name = "Sangeetha Kodadhala"
unique_id = "42732041"
topic = "home/sangeetha-2025/sensor"
broker = "192.168.0.7"
port = 1883

def publish_sensor_data():
    client = mqtt.Client()
    client.connect(broker, port)
    data = {
        "student_name": student_name,
        "unique_id": unique_id,
        "temperature": 25,
        "humidity": 60,
        "light": 350,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    client.publish(topic, json.dumps(data))
    client.disconnect()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Published to {topic}: {data}")

while True:
    publish_sensor_data()
    time.sleep(5)
