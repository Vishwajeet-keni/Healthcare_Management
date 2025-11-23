def pbLine(string=None,position=None,space=False):
    h="-"
    k=55
    if string==None:
        print(h*k)
    else:
        if position=="T":
            print(h*k)
            print(string)
        elif position=="B":
            print(string)
            print(h*k)
        elif position=="M":
            print(h*k)
            print(string)
            print(h*k)
    if space:
        print()


def BMI(height,weight):
    #height-->cm , weigth-->kg
    return (weight/(height/100)**2)*703

def calculate_risk_level(score):
    if score >= 70:
        return "Low Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "High Risk"

def test0(height, weight, bmi, age, gender):
    test_name="Lifestyle Health Risk"
    pbLine(test_name,"M")
    sleep = float(input("Hours of sleep (per day): "))
    exercise = input("Do you exercise daily? (yes/no): ").lower()
    junk_food = input("Do you eat junk food more than 3 times a week? (yes/no): ").lower()

    score = 50

    if sleep >= 7:
        score += 20
    else:
        score -= 10

    if exercise == "yes":
        score += 20
    else:
        score -= 10

    if junk_food == "yes":
        score -= 20
    else:
        score += 10

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Improve lifestyle habits."
    if risk == "Low Risk":
        suggestion = "You maintain a healthy lifestyle!"
    elif risk == "High Risk":
        suggestion = "Increase exercise, sleep more, and reduce junk food."

    return test_name, score, risk, suggestion

def test1(height, weight, bmi, age, gender):
    test_name="Heart Disease Risk Analyzer"
    pbLine(test_name,"M")
    smoke = input("Do you smoke? (yes/no): ").lower()
    bp = float(input("Enter systolic blood pressure: "))

    score = 70

    if smoke == "yes":
        score -= 30
    if bp > 130:
        score -= 25
    if bmi > 25:
        score -= 20

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Maintain good heart health."
    if risk == "High Risk":
        suggestion = "Quit smoking, reduce salt intake, and consult a doctor."

    return test_name, score, risk, suggestion

def test2(height, weight, bmi, age, gender):
    test_name = "Diabetes Early-Warning Analyzer"
    pbLine(test_name, "M")

    sugar = float(input("Enter fasting blood sugar (mg/dL): "))
    family = input("Family history of diabetes? (yes/no): ").lower()

    score = 80
    if sugar > 100:
        score -= 30
    if family == "yes":
        score -= 20
    if bmi > 25:
        score -= 15

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Sugar levels are stable."
    if risk == "High Risk":
        suggestion = "Control sugar intake and get tested professionally."

    return test_name, score, risk, suggestion


def test3(height, weight, bmi, age, gender):
    test_name = "Mental Stress Level Tracker"
    pbLine(test_name, "M")

    sleep = float(input("Hours of sleep: "))
    workload = input("Heavy workload recently? (yes/no): ").lower()
    anxiety = input("Feeling anxious often? (yes/no): ").lower()

    score = 70
    if sleep < 7:
        score -= 20
    if workload == "yes":
        score -= 20
    if anxiety == "yes":
        score -= 25

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Stress levels manageable."
    if risk == "High Risk":
        suggestion = "Take breaks, sleep well, practice meditation."

    return test_name, score, risk, suggestion

def test4(height, weight, bmi, age, gender):
    test_name = "Daily Vital Signs Health Monitor"
    pbLine(test_name, "M")

    hr = float(input("Heart rate (bpm): "))
    temp = float(input("Body temperature (°C): "))

    score = 90
    if hr < 60 or hr > 100:
        score -= 25
    if temp < 36 or temp > 37.5:
        score -= 30

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Vitals normal."
    if risk == "High Risk":
        suggestion = "Abnormal vitals detected – seek medical help."

    return test_name, score, risk, suggestion


def test5(height, weight, bmi, age, gender):
    test_name = "Obesity & Fitness Risk Analyzer"
    pbLine(test_name, "M")

    waist = float(input("Waist circumference (cm): "))

    score = 85
    if bmi > 25:
        score -= 30
    if waist > 90:
        score -= 25

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Fitness level acceptable."
    if risk == "High Risk":
        suggestion = "Adopt exercise routine and track diet."

    return test_name, score, risk, suggestion

def test6(height, weight, bmi, age, gender):
    test_name = "Personal Immunity Tracker"
    pbLine(test_name, "M")

    fruits = input("Do you eat fruits daily? (yes/no): ").lower()
    water = float(input("Liters of water per day: "))

    score = 70
    score += 10 if fruits == "yes" else -10
    score += 20 if water >= 2 else -10

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Immunity is decent."
    if risk == "High Risk":
        suggestion = "Increase hydration and vitamin-rich foods."

    return test_name, score, risk, suggestion

def test7(height, weight, bmi, age, gender):
    test_name = "Air Quality Health Risk Estimator"
    pbLine(test_name, "M")

    aqi = int(input("Local AQI level: "))
    outdoor = input("Do you spend more than 2 hours outdoors? (yes/no): ").lower()

    score = 85
    if aqi > 150:
        score -= 30
    elif aqi > 100:
        score -= 20

    if outdoor == "yes":
        score -= 15

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Air quality impact is low."
    if risk == "High Risk":
        suggestion = "Wear masks outdoors, reduce outdoor exposure."

    return test_name, score, risk, suggestion

def test8(height, weight, bmi, age, gender):
    test_name = "COVID / Flu Risk Checker"
    pbLine(test_name, "M")

    fever = input("Do you have fever? (yes/no): ").lower()
    cough = input("Do you have cough? (yes/no): ").lower()
    contact = input("Recent contact with sick person? (yes/no): ").lower()

    score = 90
    if fever == "yes":
        score -= 30
    if cough == "yes":
        score -= 20
    if contact == "yes":
        score -= 25

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Low infection probability."
    if risk == "High Risk":
        suggestion = "Consider testing and isolate if symptoms worsen."

    return test_name, score, risk, suggestion

def test9(height, weight, bmi, age, gender):
    test_name = "Senior Citizen Health Risk Monitor"
    pbLine(test_name, "M")

    falls = input("Any falls in past year? (yes/no): ").lower()
    memory = input("Any memory issues? (yes/no): ").lower()

    score = 80
    if age > 60:
        score -= 10
    if falls == "yes":
        score -= 30
    if memory == "yes":
        score -= 25

    score = max(0, min(100, score))
    risk = calculate_risk_level(score)

    suggestion = "Senior health stable."
    if risk == "High Risk":
        suggestion = "Get regular checkups and ensure safe home environment."

    return test_name, score, risk, suggestion
