def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI)"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Please enter your weight (in kilograms): "))
        height = float(input("Please enter your height (in meters): "))
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
