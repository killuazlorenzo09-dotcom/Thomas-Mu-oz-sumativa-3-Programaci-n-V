# API RESTful de Temperaturas de Ciudades de Venezuela

Este proyecto implementa una API RESTful simple utilizando **Django** y **Django REST Framework (DRF)** para gestionar registros de temperatura por ciudad. Cumple con los requisitos de autenticación (Token) para las operaciones de escritura/modificación.

---

Requisitos e Instalación

Clonar el Repositorio
git clone [https://github.com/killuazorenzo09-dotcom/Thomas-Mu-oz-sumativa-3-Programaci-n-V.git](https://github.com/killuazorenzo09-dotcom/Thomas-Mu-oz-sumativa-3-Programaci-n-V.git)
cd Thomas-Mu-oz-sumativa-3-Programaci-n-V

 Guía de Prueba de Endpoints (Postman)

El servidor debe estar corriendo para iniciar las pruebas: python manage.py runserver

 Obtener Token (Autenticación)

Este paso es obligatorio para obtener el Token de acceso que permite las operaciones de escritura/modificación.

* **Método:** POST
* **URL:** http://127.0.0.1:8000/api/get-token/
* **Body (JSON):**
    json
    {
        "username": "personal",
        "password": "personal1234"
    }
  
**Respuesta esperada:** {"token": "..."}

Crear un Registro (POST Protegido)

Esta es una operación de escritura y **requiere el Token** obtenido en el Paso 1.

* **Método:** POST
* **URL:** http://127.0.0.1:8000/api/temperatures/
* **Headers:**
    * Authorization: Token <PEGAR_TU_TOKEN_AQUÍ>
    * Content-Type: application/json
  **Body (JSON):**
    json
    {
        "city": "Ciudad Prueba",
        "temperature": "35.0"
    }
    
 **Respuesta esperada:** 201 Created
