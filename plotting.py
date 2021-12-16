import matplotlib.pyplot as plt

# This function looks at what time of day I take drugs where each drug is counted separately
def graph_drug_time_separate(data):
    size = data['Ibuprofen'].sum() + data['Tylenol'].sum() + data['OxyCodon'].sum()
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

    plt.hist(times, orientation='horizontal', rwidth=0.4)
    plt.yticks(range(24))
    plt.ylabel('Time of the day drugs are taken')
    plt.xlabel('Number of drugs taken overall')
    plt.title('Number of drugs taken at each hour of \nthe day over the course of recovery')
    plt.show()
