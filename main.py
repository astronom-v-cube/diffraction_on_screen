import matplotlib.pyplot as plt
import numpy as np
from data import *
from utils import PlotGraph

plotter_circle = PlotGraph()
plotter_circle.plotting_base_graphs(circle_8_2ghz, circle_10ghz, circle_11_8ghz)
plt.savefig(f'img/circle.png', dpi = 300)
plt.close(plotter_circle.fig)

plotter_big_circle = PlotGraph()
plotter_big_circle.plotting_base_graphs(big_circle_8_2ghz, big_circle_10ghz, big_circle_11_8ghz)
plt.savefig(f'img/big_circle.png', dpi = 300)
plt.close(plotter_big_circle.fig)

plotter_max_circle = PlotGraph()
plotter_max_circle.plotting_base_graphs(max_circle_8_2ghz, max_circle_10ghz, max_circle_11_8ghz)
plotter_max_circle.plot_additional_graph(cut_x_DOP, max_circle_8_2ghz_dop, label='8.2 GHz additional', linestyle='-', color='k')
plotter_max_circle.plot_additional_graph(cut_x_DOP, max_circle_10ghz_dop, label='10 GHz additional', linestyle='--', color='k')
plotter_max_circle.plot_additional_graph(cut_x_DOP, max_circle_11_8ghz_dop, label='11.8 GHz additional', linestyle=':', color='k')
plt.savefig(f'img/max_circle.png', dpi = 300)
plt.close(plotter_max_circle.fig)

plotter_square = PlotGraph()
plotter_square.plotting_base_graphs(square_8_2_ghz, square_10_ghz, square_11_8ghz)
plt.savefig(f'img/square.png', dpi = 300)
plt.close(plotter_square.fig)

plotter_nonsymmetrical = PlotGraph()
plotter_nonsymmetrical.plot_additional_graph(x, nonsymmetrical_8_2_ghz, label='8.2', linestyle='-', color='b')
plotter_nonsymmetrical.plot_additional_graph(x, nonsymmetrical_10_ghz, label='10 GHz', linestyle='-', color='r')
plotter_nonsymmetrical.plot_additional_graph(cut_x, nonsymmetrical_11_8ghz, label='11.8 GHz', linestyle='-', color='g')
plotter_nonsymmetrical.plot_additional_graph(cut_x_DOP, nonsymmetrical_11_8ghz_DOP, label='11.8 GHz additional', linestyle='--', color='k')
plt.grid(True)
plt.tight_layout()
plt.savefig(f'img/nonsymmetrical.png', dpi = 300)
plt.show()
plt.close(plotter_nonsymmetrical.fig)

plotter_square = PlotGraph()
plotter_square.plotting_base_graphs(square_8_2_ghz, square_10_ghz, square_11_8ghz)
plt.savefig(f'img/square.png', dpi = 300)
plt.close(plotter_square.fig)

