#!/usr/bin/python
import tornado.ioloop
import tornado.web
import urllib2
import os

# Static Ganeti URL for now
ganeti_url = "https://192.168.0.71:5080/2/"

basepath = os.getcwd()
print basepath

# Proxy the data requests to the Ganeti Cluster via Tornado
# Allows for firewall traversal
class DataHandler(tornado.web.RequestHandler):
	def get(self):
		urlpath = "/".join(self.request.path.split('/')[2:]) 
		urlpath = urlpath + "?bulk=1"
		print urlpath
		self.write(urllib2.urlopen(ganeti_url + urlpath).read())

application = tornado.web.Application([
	(r'/', tornado.web.RedirectHandler,dict(url="/index.html")),
	(r'/(.*html)', tornado.web.StaticFileHandler, { "path" : basepath + "/html"}),
	(r'/css/(.*)', tornado.web.StaticFileHandler, { "path" : basepath + "/html/css"}),
	(r'/js/(.*)', tornado.web.StaticFileHandler, { "path" : basepath + "/html/js"}),
	(r'/data/.*', DataHandler),
	(r'/data', DataHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
