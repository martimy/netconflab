#!/usr/bin/env python3

from ncclient import manager
import sys, os
import xml.dom.minidom as xdom
import get_config as g

PASS = 'Meilab123'
USER = 'student'

# modfiy the host name to mathc your group/router numbers
set_hostname = """<config>
                 <cli-config-data>
                    <cmd>hostname XRouterY</cmd>
                 </cli-config-data>
              </config>
           """

def edit_config(HOST, cfg):
    with manager.connect(host=HOST, port=22,
                username=USER, password=PASS,
                device_params={'name': 'iosxe'},
                hostkey_verify=False,
                look_for_keys=False,
                allow_agent=False) as m:

        assert(":writeable-running" in m.server_capabilities)
        m.edit_config(target='running', config=cfg)

if __name__ == '__main__':
    if(len(sys.argv)>1):
        HOST = sys.argv[1]
        print("Contacting HOST %s" % HOST)
        edit_config(HOST, set_hostname)
        g.get_config(HOST, None)
    else:
        print("Usage: python3 %s <host>" % __file__)

