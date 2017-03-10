# -*- coding: utf-8 -*-
#!/usr/bin/python
import re
import urllib2
from smb.SMBConnection import SMBConnection

from smb.SMBHandler import SMBHandler

class SambUtils():
    """
    """
    def __init__(cls):
        """
        """
        # cls.movie_server =     

    def test_find():
        """
        test
        """
        director = urllib2.build_opener(SMBHandler)

        userID = ''
        password = ''
        client_machine_name = 'localpcname'

        server_name = 'servername'
        server_ip = ['10','0','0','10']

        domain_name = 'domainname'

        conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True,
                             is_direct_tcp=True)

        server_addr = '.'.join(server_ip) 
        conn.connect(server_addr, 445)

        shares = conn.listShares()
        # import pudb
        # pudb.set_trace()
        for share in shares:
            if share.name.isupper() and len(share.name) == 1:
                print "Files in {}/".format(share.name)
                sharedfiles = None
                try:
                    sharedfiles = conn.listPath(share.name, '/Movies/')
                except Exception:
                    continue
                if sharedfiles:
                    for file in sharedfiles:
                    #     if sharedfile.filename == "Movies":
                            # path = "smb://'':''@" + server_addr + "/" + share.name
                            # print "{} was found in {}".format(sharedfile.filename, path)
                            # movies = conn.listPath(share.name + '/' + sharedfile.filename, '/')
                            # for m in movies:
                            #     print m.filename
                            # movies = director.open(path)
                        if not file.filename.startswith("."):\
                            print file.filename
        conn.close()

def _find_sever():
    """
    loop through addresses and try to connect
    """
    userID = ''
    password = ''
    client_machine_name = 'localpcname'
    server_name = 'servername'
    domain_name = 'domainname'

    for i in xrange(10,11):
        server = "10.0.0.{}".format(unicode(i))
        conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True,
                     is_direct_tcp=True)
        try:
            print "trying: {}".format(server)
            conn.connect(server, 445)
        except Exception:
            continue
        else:
            print "{} is connected on: {}.".format(server, [i.name for i in conn.listShares()])
            conn.close()



_find_sever()
