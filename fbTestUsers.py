import urllib2
import urllib
import ConfigParser

__author__ = 'pearson'
GRAPH_URL = 'https://graph.facebook.com'

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[asection]\n'
    def readline(self):
        if self.sechead:
            try: return self.sechead
            finally: self.sechead = None
        else: return self.fp.readline()

rawC = ConfigParser.RawConfigParser()
rawC.readfp(FakeSecHead(open('/etc/fifa14/config.properties')))

configValuesDict = dict(rawC.items('asection'))
CLIENT_SECRET = configValuesDict['fb_client_secret']
APP_ID = configValuesDict['fb_app_id']

def createUser(fullName, permissions):
    # https://graph.facebook.com/APP_ID/accounts/test-users
    # installed=true
    # &name=FULL_NAME
    # &locale=en_US
    # &permissions=read_stream
    # &method=post
    # &access_token=APP_ACCESS_TOKEN
    post_args = urllib.urlencode({'installed':'true',
                      'name':fullName,
                      'local': 'en_US',
                      'permissions': permissions,
                      'method':'post',
                      'access_token': APP_ID + "|" + CLIENT_SECRET})
    url = "%s/accounts/test-users"
    urllib2.urlopen(url % GRAPH_URL, post_args)
    print("createUser")

#permissions: 'read_friendlists, user_friends'
createUser("1", 'read_friendlists, user_friends')
