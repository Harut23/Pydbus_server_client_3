import random

from pydbus import SessionBus
from gi.repository import GLib

bus = SessionBus()
BUS = "org.example.demo.test"
server_object = bus.get(BUS)
loop = GLib.MainLoop()
INTERVAL = 2


def make_method_call_client_3():
    "Client sends a random name to the server"
    name_list = ["Harut", "Narek", "Arman", "Davit", "Eduard"]
    name = name_list[random.randint(0, len(name_list)-1)]

    # Client sends randomly selected "name" data
    reply = server_object.greeting(name)
    return True


if __name__ =="__main__":
    print("Starting Client Demo 1...")
    # call function to make a method call.

    # GLib to run repeating function every 2 secconds
    GLib.timeout_add_seconds(interval=INTERVAL,
                             function=make_method_call_client_3())
    loop.run()