Característica: Modificar mascotas
  Como usuario del sistema de petTrack
  quiero Modificar una mascota

  Escenario: Modificar mascota correctamente
  Dado que ingreso a la url "http://localhost:8000/entrar?next=/"
  Y escribo mi usuario "Pruebas" y mi contraseña "testing1234"
  Y presiono el botón de iniciar
  y desplegar el menu usuario 
  Y presiono el boton lista de mascotas
  y prsiono el boton de editar
  y editamos el campo edad con este nuevo valor "4"
  cuando presionamos el boton guardar
  Entonces puedo ver la modificacion en la tabla

  