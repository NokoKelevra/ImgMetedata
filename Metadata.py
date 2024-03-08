#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
import sys
import argparse
from PIL.ExifTags import TAGS
from PIL import Image

parser = argparse.ArgumentParser(prog='Metadata.py', description='Script para extraer los metadatos de imagenes', epilog='')
parser.add_argument("-f", "--file", help="Imagen a procesar en formato jpeg o png")

parser.parse_args()
args = parser.parse_args()

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

def main():
	photo = Image.open(args.file)
	if (photo.format == 'JPEG'):
		metadatos = testForExif(photo)
		if (metadatos):
			imprimirDatos(metadatos)
	elif (photo.format == 'PNG'):
		imprimirDatos(photo.info)
	else:
		print("Introduce una imagen con extensión JPEG o PNG")

if __name__ == "__main__":
    main()