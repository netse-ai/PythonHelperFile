import json
import urllib

class Tour(object):
	"""Shows an implementation of the Google Maps RESTful API"""
	def __init__(self, dest_city, orig_city, arg):
		self.dest_city = dest_city
		self.orig_city = orig_city
		self.arg = arg

	def distance(self, arg):
		for choice in arg:
			self.link = "http://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&mode=%s&sensor=false" % (self.dest_city, self.orig_city, arg)
		self.web_obj = urllib.urlopen(self.link)
		self.data = json.loads(self.web_obj.read())
		self.rendered_json = json.dumps(self.data, indent=4, sort_keys=True)

		for row in self.data['rows'][0]['elements']:
 			self.name = row.get("distance")
			self.dist = self.name['value']
			if self.dist == 0:
				raise ValueError("Something is wrong with your search! Please make a valid request!")

		return self.dist

	def time(self):
		for i in self.data['rows'][0]['elements']:
			self.name2 = i.get("duration")
			self.time = self.name2['text']
 		return self.time


def main():
	while True:
		print "*"*50
		print "Please choose two cities in the USA you want to visit and the method you want to use to get there!"
		print "Be sure to use a space where needed!"
		print "*"*50
		dest_city = raw_input("First City: ")
		orig_city = raw_input("Second City: ")
		if dest_city == orig_city:
			print "You can't choose the same city!\n Run me again!"
			exit()
		elif dest_city != orig_city:
			arg = raw_input("Driving, Walking, or Bicylcing: ").lower()
			t1 = Tour(dest_city, orig_city, arg)
			t1.distance(arg)
			print "*"*50
			print " "
			print "Your tour is from %s to %s!" % (dest_city, orig_city)
			print "By {0}, You will have to travel {1} meters to get from {2} to {3}!" .format(arg, t1.distance(arg), dest_city, orig_city)
			print "The journey will take you {0}\n\n" .format(t1.time())
			print "*"*50
			print " "
			print "Here is the rendered JSON data.  This is what the API looks like:"
			print t1.rendered_json
		else:
			print "You broke it!"

main()
