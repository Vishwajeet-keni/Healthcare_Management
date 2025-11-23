from Tests import *
import matplotlib.pyplot as plt

pbLine("HEALTH MANAGER","M")

pbLine("Presonal info:","B")
name=input("Name: ")
age=float(input("Age: "))
sex=input("Sex (Male/Female): ")
height=float(input("Height (in cm): "))
weight=float(input("Weight (in kg): "))
bmi=BMI(height,weight)

testAvalable=["LifeStyle Health Risk                (yes/no): ",    #0
              "Heart Disease                        (yes/no): ",    #1
              "Diabetes Early-Warning Analyzer      (yes/no): ",    #2
              "Mental Stress Level Tracker          (yes/no): ",    #3
              "Daily Vital Signs Health Monitor     (yes/no): ",    #4
              "Obesity & Fitness Risk Analyzer      (yes/no): ",    #5
              "Personal Immunity Tracker            (yes/no): ",    #6
              "Air Quality Health Risk Estimator    (yes/no): ",    #7
              "COVID / Flu Risk Checker             (yes/no): ",    #8
              "Senior Citizen Health Risk Monitor   (yes/no): "     #9
              ]
tests=[test0,test1,test2,test3,test4,test5,test6,test7,test8,test9]
test_asked=[]
pbLine(space=True)
pbLine("Test Avalable :","M")

for i in range(len(testAvalable)):
    if input(testAvalable[i]).lower()=="yes":
        test_asked.append(tests[i])
pbLine(space=True)

test_taken=[]
scores=[]
risk_level=[]
suggestions=[]
for task in test_asked:
    tname, score, risk, sug=task(height, weight, bmi, age, sex)
    test_taken.append(tname)
    scores.append(score)
    risk_level.append(risk)
    suggestions.append(sug)

risk_to_value = {
    "Low Risk": 80,
    "Medium Risk": 50,
    "High Risk": 20
}
risk_numeric = [risk_to_value[r] for r in risk_level]

plt.style.use("seaborn-v0_8")
plt.figure(figsize=(13, 7))
plt.plot(test_taken, scores, marker='o', linewidth=3, markersize=10, label="Health Score (0–100)")
plt.plot(test_taken, risk_numeric, marker='s', linewidth=3, markersize=10, label="Risk Level Score")
plt.title("Health Test Results Overview", fontsize=18, fontweight='bold')
plt.xlabel("Tests Taken", fontsize=14)
plt.ylabel("Score / Risk Level", fontsize=14)
plt.xticks(rotation=35, ha="right", fontsize=12)
plt.grid(True, linewidth=0.5,color="Black", linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
