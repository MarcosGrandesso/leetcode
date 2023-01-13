# https://leetcode.com/problems/roman-to-integer/
# codigo pra jogar no leetcode ta comentado no final do arquivo 

# ENTRADAS
e1 = "III"
e2 = "LVIII"
e3 = "MCMXCIV"

# QUANTO VALE CADA ALGARISMO ROMANO
values = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000,
}

def roman_to_int(ROMAN):
	x = 0
	atual = None
	anterior = None

	for letra in reversed(ROMAN):
		atual = values[letra]
		if anterior is None:
			x+= values[letra]

		elif atual < anterior:
			x-= values[letra]

		else:
			x+= values[letra]
		anterior = atual

	print(" ")
	print(F"o Algarismo romano {ROMAN} corresponde há {abs(x)}")
	print(" ")


roman_to_int(e1)
roman_to_int(e2)
roman_to_int(e3)

# jogue no leet code essa bomba aqui q passa
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         values = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000,
#         }

#         x = 0
#         atual = None
#         anterior = None

#         for letra in reversed(s):
#             atual = values[letra]
#             if anterior is None:
#                 x+= values[letra]

#             elif atual < anterior:
#                 x-= values[letra]

#             else:
#                 x+= values[letra]
#             anterior = atual
#         return abs(x)