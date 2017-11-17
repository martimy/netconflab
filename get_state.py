#!/usr/bin/env python3

from ncclient import manager
import sys, os
import xml.dom.minidom as xdom


PASS = 'Meilab123'
USER = 'student'

filter_state_cmd = """<filter>
          <config-format-text-cmd>
             <text-filter-spec> | include interface </text-filter-spec>
          </config-format-text-cmd>
          <oper-data-format-text-block>
             <show>interfaces</show>
             <show>ip route</show>
          </oper-data-format-text-block>
       </filter>"""


filter_state_blk = """<filter>
          <config-format-text-block>
             <text-filter-spec> | include interface </text-filter-spec>
          </config-format-text-block>
          <oper-data-format-text-block>
             <show>ip interface brief</show>
             <show>ip route</show>
          </oper-data-format-text-block>
       </filter>"""

def get_state(HOST, filter):
    with manager.connect(host=HOST, port=22,
                username=USER, password=PASS,
                device_params={'name': 'iosxe'},
                hostkey_verify=False,
                look_for_keys=False,
                allow_agent=False) as m:
        c = m.get(filter)
        print(c.xml)


if __name__ == '__main__':
    if(len(sys.argv)>1):
        HOST = sys.argv[1]
        print("Contacting HOST %s" % HOST)
        get_state(HOST,filter_state_blk)
    else:
        print("Usage: python3 %s <HOST>" % __file__)

