#import "preamble.typ": enunciado

#enunciado[
Te encuentras analizando un plano infinito con 
coordenadas enteras $(X, Y)$ (específicamente, la 
celda inmediatamente superior a $(0,0)$ es $(0, 1)$,
y aquella inmediatamente a su derecha es $(1, 0)$).
Inicialmente, solo la casilla $(0,0)$ es negra.
\
\
\
\
\
\
Tienes una cadena $a_1a_2dots.c a_n$ de longitud $n$
consistente de caracteres *4* y *8*, los cuales 
describen $n$ operaciones de expansión. Para cada $i$ 
desde 1 hasta $n$, la siguiente acción ocurre para todas
las celdas simultaneamente:
\
\
\
\
- Si $s_i=bold(4)$, cada posición adyacente a una celda negra se vuelve también negra (sin contar diagonales).
- Si $s_i=bold(8)$, cada posición adyacente a una celda negra -- incluyendo diagonales -- se vuelve también negra.
\
\
\
\
\
¿Es la celda $(x,y)$ negra al final del proceso?
]