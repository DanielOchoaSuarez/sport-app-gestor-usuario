# SportApp

## Gestor Usuarios

Aplicación encargada de realizar todas las operaciones necesarias del sistema relacionadas con los deportistas exceptuando su registro.

## Iniciar la aplicación

La aplicación está construida con [Flask](https://flask.palletsprojects.com/en/3.0.x/) y [pipenv](https://pipenv-es.readthedocs.io/es/latest/). Para ejecutarla localmente primero se debe configurar el archivo .env con los valores adecuados a utilizar en las variables de ambiente. En el repositorio se encuentra el archivo .env.example el cual tiene la estructura básica con la información que debe configurar para que la aplicación pueda subir de forma correcta, solo es necesario cambiar el nombre y extensión del archivo por .env y configurar los valores apropiados al ambiente de ejecución.

Una vez configuradas las variables de ambiente la aplicación puede subir de forma local de las siguientes maneras:

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

docker tag health-check:latest localhost:5000/health-check:latest
docker push localhost:5000/health-check:latest

kubectl get namespaces
kubectl create namespace desarrollo

kubectl get pods --namespace=desarrollo
kubectl get pods --namespace=desarrollo -o wide

kubectl get deployments --namespace=desarrollo
kubectl delete deployment health-check --namespace=desarrollo

kubectl logs health-check-5894697989-t42lc --namespace=desarrollo
kubectl describe pod health-check-5894697989-t42lc --namespace=desarrollo

kubectl get secrets --namespace=desarrollo
kubectl describe secret appsecrets --namespace=desarrollo

kubectl apply -f ./k8s/k8s-secrets.yaml

kubectl apply -f ./k8s/k8s-health-check.yaml

kubectl exec -it health-check-5894697989-t42lc --namespace=desarrollo -n desarrollo -- wget http://health-check-service.desarrollo.svc.cluster.local:80/health/ping
