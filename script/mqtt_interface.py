import paho.mqtt.client as mqtt

class mqtt_interface():

  mqttBroker = "brbelm0mat81.corp.jabil.org"
  qos = 1
  def connect(self, clientName):
        self.user = 'None'
        self.client = mqtt.Client(clientName)
        self.client.connect(self.mqttBroker)
        self.client.on_message=self.callback
        self.client.loop_start()
  
  def callback(self, client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    d = json.loads(message.payload)
    return d
  
  def publish(topic,message):
     self.client.publish(topic, message, self.qos)


int = mqtt_interface()
int.connect("client")
print("helo")

