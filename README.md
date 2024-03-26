# SportApp

## Gestor Usuarios

Aplicación encargada de realizar todas las operaciones necesarias del sistema relacionadas con los deportistas exceptuando su registro.

## Iniciar la aplicación

La aplicación está construida con [Flask](https://flask.palletsprojects.com/en/3.0.x/) y [pipenv](https://pipenv-es.readthedocs.io/es/latest/).

Para ejecutar la aplicación localmente primero se debe configurar el archivo .env con los valores adecuados a utilizar en las variables de ambiente. En el repositorio se encuentra el archivo .env.example el cual tiene la estructura básica con la información que debe configurar para que la aplicación pueda subir de forma correcta, solo es necesario copiar el archivo y cambiar el nombre y extensión a .env y posteriormente configurar los valores apropiados al ambiente de ejecución.

Antes de ejecutar cualquier aplicación Python del sistema SportApp se debe tener una única instancia de la base de datos. Todos los proyectos cuentan con una carpeta db la cual tiene el Docker Compose ejemplo para crear una instancia de PostgreSQL.

Si no cuenta con la base de datos creada puede ejecutar desde la ruta ./db el siguiente comando:

- `docker-compose up -d`

Una vez se tengan configuradas las variables de ambiente y la base de datos este arriba, puede subir de forma local la aplicación de las siguientes maneras:

### Flask

Ejecutar los siguientes comandos desde la ruta del proyecto a nivel del archivo Pipfile:

1. `pipenv shell`
2. `pipenv install`
3. `FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3000`

Si requiere iniciar la aplicación para desarrollar nuevas funcionalidades o corregir defectos y desea que cada modificación se carque automáticamente puede agregar la opción reload:

- `FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 3000 --reload`

### Docker

El proyecto cuenta con el archivo Dockerfile con toda la configuración necesaria para ejecutar la aplicación a través de [gunicorn](https://flask.palletsprojects.com/en/3.0.x/deploying/gunicorn/). Para crear la imagen y correr la aplicación mediante un contenedor debe ejecutar los siguientes comandos en el orden establecido:

1. `docker build . -t sport-app-gestor-usuarios`
2. `docker run -p 3000:3000 --name gestor-usuarios --env-file .env sport-app-gestor-usuarios`

## Pruebas unitarias

Las pruebas unitarias se realizan a través de la herramienta [pytest](https://docs.pytest.org/en/8.0.x/). El proyecto cuenta con el archivo pytest.ini con la configuración del log para la ejecución de pruebas.

Para correr las pruebas unitarias es necesario tener configuradas las variables de ambiente en el archivo .env como se indica en la sección **Iniciar la aplicación**. Puede ejecutar las pruebas unitarias con el siguiente comando:

- `pytest --cov-fail-under=70 --cov=src --cov-report=html`

Una vez se ejecute el comando, se corren todas las pruebas unitarias y se elabora el reporte de cobertura que puede visualizar en un navegador abriendo el archivo ./htmlcov/index.html
