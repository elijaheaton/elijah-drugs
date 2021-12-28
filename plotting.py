import matplotlib.pyplot as plt
import numpy as np


# This function looks at what time of day I take drugs where each drug is counted separately
def graph_drug_time_separate(data):
    size = data['Ibuprofen'].sum() + data['Tylenol'].sum() + data['OxyCodone'].sum()
    times = [None] * size
    offset = 0
    for i in range(len(data.index)):
        d = data.iloc[i]
        time = str(d['Time'])[11:-3]
        hour, minute = time.split(':')
        hour = int(hour)
        if int(minute) > 29:
            hour = (hour + 1) % 24

        # now find the number of drugs taken at this time and update the offset
        drugs = d[1:].sum()
        for j in range(drugs):
            times[i + offset] = hour
            offset += 1
        offset -= 1

    plt.hist(times, orientation='horizontal', rwidth=0.7, bins=range(25))
    plt.yticks(range(24))
    plt.ylabel('Time of the day drugs are taken')
    plt.xlabel('Number of drugs taken overall')
    plt.title('Number of drugs taken at each hour of \nthe day over the course of recovery')
    plt.show()


# This graph shows the average time between taking OxyCodone per week
# todo: change everything about this
def graph_oxycodone_use_per_week(data):
    oxy = data[data['OxyCodone'] > 0]['Time']
    tyl = data[data['Tylenol'] > 0]['Time']
    ibu = data[data['Ibuprofen'] > 0]['Time']

    i = 0
    length = len(data.index)
    time_o = [0] * (length - 1)
    time_t = [0] * (length - 1)
    time_i = [0] * (length - 1)

    while i < length - 1:
        if i < len(oxy) - 1:
            o1 = oxy.iloc[i]
            o2 = oxy.iloc[i + 1]
            delta = (o2 - o1).total_seconds() / 3600
            time_o[i - 1] = delta
        if i < len(tyl) - 1:
            t1 = tyl.iloc[i]
            t2 = tyl.iloc[i + 1]
            delta = (t2 - t1).total_seconds() / 3600
            time_t[i - 1] = delta
        if i < len(ibu) - 1:
            i1 = ibu.iloc[i]
            i2 = ibu.iloc[i + 1]
            delta = (i2 - i1).total_seconds() / 3600
            time_i[i - 1] = delta
        i += 1

    plt.bar(np.arange(length - 1), time_o, width=0.3, label='O')
    plt.bar(np.arange(length - 1) + 0.3, time_t, width=0.3, label='T')
    plt.bar(np.arange(length - 1) + 0.6, time_i, width=0.3, label='I')
    plt.ylabel('Number of hours between use')
    plt.xlabel('Iteration of taking drugs')
    plt.title('TBD')
    plt.show()
