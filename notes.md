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

## UnitTest (Pytest)

UnitTest es una libreria que nos va a permitir hacer diferentes tests para obtener datos y informacion de lo 
que esta pasando en nuestra automatizacion con Selenium. Tiene diferentes etapas o tests individuales:

- Test Fixture:
	Todo lo que pasa antes y despues de los demas tests o el caso de prueba. Generalmente preparaciones y finalizaciones.
- T. Case:
	Es un caso, modulo o seccion del codigo que vamos a probar, generalmente acciones que queramos que realice Selenium o funciones que 
	necesitamos probar.
- T. Suites:
	Es una collection de varios t. de cases, para hacer cada test de una forma mas secuencial y automatico

Estos tests van a ser orquestados o realizados por el Test Runner, el cual va a indicar la forma, secuencia y direccion de 
los tests. Sus resultados van a ser dados en el Test Report, el cual va a tener que tests se realizaron, tiempo, datos y errores 
u fallas.

## Drivers para los WebBrowsers

Para comunicar Python y Selenium cno los Navegadores debemos hacer uso de drivers. Cada uno podria variar.

Para Breave, Chromiun, vamos a instalar la versionde chromiun que tenga en el About Brave. 100.x.48~.
Vamos a descargar la version de linux y la vamos a dejar en ~/bin/ para mejor acceso

## Hello World

Para hacer el equivalente de Hello World, vamos a tener que abrir el navegador y 
abrir una pestaña de un sitio web.

Para esto vamos a importar 

- unittest
- HTMLTestRunner de pyunitreport
- webdriver de selenium

Vamos a crear una clase, HelloWorld, que herede de unittest.TestCase, es decir esta clase va a 
ser un caso de Testing. 

Vamos a definir 3 metodos iniciales,

- Setup
	Vamos a iniciar el driver, y hacer que espere 10 segundos para funcionar. 
	Para usar Brave vamos a tener que crear un obj de opciones el cual se va a definir su binario.
	y agregarlo al driver. Tambien se puede configurar para que sea incognito o sin header
- test\_hello\_world:
	Vamos a decirle al driver que abra una pagina web, brave.com
	Es importante que se nombre el metodo test_ nombre del metodo, 
	sin esto no va a funcionar. Al tener estos nombres van a ser 
	ejecutados sin necesidad de escribirlo en el codigo, y se realizara 
	todo el proceso de test.
- tearDown
	Va a finalizar la prueba, para que no ocurra data leak

Despues de hacer las pruebas, podemos ver el resultado de cada una en el reporte de HTML, se puede hacer en la terminal, 
pero es mas confuso y menos 'bonito'.

Al hacer cada test, el navegador se va a cerrar casi inmediatamente, para evitarlo vamos a usar un 
decorador en setUp y en tearDown, y cambiar self por 'cls' en todo el metodo

@classmethod
def setUp/tearDown (cls):
	...
	cls.x = ...

### @classmethod

Hacer que una funcion de una Clase se vuelva un metodo, accesible desde la propia clase y objetos de esta.
Pudiendo acceder a atributos y metodos de la clase, pero no los atributos de los metodos.

class Clase:
	atributo = ""

	def metodo (self):
		self.atributo_metodo = ""

	@classmethod
	def class_method (cls):
		print(cls.atributo) # Sin error
		print(cls.atributo_metodo) # AtributeError

## Find Elements

En cada sitio web se usan diferentes elementos y estructuras en HTML5, debemos encontrar diferentes 
elementos como botones, imagenes, menus y otros para poder hacer nuestras pruebas necesarias.

Se pueden encontrar los elementos bajo diferentes criterios
- ID del elemento
- Nombres de atributos
- N. de clases
- N. de etiquetas html
- XPath
- Selector de CSS
- Texto de Link
- Texto Parcial de Link
- etc...

Los mas importantes son
- S. de CSS
- XPath

Para nuestras pruebas vamos a usar Madison Island, un sitio web de prueba para selenium.
[Madison Island](http://demo-store.seleniumacademy.com/)

Con driver, despues de setear todo para abrir el sitio web, podemos buscar los elementos 
con diferentes metodos

find\_elements?\_by:
- id
- name
- class\_name
- xpath
- tag\_name
- css\_selector

Se puede usar element para solo uno o el primero que aparesca, pero se puede usar elements para hacer una lista con 
los elementos obtenidos.

Y, lo veremos mejor mas adelante, se pueden hacer condiciones en las pruebas para indicar si todo esta llendo bien, 
mirar si hay 3 imagenes en el banner

## Assertions 

Assertions son condicionales que se podran usar en los tests para verificar 
el correcto funcionamento de estos.

El uso general son el de condicionales y operadores logicos
- ==
- !=
- \<
- \>
- =\<
- =\>

## Test Suites

Cuando tenemos diferentes tests cases en diferentes archivos de testing, los tests suites nos van a permitir 
correrlos todos y hacer un gran reporte de todos los tests.


