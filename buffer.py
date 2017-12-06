import Pyro4
import threading
import random
adjectives = ["hard",
		"boundless",
		"shrill",
		"bashful",
		"opposite",
		"fluffy",
		"dear",
		"astonishing",
		"eight",
		"sick",
		"placid",
		"ad hoc",
		"ambiguous",
		"irate",
		"ordinary",
		"numerous",
		"brawny",
		"harsh",
		"calm",
		"jumbled" 
]

nouns = ["snails",
		"believe",
		"apparatus",
		"horn",
		"eggs",
		"desire",
		"snail",
		"fireman",
		"pets",
		"stocking",
		"curtain",
		"prose",
		"doctor",
		"expansion",
		"fish",
		"hammer",
		"tail",
		"profit",
		"grip",
		"regret"
];
verbs = ["lock",
		"apologise",
		"knock",
		"advise",
		"scatter",
		"nest",
		"bomb",
		"roll",
		"decorate",
		"memorise",
		"name",
		"store",
		"harass",
		"remain",
		"last",
		"hop",
		"yell",
		"mug",
		"object",
		"weigh"
];
ponctuation =[ "?", "!" ,".", "...!"];

BUFFER_SIZE = 3
indexBuffer = -1

mutex = threading.Semaphore(1)
buffer = list(range(BUFFER_SIZE))	

@Pyro4.expose
class Client(object):


	def Produce(self):
		global BUFFER_SIZE, indexBuffer, mutex, buffer
		mutex.acquire()

		sentence = adjectives[random.randint(0, len(adjectives)-1)] + " "

		sentence += nouns[random.randint(0, len(nouns)-1)] + " "

		sentence += verbs[random.randint(0, len(verbs)-1)] + " "

		sentence += ponctuation[random.randint(0, len(ponctuation)-1)]
		
		if indexBuffer == BUFFER_SIZE - 1:
			mutex.release()
			return "full buffer"
		else:
			indexBuffer += 1
			buffer[indexBuffer] = sentence
			print ("Armazenei " + sentence)
			mutex.release()
			return "Sucesso"	
		

	def Consume (self):
		global BUFFER_SIZE, indexBuffer, mutex, buffer
		mutex.acquire()
		if indexBuffer == -1:
			mutex.release()
			return "empty buffer"
		else :
			indexBuffer -= 1
			print ("Item consumido " + buffer[indexBuffer + 1])
			mutex.release()
			return (buffer[indexBuffer+1] )
		


daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(Client)   # register the greeting maker as a Pyro object
ns.register("client", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls                # start the event loop of the server to wait for calls