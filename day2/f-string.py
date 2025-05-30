bmi = 84 / 1.65 ** 2

# Floating number 30.85399449035813
print(bmi)

# After Round function 31
print(round(bmi))

# Round to 2 decimal spaces 30.85
print(round(bmi, 2))

#Assignment Operators += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
score = 0
score += 1

# score -=1 also possible
# the result will be 1
print(score)

# f-strings - mix strings and different data types
# we need to add str function to score in order to match the both data types
print("Your score is " + str(score))

# To avoid all the conversions we use f-string -> f""
score = 0
height = 1.8
is_winning = True

# Result "Your score is 0"
print(f"Your score is {score}")
# Result: "Your score is 0, your height is 1.8. You are winning is True"
print(f"Your score is {score}, your height is {height}. You are winning is {is_winning}")