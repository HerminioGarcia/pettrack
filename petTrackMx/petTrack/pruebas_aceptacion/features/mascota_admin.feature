Característica: Inicio de Sesión admin
  Como administrador del sistema de petTrack
  quiero iniciar sesión para visualizas dashboard de mascotas

  Escenario: Credenciales validas admin
  Dado que ingreso url "http://localhost:8000/admin/login/?next=/admin/"
  Y usuario "Mino20Mtz" contrasena "chile10203986"
  Y presiono el boton de identificarse
  Y puedo ver mi usuario "MINO20MTZ"
  Cuando presiono mascotas
  Entonces puedo ver msj "Seleccione mascota a modificar"