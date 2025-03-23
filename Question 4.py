'''
Question 4 

A magician has a special trick where he can transform words by swapping adjacent letters.
However, he wants to know the minimum number of swaps required to convert one word into another.
Your task is to find the minimum number of swaps needed to transform a given word A into another word B by only swapping adjacent letters.
If the transformation is not possible, print -1.

Input Format:
The first line contains an integer N, the length of both words.
The second line contains a string A (original word).
The third line contains a string B (target word).

Output Format: 
A single integer representing the minimum number of swaps required to transform A into B. 
If it's not possible to transform A into B by swapping adjacent letters, output -1.

Example 1: 

Input:
         5
         abcde
         edcba
Output: 10
Explanation:
To transform "abcde" into "edcba", the following swaps occur:
Swap d and e: abcd**e** → ab**e**cd
Swap c and e: abe**c**d → ab**ec**d
Swap b and e: abecd → **aeb**cd
Swap a and e: aebcd → **eab**cd
Move d and c leftward similarly...
Total swaps required = 10

Example 2: 

Input:
         4 
         abcd 
         dcba
Output: 6
Explanation:
Swaps are needed to bring d to the first position and a to the last, requiring 6 swaps.

Example 3: 

Input:
         4 
         abcd 
         dabc
Output: -1
Explanation:
It's not possible to rearrange "abcd" into "dabc" using only adjacent swaps, so the answer is -1

Solution:'''

n=int(input())
a=list(input().strip())
b=list(input().strip())
if a!=b[::-1]:print(-1)
else:print(n*(n-1)//2)
