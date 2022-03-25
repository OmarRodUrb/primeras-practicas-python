print ("inserta tu año de nacimiento")
anioN = int (input ())
print ("inserta tu mes de nacimiento EJEMPLO Enero 01 Febrero 02 ETC")
print ("recuerda no tilizar numeros mallores a 12")
#codigo que restrinja poner numeros mallores a 12 
mesN = int (input ())
if mesN > 12:
    print ("dato no valido")
    quit ()
print ("inserta el año actual")
anioA = int (input ())
print ("inserta mes actual en formato numerico. EJEMPLO Enero = 01 Febrero = 02 ETC")
print ("recuerda no tilizar numeros mallores a 12")
#codigo que restrinja poner numeros mallores a 12
mesA = int (input ())
if mesN > 12:
    print ("dato no valido")
    quit ()
edad = str (anioA - anioN)
Meses = str (mesA - mesN)
if mesA < mesN :
    edad = edad - 1
    Meses = Meses + 12
print (" tu edad es " + edad + " años con " + Meses + " meses")
