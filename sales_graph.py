import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June']

sales_2024 = [30000, 44500, 22000, 19000, 37500, 46500]
sales_2025 = [25000, 29500, 14500, 38000, 39500, 32500]

# Create figure
plt.figure(figsize=(10, 6))

# Plot 2024 sales
plt.plot(
    months,
    sales_2024,
    linestyle='--',
    marker='o',
    markersize=10,
    linewidth=2.5,
    color='teal',
    markerfacecolor='yellow',
    markeredgecolor='gold',
    label='2024 Sales Data'
)

# Plot 2025 sales
plt.plot(
    months,
    sales_2025,
    linestyle='--',
    marker='o',
    markersize=10,
    linewidth=2.5,
    color='lightcoral',
    markerfacecolor='yellow',
    markeredgecolor='gold',
    label='2025 Sales Data'
)

# Title and labels
plt.title('Sales Data of Two Years', fontsize=18)
plt.xlabel('Months', fontsize=14)
plt.ylabel('Sales Data', fontsize=14)

# Grid
plt.grid(True, linestyle='-', alpha=0.3)

# Rotate month labels
plt.xticks(rotation=45)

# Legend
plt.legend()

# Show graph
plt.show()