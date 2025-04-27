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

    def _prepare_x_and_y(self, y_array: np.ndarray):
        n = len(y_array)
        full_len = len(self.full_x)

        if n > full_len:
            raise ValueError("Массив измерений длиннее базовой оси X")

        center = full_len // 2
        half = n // 2

        if n % 2 == 0:
            # Чётное число точек — симметрично вокруг центра, напр. [-1, 1]
            start = center - half
            end = center + half
        else:
            # Нечётное — тоже симметрично, но включая центральную точку
            start = center - half
            end = center + half + 1

        x_trimmed = self.full_x[start:end]
        return y_array, x_trimmed


    def cubic_spline_interpolation(x, y, x_for_spline):
        cs = CubicSpline(x, y)
        new_y = cs(x_for_spline)
        return new_y

    def dbm2linear(dbm_list):
        linear_list = [10 ** (dbm_value / 10) for dbm_value in dbm_list]
        return linear_list

    def plotting_base_graphs(self, array82ghz: np.ndarray, array10ghz: np.ndarray, array118ghz: np.ndarray, dbm2linear: Boolean = False):

        if dbm2linear:
            array82ghz = PlotGraph.dbm2linear(array82ghz)
            array10ghz = PlotGraph.dbm2linear(array10ghz)
            array118ghz = PlotGraph.dbm2linear(array118ghz)

        array82ghz, x82 = self._prepare_x_and_y(array82ghz)
        array10ghz, x10 = self._prepare_x_and_y(array10ghz)
        array118ghz, x118 = self._prepare_x_and_y(array118ghz)

        x_for_spline_82 = np.linspace(x82[0], x82[-1], 4096)
        x_for_spline_10 = np.linspace(x10[0], x10[-1], 4096)
        x_for_spline_118 = np.linspace(x118[0], x118[-1], 4096)

        y82 = PlotGraph.cubic_spline_interpolation(x82, array82ghz, x_for_spline_82)
        y10 = PlotGraph.cubic_spline_interpolation(x10, array10ghz, x_for_spline_10)
        y118 = PlotGraph.cubic_spline_interpolation(x118, array118ghz, x_for_spline_118)

        print(y82)

        self.ax.plot(x_for_spline_82, y82, label='8.2 GHz', color='b', linewidth=3)
        self.ax.plot(x_for_spline_10, y10, label='10 GHz', color='r', linewidth=3)
        self.ax.plot(x_for_spline_118, y118, label='11.8 GHz', color='g', linewidth=3)

        self.ax.grid(True)
        self.ax.legend()
        plt.tight_layout()

    def plot_additional_graph(self, y_data, dbm2linear: Boolean = False, **kwargs):
        if dbm2linear:
            y_data = PlotGraph.dbm2linear(y_data)

        y_data, x_data = self._prepare_x_and_y(y_data)
        x_for_spline = np.linspace(x_data[0], x_data[-1], 4096)
        y_data = PlotGraph.cubic_spline_interpolation(x_data, y_data, x_for_spline)
        self.ax.plot(x_for_spline, y_data, linewidth=3, **kwargs)
        plt.legend()