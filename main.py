# This is a project I'm writing slowly because I was hit by a car, have to take drugs to
#   alleviate the pain, and love graphs.
import pandas as pd
import datetime
import os
import re

from plotting import *


def print_menu_options():
    print('\t1) Upload new data')
    print('\t2) See data')
    print('\t3) See graphs')
    print('\tq) quit')


def print_graph_options():
    print('\t1) Drug use per time of day')
    print('\t2) Time between uses of of OxyCodone per week')
    print('\tb) Back')


def error_check_date(date):
    pattern = '^0[1-9]|1[0-2]/(([0-2][0-9])|3[0-1])/[12][0-9]{3}$'
    return re.match(pattern, date)


def error_check_time(time):
    pattern = '^(([0-1][0-9])|(2[0-3])):[0-5][0-9]$'
    return re.match(pattern, time)


def input_data(data):
    # Get date
    print('Please input the date of taking the drugs in mm/dd/yyyy format: ', end='')
    while True:
        date = input()
        if error_check_date(date):
            break
        else:
            print('Please try again using the mm/dd/yyyy format for a valid date: ', end='')

    date = [int(d) for d in date.split('/')]

    # Get time
    print('Please input the time of taking the drugs in 24-hour hh:mm format: ', end='')
    while True:
        time = input()
        if error_check_time(time):
            break
        else:
            print('Please try again using the hh:mm format for a valid time: ', end='')

    time = [int(t) for t in time.split(':')]

    # Convert to datetime
    dt = datetime.datetime(date[2], date[0], date[1], time[0], time[1])

    print('Did you take Ibuprofen? y/n: ', end='')
    ibuprofen = input()
    ibuprofen = 1 if ibuprofen == 'y' else 0

    print('Did you take Tylenol? y/n: ', end='')
    tylenol = input()
    tylenol = 1 if tylenol == 'y' else 0

    print('Did you take OxyCodone? y/n: ', end='')
    oxycodone = input()
    oxycodone = 1 if oxycodone == 'y' else 0

    # add to dataframe
    data.loc[len(data.index)] = [dt, ibuprofen, tylenol, oxycodone]
    return data.sort_values(by='Time').set_index(pd.Index(range(len(data.index))))


def see_data(data):
    print(data, end='\n\n')


def save_data(data, file):
    print('Saving your data to ed.csv...', end='')
    data.to_csv(file, index=False)
    print('Done!')


def make_graphs(data):
    i = ''
    while i != 'b':
        print_graph_options()
        print('What would you like to do? ', end='')
        i = input()
        if i == '1':
            graph_drug_time_separate(data)
        elif i == '2':
            graph_oxycodone_use_per_week(data)
        else:
            print('Sorry, that is not an option yet.')


if __name__ == '__main__':
    # first set up dataframe
    file = 'ed.csv'

    if file in os.listdir():
        print('Uploading data from ed.csv...', end='')
        data = pd.read_csv(file)
        data['Time'] = pd.to_datetime(data['Time'])
    else:
        print('File ed.csv not found. Creating a new dataframe...', end='')
        data = pd.DataFrame(columns=['Time', 'Ibuprofen', 'Tylenol', 'OxyCodone'])
    print('Done!')

    # next see what the user wants to do
    while True:
        print_menu_options()
        print('What would you like to do? ', end='')
        response = input()

        if response == '1':
            data = input_data(data)
        elif response == '2':
            see_data(data)
        elif response == '3':
            make_graphs(data)
        elif response == 'q':
            save_data(data, file)
            break
