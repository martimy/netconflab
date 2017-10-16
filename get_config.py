#!/usr/bin/env python
#
# Get configured interfaces using Netconf
#

from ncclient import manager
import sys, yaml
import xml.dom.minidom

FILE = 'filter_interfaces.xml'

def get_configuration(strfilter, p):
    with manager.connect(host=p['HOST'], port=p['PORT'], username=p['USER'],
                         password=p['PASS'], hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:
        return(m.get_config('running', strfilter))


def main(filename, parm):
    with open(filename) as f:
        config = get_configuration(f.read(), parm)
        configxml = xml.dom.minidom.parseString(config.xml)
        configlist = configxml.getElementsByTagName("interfaces")
        for e in configlist:
            print(e.toprettyxml())

if __name__ == '__main__':
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        main(FILE, cfg)   
