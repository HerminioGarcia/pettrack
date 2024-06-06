# language: es
Característica: Ver usuarios en el panel de administración de Django

  Escenario: Ver la lista de usuarios
    Dado que el administrador ha iniciado sesión en el panel de administración caso usuarios totales 1
    Cuando el administrador ingresa a la url "http://localhost:8000/admin"
    Y navega en la página de usuarios
    Entonces el administrador debería ver la lista de todos los usuarios

  Escenario: Ver los detalles de un usuario
    Dado que el administrador ha iniciado sesión en el panel de administración caso usuarios totales 2
    Y el administrador está en la página de usuarios
    Cuando el administrador hace clic en un usuario
    Entonces el administrador debería ver los detalles de ese usuario