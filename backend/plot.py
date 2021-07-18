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
    plt.xlabel("Stress")
    plt.ylabel("Height")
    plt.legend()
    plt.show()


def plot_many(beams:list, plancks:list, labels:list, vlines:list, vlabels:list):
    for plot in range(len(beams)):
        color = (random(), random(), random())
        plt.plot(beams[plot][0], beams[plot][1], label=labels[plot], color=color)
        plt.plot(plancks[plot][0], plancks[plot][1], color=color)
    for v in range(len(vlines)):
        plt.vlines(vlines[v], -70, 70, label=vlabels[v])
    plt.xlabel("Stress")
    plt.ylabel("Height")
    plt.legend()
    plt.show()