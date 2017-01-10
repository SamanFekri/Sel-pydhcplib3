# In The Name Of God
# ========================================
# [] File Name : client.py
#
# [] Creation Date : 10-01-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from pydhcplib.dhcp_packet import *
from pydhcplib.dhcp_network import *

netopt = {'client_listen_port': 68,
          'server_listen_port': 67,
          'listen_address': "0.0.0.0"
          }


class Client(DhcpClient):
    def __init__(self, options):
        DhcpClient.__init__(self, options["listen_address"],
                            options["client_listen_port"],
                            options["server_listen_port"])

    def HandleDhcpOffer(self, packet):
        print(packet.str())

    def HandleDhcpAck(self, packet):
        print(packet.str())

    def HandleDhcpNack(self, packet):
        print(packet.str())


client = Client(netopt)

# Use BindToAddress if you want to emit/listen to an internet address
# (like 192.168.1.1)
# or BindToDevice if you want to emit/listen to a network device (like eth0)
client.BindToAddress()

while True:
    client.GetNextDhcpPacket()
    print(client.str())
