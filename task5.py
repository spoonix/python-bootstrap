#!/usr/bin/python

import json

class EtcHosts(object):
    entries = {
    "google.com":'216.58.218.174',
    "trueability.com":'50.56.167.156',
    'fsf.org':'208.118.235.131',
    'linux.com':'140.211.167.51'
    }

    def load(self,filename):
        if len(filename) <= 0:
            filename = open('/etc/hosts','r')
            for line in filename:
                self.entries = filename
        else:
            with open(filename) as in_file:
                self.entries = json.load(in_file)

    def count(self):
        return len(self.entries.keys())

    def find_hostnames(self,ip):
        for name, addr in self.entries.iteritems():
            if addr == ip:
                ip_found = True
                return name
            if not ip_found:
                print "none"

    def find_ip(self,hostname):
        hostname_found = 0
        for name, addr in self.entries.iteritems():
            if str(name) == str(hostname):
                return addr

    def find_ip(self,hostname):
        if len(hostname) == 0:
            return "Error: Invalid Hostname"
        hostname_found = False
        for name, addr in self.entries.iteritems():
            if name == hostname:
                hostname_found = True
                return addr
        if not hostname_found:
            return "none"

    def add_entry(self, ip, hostname):
        self.entries[hostname] = ip

    def save(self,filename):
        with open(filename, 'w') as outfile:
            json.dump(self.entries, outfile)
        return True





e=EtcHosts()
#e.load('')
#e.save('')
e.add_entry('127.0.0.1','localhost')
print str(e.count())
print e.find_hostnames('50.56.167.156')
print e.find_ip('google.com')
print e.entries
