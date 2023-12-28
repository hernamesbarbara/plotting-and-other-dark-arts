import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

csv_file = "data.csv"

df = pd.read_csv(csv_file, sep=',')

window_length = 5
poly_order = 2
df['n_smooth'] = savgol_filter(df['n'], window_length, poly_order)

# Plotting adjustments
plt.xkcd()  # Apply XKCD style
fig, ax = plt.subplots()

ax.plot(df['date'], df['n_smooth'], color='#00b42e',
        linewidth=4, solid_capstyle='round')

# Setting x-axis ticks and labels
ax.set_xticks(df['date'][::2])  # only label every-other date for readability
# rorate x labs 45 degrees too
ax.set_xticklabels(df['date label'][::2], rotation=45)

ax.set_ylabel("i'm flying !!", fontsize=24)  # 20pt increased by 20%

# rm y-tick labs
ax.tick_params(axis='y', labelsize=0)

# specifiy num y-ticks
current_yticks = ax.get_yticks()
new_yticks = np.linspace(current_yticks[0], current_yticks[-1], 10)
ax.set_yticks(new_yticks)

ax.spines['top'].set_linewidth(0)  # Hide the top spine
ax.spines['right'].set_linewidth(0)  # Hide the right spine
ax.spines['bottom'].set_linewidth(4)
ax.spines['left'].set_linewidth(4)

# Removing gridlines
ax.grid(False)

ax.set_title("from thoropass.arr import antigravity", fontsize=30)

ax.set_xlabel('')


plt.tight_layout()
plt.show()
