class AnimalAction():
	def walk(self): return self.string['walk']
	def talk(self): return self.string['talk']
	def eat(self): return self.string['eat']
	def sleep(self): return self.string['sleep']

	def love(self):
		return self.string['love']


class Human(AnimalAction):
	string = dict(
			walk = "Normally walk by two legs",
			talk = "Understandable",
			eat = "Vegitarian and eat meat also",
			sleep = "standard 8 hours",
			love = "emotional"
		)


class Tiger(AnimalAction):
	string = dict(
			walk = "Walk and run by 4 legs",
			talk = "Can't human understandable",
			eat = "Eat Meat",
			sleep = "No Idea",
			love = "Don't know"
		)



suchi = Human()
chitta = Tiger()

print(chitta.love())

