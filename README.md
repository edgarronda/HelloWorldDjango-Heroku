# HelloWorldDjango-Heroku
Promote Django to Heroku step by step.

## Crear cuenta en Heroku.
* Lo primero que requerimos es crear nuestra cuenta en Heroku, para esto visitamos
[https://signup.heroku.com/login](https://signup.heroku.com/login) y creamos una cuenta
gratuita.

* Una vez que tenemos nuestra cuenta procedemos a iniciar sesion, al ingresar tendremos un 
dashboard similar a este, el de ejemplo ya cuenta con alguans APPS, el tuyo si es nuevo estara vacio.
[Imgur](https://i.imgur.com/SUPkRoz.png)


## Crear un Pipeline.
Un Pipeline es una flujo estructurado para un grupo de APPS de un mismo repositorio, cada APP esta ligada a un branch en especifico de nuestro repo, en nuestro caso vamos a crear un Pipeline el cual contendra 2 APPS (Prod y Staging). Nuestra estructura sera:

Pipeline
    |__ Prod: Esta APP estara ligada a nuestro branch Master, fungira como produccion.
    |__ Staging: Esta APP estara ligada a nuestro branch Develop, fungira como Staging.

Existen varias formas de controlar el flujo de nuestra APP en Heroku por medio de herramientas de CD en Heroku, para nuestro ejemplo solo montaremos la estructura y seguiremos el flujo de la estructura de arriba.

Cada commit o PR en el brnch de Develop se mandara a nuestra app Staging de Heroku.

* Para crear nuestro Pipeline en nuestro panel en la parte superior derecha seleccionamos 
NEW -> CREATE NEW PIPELINE.
[Imgur](https://i.imgur.com/2C1RG5W.png)

* Llenamos el siguiente formato:
    Pipeline name: El nombre en minusculas de nuestro pipeline.
    Pipeline Owner: Si pertenemos a ORGS en nuestra cuenta, aqui se pueden asignar a alguna o nuestra cuenta.
    Connect to Github: Requerimos conectarnos para hacer uso de la integracion con Github y selecionar nuestro Repo. Aqui buscamos y selecionamos nuestro repo que deseamos conectar con Heroku.
[Imgur](https://i.imgur.com/3dCpSU9.png)

* Una vez conectado nuestro repo, observaremos una pantalla similar, finalizamos seleccionando CREATE PIPELINE.
[Imgur](https://i.imgur.com/N5Fmaxa.png)

* Ya tenemos nuestro Pipeline y tenemos 2 espacios listos para crear apps y onectar con un branch de nuestro repo. En esta caso como ya vimos tendremos Staging y Production.
[Imgur](https://i.imgur.com/nCIhuLw.png)


## Crear nuestras Apps en el Pipeline
* Procedemos a crear nuestra App de Staging que estar conectada a nuestro branch DEVELOP. Para esto seleccionamos ADD APP sobre nuestro cuadro de STAGING.
[Imgur](https://i.imgur.com/nCIhuLw.png)

* A continuacion llenamos con el nombre que deseamos para nuestra app y seleccionamos CREATE NEW APP.
[Imgur](https://i.imgur.com/UqByO75.png)

* En la siguiente pantalla validamos el nombre de nuestra APP asi como la region del server donde vivira.
confirmamos seleccionando CREATE APP.
[Imgur](https://i.imgur.com/cwuTegP.png)

* Hemos creado nuestra app de Staging, ahora procedemos a ligarla con nuestro branch DEVELOP, para eso seleccionamos la opcion <> y luego CONFIGURE AUTOMATIC DEPLOYS.
[Imgur](https://i.imgur.com/9XrEEdF.png)

* Asignamos el branch que deseamos ligar con el APP y confirmamos con ENABLE AUTOMATIC DEPLOYS.
[Imgur](https://i.imgur.com/yVe4RQj.png)

* Obtendremos la confirmacion de que nuestra app ha sido configurada con deploys automaticos.
[Imgur](https://i.imgur.com/TieCUyU.png)



## Configurar Postgres.
Heroku nos ofrece una instancia de Postgres en forma de un ADD-ON, vamos a configurarlo.

* Sobre nuestro dashboar damos clic sobre el nombre de nuestra app de STAGING.
[Imgur](https://i.imgur.com/6WU3APu.png)

* A continu nos mostrara el panel de nuestra app, en este caso en la seccion INSTALLED ADD-ONS seleccionaremos CONFIGURE ADD-ONS. 
[Imgur](https://i.imgur.com/AI9M1hY.png)

* En el cuadro de busqueda de ADD-ONS buscamos Postgres y selecionamos dando click sobre HEROKU POSTGRES.
[Imgur](https://i.imgur.com/5R1AiDc.png)

* Una vez seleccionado nos muestra las opciones de planes, nos quedaremos con Hobby Free y confirmamos con clic en PROVISION.
[Imgur](https://i.imgur.com/hwZMzI7.png)

* Listo tenemos agregado nuestro ADD-ON, con la integracion de Heroku obtendremos las credenciales por medio de una variable de entorno propia de Heroku, pero si requieres las credenciales debes dar click sobre HEROKU POSTGRES y te llevara al panel de administracion de Postgres.
[Imgur](https://i.imgur.com/bgBubXR.png)

* Las credenciales viven en Settings-> Database Credentials -> VIEW CREDENTIALS.
[Imgur](https://i.imgur.com/HfGAZm7.png)

## Configurar Buildpack de Python.
Para iniciar nuestra app heroku requiere correr ciertos comandos como levantar Unicorn, para esto, le diremos que nuestro app es de Python para que ejecute las instrucciones correctas.

* En nuestro panel de admin de nuestra app STAGING, nos vamos al tab SETTINGS.
[Imgur](https://i.imgur.com/8iJUvpD.png)

* Aqui nos vamos hasta la seccion de BUILDPACK y seleccionamos ADD BUILDPACK.
[Imgur](https://i.imgur.com/d0lkR3Y.png)

* Seleccionamos Python en nuestro caso.
[Imgur](https://i.imgur.com/AYmH73T.png)

## Configurar variables de entorno.
Recuerdas que en la seccion de Postgres te comente que las credenciales las tomariamos de una variable de entorno, pues en esta seccion de SETTINGS de nuestra app STAGING arriba de BUILDPACK esta la seccion CONFIG VARS.

* Seleccionamos REVEAL CONFIG VARS.
[Imgur](https://i.imgur.com/dLfMcGC.png)

* Por defecto ya tendremos DATABASE_URL, pero agregaremos 2 mas.
    - DATABASE_URL: Son las credenciales de Postgres.
    - DEBUG_VALUE: Este vive en nuestro settings.py y servira para activar o desactivar el DEBUG dependiendo nuestro ambiente. En staging estara encendido y en Prod lo apagaremos.
    - SECRET_KEY: Es nuestra llave para mantener segura la sesion servidor-cliente.

[Imgur](https://i.imgur.com/SjEoZGR.png)

Listo hemos terminado de configurar todo del lado de Heroku, ahora procedemos a preparar nuestro proyecto de python.

## Preparar nuestro Requirement.txt
Heroku instala nuestras librerias usando requierements.txt, este proyecto ya tiene el suyo, para crear
el tuyo primero valida que tengas las siguientes librerias intaladas.
* PRIMERO valida que estas dentro de tu ambiente virtual, luego usando "pip freeze" obtendremos la lista de librerias.
    - dj-database-url
    - Django
    - gunicorn
    - psycopg2

* Si no las tienes instaladas, procede a hacerlo haciendo uso de PIP, ejem: "pip install gunicorn".

* Ahora procedemos a crear nuestro archivo usando "pip freeze > requirements.txt".

## Configurar settings.py
Aqui haremos un par de modificaciones, recuerdas que en Heroku asignamos variables de configuracion, pues las llamaremos en nuestro archivo de settings y esto haciendo uso de dj_database_url. Este proyecto ya tiene estas configuraciones y lo puedes ver en settings.py

* Primero importaremos DJ DATABASE_
```python
    import os
    import dj_database_url
```

* Modificamos nuestro SECRET KEY para leerlo desde Heroku y no tenerlo amarrado en el codigo.
```python
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')
```
* Lo mismo haremos con DEBUG, este se activara dependiendo la instancia en Heroku (Prod/Staging)
```python
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = os.environ.get('DEBUG_VALUE', 'TRUE').upper() == 'TRUE'
```

* Ahora dejaremos que nuestra instancia de Heroku pueda leer nuestra app, aqui debemos asignar la URL de heroku o dejar que todos se comuniquen con ella.
```python
    ALLOWED_HOSTS = ['*']
```

* Para leer las credenciales de nuestra BDD desde Heroku, asignamos su variable de configuracion.
```python
    if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(default=os.environ['DATABASE_URL'])
```

* Configuramos los Static Files, por ahorita solo los paths pero al momento de usar statics requerimos installar la libreria de WhiteNoise, por el momento solo asignaremos los paths. 
```python
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
```

## Configurar Procfile
El siguiente paso es crear nuestro archivo Procfile, este archivo son las instrucciones que le damos a Heroku cada que se hace deploy.

```python
    web: gunicorn web_project.wsgi --log-file -
```

## Configurar Runtime.
Aqui solo le diremos a Heroku que version de Python deseamos utilizar.
```python
    python-3.7.4
```

## Agregar carpeta static.
Ahora solo agregaremos una carpeta llamada static en nuestro proyecto con un archivo cualquiera, en este caso un ".keep", esto porque Heroku al hacer deploy corre un comando para recolectar los archivos estaticos, si no encuentra esta carpeta nos lanzara un error en el log de Heroku.