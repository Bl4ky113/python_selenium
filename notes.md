# Curso de Selenium con Python

## Historia de Selenium

Selenium es una suit o grupo de herramientas que nos ayuda a hacer diferentes acciones con 
navegadores, generalmente usos cómo testing o web scrapping, sepa quien sepa que sea eso.

Se origino cómo un testing usando Javascript, se desarrollo Selenium RC para 
poder usarlo en diferentes y varios sitios web. Se creo un IDE para usarlo desde chrome y 
firefox sin usar codigo. Y al final se usa con diferentes lenguajes de programación 
cómo python, llamada esta herramienta WebDriver.

### RC
- Ventajas
	- Rapido
	- Uso de datos para hacer el test
	- Toma de datos
- Desventajas
	- Necesita un servidor para comunicarse con el navegador
	- Muy dificil de descargar a comparación
	- Ya no es utilizado en hoy en día

### IDE
- Ventajas
	- No usa código
	- Sencilla utilización
	- Varias opciones
- Desventajas
	- Limitado a Firefox y Chromium
	- No usa datos para tests

### WebDriver
- Ventajas
	- Multiple soporte de lenguajes
	- sencilla instalación
	- Comunicación directa con el navegador
	- Puede usar datos
- Desventajas
	- No genera datos o reportes
	- Requiere programar
	- No soporta algun que otro navegador

Existe tambien el Selenium Grid que es una herramienta para RC
que permite hacer scripts que corran en el fondo que es conveniente 
para el tiempo

## Otras Herramientas de Automatización y Testing

Algunas herramientas extra, dado a que Selenium no es 
perfecto.

### Puppeteer 

Herramienta principalmente para chrome que tiene:
- Soporte de Google
- Data Performance Analysis de Chrome
- Mayor control de Chrome
- No requiere drivers externos

Pero:
- Solo funciona principalmente en Chrome y con JS
- La comunidad es pequeña

### Cypress.io

Herramienta tambien principalmente para chrome que tiene:
- Excelente documentación con amor <3
- Agil en Pruebas End to End
- Orientado a Desarrolladores
- Excelente asincronismo

Pero:
- Principalmente Chrome y JS
- Pruebas en paralelo solo con versiones de pago

Elegir las una de las opciones requiere ver las condiciones que tenemos cómo:
- Que lenguaje vamos a usar
- Que vamos a necesitar
- Que caracteristicas necesitamos

## Preparacion de Entorno de Trabajo

- Python > 3.6, < 3.9
- Instalar con PIP
	- Selenium 3
		Selenium WebDriver
	- pyunitreport
		Para hacer reportes en HTML

### Cambiar de versiones con Pyenv

Para instalar una versión inferior de python, vamos a
tener que hacer uso de pyenv.

#### Instalacion

Usando distribuciones de Linux es la mejor forma de usar pyenv.
Vamos a tener que instalar este modulo, lo mejor es mirar si se 
puede descargar con el packet manager de la distro. pacman, apt, etc.

Si no, se puede descargar desde su repositorio y agregarlo a 
el enviroment en PATH. Y dejar su init en .bash-profile

#### Uso

Despues de instalarlo vamos a descargar la version que vayamos a usar, 
nosotros vamos a usar python 3.8.6. Ponemos el comando y este se descargara:

pyenv install -v 3.8.6

Se demoro 22min en completar toda la descarga.
Podemos verificar las versiones que tengamos descargadas y disponibles para usar 
viendolas en la carpeta de pyenv en Home.

ls ~/pyenv/versions/
o
pyenv versions

Y si necesitamos desinstalar una version

pyenv uninstall x.x.x

Para usarlas, hay dos formas:
- Global:
	Cambia la version de python en todo el OS
	pyenv global x.x.x
- Local:
	Cambia la version de python en solo un folder
	pyenv local x.x.x

para cambiar la version del OS

pyenv global/local system

Podemos hacer virtual enviroments para hacer usar versiones de python especificas 
y de paso tener las ventajas de un venv normal de python.
Ojo estos venv son una extension que se debe instalar por separado, este no 
esta en pacman, entonces toca agregarlo desde github

Para su instalacion solo debemos hacer pull de su repo y ponerlo en la carpeta de 
pluggins de pyenv, generalmente en ~/.pyenv/
Agregar su init en .bash-profile y listo para usar

Para generar un venv

pyenv virutalenv version-python nombre-venv

Pero para activarla vamos a tener que usar

pyenv local nombre-venv

En cualquier momento que queramos verificar que version estamos usando
podemos seguir usando python --version, aunque pyenv tambien nos 
da la herramienta de pyenv which python

Una vez que ya tengamos python <3.9, vamos a instalar las librerias y demas cosas.

## Hello World

