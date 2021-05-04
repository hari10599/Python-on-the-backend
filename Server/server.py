import tornado.web
import tornado.ioloop

class test(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World')

if __name__ == '__main__' :
    app = tornado.web.Application([
        (r'/test', test)
    ])
    port = 12345
    app.listen(port)
    print(f'Listening on port {port}')
    tornado.ioloop.IOLoop.current().start()
