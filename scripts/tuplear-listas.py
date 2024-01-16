#!/usr/bin/env python3

odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8]

#no tienen los mismos numero de elementos una tiene 4 y la otra 5

result = zip(odd_numbers,even_numbers)

for element in result:
        print (element) # solo aparecen las tuplas que puede formar el numero 9 no aparece 
        # (1, 2)
        # (3, 4)
        # (5, 6)
        # (7, 8)
	#print (type(element)) # regresa <class tuple>
