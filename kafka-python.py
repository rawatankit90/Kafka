 client = AdminClient({"bootstrap.servers": BROKER_URL}) # Creating topics, changing topics config
 topic = NewTopic(TOPIC_NAME, num_paritions=1, replication_factor=1)
 # create topics on  kafka broker. This function takes an argument of list
 client.create_topics([topic])
 client.delete_topics([topic])
 
 to see logs
 
 tail -f /var/log/journal/confluent-kafka.service.log
 
 ## To produce
 async def produce(topic_name):
 p = Producer({"bootstrap.servers": BROKER_URL})
 
 p.produce(TOPIC_NAME, f"Message: ankit")
 
 ## To consume
 c = Consumer({"bootstrap.servers": BROKER_URL,"group.id": "first-python-consumer-group"})}
 c.subscribe([TOPIC_NAME])
  
 ## To poll the message
 message = c.poll(1.0)
 
 
