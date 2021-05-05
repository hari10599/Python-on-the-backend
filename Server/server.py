import tornado.web
import tornado.ioloop
import json

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
    def get(self, name, id):
        self.write(f'Favorite Language is {name} with id {id}')

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fileHandler = open('Server/lang.txt', 'r')
        lang = fileHandler.read().splitlines()
        self.write(f'The languges are {json.dumps(lang)}' )

if __name__ == '__main__' :
    app = tornado.web.Application([
        (r'/', basicRequestHandler),
        (r'/html', htmlRequestHandler),
        (r'/query',queryParamRequestHandler),
        (r'/([a-z]+)/([0-9]+)',resourceParamRequestHandler),
        (r'/list', listRequestHandler)
    ])
    port = 12345
    app.listen(port)
    print(f'Listening on port {port}')
    tornado.ioloop.IOLoop.current().start()
