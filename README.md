####На локальной машине все работает.
 * установить зависимости: 
   * pip install -r requirements.txt
     * python server.py
     * python client.py
     

 * docker pull rabbitmq:3.6.14-management
 * docker volume create rabbitmq_data
 * docker run -d --hostname rabbitmq --log-driver=journald --name rabbitmq -p 5672:5672 -p 15672:15672 -p 15674:15674 -p 25672:25672 -p 61613:61613 -v rabbitmq_data:/var/lib/rabbitmq rabbitmq:3.6.14-management

####При создании контейнеров не работает.

Конфликт, не могу понять где.

Создание и запуск контейнеров:

 * docker-compose up
 * docker-compose up

Здесь конфликтует