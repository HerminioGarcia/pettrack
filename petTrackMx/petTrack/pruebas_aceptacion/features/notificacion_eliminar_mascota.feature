Característica: Eliminar Mascota
  Como usuario nuevo del sistema de petTrack
  quiero eliminar mi mascota y verificar si si llego el correo

Escenario: eliminar mascota correctamente
  Dado que ingreso a la url "http://localhost:8000/entrar?next=/"
  Y escribo mi usuario "Pruebas" y mi contraseña "testing1234"3986"
  Y presiono el botón de iniciar
  y desplegar el menu usuario 
  Y presiono el boton lista de mascotas
  y cuando el boton de eliminar
  Entonces puedo ver que la mascota ya no esta en la tabla 

Escenario: Validar notificacion en correo
  Dado que ingreso a la udirección "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=153&ct=1717652107&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f%253frealm%253doutlook.com%26RpsCsrfState%3d337dfc11-7287-69e4-66c1-104ed9db05d1&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c"
  Y escribo mi correo "prueapettrack@outlook.com" y presiono el otón siguiente
  Y escribo mi contraseña "testing1234"
  Y presiono el botón de Iniciar sesión
  Y presiono el botón de mantener sesión iniciada
  Y cuando presiono el boton el correo de verificación de eliminacion
  Entonces puedo ver la mascota ha sido eliminada correctamente