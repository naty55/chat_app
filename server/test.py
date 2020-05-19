from client import Client
from time import sleep
from threading import Thread


def update_msg(client):
    """
    updates the local list of messages
    :param client: client
    :return: None
    """
    msgs = []
    run = True
    while run:
        print(client.is_closed())
        sleep(0.1)  # Update every 1/10 seconds
        new_messages = client.get_messages()  # get new messages if any from client
        msgs.extend(new_messages)  # Add to local list of messages
        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False


c1 = Client("c1")
a = Thread(target=update_msg, args=(c1,))
a.start()

sleep(2)
c2 = Client("C2")
b = Thread(target=update_msg, args=(c2,))
b.start()

sleep(2)
c1.send("Hello")
sleep(2)
c2.send("whats up")
sleep(1)
c1.send("Nothing much")
sleep(1)
c2.send("Boring...")
sleep(2)
c1.disconnect()
sleep(2)
c2.disconnect()


sleep(1)
c2.send("OK")
sleep(1)
c2.send("HIII")

c2.disconnect()

