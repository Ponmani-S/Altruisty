'''Question 2: 

A treasure hunter follows a path represented by a string. The character T represents a treasure, and . represents an empty space.
The string consists of only these two characters. Your task is to determine the number of treasures found within given segments of the path. 
You will be given multiple queries, each specifying a start index and an end index (1-indexed). For each query, count the number of treasures (T) in the specified range.

Input Format:
The first line contains a string s consisting of T (treasures) and . (empty spaces).
The second line contains an integer n, representing the number of queries.
The next n lines each contain two integers, representing startIndex[i] and endIndex[i] (1-indexed).

Output Format: For each query, print a single integer representing the number of treasures found in the given range.

Example 1:

Input: 
          T..T.T
          2
          1 5
          3 6
Output: 
           2
           2
Explanation:
1️⃣ Substring from index (1,5) → "T..T." → Contains 2 treasures.
2️⃣ Substring from index (3,6) → ".T.T" → Contains 2 treasures.

Example 2: 

Input: 
          T.T.TT.T
          3
          2 5
          1 7
          4 8
Output:
           2
           4 
           3
Explanation:
1️⃣ Substring from index (2,5) → ".T.T" → Contains 2 treasures.
2️⃣ Substring from index (1,7) → "T.T.TT." → Contains 4 treasures.
3️⃣ Substring from index (4,8) → "T.TT.T" → Contains 3 treasures.

Solution:'''

a=input().strip()
for i in range(int(input())):
    b,c=map(int,input().split())
    print(a[b-1:c].count('T'))
