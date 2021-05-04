import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World')

class htmlRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

if __name__ == '__main__' :
    app = tornado.web.Application([
        (r'/', basicRequestHandler),
        (r'/html', htmlRequestHandler)
    ])
    port = 12345
    app.listen(port)
    print(f'Listening on port {port}')
    tornado.ioloop.IOLoop.current().start()
