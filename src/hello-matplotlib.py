import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class MatplotlibPlot:
    @staticmethod
    def _load_csv_data():
        script_dir = Path(__file__).parent
        csv_path = script_dir.parent / "data/data_matplotlib.csv"

        return pd.read_csv(csv_path)

    def __init__(self):
        self.data = self._load_csv_data()

    def basic_plot(self):
        """
        Sinusoid graph </br>
        Multiple plots
        """
        x = np.linspace(0, 2 * np.pi, 360)
        y = np.sin(x)

        fig, ax = plt.subplots()
        fig.suptitle("Sine function")

        plt.xlabel("Radians")
        plt.ylabel("Value")
        ax.plot(x, y, label="sine")
        ax.legend()

        plt.show()
        ax.clear()

        # Multiple plots
        fig, axs = plt.subplots(3, 2)
        fig.suptitle("Trigonometric functions")

        axs[0, 0].plot(x, np.sin(x), color="red")
        axs[0, 0].set_title("sin")

        y_cosec = np.where(abs(np.sin(x)) > 0.01, 1 / np.sin(x), np.nan)
        axs[0, 1].plot(x, y_cosec, color="blue")
        axs[0, 1].set_title("cosec")

        axs[1, 0].plot(x, np.cos(x), color="orange")
        axs[1, 0].set_title("cos")

        y_sec = np.where(abs(np.cos(x)) > 0.01, 1 / np.cos(x), np.nan)
        axs[1, 1].plot(x, y_sec, color="green")
        axs[1, 1].set_title("sec")

        y_tan = np.where(abs(np.cos(x)) > 0.01, np.sin(x) / np.cos(x), np.nan)
        axs[2, 0].plot(x, y_tan, color="yellow")
        axs[2, 0].set_title("tan")

        y_cot = np.where(abs(np.sin(x)) > 0.01, np.cos(x) / np.sin(x), np.nan)
        axs[2, 1].plot(x, y_cot, color="black")
        axs[2, 1].set_title("cot")

        # fig.tight_layout()
        plt.show()

        ax.clear()

    def single_plot_single_variable(self):
        """
        Single plot line </br>
        Miscellaneous
        """
        df = self.data

        fig, ax = plt.subplots()

        # Single line plot. Amount vs Default row index. Chart and axes title title
        ax.plot(df["amount"])
        ax.set_xlabel("The default row index of DF")
        ax.set_ylabel("Amount")
        ax.set_title("Amount line chart")
        plt.show()
        ax.clear()

        # Single line plot. Amount vs date. Chart and axes title title
        fig, ax = plt.subplots()
        ax.plot(df["date"], df["amount"])
        ax.set_xlabel("Date")
        ax.tick_params(axis="x", rotation=45)
        ax.set_ylabel("Amount")
        ax.set_title("Amount vs date line chart")
        plt.show()
        ax.clear()

        # Single Bar plot. Amount vs date. Chart and axes title
        fig, ax = plt.subplots()
        ax.bar(df["date"], df["amount"])
        ax.set_xlabel("Date")
        ax.tick_params(axis="x", rotation=45)
        ax.set_ylabel("Amount")
        # Add value labels on top of each bar
        for x, y in zip(df["date"], df["amount"]):
            ax.text(x, y, str(y), ha="center", va="bottom")

        ax.set_title("Amount vs date bar chart")
        plt.show()
        fig.tight_layout()
        ax.clear()

        # Single Bar plot. Amount vs category. Chart and axes title
        # ax.bar(df["category"], df["amount"]) # This will set y to a randomly chosen sample.
        df_grouped = df.groupby("category")["amount"].sum().reset_index()

        fig, ax = plt.subplots()
        ax.bar(df_grouped["category"], df_grouped["amount"])
        ax.set_xlabel("category")
        ax.tick_params(axis="x", rotation=45)
        ax.set_ylabel("amount")

        ax.set_title("Total Amount per category bar chart")
        plt.show()
        fig.tight_layout()
        ax.clear()

        # Histogram of amount
        fig, ax = plt.subplots()
        ax.hist(df["amount"], bins=100, color="Red")
        ax.set_xlabel("Amount, bin=100")
        ax.set_ylabel("Count")
        ax.set_title("Amount, bin by 100")
        fig.tight_layout()

        plt.show()

    def multiple_elements_same_plot(self):
        """
        Multiple lines on the same axes
        """
        self._load_csv_data()
        df_raw = self.data

        # Multiple lines on the same axes
        fig, ax = plt.subplots()

        # Select the row and column. All three versions work.
        # df_amount = df_raw.iloc[0::2, 2:3]
        # df_amount = df_raw.loc[df_raw.index[0::2], ["amount"]]
        df_amount = df_raw.loc[df_raw.index % 2 == 0, ["amount"]]
        df_amount_pct = round(df_amount * 100 / df_amount.sum(), 2)
        ax.plot(df_amount.index, df_amount, color="red", label="count")
        ax.plot(df_amount.index, df_amount_pct, color="green", label="percent")
        ax.legend()  # To display the red and green labels as legend.
        plt.show()

        # Multiple lines on the same axes
        # Multiple bars in one chart
        # Overlay multiple histograms

    def different_plot_types(self):
        """
        Line plot for one column </br>
        Bar plot for another column
        """

        self._load_csv_data()
        df_raw = self.data

        # Multiple lines on the same axes
        fig, ax = plt.subplots()

        df_amount = df_raw.loc[df_raw.index % 2 == 0, ["amount"]]
        ax.plot(df_amount.index, df_amount, color="red", label="count")

        df_qty = df_raw.loc[df_raw.index % 2 == 0, "quantity"]
        ax.bar(df_amount.index, df_qty * 10, label="quantity")

        ax.legend()  # To display the red and green labels as legend.
        plt.show()
        pass

        # Line plot for one column
        # Bar plot for another column
        # Line plot for one column
        # Bar plot for another column
        # Scatter plot using two columns
        pass

    def grouped_categorical_plots(self):
        """
        # Grouped chart
        """
        self._load_csv_data()
        df_raw = self.data

        fig, ax = plt.subplots()

        df = df_raw.groupby("category").sum("amount")[["amount"]]
        ax.bar(df.index, df["amount"])
        plt.show()

        pass


if __name__ == "__main__":
    matplotlibPlot = MatplotlibPlot()

    os.system("clear")
    matplotlibPlot.basic_plot()
    # matplotlibPlot.single_plot_single_variable()
    # matplotlibPlot.multiple_elements_same_plot()
    # matplotlibPlot.different_plot_types()
    # matplotlibPlot.grouped_categorical_plots()
