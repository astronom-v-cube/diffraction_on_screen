from xmlrpc.client import Boolean
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.rcParams.update({'font.size': 20})

class PlotGraph():

    def __init__(self):
        self.fig, self.ax = plt.subplots(num="График", figsize=(12, 8))
        self.full_x = np.linspace(-100, 100, 41)
        self.cut_x_60 = np.linspace(-60, 60, 25)
        self.cut_x_25 = np.linspace(-25, 25, 26)
        self.cut_x_50 = np.linspace(-50, 50, 51)

    def cubic_spline_interpolation(x, y, x_for_spline):
        cs = CubicSpline(x, y)
        new_y = cs(x_for_spline)
        return new_y

    def dbm2linear(dbm_list):
        linear_list = [10 ** (dbm_value / 10) for dbm_value in dbm_list]
        return linear_list

    def plotting_base_graphs(self, array82ghz: np.ndarray, array10ghz: np.ndarray, array118ghz: np.ndarray, x_arr: str = 'normal', dbm2linear: Boolean = False):

        if x_arr == 'normal':
            x = self.full_x
        elif x_arr == 'cut_25':
            x = self.cut_x_25
        elif x_arr == 'cut_50':
            x = self.cut_x_50
        elif x_arr == 'cut_60':
            x = self.cut_x_60

        if dbm2linear:
            array82ghz = PlotGraph.dbm2linear(array82ghz)
            array10ghz = PlotGraph.dbm2linear(array10ghz)
            array118ghz = PlotGraph.dbm2linear(array118ghz)

        x_for_spline = np.linspace(x[0], x[-1], 4096)

        array82ghz = PlotGraph.cubic_spline_interpolation(x, array82ghz, x_for_spline)
        array10ghz = PlotGraph.cubic_spline_interpolation(x, array10ghz, x_for_spline)
        array118ghz = PlotGraph.cubic_spline_interpolation(x, array118ghz, x_for_spline)

        self.ax.plot(x_for_spline, array82ghz, label='8.2 GHz', color='b', linewidth = 3)
        self.ax.plot(x_for_spline, array10ghz, label='10 GHz', color='r', linewidth = 3)
        self.ax.plot(x_for_spline, array118ghz, label='11.8 GHz', color='g', linewidth = 3)

        self.ax.grid(True)
        self.ax.legend()
        plt.tight_layout()

    def plot_additional_graph(self, x_data, y_data, dbm2linear: Boolean = False, **kwargs):

        if dbm2linear:
            y_data = PlotGraph.dbm2linear(y_data)
        x_for_spline = np.linspace(x_data[0], x_data[-1], 4096)
        y_data = PlotGraph.cubic_spline_interpolation(x_data, y_data, x_for_spline)
        self.ax.plot(x_for_spline, y_data, linewidth = 3, **kwargs)
        plt.legend()
