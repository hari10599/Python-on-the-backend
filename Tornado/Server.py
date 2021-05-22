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
        lang = self.get_argument('lang')
        self.write(f'Favorite Language is {lang}')

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, name, id):
        self.write(f'Favorite Language is {name} with id {id}')

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fileHandler = open('Tornado/languages.txt', 'r')
        lang = fileHandler.read().splitlines()
        fileHandler.close()
        self.write(f'The languges are {json.dumps(lang)}')
    
    def post(self):
        #Request Body Format {'lang' : 'JS'}
        body = json.loads(self.request.body)
        fileHandler = open('Tornado/languages.txt', 'a')
        fileHandler.write(body['lang'] + '\n')
        fileHandler.close
        self.write(json.dumps({'status' : 'Language added.'}))


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