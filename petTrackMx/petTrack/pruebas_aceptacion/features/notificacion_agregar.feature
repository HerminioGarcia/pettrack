Característica: Buscar correo electrónico en Gmail
    Como usuario
    Quiero buscar un correo electrónico específico en Gmail
    Para poder encontrarlo fácilmente

Escenario: Buscar correo electrónico específico
    Dado que el navegador está abierto caso agregar 1
    Cuando navego a Gmail e ingreso mi correo electrónico y contraseña y busco "caphdfa@gmail.com"
    Entonces debería ver el correo electrónico "caphdfa@gmail.com"

Escenario: Buscar correo electrónico específico con errores
    Dado que el navegador está abierto caso agregar 2
    Cuando navego a Gmail e ingreso mi correo electrónico y contraseña incorrectamente y busco "caphdfa@gmail.com"
    Entonces debería ver un mensaje de error