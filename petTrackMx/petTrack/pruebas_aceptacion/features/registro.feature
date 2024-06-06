Característica: Registro de usuario
  Como usuario nuevo del sistema de petTrack
  quiero registrarme para poder acceder al sitio

  Escenario: Registro exitoso
  Dado que ingreso al enlace "http://192.168.33.10:8000/entrar"
  Y presiono el botón Regístrate
  Y en la pantalla de registro escribo el nomre de usuario "Pruebas" y el correo "prueapettrack@outlook.com" y la contraseña "testing1234" y repito la contraseña "testing1234"
  Cuando presiono el botón de Registrarse
  Entonces puedo ver que me envió un coreo de verificación

  Escenario: Validar correo
  Dado que ingreso a la udirección "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=153&ct=1717652107&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f%253frealm%253doutlook.com%26RpsCsrfState%3d337dfc11-7287-69e4-66c1-104ed9db05d1&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c"
  Y escribo mi correo "prueapettrack@outlook.com" y presiono el otón siguiente
  Y escribo mi contraseña "testing1234"
  Y presiono el botón de Iniciar sesión
  Y presiono el botón de mantener sesión iniciada
  Y abro el correo de verificación
  Y presiono el botón de verificación
  Entonces puedo ver el mensaje de que mi correo fue verificado