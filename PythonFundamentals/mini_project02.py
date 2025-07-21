# MINI PROJECT 2: Server Cost Calculator
print("\nMINI PROJECT 2: Server Cost Calculator")
print("-" * 50)

# Given data
cost_per_hour = 0.51
hours_per_day = 24
days_per_week = 7
days_per_month = 30  
budget = 918

# Calculations
cost_per_day = cost_per_hour * hours_per_day
cost_per_week = cost_per_day * days_per_week
cost_per_month = cost_per_day * days_per_month
days_with_budget = budget / cost_per_day

print(f"Server hosting cost analysis:")
print(f"Cost per hour: ${cost_per_hour}")
print(f"Hours per day: {hours_per_day}")
print()
print(f"How much does it cost to operate one server per day? ${cost_per_day:.2f}")
print(f"How much does it cost to operate one server per week? ${cost_per_week:.2f}")
print(f"How much does it cost to operate one server per month? ${cost_per_month:.2f}")
print(f"How many days can I operate one server with $918? {days_with_budget:.1f} days")

print("\n" + "="*60)
print("="*60)
