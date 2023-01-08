import os
import subprocess
import sys
import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    print(f"{message.topic}: {message.payload}", file=sys.stderr)
    subprocess.run(['play', '/sounds/ho-ho-ho.flac'])

mqtt_host = os.environ['MQTT_HOST']
mqtt_topic = os.environ['MQTT_TOPIC']
print(f'subscribing to mqtt_host={mqtt_host} mqtt_topic={mqtt_topic}', file=sys.stderr)
subscribe.callback(
    callback=on_message_print,
    topics=[mqtt_topic],
    hostname=mqtt_host,
    port=1883
)
