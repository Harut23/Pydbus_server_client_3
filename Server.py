import time
import random
from pydbus import SessionBus  # Session or System Bus
from gi.repository import GLib
from pydbus.generic import signal


bus = SessionBus()
BUS = "https://github.com/Harut23/SearchEngine2022"
loop = GLib.MainLoop()
INTERVAL = 2
message_count = 0


class DBusService_XML:  # method name="greeting"
    """
    DBus Service XML definition
    type = "i" for integer, "S" string, "d" double, "as" list of string data
    """
    dbus = """
    <node>
        <interface name= "{}">
            <method name="greeting">
                <arg type="s" name = "person" direction="in">
                </arg>
            </method>
        <interface>
    </node>
    """.format(BUS)

    # Greeting receiving a value for name:(classmethod)
    def greeting(self, name):
        " Return Hello and the persons name "

        # output to server console
        print("Hello {}".format(name))
        return

if __name__ == "__main__":

    bus.publish(BUS, DBusService_XML())

    loop.run()