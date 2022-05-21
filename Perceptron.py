import matplotlib.pyplot as plt
import numpy as np
# Funcion de transferencia


class Punto():
    def __init__(self, x, y, clase, clasificado, funcion_transferencia):
        self.x = x
        self.y = y
        self.clase = clase
        self.clase_obtenida = clase
        self.clasificado = clasificado
        self.suma = 0
        self.funcion_transferencia = funcion_transferencia

    def verificar_clasificacion(self):
        self.clase_obtenida = self.funcion_transferencia(self.suma)
        if self.clase_obtenida != self.clase:
            self.clasificado = False
        else:
            self.clasificado = True


def f(N):
    if N > 0:
        return 1
    else:
        return 0


def suma(coordenada, w1, w2, bias):
    x1, x2 = coordenada
    s = x1*w1 + x2*w2 + bias
    return s


def ajuste_pesos(w1, w2, error, coordenada):
    x1, x2 = coordenada
    x1 *= error
    x2 *= error
    w1 += x1
    w2 += x2
    return (w1, w2)


def graficar(puntos, a, b, c, recta):
    for punto in puntos:
        plt.plot(punto.x, punto.y, marker="o", color="b")

    x = np.arange(-5, 5, 0.1)
    y = ((-a*x) - c) / b
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Perceptron ' + recta)
    plt.show()


def main():
    print("Inicio del programa")
    w1 = 0.2
    w2 = -0.9
    bias = 0.8
    puntos = [
        # X1     X2      Clase
        Punto(2, 0, 0, False, f),
        Punto(2, 2, 0, False, f),
        Punto(0, 2, 0, False, f),
        Punto(-2, 2, 1, False, f),
        Punto(-2, 0, 0, False, f),
        Punto(-2, -2, 0, False, f),
        Punto(0, -2, 0, False, f),
        Punto(2, -2, 0, False, f)
    ]
    clasificado_todo = True
    epoca = 1
    for punto in puntos:
        clasificado_todo *= punto.clasificado
    while clasificado_todo == False:
        print("Época ",epoca)
        print("Valores iniciales [W1 = {:0.2f}, W2 = {:0.2f}, bias = {:0.2f}]".format(
            w1, w2, bias))
        for punto in puntos:
            print("\nPunto ({}, {}) = {} ← clase esperada".format(punto.x, punto.y, punto.clase))
            coordenada, clase_esperada = (punto.x, punto.y), punto.clase
            print("Se suma la multiplicación de los pesos por la coordenada junto con el bias.")
            punto.suma = suma(coordenada, w1, w2, bias)
            punto.verificar_clasificacion()
            print("\tsuma = ({:0.2f} x {}) + ({:0.2f} x {}) + ({:0.2f}) = {:0.2f}".format(w1,coordenada[0],w2,coordenada[1],bias,punto.suma))
            clase_obtenida = f(punto.suma)
            print("Se evalúa el resultado de la suma en la función de transferencia: ")
            print("\tClase obtenida = f({:0.2f}) = {} ← clase obtenida".format(punto.suma, clase_obtenida))
            if clase_obtenida != clase_esperada:
                print("La clase obtenida es diferente de la clase esperada, por lo tanto, se realiza un ajuste de pesos.")
                error = clase_esperada - clase_obtenida
                print("\tSe modifica el error: error = clase esperada - clase obtenida")
                print("\t\terror = ({}) - ({}) = {:0.2f}".format(clase_esperada,clase_obtenida,error))
                bias += error
                print("\tSe modifica el bias: bias = bias + error")
                print("\t\tbias = ({:0.2f}) + ({}) = {:0.2f}".format(bias-error, error, bias))
                wa = w1
                wb = w2
                w1, w2 = ajuste_pesos(w1, w2, error, coordenada)
                print("\tSe ajustan los pesos: nuevos pesos = pesos anteriores + error x punto")
                print("\t\tnuevos pesos = ({:0.2f}, {:0.2f}) + ({})({}, {}) = ({:0.2f}, {:0.2f})".format(wa,wb,error,coordenada[0],coordenada[1],w1,w2))
            else:
                print("Como la clase obtenida es igual que la clase esperada, no se realiza ajuste y los pesos no cambian.")
            print("Se prosigue con el siguiente punto.")
        print("Terminada la época, se procede a verificar todos los puntos para asegurarse que clasifica correctamente con los pesos y bias obtenidos.")
        for punto in puntos:
            print("Punto ({}, {}) = {} ← clase esperada | {} ← clase obtenida".format(punto.x, punto.y, punto.clase, punto.clase_obtenida))

        clasificado_todo = True
        for punto in puntos:
            clasificado_todo *= punto.clasificado
        print("\nValores finales [W1 = {:0.2f}, W2 = {:0.2f}, bias = {:0.2f}]".format(
            w1, w2, bias))
        print("\nSe obtiene la recta: ")
        print("y = ({:0.2f}x + {:0.2f}) / {:0.2f}".format(-w1, -bias,w2))
        print("\n\n")
        epoca += 1
main()
