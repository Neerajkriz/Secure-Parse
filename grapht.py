import matplotlib.pyplot as plt
import numpy as np

# Pipelines and their corresponding scores
pipelines = ['Default Presidio', 'SecureParse']
precision = [0.71, 0.83]
recall = [0.74, 0.86]
f1_score = [0.72, 0.84]

# Set up bar positions
x = np.arange(len(pipelines))
width = 0.25

# Plot setup
fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width, precision, width, label='Precision', color='skyblue')
bars2 = ax.bar(x, recall, width, label='Recall', color='orange')
bars3 = ax.bar(x + width, f1_score, width, label='F1-score', color='green')

# Labels, title, ticks
ax.set_ylabel('Score')
ax.set_title('Graph 4.2: Comparison of Default Presidio vs SecureParse')
ax.set_xticks(x)
ax.set_xticklabels(pipelines)
ax.set_ylim([0, 1.0])
ax.legend()

# Function to annotate bars with values
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width()/2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

fig.tight_layout()

# Save the plot
output_file = 'presidio_vs_secureparse.png'
plt.savefig(output_file)
print(f"Graph saved as: {output_file}")

# Show the plot
plt.show()
