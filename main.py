#!/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------
# author      : Ahmet Ozlu
# mail        : ahmetozlu93@gmail.com
# date        : 05.05.2019
# -----------------------------------------

import cv2
import dewapper
import unsharpen
import color_correlation
import signature_extractor

source_image = cv2.imread("test.jpg")
img = 0
try:	
	# read the source input image and call the dewarp_book function to perform cropping with the margin and book dewarping
	img = dewapper.dewarp_book(source_image)
	print("- step1 (cropping with the argins + book dewarpping): OK")
except Exception as e:
	print("type error: " + str(e))
	print("ERROR IN CROPPING & BOOK DEWARPING! PLEASE CHECK LIGTHNING, SHADOW, ZOOM LEVEL AND ETC. OF YOUR INPUT BOOK IMAGE!")
try:
	# call the unsharpen_mask method to perform unsharpening mask
	unsharpen.unsharpen_mask(img)
	print("- step2 (unsharpening mask): OK")
except Exception as e:
	print("type error: " + str(e))
	print("ERROR IN BOOK UNSHARPING MASK! PLEASE CHECK LIGTHNING, SHADOW, ZOOM LEVEL AND ETC. OF YOUR INPUT BOOK IMAGE!")
try:
	# call the funcBrightContrast method to perform color correction
	img = color_correlation.funcBrightContrast(img)
	cv2.imwrite("sa.jpg", img)
	print("- step3 (color correlation): OK")
except Exception as e:
	print("type error: " + str(e))
	print("ERROR IN BOOK COLOR CORRELATION! PLEASE CHECK LIGTHNING, SHADOW, ZOOM LEVEL AND ETC. OF YOUR INPUT BOOK IMAGE!")
signature_extractor.extract_signature(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
