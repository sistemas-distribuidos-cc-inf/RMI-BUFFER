import Pyro4
import time
producer = Pyro4.Proxy("PYRONAME:client") 
cont = 1  
while True:
	if producer.Produce() == "Sucesso":
		print("Produzido com Sucesso")
	else:
		print("Buffer esta cheio")
	time.sleep(2)