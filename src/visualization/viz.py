# src/visualization/viz.py
import matplotlib.pyplot as plt

def plot_series(time, series, xlabel='Time', ylabel='Value', title=None):
    plt.figure(figsize=(10, 6))
    plt.plot(time, series)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title:
        plt.title(title)
    plt.grid(True)
    plt.show()
