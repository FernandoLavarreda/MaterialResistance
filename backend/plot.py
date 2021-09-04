# Fernando Lavarreda
# Graph beam with planck stress for a given momentum

from random import random
import matplotlib.pyplot as plt


def plot_one(beams:list, plancks:list, label:str, vlines:list, vlabels:list):
    color = (random(), random(), random())
    plt.plot(beams[0], beams[1], label=label, color=color)
    plt.plot(plancks[0], plancks[1], color=color)
    for v in range(len(vlines)):
        plt.vlines(vlines[v], beams[1][0]*2, plancks[1][1]*2, label=vlabels[v])
    plt.vlines(0, beams[1][0]*2, plancks[1][1]*2, color="black")
    plt.hlines(0, min(vlines)*1.2, max(vlines)*1.2, color="black")
    plt.xlabel("Esfuerzo")
    plt.ylabel("Altura")
    plt.title("Altura/Esfuerzo")
    plt.legend()
    plt.show()


def plot_many(beams:list, plancks:list, labels:list, vlines:list, vlabels:list):
    COLORS =["#ff2400", "blue", "#d0f0c0", "#e34234"]
    for plot in range(len(beams)):
        color = (random(), random(), random())
        plt.plot(beams[plot][0], beams[plot][1], label=labels[plot], color=color)
        plt.plot(plancks[plot][0], plancks[plot][1], color=color)
        plt.annotate(round(beams[plot][0][0], 2), (beams[plot][0][0], beams[plot][1][0]))
        plt.annotate(round(beams[plot][0][1], 2), (beams[plot][0][1], beams[plot][1][1]))
        plt.annotate(round(plancks[plot][0][0], 2), (plancks[plot][0][0], plancks[plot][1][0]))
        plt.annotate(round(plancks[plot][0][1], 2), (plancks[plot][0][1], plancks[plot][1][1]))
    for v in range(len(vlines)):
        plt.vlines(vlines[v], -70, 70, label=vlabels[v], color=COLORS[v])
    plt.vlines(0, -140, 140, color="black", linewidth=0.4)
    plt.hlines(0, min(vlines)*1.2, max(vlines)*1.2, color="black", linewidth=0.4)
    plt.xlabel("Esfuerzo")
    plt.ylabel("Altura")
    plt.title("Altura/Esfuerzo")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_momentum(values:list, labels:list, annotations:list):
    x = 0
    for value in values:
        plt.scatter(x, value, label=labels[x])
        plt.annotate(round(annotations[x]), (x, value+0.5))
        x+=1
    plt.ylabel("Momento")
    plt.title("Momento")
    plt.legend()
    plt.tight_layout()
    plt.show()
