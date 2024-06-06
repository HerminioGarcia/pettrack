Característica: eliminar mascota
  Como usuario del sistema de petTrack
  quiero eliminar una mascota de mi lista
  para no tener en la lista mascotas no deseadas

  Escenario: eliminar mascota correctamente
  Dado que ingreso a la url "http://localhost:8000/entrar?next=/"
  Y escribo mi usuario "Pruebas" y mi contraseña "testing1234"
  Y presiono el botón de iniciar
  y desplegar el menu usuario 
  Y presiono el boton lista de mascotas
  y cuando el boton de eliminar
  Entonces puedo ver que la mascota ya no esta en la tabla 