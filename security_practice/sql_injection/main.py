import os.path
import  tornado.httpserver

import tornado.ioloop
import tornado.options
import tornado.web
import datetime
import sqlite3


from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class RequestHandelr(tornado.web.RequestHandler):
    def post(self):
        self.conn=sqlite3.connect("practice.db")
        self.curs=self.conn.cursor()

        print(self.curs.execute("select name from sqlite_master where type='table'"))
        print(self.curs.fetchall())
        name=self.get_argument("name")
        password=self.get_argument("password")
        #print(password)
        self.curs.execute("select * from zoo where name='%s' and pass='%s'" % (name, password))
        #self.curs.execute("select * from zoo where name='%s'" % (name))

        result=len(self.curs.fetchall())
        if result>0:
            message="login success"
        else:
            message="login failed\ninccorect name or inccorect password"
        #message="aiueo"
        self.render("finish.html",message=message)



        self.conn.commit()

        self.curs.close()


if __name__=="__main__":
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[(r'/',IndexHandler),(r'/check',RequestHandelr)],
                                template_path=os.path.join(os.path.dirname(__file__),"templates"))

    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()