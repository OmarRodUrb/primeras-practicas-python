print ("introduce una contraseña")
contrasena = str (input ())
print ("confirma tu contraseña") 
confirmacion = str (input ())
if contrasena  == confirmacion :
    print ("tu nueva contraseña es: ",contrasena)
else :
    print ("las contraseñas no coinciden")