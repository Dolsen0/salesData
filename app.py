import matplotlib.pyplot as plt

import plotly.graph_objects as go

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
revenue = [1003, 300, 300, 566, 387, 660, 1100]

def revenue_by_day(days, revenue):
    plt.figure(figsize=(7, 7))
    plt.subplot(131)
    plt.bar(days, revenue, color='green')
    plt.subplot(133)
    plt.plot(days, revenue, color='blue')
    plt.suptitle('Revenue by Day', fontsize=20)
    plt.show()
# revenue_by_day(days, revenue)

def gauge_chart(days, revenue):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = revenue[0],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"{days[0]} Sales Revenue"}))

    fig.show()

gauge_chart(days, revenue)