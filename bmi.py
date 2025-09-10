# BMI Calculator in Python

def calculate_bmi():
    print("=== BMI Calculator ===")
    
    # User input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Display result
    print(f"\nYour BMI is: {bmi:.2f}")
    
    # BMI categories
    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

# Run the function
if __name__ == "__main__":
    calculate_bmi()
