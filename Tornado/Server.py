import tornado.web
import tornado.ioloop
import json

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello Gamer')

class htmlRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        game = self.get_argument('game')
        self.write(f'Favorite Game is {game}')

class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, name, id):
        self.write(f'Favorite game is {name} with Playing hours {id}')

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fileHandler = open('Tornado/games.txt', 'r')
        games = fileHandler.read().splitlines()
        fileHandler.close()
        self.write(f'The languges are {json.dumps(games)}')
    
    def post(self):
        #Request Body Format {'lang' : 'JS'}
        body = json.loads(self.request.body)
        fileHandler = open('Tornado/games.txt', 'a')
        fileHandler.write(body['game'] + '\n')
        fileHandler.close
        self.write(json.dumps({'status' : 'Game added.'}))


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
