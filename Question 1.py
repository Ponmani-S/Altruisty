'''Question 1 

Rahul is a stock trader who aims to maximize his profit by buying and selling stocks. However, he follows a strict strategy:
He buys a stock only once and sells it only once to maximize his profit. He can only buy before he sells (i.e., the buying day must be earlier than the selling day). 
If stock prices continuously decline, Rahul does not make any transactions. Your task is to determine the maximum profit Rahul could have made given the daily stock prices.

Input Format: The first line contains an integer n, representing the number of days. The next n lines each contain an integer, representing the stock price on that day. 
Output Format: A single integer representing the maximum profit Rahul could have made. If no profit is possible, return 0. 

Example 1: 

Input: 5 7 1 5 3 6 
Output: 5
Explanation: Rahul buys at price 1 on the second day and sells at price 6 on the fifth day, making a profit of 6 - 1 = 5.

Example 2:

Input: 4 10 9 8 6 
Output: 0 
Explanation: Since the prices keep decreasing, Rahul does not buy any stock. Hence, the maximum profit is 0.

Soltuion:'''

n,m=int(input()),0
a=list(map(int,input().split()))
b=a[0]
for i in range(1,n):
    b=min(b,a[i])
    m=max(m,a[i]-b)
print(m)
