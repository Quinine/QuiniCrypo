#!/usr/bin/python
# QuiniCrypo version 1.1, Base64
# Filename: QuiniCrypoBase64.py
# Author: Kinine
version = '0.3'
import base64
import re

def base64_isvalid(string):
	match = re.match("^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$", string)
	if match is not None:
   		return "valid"
   	else:
   		return "notvalid"

def encode_base64x(string, layers):
		tmp_string = string
		for x in range(0, layers):
			print "yeah that's the %d'th time " % (x + 1)
			temp = base64.b64encode(tmp_string)
			tmp_string = temp
		return tmp_string

def encode_base64(string):
	temp = base64.b64encode(string)
	return temp

def decode_base64x(string, layers):
		tmp_string = string
		for x in range(0, layers):
			x += 1
			print "that's %d layers of encoding" % x
			temp = base64.b64decode(tmp_string)
			tmp_string = temp
		return tmp_string

def decode_base64(string):
	temp = base64.b64decode(string)
	return temp

def decode_base64_auto(string):
	if base64_isvalid(string) == "valid":
		x = 0
		tmp_string = string
		while base64_isvalid(tmp_string) == "valid":
				x += 1
				print "that's %d layers of encoding" % x
				temp = base64.b64decode(tmp_string)
				tmp_string = temp
		return tmp_string
	else:
		print "that's no valid bro"
# End of QuiniCrypoBase64.py