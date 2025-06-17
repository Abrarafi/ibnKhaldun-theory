import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
from matplotlib.patches import FancyArrowPatch

# Set up dark theme
plt.style.use('dark_background')
plt.rcParams.update({
    'axes.facecolor': '#0d1117',
    'figure.facecolor': '#0d1117',
    'grid.color': '#3b3b3b',
    'text.color': '#e6e6e6'
})

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))
fig.subplots_adjust(left=0.08, right=0.92, top=0.88, bottom=0.12)

# Empire curve function
def empire_curve(x):
    rise = 1 / (1 + np.exp(-0.08*(x-30)))
    fall = 1 / (1 + np.exp(0.06*(x-90)))
    return 100 * rise * fall

x = np.linspace(0, 120, 200)
y = empire_curve(x)

# Plot curve with elegant gradient color
ax.plot(x, y, linewidth=4, color='#66c2a5', zorder=5)
ax.fill_between(x, y, color='#66c2a5', alpha=0.15)

# Refined color palette for phases
phases = [
    (15, "Tribal\nBeginnings", "#a6d854", (0, -30), (5, 70), "Asabiyyah forms\nin harsh conditions"),
    (45, "Conquest &\nConsolidation", "#8da0cb", (0, -35), (-60, 10), "Military victories\nCentralized rule"),
    (60, "Golden Age", "#ffd92f", (0, -25), (0, 20), "Cultural flourishing\nEconomic prosperity"),
    (80, "Decadence", "#fc8d62", (0, -35), (30, 30), "Luxury weakens\nsocial cohesion"),
    (105, "Collapse", "#e78ac3", (0, -30), (20, 40), "Fragmentation\nExternal conquest")
]

for x_pos, label, color, (label_dx, label_dy), (desc_dx, desc_dy), desc in phases:
    y_pos = empire_curve(x_pos)
    ax.scatter(x_pos, y_pos, s=120, color=color, edgecolor='white', linewidth=1.5)
    
    # Phase label
    ax.annotate(label, (x_pos, y_pos),
                xytext=(label_dx, label_dy),
                textcoords='offset points',
                ha='center',
                va='bottom' if label_dy > 0 else 'top',
                fontsize=11,
                weight='bold',
                color=color,
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1a1a', edgecolor=color, alpha=0.8))
    
    # Description
    ax.annotate(desc, (x_pos, y_pos),
                xytext=(desc_dx, desc_dy),
                textcoords='offset points',
                ha='center' if desc_dx > 0 else 'center',
                va='center',
                fontsize=9,
                weight='semibold',
                color='#cccccc',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#1a1a1a', edgecolor='none', alpha=0.7))

# Cycle arrow
arrow = FancyArrowPatch((110, 30), (10, 30),
                        arrowstyle='fancy,head_length=15,head_width=15,tail_width=5',
                        color='#d8b365',
                        mutation_scale=20)
arrow.set_alpha(0.3)  # Set opacity to 30%
ax.add_patch(arrow)


ax.add_patch(arrow)
ax.text(60, 30, "Cyclical Pattern Repeats", ha='center', va='center',
        fontsize=11,weight='semibold', color='#cccccc', bbox=dict(facecolor='#1a1a1a', edgecolor='none', pad=4))

# Final formatting
ax.set(xlim=(0, 120), ylim=(0, 110))
ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=12))
ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xlabel("Generations (Approx. 30 years each)", fontsize=15, weight = 'black', labelpad=10)
ax.set_ylabel("Civilizational Strength\n(Asabiyyah + Institutional Power)", fontsize=12, labelpad=10, weight='bold')
ax.set_title("Ibn Khaldun's Cyclical Theory of Empires", fontsize=16, pad=20, weight='black')

fig.text(0.52, -0.01, "Based on the Asabiyyah concept from Ibn Khaldun's Muqaddimah (1377 CE)", 
         ha='center', fontsize=9, color='#808080',weight='semibold')
fig.text(0.95, 0.02, "@Abrarafi",
         ha='right', fontsize=10, color='#808080',weight='semibold')

plt.tight_layout()
plt.savefig('ibn_khaldun_cycle.svg', bbox_inches='tight')
plt.show()

from google.colab import files
files.download('ibn_khaldun_cycle.svg')
