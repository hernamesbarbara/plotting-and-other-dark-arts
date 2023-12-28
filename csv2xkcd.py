import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

matplotlib.rcParams['font.family'] = 'Humor Sans'


def smooth_series(series, window_length=5, poly_order=2):
    return savgol_filter(series, window_length, poly_order)


def plot_smoothed_data(df, xlabel, ylabel, title, subtitle, xticks_step=2, linewidth=3.5, xlabel_fontsize=18, ylabel_fontsize=18, title_fontsize=24, plot_size=8):
    # Apply XKCD style
    plt.xkcd(scale=2.5, length=250, randomness=10)
    fig, ax = plt.subplots(figsize=(plot_size, plot_size//1.15))

    # Plot
    ax.plot(df['date'], df['n_smooth'], color='#00b42e',
            linewidth=linewidth, solid_capstyle='round')

    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

    # X-axis formatting
    # Adjust tick step for readability
    ax.set_xticks(df['date'][::xticks_step])
    ax.set_xticklabels(df['date_label'][::xticks_step], rotation=45)
    ax.set_xlabel(xlabel, fontsize=xlabel_fontsize)

    # Y-axis formatting
    ax.set_ylabel(ylabel, fontsize=ylabel_fontsize)
    ax.tick_params(axis='y', labelsize=0)

    # Adjust y-ticks number
    current_yticks = ax.get_yticks()
    new_yticks = np.linspace(current_yticks[0], current_yticks[-1], 10)
    ax.set_yticks(new_yticks)

    # Adjust spines
    ax.spines['top'].set_linewidth(0)  # Hide top spine
    ax.spines['right'].set_linewidth(0)  # Hide right spine
    ax.spines['bottom'].set_linewidth(linewidth)
    ax.spines['left'].set_linewidth(linewidth)

    # Grid and Title
    ax.grid(False)
    ax.set_title(title, fontsize=title_fontsize)
    ax.text(0.5, 1.03, subtitle, transform=ax.transAxes,
            ha="center", va="top", fontsize=title_fontsize*0.75)

    plt.tight_layout()
    plt.show()


# Load data
csv_file = "data.csv"
df = pd.read_csv(csv_file, sep=',')
df['n_smooth'] = smooth_series(df['n'])
# df.loc[0, 'n_smooth'] = 0

plot_size = 8  # 8x8 inches for a square plot
plot_smoothed_data(df, xlabel="this is my horse. my horse is amazing.", ylabel="i'm flying !!",
                   title="from thoropass.arr import antigravity", subtitle='',
                   plot_size=plot_size)
