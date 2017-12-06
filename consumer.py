import Pyro4
import time
producer = Pyro4.Proxy("PYRONAME:client")    
cont = 0
while True:
	s = producer.Consume()
	if s != "empty buffer":
		print("Consumi " + s)
	else:
		print("Buffer vazio")
	time.sleep(2)