import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World')

class htmlRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        lang = self.get_arguments('lang')
        self.write(f'Favorite Language is {lang}')

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, name):
        self.write(f'Favorite Language is {name}')

if __name__ == '__main__' :
    app = tornado.web.Application([
        (r'/', basicRequestHandler),
        (r'/html', htmlRequestHandler),
        (r'/query',queryParamRequestHandler),
        (r'/([a-z]+)',resourceParamRequestHandler),
    ])
    port = 12345
    app.listen(port)
    print(f'Listening on port {port}')
    tornado.ioloop.IOLoop.current().start()
