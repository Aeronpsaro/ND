# Algoritmo ND en Lego Mindstorm EV3 :robot:
Implementación básica del algoritmo de evitación de obstáculos ND en Lego Mindstorm EV3 con Python.

## Estado del proyecto :ok:
Primera versión finalizada :white_check_mark:

## Construcción de la plataforma :hammer:
Para la realización del proyecto, se construye una plataforma diferencial, con sensor de ultrasonidos, brújula y un pulsador. <br/>
Mediante un motor mediano, el sensor ultrasónico puede realizar un giro de 180º para captar los obstáculos que se encuentran a su alrededor. <br/>
El pulsador en la parte frontal impide que el vehículo choque con un obstáculo de manera frontal, de manera que si detecta que ha sido pulsado, se acciona una parada de emergencia.
<p align="center">
  <img width="441" alt="Captura de Pantalla 2023-01-23 a las 3 53 15 p  m" src="https://user-images.githubusercontent.com/56322714/214085210-e622cc88-8e84-4257-9f54-164b61398d0c.png">
</p>

Sensores empleados:
* :green_circle: Sensor de ultrasonidos, señalado en verde
* :large_blue_circle: Brújula, señalado en azul
* :red_circle: Sensor de contacto (pulsador), señalado en rojo

## Funcionamiento :nut_and_bolt:
El funcionamiento del robot sigue el siguiente diagrama de flujo.
<p align="center">
<img width="309" alt="Captura de Pantalla 2023-01-23 a las 4 31 22 p  m" src="https://user-images.githubusercontent.com/56322714/214094957-a31cec6c-5879-4629-b143-c6b5891fa85f.png">
</p>


## Futuras mejoras :fast_forward:
- [ ] Cubrir la estructura de posibles impactos que no sean en la parte frontal
- [ ] Añadir control proporcional a la velocidad
- [ ] Añadir mejores sensores de ultrasonidos
- [ ] Lectura del sensor de ultrasonidos a la misma vez que se mueve el robot


## Enlaces importantes :link:
* [Manual de construcción de la plataforma](http://robotsquare.com/wp-content/uploads/2013/10/45544_educator2.pdf)
* [Información de la brújula](https://tienda.esteamedu.es/home/95-sensor-ir-irseeker-v2-hitechnic.html)
* [Información de la brújula](https://modernroboticsinc.com/product/hitechnic-nxt-compass-sensor/)
* [Información de uso de los motores](https://sites.google.com/site/ev3devpython/learn_ev3_python/using-motors)
* [Programación multihilos en EV3](https://sites.google.com/site/ev3devpython/learn_ev3_python/threads)


## Contribuidores :busts_in_silhouette:
<a href="https://github.com/Aeronpsaro/ND/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Aeronpsaro/ND" />
</a>
