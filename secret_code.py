import random
print("Welcome to coding , decoding Centre\nHere you can code your sentence and decode also!!!")
code = str(input("Enter your sentence : "))

words = code.split(" ")
select = int(input("Enter 1 for coding and 2 for decoding : "))
if select == 1:
	coding = True
else:
	coding = False
if (coding):
	newwords = []
	for word in words:
		if len(word) >=3 :
			chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
			
			r1 = ""
			r2 = ""
			for a in range(3):
				r1+=random.choice(chars)
			for a in range(3):
				r2+=random.choice(chars)
			coded = r1 + word[1 : ] + word[0] + r2
			newwords.append(coded)
		else:
			newwords.append(word[::-1])
	print(" ".join(newwords))
		
else:
	newwords = []
	for word in words:
		if len(word) >=3 :
			coded = word[3:-3]
			coded = coded[-1] + coded [:-1]
			newwords.append(coded)
		else:
			newwords.append(word[::-1])
	print(" ".join(newwords))
	