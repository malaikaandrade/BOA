c(2, TRUE, 3.5)

c(4.5, 6.76, 'Malaika')


rep('Hola', 13)

scan()

x<- c(1, 2, 3, 4)

fix(x)

x

nombres <- c('Malaika', 'Donaldo', 'Aixa', 'Angeles')
nombres

fix (nombres)
class(nombres)


rep(1996, 10)

rep(c(4,5,6,7), 15)

y <- c(16, 0, 1, 20, 1.7, 88, 5, 1, 9)
y
fix(y)
y

#PROGRESIONES Y SECUENCIAS ARITMETICAS

seq(5, 60, by = 6)

seq(100, 6, by = -9)

seq(5, 60, by= 3.6)

#le dices que empiece en 4 hasta 35 y de 7 en 7
seq(4, 35, length.out = 7)

#en este caso le estas diciendo que empieza en 4 de 3 en 3 y que tenga 7 componentes
seq(4, length.out = 7, by = 3)

#ejercicios
seq(1, 20, by = 1)
seq(2, 20, by = 2)

seq(17, 98, length.out = 4)

#puedes concatenar los vectores son las progresiones y las secuencias aritmeticas
c(rep(pi, 5), 5:10, -7)-> x
c(0, x, 10, x, 20)

#funciones
x = 1: 10 
x

x + pi
pi * x
sqrt(x)

2^x

x^2

sapply(x, FUN = function(elemento){sqrt(elemento)})

cd = function(x){summary(lm((1:4)~c(1:3, x)))$r.squared}

cd(5)
sapply(x, FUN = cd)

1:10 + 1:10


(1:10)*(1:10)

n = 1:1000
x = 2*3^(n/2)-15
x

y = n^2/(n^2+1)
y

#FUNCIONES

cuadrado = function(x){x^2}
v = c(1,2,3,4,5,6)
sapply(v, FUN = cuadrado )
#media
mean(v)
#sumas acumuladas
cumsum(v)
#ordena los objetos 
sort(v)
#invierte el orden 
rev(v)

sort(v, decreasing = TRUE)


