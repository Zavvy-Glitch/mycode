#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Practice using MatPlotLib """

import matplotlib.pyplot as plt


def main():

    """ FUNCTION TO GRAPH INSECT POPULATION """

    fig, ax = plt.subplots()
    
    # Contains insect information to build graph
    insects = ['Bees', 'Beetle', 'Dragonfly', 'Mosquito']
    counts = [40, 100, 70, 180]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(insects, counts, label=bar_labels, color=bar_colors)

    # Used to label the bar graph
    ax.set_ylabel('Insect Population (thousands)')
    ax.set_title('Insect Population by kind and color')
    ax.legend(title='Insect Color')

    # Saves file to desired location and desired file type
    plt.savefig("/home/student/mycode/graphing/graphmaker1.png")
    plt.savefig("/home/student/static/graphmaker1.png")

main()
