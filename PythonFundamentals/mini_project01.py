# MINI PROJECT 1: Travel Mode Suggestion
print("\nMINI PROJECT 1: Travel Mode Suggestion")
print("-" * 50)

def suggest_transport(distance):
    if distance < 3:
        return "Bicycle"
    elif distance < 300:
        return "Motor-cycle"
    else:
        return "Super-Car"

# Test Mini Project 1
try:
    distance = float(input("How far would you like to travel in miles? "))
    transport = suggest_transport(distance)
    print(f"I suggest {transport} to your destination")
except ValueError:
    print("Please enter a valid number for distance")