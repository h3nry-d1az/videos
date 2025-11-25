#import "preamble.typ": enunciado

#enunciado[
  #set text(size: 43pt)
  Sea ${x_n}_(n >= 0)$ la sucesión definida por $ x_0 = 0, wide x_(n+1) = 2x_n + sqrt(3 x_n^2 +4). $
  Demostrar que $x_n in ZZ$ para todo $n >= 0$.
]

// #enunciado(align(center)[
//   #set text(size: 43pt)
//   $ x_0 = 0, wide x_(n+1) = 2x_n + sqrt(3 x_n^2 +4) $
//   Demostrar que #box(fill: rgb("#32fe8e"), inset: 0.2em, outset: 1pt)[$x_n in ZZ$] para $n >= 0$.
// ])