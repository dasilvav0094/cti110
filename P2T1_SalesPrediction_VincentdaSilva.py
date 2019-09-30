#A program to predict projected sales profit
#09.29.19
#CTI-110 P2T1 - Sales Prediction
#Vincent daSilva
#

""" Pseudocode

Input the total sales

Calculate the profit as 23 percent of total sales

Display the profit
"""

#User input total sales
total_sales = float(input("Enter the projected sales: "))

#calculate profit as 23 percent of total sales
profit = total_sales * 0.23

#display the profit
print('The profit is $', format(profit, ',.2f'))
