'''Question 5

In a smart classroom, energy efficiency is monitored using 5 smart sensors that record power consumption (in watts) at 4 different times during the day.
Your task is to analyze the power consumption data and determine: The sensor with the highest average power consumption (rounded to the nearest integer).
If all sensors consume an average below 50W, display "Energy consumption is optimal."

Input Format: 20 integer values representing power consumption readings for each sensor at 4 different times, organized as follows:

Time 1:
Sensor 1 reading
Sensor 2 reading
Sensor 3 reading
Sensor 4 reading
Sensor 5 reading
Time 2:
Sensor 1 reading
Sensor 2 reading
Sensor 3 reading
Sensor 4 reading
Sensor 5 reading
Time 3:
Sensor 1 reading
Sensor 2 reading
Sensor 3 reading
Sensor 4 reading
Sensor 5 reading
Time 4:
Sensor 1 reading
Sensor 2 reading
Sensor 3 reading
Sensor 4 reading
Sensor 5 reading 

Output Format:
If any power reading is outside the range [10, 200], print "INVALID INPUT" and stop.
Print the sensor number(s) with the highest average power consumption.
If the highest average power consumption is below 50W, print "Energy consumption is optimal."

Example 1: 

Input: 120 110 90 85 80 100 115 85 95 90 110 130 100 80 75 105 125 95 100 85
Output:  Sensor Number : 2
Explanation:The average power consumption per sensor:
Sensor 1: (120+100+110+105​)/4=109
Sensor 2: (110+115+130+125​)/4=120
Sensor 3: (90+85+100+95​)/4=93
Sensor 4: (85+95+80+100)/4​=90
Sensor 5: (80+90+75+85)/4​=83
Sensor 2 has the highest average power consumption of 120W, making it the highest consumer.

Example 2: 

Input: 45 40 35 30 25 50 45 40 35 30 42 38 36 32 28 48 42 37 34 29
Output: Energy consumption is optimal.
Explanation: All sensors have an average power consumption below 50W, so the energy usage is optimal.

Example 3 (Invalid Case): 

Input: 120 110 90 85 220 100 115 85 95 90 110 130 100 80 75 105 125 95 100 85
Output:  INVALID INPUT
Explanation: Since 220 is outside the valid range [10, 200], the input is invalid, and we output "INVALID INPUT".

Solution:'''

a=list(map(int,input().split()))
if not(min(a)>=10 and max(a)<=200):print("INVALID INPUT")
else:
    b=[sum(a[0:20:5])//4,sum(a[1:20:5])//4,sum(a[2:20:5])//4,sum(a[3:20:5])//4,sum(a[4:20:5])//4]
    if max(b)<50:print("Energy consumption is optimal.")
    else:print("Sensor Number:",b.index(max(b))+1)
