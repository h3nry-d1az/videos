#let enunciado = contenido => {
set page(
  width: 1250pt,
  height: 500pt,
  margin: (
    top: 2.5cm,
    right: 1.85cm,
    bottom: 2.5cm,
    left: 1.85cm,
  )
)

set par(justify: true)

set text(
  lang: "es",
  font: "New Computer Modern",
  size: 22pt,
)
show math.equation: set text(font: "New Computer Modern Math")

[#contenido]
}