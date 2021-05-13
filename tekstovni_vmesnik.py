import model

def izpis_igre(igra):
	if igra.stevilo_napak() == 0:
		slika = f''''''
	elif igra.stevilo_napak() == 1:
		slika = f'''\n
_|______'''
	elif igra.stevilo_napak() == 2:
		slika = f'''\n
 |
_|______'''
	elif igra.stevilo_napak() == 3:
		slika = f'''\n
 |
 |
_|______'''
	elif igra.stevilo_napak() == 4:
		slika = f'''\n
 |
 |
 |
_|______'''
	elif igra.stevilo_napak() == 5:
		slika = f'''\n
 |
 |
 |
 |
_|______'''
	elif igra.stevilo_napak() == 6:
		slika = f'''\n
 _____
 |
 |
 |
 |
_|______'''
	elif igra.stevilo_napak() == 7:
		slika = f'''\n
 _____
 |   |
 |
 |
 |
_|______'''

	elif igra.stevilo_napak() == 8:
		slika = f'''\n
 _____
 |   |
 |   o
 |
 |
_|______'''
	elif igra.stevilo_napak() == 9:
		slika = f'''\n
 _____
 |   |
 |   o
 |  /|\\ 
 |
_|______'''
	elif igra.stevilo_napak() == 10:
		slika = f'''\n
 _____
 |   |
 |   o
 |  /|\\ 
 |  / \\ 
_|______
'''
	besedilo = f'''####################################\n
	{igra.pravilni_del_gesla()}\n
	Število poskusov: {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}\n
	Nepravilni ugibi: {igra.nepravilni_ugibi()}\n
	{slika}\n
####################################'''
	return besedilo

def izpis_zmage(igra):
	besedilo = f'''####################################\n
	BRAVO! ZMAGALI STE!!!!\n
	UGANILI STE BESEDO: {igra.pravilni_del_gesla()}\n
####################################'''
	return besedilo

def izpis_poraza(igra):
	slika = f'''\n
 _____
 |   |
 |   o
 |  /|\\ 
 |  / \\ 
_|______
'''
	besedilo = f'''####################################\n
Prekoračili ste število nepravilnih ugibov, beseda je bila {igra.geslo}.\n
	{slika}\n
####################################'''
	return besedilo

def zahtevaj_vnos():
	vnos = input("Vpišite črko: ")
	while(not vnos.isalpha() or len(vnos) > 1):
		print("Nepravilen vnos!")
		vnos = input("Vpišite črko: ")
	return vnos

def pozeni_vmesnik():
	igra = model.nova_igra()
	igranje = True
	while igranje:
		naprej = ""
		print(igra.ugibaj(zahtevaj_vnos()))
		if(igra.zmaga()):
			print(izpis_zmage(igra))
			while(naprej != "ne" and naprej != "ja"):
				naprej = input("Želite nadaljevati? (ja/ne)\n")
				if(naprej == "ne"):
					igranje = False
				elif(naprej == "ja"):
					igra = model.nova_igra()
				else:
					print("Nepravilen vnos!")
		elif(igra.poraz()):
			print(izpis_poraza(igra))
			while(naprej != "ne" and naprej != "ja"):
				naprej = input("Želite nadaljevati? (ja/ne)\n")
				if(naprej == "ne"):
					igranje = False
				elif(naprej == "ja"):
					igra = model.nova_igra()
				else:
					print("Nepravilen vnos!")
		else:
			print(izpis_igre(igra))

pozeni_vmesnik()