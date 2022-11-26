import io

from flask import Response
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
app = Flask(__name__)
@app.route('/plot/'
           'a:<float(signed=True):a>/'
           'b:<float(signed=True):b>/'
           'c:<float(signed=True):c>/'
           'xmin:<int(signed=True):xmin>/'
           'xmax:<int(signed=True):xmax>/'
           'ymin:<int(signed=True):ymin>/'
           'ymax:<int(signed=True):ymax>')
def plot_png(a, b, c, xmin, xmax, ymin,ymax):
    fig = Figure(figsize=(12, 7))
    ax1 = fig.add_subplot(111)
    ax1.grid()
    ax1.set_ylim([ymin, ymax])
    x = np.linspace(xmin, xmax, 100)
    y = a*x**2 + b*x + c
    ax1.plot(x, y)

    output = io.BytesIO()
    FigureCanvas(fig).print_figure(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)