# Notas de uso
1. Necesitas instalar pipenv de manera global con el comando:

        pip install pipenv

2. Para crear el entorno virtual asegurate de estar en la carpeta donde tienes el proyecto (Es donde se encuentra el file main.py) y utiliza el comando

        pipenv install

    Este comando instalara todas las dependencias que se encuentran dentro del archivo Pipfile y agrega las futuras dependencias que puedas llegar a necesitar. Si despues quieres instalar una dependencia que no esta dentro del archivo de Pipfile utiliza el comando
        
        pipenv install <nombre_de_la_dependencia>

3. Ya una vez instalaste todo lo necesario necesitas activar el entorno virtual con el comando:

        pipenv shell

4. Para correr el script utiliza el comando:

        python main.py