import random
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError
 
producer = KafkaProducer(bootstrap_servers="localhost:9092")
    
topic  = "power"
AT     = "19.651231" 
V      = "54.305804"
AP     = "1013.259078"
RH     = "73.308978"

def getAT():
     return  str(round(random.uniform(1.81, 37.11),2))
     
def getV():
     return str(round(random.uniform(25.36, 81.56),2)) 

def getAP():
    return str(round(random.uniform(992.89, 1033.3),2))  

def getRH():
    return str(round(random.uniform(25.56, 100.16),2))  
    
for i in range(1000):
            
    message = "{\"AT\" : " + getAT() + "," + "\"V\" : " +getV() + "," + "\"AP\" : " +getAP() + "," + "\"RH\" : " + getRH() + "}" 
    producer.send(topic, key=str.encode('key_{}'.format(i)), value=(message.encode('utf-8')))

    time.sleep(1)
 
producer.close()
