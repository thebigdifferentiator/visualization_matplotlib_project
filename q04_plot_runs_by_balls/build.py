# %load q04_plot_runs_by_balls/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_runs_by_balls():
    x=ipl_df.groupby(['match_code','batsman']).count()['delivery']
    y=ipl_df.groupby(['match_code','batsman']).sum()['runs']
    plt.scatter(x,y)


