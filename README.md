# Pancakes IDA*

Este programa resuelve el problema de pancake sorting mediante el uso del algoritmo IDA*.

**Lenguaje utilizado**: Python

## Funciones

 ### **'__ init __(self, pancakes)'**
 Este el constructor de la clase Pancakes que recibe como parametros una lista de letras desordenadas.
 
 ### **'voltear(self, posicion, pancakes)'**
 
Esta funcion recibe como parametro la posición donde se van a voltear los pancakes y la lista a voltear y devuelve los pancakes volteados  
desde esa posición.

 ### **'h(self, nodo)'**
 Esta función se encarga de la heuristica del programa, devuelve el valor de la heuristica del nodo introducido como parametro de la función.
 
 ### **'ida(self, nodo)'**
  Esta función recibe como parametro el nodo a partir del cual iniciará el programa y devolverá la solución del problema en caso de que la función busqProfundidad() haya encontrado solución
  y en caso de que no haya encontrado solución actualiza el valor de la cota.
 
 ### **'busqProfundidad(self, nodo, ant, cota)'**
Esta funcion recibe como parametros el nodo a partir del cual se realizará la busqueda en profundidad, el movimiento anterior que se realizó (en forma de lista) y la cota actual del programa y en caso de encontrar solución con la cota proporcionada va a retornar la serie de 
 movimientos que se tiene que realizar para ordenar de menor a mayor los pancakes y en caso de no encontrar solución retornará el valor heuristico minimo de los nodos analizados.
 
 ## Como utilizar el código
 Para poder utilizar el código se tiene que crear una instancia de la clase "Pancakes" añadiendole como parametro una lista desordenada  
 de letras minusculas y luego llamar a la funcion ida() dandole como parametro la lista a ordenar. El resultado de la ejecución será una serie de numeros que indican los movimientos que se tienen que realizar para resolver ese problema.
 
A continuación se presenta un ejemplo de como utilizar el código:

![image](https://user-images.githubusercontent.com/125157604/229014426-1fd207c6-1fed-48e5-94c8-60e712e0668e.png)


