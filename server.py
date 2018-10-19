import soaplib
from soaplib.core.service import rpc, DefinitionBase
from soaplib.core.model.primitive import String, Integer, Boolean
from soaplib.core.server import wsgi
from soaplib.core.model.clazz import Array
from soaplib.core.service import soap
from soaplib.core.model.clazz import ClassModel
import overfitGraph
import os


class Rules(ClassModel):
    __namespace__ = "Rules"
    username = String
    emotion = String


class HelloWorldService(DefinitionBase):
    @soap(String, Integer, _returns=Array(String))
    def say_hello(self, name, times):
        results = []
        for i in range(0, times):
            results.append('Hello, %s' % name)
        return results

    @soap(Rules, _returns=Boolean)
    def get_recommend(self, rules):
        print rules.username
        print 111
        print rules.emotion
        return 1

    @soap(String, _returns=String)
    def get_hi(self, name):
        result = "hi,"+name
        return result

    @soap(String, _returns=String)
    def get_graph(self, name):
        result = "hi," + name
        overfitGraph.save_graph(name)
        return result


if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        soap_application = soaplib.core.Application([HelloWorldService], 'tns')
        wsgi_application = wsgi.Application(soap_application)
        server = make_server('localhost', 7789, wsgi_application)
        server.serve_forever()
    except ImportError:
        print "Error: example server code requires Python >= 2.5"

