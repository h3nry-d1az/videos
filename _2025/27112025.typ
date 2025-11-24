#import "preamble.typ": enunciado

// #enunciado[
// #set text(size: 75pt)
// $ integral_0^infinity {x}/m^floor(x) dif x, wide m >= 2 $
// ]

#enunciado[
#set text(size: 75pt)
$ integral_0^infinity #box(${x}$, fill: rgb("#8989fb"), outset: 5pt, inset: 0.05em)/(#box($m^floor(x)$, inset: 0.05em, fill: rgb("#f98080"))) dif x, wide m >= 2 $
]