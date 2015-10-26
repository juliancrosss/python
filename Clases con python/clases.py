class Moto():
	def __init__(self,marca):
		self.marca = marca

	def acelerar(self):
		print("La moto {} esta acelerando".format(self.marca))

	def frenar(self):
		print("La moto {} esta frenando".format(self.marca))


moto_de_julian = Moto("bmw")
moto_de_julian.acelerar()
moto_de_julian.frenar()