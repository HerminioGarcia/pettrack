
Característica: Inicio de Sesión
  Como usuario del sistema de petTrack
  quiero iniciar sesión para ingresar al inicio del sitio

  Escenario: Credenciales validas
  Dado que ingreso a la url "http://localhost:8000/entrar?next=/"
  Y escribo mi usuario "minitros555" y mi contraseña "chile10203986"
  Cuando presiono el botón de iniciar
  Entonces puedo ver que pude entrar exitosamente a la pagina de "adolfo"

  Escenario: Credenciales invalidas
  Dado que ingreso a la url "http://localhost:8000/entrar?next=/"
  Y escribo mi usuario incorrecto "usuario-incorrecto" y mi password incorrecta "incorrecto" 
  Cuando presiono el botón de iniciar
  Entonces puedo ver "Contraseña y/o Equipo incorrecto."

  