#!/usr/bin/env python3

import re
import sys

pile = ""
V = "âäîïàùûüôöaeiouéèêëy"
C = "zrtpmlkjhgfdsqwxcvbnç"
consonnes = list(C)
voyelles = list(V)

def consCons(pile):
	global ptr
	res = ""
	while ptr<len(pile) and pile[ptr] in consonnes:
		res += pile[ptr]
		ptr += 1
	return res

def consVoy(pile):
	global ptr
	res = ""
	while ptr<len(pile) and pile[ptr] in voyelles:
		res += pile[ptr]
		ptr += 1
	return res

# règles de découpage spécifique à appliquer
# après la règle générale
def finalize(mot):
	# deux consonnes qui se suivent après un découpage
	mot = re.sub("-(["+C+"])(["+C+"])","\\1-\\2",mot)
	# doublement de consonne avant un découpage
	mot = re.sub("([smt])\\1-","\\1-\\1",mot)
	# on enlève la coupure pour les consonnes en fin de mot
	mot = re.sub("-([zrtpmlkjhgfdsqwxcvbnç]*)$","\\1",mot)
	# découpages had oc
	mot = re.sub("([ct])-h","-\\1h",mot)
	mot = re.sub("b-([rls])","-b\\1",mot)
	mot = re.sub("([tdv])-r","-\\1r",mot)
	mot = re.sub("g-([nrl])","-g\\1",mot)
	mot = re.sub("p-([rh])","-p\\1",mot)
	mot = re.sub("oy","oi-y",mot)
	mot = re.sub("ria","ri-a",mot)
	mot = re.sub("ï-","-ï-",mot)
	mot = re.sub("oï","o-ï",mot)
	mot = re.sub("aï","a-ï",mot)
	mot = re.sub("aé","a-é",mot)
	return mot

# règle de découpage générale :
# 1) on consomme les consonnes qui se suivent
# 2) on consomme les voyelles qui se suivent
# -> coupure
def decoupe(pile):
	res = []
	while ptr < len(pile):
		tmp = consCons(pile)
		tmp += consVoy(pile)
		res.append(tmp)
	return "-".join(res)

for ligne in open(sys.argv[1]):
	ligne = ligne.rstrip()
	mot = re.sub("-","",ligne)
	ptr = 0
	motDec = finalize(decoupe(mot))
	print(mot,motDec)
