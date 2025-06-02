def custom_greeting(name, time_of_day):
    return f"Good {time_of_day}, {name}!"
name = input("Enter your name: ")
time = input("Enter time of day (morning, afternoon, evening): ")

print(custom_greeting(name, time))
