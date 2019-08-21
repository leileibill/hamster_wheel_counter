
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import glob
import plotly.offline as plt

master_df = pd.DataFrame()

for file in glob.glob("data/*.csv"):
    print(file)

    df = pd.read_csv(file, header=None)

    master_df = pd.concat([master_df, df])

master_df = pd.DataFrame(master_df.values, columns=['time', 'count'])

master_df['time'] = pd.to_datetime(master_df['time'])

master_df = master_df.set_index('time')

master_df['count'] = master_df['count'].astype('int64')

diff_df = pd.DataFrame(master_df)

diff_df = diff_df.diff()


plot_df_1 = master_df
plot_df_2 = diff_df.groupby(diff_df.index.hour).sum()
# plot_df_2 = plot_df_2.set_index(pd.to_datetime(plot_df_2.index, format='%H'))
plot_df_3 = master_df.resample('D').max()

data = [
    go.Scatter(x=plot_df_1.index, y=plot_df_1['count'],
        marker_line_width=0
        # mode='markers'
    )
]

fig1 = go.Figure(data)

data = [
    go.Bar(x=plot_df_2.index, y=plot_df_2['count'],
        marker_line_width=0
        # mode='markers'
    )
]

fig2 = go.Figure(data=data)
fig2.update_layout(
    title='Count by hour of the day'
)



data = [
    go.Bar(x=plot_df_3.index, y=plot_df_3.diff()['count'],
        marker_line_width=0
        # mode='markers'
    )
]

fig3 = go.Figure(data=data)
fig3.update_layout(
    title='Count by days'
)
plt.plot(fig1, filename='total_count.html')
plt.plot(fig2, filename='count_by_hour_of_the_day.html')
plt.plot(fig3, filename='count_by_days.html')
