Característica: Recuperación de contraseña
  Como usuario del sistema de petTrack
  quiero recuperar mi contraseña para poder acceder al sitio

  Escenario: Recuperar contraseña
  Dado que ingreso a la dirección "http://192.168.33.10:8000/entrar"
  Y presiono el texto Has olvidado tu contraseña?
  Y pongo mi correo "prueapettrack@outlook.com"
  Y presiono el botón Enviar
  Entonces puedo ver que me enviaron un correo para restablecer mi contraseña


  Escenario: Correo de recuperación
  Dado que me voy al enlace "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=153&ct=1717652107&rver=7.0.6738.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fcobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26nlp%3d1%26deeplink%3dowa%252f%253frealm%253doutlook.com%26RpsCsrfState%3d337dfc11-7287-69e4-66c1-104ed9db05d1&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c"
  Y agrego mi correo "prueapettrack@outlook.com"
  Y agrego mi contraseña "testing1234"
  Y abro el correo de recuperación de contraseña
  Y abro el enlace del correo
  Y escribo la nueva contraseña "testing1234"
  Y verifico la nueva contraseña "testing1234"
  Y me voy a la pagína de inicio de sesión
  Entonces puedo ver que mi contraseña fue reestablecida correctamente