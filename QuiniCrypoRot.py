#!/usr/bin/python
# QuiniCrypo version 1.1, Base64
# Filename: QuiniCrypoRot.py
# Author: Kinine
version = '0.3'
import string

def abc_percentage(string, letter):
	length = len(string)
	occurence = string.count(letter)
	percentage = float(float(occurence)/float(length)*100)
	
	return percentage

def english_rightness(string):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
	'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
	eng_frequency = {
		'a':8.167,'b':1.492,'c':2.782,'d':4.253,
		'e':12.702,'f':2.228,'g':2.015,'h':6.094,
		'i':6.966,'j':0.153,'k':0.772,'l':4.025,
		'm':2.406,'n':6.749,'o':7.507,'p':1.929,
		'q':0.095,'r':5.987,'s':6.327,'t':9.056,
		'u':2.758,'v':0.978,'w':2.360,'x':0.150,
		'y':1.974,'z':0.074
	}
	pentaltypoints = 0.000000000
	rightness = 0.000000000
	for x in range(0, 26):
		pentaltypoints += abs(abc_percentage(string, alphabet[x])-eng_frequency[(alphabet[x])])
	return pentaltypoints

def rot_chooser(string):
	rots = {}
	for x in range (0, 26):
		rots[x]=english_rightness(rot_n(string, x))
     	v=list(rots.values())
     	k=list(rots.keys())
     	rot_key = k[v.index(min(v))]
     	return rot_key

def rot_autosolve(string):
	solved_rot = rot_n(string, rot_chooser(string))
	return solved_rot


def rot_convertchipher(n):
	convertedchipher = abs(n - 26)
	return convertedchipher


def rot_n(encrypted_string,x):
	decodedstring = encrypted_string.translate(
		string.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[x:] +
           string.ascii_uppercase[:x] +
           string.ascii_lowercase[x:] +
           string.ascii_lowercase[:x]
           )
       )
	return decodedstring
# End of QuiniCrypoRot.py