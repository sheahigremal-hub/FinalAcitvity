class Car:
	def move(self):
		print("The car drives down the road.")


class Person:
	def move(self):
		print("The person walks along the path.")


class Robot:
	def move(self):
		print("The robot rolls across the floor.")


def make_it_move(thing):
	thing.move()


things = [Car(), Person(), Robot()]

for thing in things:
	make_it_move(thing)
