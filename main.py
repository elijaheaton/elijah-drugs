# This is a project I'm writing slowly because I was hit by a car, have to take drugs to
#   alleviate the pain, and love graphs.
import pandas as pd
import datetime
import os

from plotting import *


def print_menu_options():
    print('\t1) Upload new data')
    print('\t2) See data')
    print('\t3) See graphs')
    print('\tq) quit')


def input_data(data):
    print('Please input the date of taking the drugs in mm/dd/yyyy format: ', end='')
    date = input()

    # TODO error check
    date = [int(d) for d in date.split('/')]

    print('Please input the time of taking the drugs in 24-hour hh:mm format: ', end='')
    time=input()

    # TODO error check
    time = [int(t) for t in time.split(':')]

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
    print('\t1) Drug use per time of day')
    print('\t2) Time between uses of of OxyCodone per week')
    i = input()
    if i == '1':
        graph_drug_time_separate(data)
    elif i == '2':
        graph_oxycodone_use_per_week(data)
    # todo make repeatable


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

