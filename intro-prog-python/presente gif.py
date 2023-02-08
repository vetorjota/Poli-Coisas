import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os


class Domain:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @property
    def interval(self):
        return np.arange(self.start, self.end, e)


class Function:
    def __init__(self, f, domain, color='k'):
        self.f = f
        self.domain = domain
        self.color = color


def derivative(f, order=1):
    def df(x, h=0.1e-1):
        return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)

    if order == 1:
        return df
    else:
        return derivative(df, order - 1)

def taylor(f, x0, order):
    t = lambda x: f(x0)
    for i in range(order):
        t = lambda x, j=i + 1, k=t: k(x) + derivative(f, j)(x0) / factorial(j) * (x - x0) ** j
    return t

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def config_subplot():
    axes = plt.gca()
    axes.set_xlim([-10, 10])
    axes.set_ylim([-10, 10])

def add_figure_to_images(images, frames):
    fig.savefig('temp.png')
  
    for i in range(frames):
        images.append(imageio.imread('temp.png'))
    os.remove('temp.png')
    ax.clear()
    
def plot_functions(functions):
    for function in functions:
          ax.plot(function.domain.interval, function.f(function.domain.interval), function.color)


if __name__ == "__main__":
    e = 0.0001
    polynomial_domain = Domain(-10, 10)
    functions = [
      Function(lambda t: (1 - (abs(t) - 1) ** 2) ** (1 / 2), Domain(0, 2), color = 'r'),
      Function(lambda t: (1 - (abs(t) - 1) ** 2) ** (1 / 2), Domain(-2, 0), color = 'g'),
      Function(lambda t: -3.0 * (1 - (abs(t) / 2) ** (1 / 2)) ** (1 / 2), Domain(0, 2), color = 'y'),
      Function(lambda t: -3.0 * (1 - (abs(t) / 2) ** (1 / 2)) ** (1 / 2), Domain(-2, 0), color = 'b')
    ]
    images = []
  
    fig = plt.figure()
    ax = fig.add_subplot(111)
  
    config_subplot()
    ax.set_title("Funções originais")
    plot_functions(functions)
    add_figure_to_images(images, 20)
  
    for i in range(1, 7):
        config_subplot()
        ax.set_title("{}{}".format("Ordem = ", i))
        plot_functions(functions)
        
        polynomials = [
         Function(taylor(functions[0].f, 1, i), Domain(-10, 10), 'r--'),
         Function(taylor(functions[1].f, -1, i), Domain(-10, 10), 'g--'),
         Function(taylor(functions[2].f, 1, i), Domain(-10, 10), 'y--'),
         Function(taylor(functions[3].f, -1, i), Domain(-10, 10), 'b--')
        ]
  
        plot_functions(polynomials)
        add_figure_to_images(images, 15)
        
    for function in functions:
        function.color = 'r' 
    config_subplot()
    plot_functions(functions)
    add_figure_to_images(images, 20)
  
    imageio.mimsave('grafico.gif', images)
    print('Gif gerado com sucesso!')


