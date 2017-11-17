#!/usr/bin/env python3

from ncclient import manager
import sys

HOST = None
PORT = 22
USER = 'student'
PASS = 'Meilab123'


def get_capabilities():
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'iosxe'},
                         look_for_keys=False, allow_agent=False) as m:

        # print all NETCONF capabilities
        print('==== Capabilities of %s ====' % HOST)
        cap = m.server_capabilities
        for capability in cap:
            print(capability.split('?')[0])
        print('=' * 40)

if __name__ == '__main__':
    if(len(sys.argv)>1):
        HOST = sys.argv[1]
        print("Contacting host %s" % HOST)
        get_capabilities()
    else:
        print("Usage: python3 %s <host>" % __file__)
