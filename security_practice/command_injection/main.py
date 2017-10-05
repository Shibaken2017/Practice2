import os.path
import  tornado.httpserver

import tornado.ioloop
import tornado.options
import tornado.web
import datetime
import sqlite3
TARGET_DIR="/home/shibaken/tmp"

from tornado.options import define,options
define("port",default=9000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class RequestHandelr(tornado.web.RequestHandler):
    def get(self):
        fname=self.get_argument("filename")
        print(fname)
        os.chdir(TARGET_DIR)
        #print(os.getcwd())
        command="find {}".format(fname)
        print(command)
        test=(os.system(command))

        if test==0:
            message="existence"
        else :
            message="non-existence"



        self.render("finish.html",message=message)
        #print(test)

        #self.render("inish.html",message=message)





if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r'/',IndexHandler),(r'/search',RequestHandelr)],
                                template_path=os.path.join(os.path.dirname(__file__),"templates"))

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()