class Mario():
	def move(self):
		print("I am moving");


class Shroom():
	def eat_shroom(self):
		print("I am big");

class BigMario(Mario,Shroom): #multi inher
	pass # to ignore the err


bm =BigMario();
bm.move();
bm.eat_shroom();



