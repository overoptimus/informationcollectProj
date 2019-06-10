import nmap
import sys
from socket import gethostbyname

class Portscan:
    def __init__(self, network_prefix, port_range):
        self.network_prefix = network_prefix
        if (port_range is None) or (port_range == ''):
            self.port_range = '1-1024'
        else:
            self.port_range = port_range
        self.nm = nmap.PortScanner()
        self.result = []

    def startScan(self):
        print('start scan')
        scan_result = self.nm.scan(hosts=self.network_prefix, ports=self.port_range, arguments='-Pn -sV')
        self._work(scan_result)
        return self.result

    def _work(self, scan_result):
        scan_result = scan_result['scan']
        for ip, more_info in scan_result.items():
            port_list = more_info['tcp']
            for port, info in port_list.items():
                port_dict = {
                    'port': port,
                    'status': info['state'],
                    'reason': info['reason'],
                    'name': info['name'],
                    'product': info['product'],
                    'version': info['version']
                }
                self.result.append(port_dict)