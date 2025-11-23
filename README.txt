============================================================
                      HEALTH MANAGER PROJECT
============================================================

This is a simple Python-based "Health Manager" that allows a 
user to enter their basic details and take different health 
tests. Each test gives a score, risk level, and a small 
suggestion. At the end, the program also plots all the results 
on a clean Matplotlib graph.

I created this project mainly to practice Python functions, 
modular programming, and some basic data visualization.

------------------------------------------------------------
1. What This Program Does
------------------------------------------------------------

• Takes user inputs like age, gender, height, and weight  
• Calculates BMI  
• Lets the user choose from 10 different health-related tests  
• Each test:
    - Asks a few questions
    - Calculates a “Health Score” (0–100)
    - Determines a Risk Level (Low / Medium / High)
    - Gives a suggestion based on the risk  
• Plots all the selected tests in a single graph

The idea is to get a quick, simple overview of different
health factors — not a medical diagnosis.

------------------------------------------------------------
2. The 10 Available Tests
------------------------------------------------------------

1) Lifestyle Health Risk  
2) Heart Disease Risk  
3) Diabetes Early-Warning Analyzer  
4) Mental Stress Level Tracker  
5) Daily Vital Signs Monitor  
6) Obesity & Fitness Analyzer  
7) Personal Immunity Tracker  
8) Air Quality Health Risk Estimator  
9) COVID / Flu Risk Checker  
10) Senior Citizen Health Risk Monitor

Each of these tests is written as a separate function inside
`Tests.py` so the main file stays clean and easy to read.

------------------------------------------------------------
3. Project Structure
------------------------------------------------------------

Group_Project/
│
├── main.py       → Main program (user input + flow)  
├── Tests.py      → All test functions (test0–test9)
├── README.md     → Project description
└── README.txt    → You're reading this :)  


------------------------------------------------------------
4. How to Run the Program
------------------------------------------------------------

1. Make sure Python 3 is installed  
2. Install matplotlib:
       pip install matplotlib

3. Run the program using:
       python3 main.py

Then just follow the on-screen instructions. After you finish 
the selected tests, the program will show a Matplotlib graph 
with your scores and risk levels.

------------------------------------------------------------
5. Graph Output
------------------------------------------------------------

The graph shows:
• X-axis → Names of the tests you took  
• Y-axis → Health Score + Risk Level  
• Two lines → One for score, one for risk  

The test names are slightly tilted for readability.

------------------------------------------------------------
6. Why I Built This
------------------------------------------------------------

I wanted a project that:
• Is simple but looks complete  
• Uses functions and modular programming properly  
• Involves user interaction  
• Includes data visualization with Matplotlib  

It’s also easy to expand — new tests can be added just by 
writing another function.

------------------------------------------------------------
7. Notes
------------------------------------------------------------

This program is **not** medically accurate or scientifically 
validated. It's just a learning project meant to demonstrate:
• Python basics  
• Logic building  
• Data visualization  

------------------------------------------------------------
8. Author
------------------------------------------------------------

Created by: **Vishwajeet Keni**  
Project: **Health Manager (Python)**

------------------------------------------------------------
End of README
------------------------------------------------------------
