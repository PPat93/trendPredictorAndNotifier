""" 
Plotter Comb:
Sends/Receives data from Integrator: <- Analyzer, <- Database, -> Mailer;
Creates graphs for content of notification emails;
"""

import matplotlib.pyplot as plt

def plot_one_graph(data, graph_name, ticker, start_date, end_date, *horizontal_lines):

    fig, ax = plt.subplots()
    ax.plot(data)
    ax.legend()
    ax.set_xlabel('Date')
    ax.set_ylabel(graph_name)
    ax.set_title(f"{ticker} Stock {graph_name} graph ({start_date} to {end_date})")
    ax.hlines(y=horizontal_lines, xmin=start_date, xmax=end_date, linewidth=2, color='r')
    plt.show()

# plot_one_graph([1, 2, 3], "MACD", "NVDA", "1", "12", 4)