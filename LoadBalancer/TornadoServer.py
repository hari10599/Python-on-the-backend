import tornado.web
import tornado.ioloop
import sys
import os

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f'Hello World : {os.getpid()}')


if __name__ == '__main__' :
    app = tornado.web.Application([
        (r'/basic', basicRequestHandler)
    ])
    port = sys.argv[1]
    app.listen(port)
    print(f'Listening on port {port}')
    tornado.ioloop.IOLoop.current().start()
