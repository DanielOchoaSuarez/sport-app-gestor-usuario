# Probar Kubernetes Local

Para realizar pruebas localmente se debe tener instalado Docker, Docker Registry y configurado un clúster de Kubernetes.
El archivo ./k8s/docker-compose.yml tiene la configuración necesaria para crear un contenedor Registry y realizar pruebas locales.
Para realizar la prueba local ejecutar los siguientes comandos en el orden establecido:

## Crear imagen y publicarla

1. `pipenv shell`
2. `pipenv install`
3. `docker build . -t sport-app-gestor-usuarios`
4. `docker tag sport-app-gestor-usuarios:latest localhost:5000/sport-app-gestor-usuarios:latest`
5. `docker push localhost:5000/sport-app-gestor-usuarios:latest`

## Crear el namespace desarrollo

6. `kubectl create namespace desarrollo`

## Desplegar secretos y aplicación

7. `kubectl apply -f ./k8s/k8s-gestor-usuarios-secrets.yaml`
8. `kubectl apply -f ./k8s/k8s-gestor-usuarios.yaml`

## Probar aplicación

9. Abrir un navegador con la dirección http://127.0.0.1:8080/gestor-usuarios/health/ping

## Comandos útiles para ejecutar pruebas

- Namespace

```
kubectl get namespaces
kubectl create namespace desarrollo
kubectl delete namespace desarrollo
```

- Pods

```
kubectl get pods --namespace=desarrollo
kubectl get pods --namespace=desarrollo -o wide
kubectl describe pod <nombre_pod> --namespace=desarrollo
```

- Deployments

```
kubectl get deployments --namespace=desarrollo
kubectl apply -f ./k8s/k8s-gestor-usuarios.yaml
kubectl delete deployment gestor-usuarios --namespace=desarrollo
```

- Secrets

```
kubectl get secrets --namespace=desarrollo
kubectl apply -f ./k8s/k8s-secrets.yaml
kubectl describe secret gestor-usuarios-secrets --namespace=desarrollo
```

- Probar conexión interna a tráves del service

```
kubectl exec -it <nombre_pod> --namespace=desarrollo -n desarrollo -- wget -qO- http://gestor-usuarios-service.desarrollo.svc.cluster.local:8080/gestor-usuarios/health/ping
```
