# flask_rest_api_example
Es un ejemplo de API Rest en Flask

1. Se deben los siguiente comandos para alistar nuestro entorno virtual
```bash
# Crear un entorno virtual
python3 -m venv venv
# activar el entorno virtual
source venv/bin/activate
# En caso de que se quiera desactivar el entorno virtual
deactivate
# instalar nuestras dependencias
pip3 install -r requirements.txt

```
2. Se debe correr el proyecto
```bash
# Estar seguros de que estamos en nuestra raiz del proyecto 
# donde se encuentra el app.py y corremos el api con el puerto
# que necesitamos donde corra
flask run -p 5001
```

3. Para correrlo en docker
```bash
# Subir el contenedor o grupo de contenedores
docker-compose up -d --build
# Bajar el contenedor o grupo de contenedores
docker-compose down
```