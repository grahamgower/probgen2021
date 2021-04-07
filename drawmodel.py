import sys

import demes
import demesdraw
import matplotlib
import matplotlib.pyplot as plt


def size_max(graph):
    return max(
        max(epoch.start_size, epoch.end_size)
        for deme in graph.demes
        for epoch in deme.epochs
    )


def get_axes(aspect, scale):
    fig_w, fig_h = plt.figaspect(aspect)
    fig, ax = plt.subplots(figsize=(scale * fig_w, scale * fig_h))
    fig.set_tight_layout(True)
    return ax


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: {sys.argv[0]} in.yaml out.pdf")
        exit(1)

    yaml_file, plot_file = sys.argv[1:]
    graph = demes.load(yaml_file)
    w = 1.5 * size_max(graph)
    positions = dict(X=0, A=-w, B=w)
    ax = get_axes(aspect=3 / 4, scale=0.5)
    ax = demesdraw.tubes(graph, positions=positions, ax=ax, inf_ratio=0.4, seed=1)
    ax.figure.savefig(plot_file)
