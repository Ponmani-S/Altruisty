'''Question 3 

A row of magical lanterns is represented by an array where each element indicates the brightness level of a lantern.
Your task is to find the maximum brightness level in every contiguous subarray of size ‘k’.
Then, return the minimum value among all those maximum brightness levels.

Input Format:
The first line contains an integer k, the size of the subarray. The second line contains an integer n, the size of the brightness array.
The next n lines each contain an integer representing the brightness level of a lantern.
Output Format: Print a single integer representing the minimum value among all maximum brightness levels in each subarray of size k.

Example 1: 

Input: 3 7 1 3 5 2 8 6 4
Output: 5
Explanation:
The contiguous subarrays of size k=3 are:
[1, 3, 5] → Maximum = 5
[3, 5, 2] → Maximum = 5
[5, 2, 8] → Maximum = 8
[2, 8, 6] → Maximum = 8
[8, 6, 4] → Maximum = 8
The minimum of these maximums is 5.

Example 2: 

Input: 2 5 10 20 30 40 50
Output: 20
Explanation:
The contiguous subarrays of size k=2 are:
[10, 20] → Maximum = 20
[20, 30] → Maximum = 30
[30, 40] → Maximum = 40
[40, 50] → Maximum = 50
The minimum of these maximums is 20.

Soltuion:'''

m=int(input())
n=int(input())
a=list(map(int,input().split()))
b=max(a)
for i in range(n-m+1):
    b=min(b,max(a[i:i+m]))
print(b)
