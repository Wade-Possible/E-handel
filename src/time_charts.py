import matplotlib.pyplot as plt

def plot_bar(labels, values, title, x_label, y_label):
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.bar(labels, values, color="steelblue")  # draw one bar per label
    ax.bar_label(bars, fmt="%.0f")  # write the value on top of each bar
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    return fig # send the chart back