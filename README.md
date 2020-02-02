1. Java 1.8 install
2. JAVA_HOME is setup
3. Ubuntu Confluent Installation
    * Install the Confluent public key, which is used to sign the packages in the APT repository.
        $ wget -qO - https://packages.confluent.io/deb/3.3/archive.key | sudo apt-key add -
    * Add the repository to your /etc/apt/sources.list:
        $ sudo add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/3.3 stable main"
    * Run apt-get update and install Confluent Platfor for Open Source
        $ sudo apt-get update && sudo apt-get install confluent-platform-oss-2.11

        https://docs.confluent.io/3.3.0/installation/installing_cp.html
        https://docs.confluent.io/3.3.0/quickstart.html#quickstart

4. Python3.7
5. pip3 install confluent-kafka
6. Start the Confluent
    confluent start schema-registry

Alternatively, to manually start each service in its own terminal, the equivalent commands are:
  ```
    $  /usr/bin/zookeeper-server-start ./etc/kafka/zookeeper.properties
     $  /usr/bin/kafka-server-start ./etc/kafka/server.properties
     $  /usr/bin/schema-registry-start ./etc/schema-registry/schema-registry.properties
   ```

In case multiple Python3/Java are present, then run below and choose the right
  ```
  sudo update-alternatives --config python3
  JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre/  in sudo vi /etc/environment and then source /etc/environment
  ```


https://kafka.apache.org/documentation.html#topicconfigs


## Kafka Producer
  * Synchronous Producer->
                        * data is sent before application proceeds further. It
                        should not be default choice but if there is a specific
                        need.
                        * In Python, flush function on python makes producer sync

  * Async producer -> Its most common method. Max throughput of Kafka .
                    It should be default choice.Producer can be configured on
                    fire and forgot mechanism

### Kafka producer properties
  * client.id -> All producers should provide for better debugging experience

  * enable.idempotennce for true in-order retry

  * Configure retry to ensure data is delivered

  * Configure compression on individual topics. compression will happen on client.

  * https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md

![Producer_configuration](Producer_conf.png)
## Message Serialization

    * Process of transforming application internal data into a data model
    suitable for data stores is called as Serialization.

    * eg. JSO, AVRO

    * Kafka does not handle Serialization but kafka client library handles it.

    * Never change Serialization on a topic.

    *

# Delete Kafka Topics
   * ensure that delete.topic.enable = true in server.properties file
   * kafka-topics --delete --topic "org.udacity.exercise3.purchases" --zookeeper localhost:2181
   * kafka-topics --list --zookeeper localhost:2181
