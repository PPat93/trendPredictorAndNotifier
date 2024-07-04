""" 
Plotter Comb:
Sends/Receives data from Integrator: <- Analyzer, <- Database, -> Mailer;
Creates graphs for content of notification emails;
"""

import matplotlib.pyplot as plt

def plot_graph(data, ticker, start_date, end_date, *horizontal_lines):

    fig, ax = plt.subplots()
    ax.plot(data)
    ax.legend()
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title(f"{ticker} Stock Price ({start_date} to {end_date})")
    plt.show()

plot_graph([1, 2, 3], "NVDA", "121", "12")