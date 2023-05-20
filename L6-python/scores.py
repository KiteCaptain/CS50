import random
scores = [random.randint(0, 100) for _ in range(10)]
print(scores)
average = sum(scores) / len(scores)
print(f"Average: {average}")