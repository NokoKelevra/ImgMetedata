#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys
from PIL.ExifTags import TAGS
from PIL import Image

def testForExif(imgFile):
	exifData = {}
	info = imgFile._getexif()
	if info:
		for (tag,value) in info.items():
			decoded = TAGS.get(tag, tag)
			exifData[decoded] = value
		return exifData
	else:
		print("No se han encontrado metadatos.")

def imprimirDatos(datos):
	for campo,valor in datos.items():
		print('[+] ' + str(campo) + ' : ' + str(valor))

photo = Image.open(sys.argv[1])
if (photo.format == 'JPEG'):
	metadatos = testForExif(photo)
	if (metadatos):
		imprimirDatos(metadatos)
elif (photo.format == 'PNG'):
	imprimirDatos(photo.info)
else:
	print("Introduce una imagen con extensión JPEG o PNG")
