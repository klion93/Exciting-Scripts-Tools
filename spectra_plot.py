import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy as np 

# Format für y-Achse
y_formatter = matplotlib.ticker.ScalarFormatter(useOffset=False)
ax.yaxis.set_major_formatter(y_formatter)