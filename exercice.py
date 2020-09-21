#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	TAX_RATE = 0.15

	#Calculer le sous-total (sommes des items)
	sum = 0
	for item in data:
		sum += item[INDEX_QUANTITY]*item[INDEX_PRICE]

	#Calciler les taxes et total
	taxes = TAX_RATE * sum
	total = sum + taxes

	#Retourner la facture formatée (sous-total, taxes, total)
	titles =[
			"SOUS TOTAL ",
			"TAXES      ",
			"TOTAL      "
	]

	bill_data = [
		("SOUS TOTAL", sum),
		("TAXES     ", sum),
		("TOTAL     ", sum)
	]
	result = name
	for bd in bill_data:
		result += "\n" + f"bd[0] {bd[1] : >10.2f} $"

	#Code avec repetition
	result = name
	result += "\n" + f"SOUS TOTAL {sum : >10.2f} $"
	result += "\n" + f"TAXES      {taxes : >10.2f} $"
	result += "\n" + f"TOTAL      {total : >10.2f} $"
	return result


def format_number(number, num_decimal_digits):
	#Separer les parties entiere et decimale
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))

	#Formater la partie decimale
			#decimal_str = f"{decimal_part :.{num_decimal_digits}f}"[1:]
	decimal_str = str(int(round(decimal_part * 10**num_decimal_digits)))
	decimal_str = "." + "0" * ((num_decimal_digits) - len(decimal_str)) + decimal_str

	#Formater la partie entiere
	whole_part_str = ""
	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part //= 1000
	whole_part_str = str(whole_part) + whole_part_str
	#Concaterner les deux parties
	return ("-" if number < 1 else "") + whole_part_str + decimal_str

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"

	#Calcler la largeur
	triangle_wicth = 1 + 2* (num_rows-1)

	#Construire premiere et derniere ligne (bordures pleines)
	border_row = BORDER_CHAR * (triangle_wicth +2)

	#Afficher le triangle
	result = border_row
	#Pour chaque ligne du triangle
	for i in range(num_rows):
		num_triangle_chars = i * 2 + 1
		triangle_chars =  TRIANGLE_CHAR * num_triangle_chars
		triangle_line = f"{triangle_chars : ^{triangle_wicth}}"
		result += "\n" + BORDER_CHAR + triangle_line + BORDER_CHAR
	result += "\n" + border_row
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print("----------------------------------------")

	print(format_number(-12345.678, 2))

	print("----------------------------------------")

	print(get_triangle(2))
	print(get_triangle(5))
