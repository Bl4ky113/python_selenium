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


