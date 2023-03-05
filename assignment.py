# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:33:22 2023

@author: Nimasha
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Read the csv file
# Data in Health expenditure of five countries from 2000 to 2020
health_ex = pd.read_csv("health.csv")
print(health_ex)


def plot_line():
    """ Plot the line chart using above data frames """


# plot the line charts
plt.figure()

plt.plot(health_ex["Year"], health_ex["United Kingdom"],
         label="United Kingdom")
plt.plot(health_ex["Year"], health_ex["United States"], label="United States")
plt.plot(health_ex["Year"], health_ex["Japan"], label="Japan")
plt.plot(health_ex["Year"], health_ex["China"], label="China")
plt.plot(health_ex["Year"], health_ex["Canada"], label="Canada")


plt.xlabel("Year")
plt.ylabel("GDP")
plt.xticks([2000, 2005, 2010, 2015, 2020])
plt.title("Health Expenditure (% of GDP)")
plt.legend()

plt.savefig("Line_plot.png")
plt.show()


# call the function plot_line
plot_line()


def plot_bar():
    """ Plot the bar chart using above data frames """


df = health_ex.iloc[10:]

# create the Bar chart about health expenditure in China from 2010 to 2020
plt.figure()

plt.bar(df["Year"], df["China"])
plt.xlabel("Year")
plt.ylabel("GDP")
plt.xticks([2010, 2011, 2012, 2013, 2014, 2015, 2016,
           2017, 2018, 2019, 2020], rotation=45)
plt.yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])
plt.title("Health Expenditure (% of GDP) - China")
plt.legend()
plt.savefig("Bar_plot.png")
plt.show()


# call the function plot_bar
plot_bar()


def plot_pie():
    """ Plot the pie chart using above data frames """


# create the pie chart of health expenditure in 2000
plt.figure()
plt.figure()
health_ex.iloc[0, 2:].plot.pie()
plt.title("Health Expenditure (% of GDP) - 2000")
plt.legend()
plt.savefig("Pie_plot_2000.png")
plt.show()

# create the pie chart of health expenditure in 2020
plt.figure()
health_ex.iloc[20, 2:].plot.pie()
plt.title("Health Expenditure (% of GDP) - 2020")
plt.legend()
plt.savefig("Pie_plot_2020.png")
plt.show()


# call the function plot_pie
plot_pie()
