sandwich_orders = ["tuna", "italian", "club", "reuben", "muffuletta"]

sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in sandwiches:
    print(f"- {sandwich}")