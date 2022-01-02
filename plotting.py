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


# This graph shows the average time between taking Ibuprofen and Tylenol, by iteration
def graph_drug_use_per_iteration(data):
    tyl = data[data['Tylenol'] > 0]['Time']
    ibu = data[data['Ibuprofen'] > 0]['Time']

    i = 0
    length = len(data.index)
    len_t = len(tyl) - 1
    len_i = len(ibu) - 1

    time_t = [0] * len_t
    time_i = [0] * len_i

    while i < length - 1:
        if i < len_t:
            t1 = tyl.iloc[i]
            t2 = tyl.iloc[i + 1]
            delta = (t2 - t1).total_seconds() / 3600
            time_t[i] = delta
        if i < len_i:
            i1 = ibu.iloc[i]
            i2 = ibu.iloc[i + 1]
            delta = (i2 - i1).total_seconds() / 3600
            time_i[i] = delta
        i += 1

    plt.plot(np.arange(len_t), time_t, label='Tylenol')
    plt.plot(np.arange(len_i) + 0.2, time_i, label='Ibuprofen')
    plt.ylabel('Number of hours between use')
    plt.xlabel('Iteration of taking drugs')
    plt.title('How long Elijah was able to go\nwithout using Ibuprofen or Tylenol')
    plt.legend()
    plt.show()


# Find color for a bar based on which drug is most common in that bar
#   TODO: apply this to graph 1
def color_triangle(data):
    total = len(data)
    i, o, t = 0
    for d in data:
        i += 1 if d == 'i' else 0
        o += 1 if d == 'o' else 0
        t += 1 if d == 't' else 0

    return [i/total, t/total, o/total]
