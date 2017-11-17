#!/usr/bin/env python3

from ncclient import manager
import sys, os
import xml.dom.minidom as xdom


PASS = 'Meilab123'
USER = 'student'

filter_cmd = """<filter>
         <config-format-text-cmd>
            <text-filter-spec> | inc interface </text-filter-spec>
         </config-format-text-cmd>
                </filter>"""

filter_blk = """<filter>
         <config-format-text-block>
            <text-filter-spec> | include interface </text-filter-spec>
         </config-format-text-block>
                </filter>"""

def get_config(HOST, filter):
    with manager.connect(host=HOST, port=22,
                username=USER, password=PASS,
                device_params={'name': 'iosxe'},
                hostkey_verify=False,
                look_for_keys=False,
                allow_agent=False) as m:
        c = m.get_config('running', filter)
        print("=== Configuration of %s ===" % HOST)
        print(c.xml)
        #xtr = xdom.parseString(c.xml)
        #print(xtr.toprettyxml())

if __name__ == '__main__':
    if(len(sys.argv)>1):
        HOST = sys.argv[1]
        print("Contacting HOST %s" % HOST)
        get_config(HOST,filter_blk)
    else:
        print("Usage: python3 %s <host>" % __file__)

