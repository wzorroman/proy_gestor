# Proyecto de procesos documentarios en una institucion
Es un proyecto para gestionar el paso de la solicitud de algun tramite documentario por las diversas areas hasta su completa atencion de dicha solicitud.

---
- Se reviso la libreria `django-crum` en https://pythonhosted.org/django-crum
- Como BD use el por defecto sqlite3, asi el administrador de BD = DBeaver

## Instalando el proyecto

- Instalar pip `sudo apt-get install python-pip`
- Instalar enviroment `sudo pip install virtualenv`
- Crear un entorno virtual virtualenv env_gestor
- activar entorno `source env_log\bin\active`


 Descargar el git y el enviroment (.env)
 - Luego instalar los requerimientos con el entorno activado :
 `(env_gestor)$ pip install --upgrade -r requirements/dev.txt`

 - Correr en la consola usando:
 `(env_gestor)$ python manage.py runserver --settings=proy_gestor.settings.dev`

 - Correr las migraciones:
  `python manage.py migrate --settings=proy_gestor.settings.dev`

## Para crear una nueva app
 - Se tiene que crear con el comando:
   `python manage.py startapp name_my_app`
 - Luego moverla a la carpeta **apps**, en donde se encuentra todas las apps creadas previamente.

## Sobre uso de constantes en el proyecto
 - El manejo de todas las constantes esta en el archivo **constants** para todo el proyecto, la ubicacion esta en la carpeta "commons" dentro de apps
