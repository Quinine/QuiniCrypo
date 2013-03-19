#!/usr/bin/python
# QuiniCrypo version 1.1, Demo
# Filename: RotCipher.py
# Author: Quinine
import QuiniCrypoRot

def dechipher_demo(ciphertext):
	print """	The deciphered text is probaly: '%s',
	rot %d was used to decipher the message, 
	which means the chipher with which it was encoded was rot %d\n""" % (
		 QuiniCrypoRot.rot_autosolve(ciphertext) ,
		 QuiniCrypoRot.rot_chooser(ciphertext) ,
		 QuiniCrypoRot.rot_convertchipher(QuiniCrypoRot.rot_chooser(ciphertext))
	)

dechipher_demo("fecp kyivv nfiuj")
dechipher_demo("jajs xmtwyjw")
dechipher_demo("kxydrobcrybdcoxdoxmo")
dechipher_demo("uocnn ugpvgpeg ")
dechipher_demo("Bpm twvomz bpm bmfb, bpm uwzm zmtqijtm qb qa qvlmml, jcb qb ewzsa ycqbm emtt eqbp apwzb bmfba bww. ")
# End of RotChiperDemo.py