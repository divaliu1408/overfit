# coding:utf-8

from soaplib.core.model.clazz import ClassModel
from spyne import Application, rpc, ServiceBase
from spyne import Integer, Unicode, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import sys
from spyne.model.complex import ComplexModel
from pymysql import connect
import os,base64,logging

#第二步：记录python Web services服务端的logging文件
logging.basicConfig(level=logging.DEBUG, filename='my_server.log')
logging.getLogger('spyne.application.server').setLevel(logging.DEBUG)

# 第三步 声明接收的客户端的变量名，也就是子段，或者xml标签，由于是数据多，就用的复杂性model，
#得声明空间，在客户端创建对象或者字典都可以，作为对象的一个属性，或者字典的key，value来保存数据的传递。
class Project(ComplexModel):
    __namespace__ = 'Project'
    name = Unicode
    phone = Unicode
    address = Unicode
    location = Unicode
    time = Unicode
    level = Unicode
    message = Unicode
    #多少都可以，前提是客户端得给你传过来，你才能接收到，但是客户端有的字段，你这里必须有，否则会报错，
    # ... = ...

#第四步：声明服务的类，类的方法，就是客户端访问的服务，业务逻辑，操作都在这里面，
#project就是字典，或者对象，

class SServices(ServiceBase):
    @rpc(Project, _returns=Unicode)
    def make_func(self, project):
        # return "链接成功，webservice 服务器已接收到数据"
        print(project)
        #业务逻辑放这里，把接收到的参数就是project，可以保存到数据库，等操作，
        print("save success")


# 第五步代码的执行，ip port就是你本地的地址，或者你的ip地址，ifcofig，
#创建服务名：SServices，服务调用的函数是make_func
if __name__ == "__main__":
    # ip = '127.0.0.1'
    # ip="192.168.10.73"
    ip="192.168.1.107"
    port = 6667
    soap_app = Application([SServices],
                           'SampleServices',
                           in_protocol=Soap11(validator="lxml"),
                           out_protocol=Soap11())
    wsgi_app = WsgiApplication(soap_app)
    server = make_server(ip, port, wsgi_app)
    sys.exit(server.serve_forever())