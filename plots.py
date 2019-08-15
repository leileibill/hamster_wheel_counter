
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import glob

master_df = pd.DataFrame()

for file in glob.glob("*.csv"):
    print(file)

    df = pd.read_csv(file, header=None)

    master_df = pd.concat([master_df, df]) 
    
master_df = pd.DataFrame(master_df.values, columns=['time', 'count'])

master_df['time'] = pd.to_datetime(master_df['time'])

master_df = master_df.set_index('time')

master_df['count'] = master_df['count'].astype('int64')


# plot_df = master_df['2019-08-13']
plot_df = master_df

data = [
    go.Bar(x=plot_df.index, y=np.diff(plot_df['count']),
        marker_line_width=0
        # mode='markers'
    )
]

fig = go.Figure(data)
fig.update_layout(bargap=0)
fig.show()