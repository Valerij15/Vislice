import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA, PORAZ = 'W', 'X'

class Igra:

	def __init__(self, geslo, crke):
		self.geslo = geslo
		self.crke = crke

	def napacne_crke(self):
		napacne = []
		for i in self.crke:
			if i not in self.geslo.upper():
				napacne.append(i)
		return napacne

	def pravilne_crke(self):
		pravilne = []
		for i in self.crke:
			if i in self.geslo.upper():
				pravilne.append(i)
		return pravilne

	def stevilo_napak(self):
		napake = 0
		for i in self.crke:
			if i not in self.geslo.upper():
				napake += 1
		return napake

	def zmaga(self):
		for i in self.geslo.upper():
			if i not in self.crke:
				return False
		return True
		
	def poraz(self):
		return self.stevilo_napak() == STEVILO_DOVOLJENIH_NAPAK

	def pravilni_del_gesla(self):
		niz = ""
		for i in self.geslo.upper():
			if i in self.crke:
				niz += i
			else:
				niz += "_"
		return niz

	def nepravilni_ugibi(self):
		niz = ""
		for i in self.napacne_crke():
			niz += i + " "
		return niz

	def ugibaj(self, crka):
		crka = crka.upper()
		if(crka in self.crke):
			return PONOVLJENA_CRKA
		self.crke += crka
		if(self.zmaga()):
			return ZMAGA
		elif(crka in self.pravilne_crke()):
			return PRAVILNA_CRKA
		else:
			return NAPACNA_CRKA

def nova_igra():
	beseda = random.choice(bazen_besed)
	return Igra(beseda, "")

f = open("besede.txt", "r", encoding = "utf-8")
bazen_besed = []
for x in f:
	bazen_besed.append(x.replace("\n", ""))
f.close()
