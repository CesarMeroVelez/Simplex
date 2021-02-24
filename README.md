# SIMPLEX
Calculadora simplex 

# Elaborado por:
Mero Vélez César Enrique

# Funcionamiento
1.	Para empezar, debemos tener un compilador de Python para así poder ejecutar el programa
2.	Debemos bajar el programa que se encuentra en el siguiente repositorio de GitHub https://github.com/CesarMeroVelez/Simplex
3.	Luego de bajarlo y añadirlo al compilador debemos instalar un complemento que se llama pandas, el cual es una biblioteca de software escrita como extensión de NumPy para manipulación y análisis de datos para el lenguaje de programación Python. En particular, ofrece estructuras de datos y operaciones para manipular tablas numéricas y series temporales. Para ello utilizamos el comando “pip install pandas” 
4.	Luego ya podemos ejecutarlo y cabe recalcar que en este caso todo funciona en consola
5.	Iniciamos presionando el icono verde que se encuentra en la parte superior derecha 
6.	Lo primero que aparecerá en consola será seleccionar con un numero una opcion lo cual tendremos que presionar una de las dos opciones: 1 para maximización y 2 para minimización
7.	Luego de ingresar un numero valido, tendremos que presionar enter y lo siguiente que veremos es lo siguiente que es ingresar la cantidad de variables aquí lo que haremos es ingresar la cantidad de variables (numéricas) que tiene nuestro problema y presionar enter
8.	Luego de ingresar el numero de variables, ahora nos pedirá el número de restricciones así como en el punto anterior agregamos el numero de restricciones 
9.	El siguiente paso es dependiendo del numero de restricciones, pues para hacerlo mas entendible decidí añadirle la opción de agregarle un nombre a cada una de las restricciones, por ejemplo: R1, R2, R3
10.	Lo siguiente es como lo dice la siguiente imagen, ingresar el valor (numérico) de X1 en la función principal
Luego nos pedirá los siguientes valores, ejemplo X2, X3… etc
Para este ejemplo utilizaremos lo siguiente:
Entonces ingresamos los datos tal como nos pide:
11.	Lo siguiente es ingresar los valores numéricos de las restricciones:
Llenamos conforme a las restricciones que tenemos.
 
12.	Nos pedirá también el valor de R1 que en este caso será 430, en R2 460 y en R3 420
 
13.	Para finalizar debemos ingresar en valor numérico el numero de decimales que deseamos añadir, en este caso añadiremos 2 decimales. Y con esto el programa se ejecutará y mostrará las tablas con los resultados.
 

Tenemos un caso en particular, en la solución Z los valores salen en positivo, pero solamente debemos tomar en cuenta que en realidad son valores negativos, solamente que la resolución los pone de esta manera por el proceso, pero el proceso está correcto, solo tomando de referencia estos valores finales. Y Con esto tenemos nuestro programa funcionando.





## Iniciar sesión
Luego de estár en este apartado nos vamos a dirigir a la parte de abajo donde dice "Regístrate ahora" para así poder registrarnos.
Dentro del registro procedemos a llenar el formulario con los Nombres, Apellidos, Correo Electronico y por ultimo una contraseña que tiene que tener entre 8 y 16 caracteres, al menos un dígito, al menos una minúscula y al menos una mayúscula.
Luego de ingresar los datos correctamente procedemos a dar clic en "Registrarse" si todo está correcto aparece un aviso de confirmación donde nos dice que nuestro usuario fue registrado con éxito, le damos clic en "ok"

Automaticamente volveremos a la página de incio de sesion, lo que haremos ahora es en el formulario que nos solicita nuestro correo y contraseña, ingresar los que previamente habiamos ingresado para registrarnos y damos clic en "INGRESAR"
Nos aparece una animación mientras inicia sesión, si la información no es correcta nos aparece un aviso de que la contraseña es incorrecta o el usuario no está registrado dependiendo de cual es el caso. Al ingresar correctamente la información y dar clic en ingresar, automaticamente nos llevará al FORMULARIO DE SOLICITUD DE CITAS donde tenemos que llenar un nuevo formulario para empezar a solicitar una cita.
## Reservar una cita para una consulta
En el formulario tenemos que llenarlo con nuestro nombre, apellidos, cédula, edad, género, teléfono, especialidad solicitada para la cita, fecha que requerimos la cita, hora que requerimos la cita y una descripción del malestar que tenemos.
Damos clic en "reservar" y nos aparece un aviso de que nuestra cita fue guardada y damos clic en "OK" 

## Menú
En el menú superior tenemos cinco (5) apartados
1. Inicio: Aquí se muestra la información principal de nuestro sistema y algunas palabras sobre nosotros
2. Reservar cita: En este apartado tenemos el formulario donde podemos llenarlo para solicitar una cita
3. Mis citas: Aquí podemos ver las citas que hemos solicitado y su estado, es decir si han sido aprobadas, rechazadas, cambiadas o sin aprobación aun.
4. Nosotros: En este apartado Aparece información puntual sobre nosotros (SAGE) los valores y el contacto directo con nosotros.
5. Cerrar Sesión: En este botón del menú hacemos clic cuando querramos finalizar sesión y nos llevará automaticamente al apartado de inicio de sesión con nuestra sesión ya finalizada y listo para iniciar una nueva sesión.


# Administrador
Al ingresar al sistema con las credenciales de administrador, tenemos un unico apartado donde podemos añadir un doctor llenando el formulario con los nombres, apellidos del doctor, seleccionando una (1) de las cuatro (4) especialidades que dispone, ingresamos el correo electronico y la contraseña para crearlo, damos clic en "registrarse" y tendremos una cuenta de doctor creada.

# Doctor
Al ingresar al sistema con las credenciales de Doctor de alguna de las areas que se disponen tenemos un filtro para buscar en la lista de citas con el número de cédula y también otro filtro para buscar por medio de dos fechas, una inicial y una final.
En la parte final tenemos la lista completa de citas requeridas con la información del paciente que solicita.
damos clic en detalle para mostrar más información, donde podemos modificar la fecha y hora, así como de aprobar o negar la cita.

## Menú
En el menú tenemos tres (3) apartados los cuales son:
1. Consulta: donde vemos la lista completa de citas requeridas con la información del paciente que solicita.
2. Administración: donde podemos ver las citas que hemos aprobado y tenemos un botón para cuando hayamos terminado la atención en esa cita y retirarla de los pendientes en este apartado.
3. Cerrar sesión: En este botón del menú hacemos clic cuando querramos finalizar sesión y nos llevará automaticamente al apartado de inicio de sesión con nuestra sesión ya finalizada y listo para iniciar una nueva sesión.

# Cuentas
## Cuenta del Administrador:
#### El administrador es el unico que puede creear las cuentas a los doctores.
    usuario: administrador1@gmail.com
    contraseña: admin1

## Cuentas de los doctores:
### Medicina General:
    usuario: doctor1@gmail.com
    contraseña: doctor1
### Ginecología:
    usuario: doctor2@gmail.com
    contraseña: doctor2
### Cardiología:
    usuario: doctor3@gmail.com
    contraseña: doctor3
### Odontología:
    usuario: doctor4@gmail.com
    contraseña: doctor4


# Acerca del proyecto
    Para la realización de este proyecto utilizamos:
    HTML
    CSS
    JavaScript
    Base de datos en Firebase
    Hosteo Gratuito de Heroku