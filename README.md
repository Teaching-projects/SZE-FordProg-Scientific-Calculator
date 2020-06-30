# SZE-FordProg-Scientific-Calculator

  A Scientific Calculator az alábbi műveletek elvégzésére alkalmas:

    -Alapműveletek ( * , / , + , - )   
    -Trigonometrikus függvények ( sin, cos, tan, arc-sin,
                              arc-cos, arc-tan)
    -Logaritmus műveletek 
    -Számhatványozás ( pow )
    -Négyzetgyökvonás ( Sqrt )
    -Abszolútérték ( Abs )

# Példák a működésre:
  •	Alapműveletek 
	
	  >>>> 5+5-3*5
	  10
	  15
	  -5
	  >>>> -3-3/2.5
	  1.2
	  -4.2



   • Trigonometrikus függvények


	  >>>> cos(5)
	  0.28366218546322625
	  >>>> sin(5)
	  -0.9589242746631385
	  >>>> tan(5)
	  -3.380515006246586
	  >>>> acos(5)
	  The adjusted value ('acos') must be between -1 and 1!
	  >>>> acos(1)
	  0.0
	  >>>> asin(0.5)
	  0.5235987755982989
	  >>>> atan(0.2)
	  0.147036858253309
	  >>>> acos(1) + asin(0.5)
	  0.0
	  0.5235987755982989
	  0.5235987755982989


  •	Logaritmus műveletek


	  >>>> log10(5)
	  0.6989700043360189
	  >>>> log2(5)
	  2.321928094887362
	  >>>> log5(5)
	  1.0
	  >>>> log30(5)
	  0.4731974454383393
	  >>>> log5(5) * log2(5)
	  1.0
	  2.321928094887362
	  2.321928094887362
	  >>>> log10(5) * log2(5)
	  0.6989700043360189
	  2.321928094887362
	  1.6229580905513437


   • Számhatványozás


	  >>>> pow(3,2)
	  9.0
	  >>>> pow(3,3)
	  27.0
	  >>>> pow(3,4)
	  81.0
	  >>>> pow(3,1)
	  3.0
	  >>>> pow(3,2) * pow(3,3) / 5
	  9.0
	  27.0
	  243.0
	  48.6


  •	Négyzetgyökvonás


	  >>>> sqrt(16)
	  4.0
	  >>>> sqrt(9)
	  3.0
	  >>>> sqrt(15)
	  3.872983346207417
	  >>>> sqrt(pow(4,2))
	  16.0
	  4.0


  •	Abszolútérték


	  >>>> abs(-33)
	  33
	  >>>> abs(33)
	  33
	  >>>> abs(-33) * 2
	  33
	  66
# Felhasznált források
	PLY (Python Lex-Yacc) David M. Beazley - https://www.dabeaz.com/ply/ply.html
	Make your Own Calculator in Python - https://youtu.be/Hh49BXmHxX8 
	Make Your Own Programming Language - https://youtu.be/LDDRn2f9fUk
	Getting Started with Pyparsing - https://learning.oreilly.com/library/view/getting-started-with/9780596514235/
