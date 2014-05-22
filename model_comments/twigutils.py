import urllib, urlparse
 
class Url(object):
    def __init__(self, url):
        """
        Construct from a string.
        """
 
        self.scheme, self.netloc, self.path, self.params, self.query_string, self.fragment = urlparse.urlparse(url)
        self.query = dict(urlparse.parse_qsl(self.query_string))
 
    def build(self):
        """
        Turn back into a URL.
        """
        return u"%s" % urlparse.urlunparse((self.scheme, self.netloc, self.path, self.params, urllib.urlencode(self.query), self.fragment))
 
    def __str__(self):
        return self.build()
 
    def __unicode__(self):
        return self.build()


from django.template import Node
 
class ContextNode(Node):
    def __init__(self, func):
        self.func = func
 
    def render(self, context):
        return self.func(context)
