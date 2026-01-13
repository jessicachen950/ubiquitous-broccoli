fruits = ["apple", "banana","cantaloupe","dragonfruit"]
for fruit in fruits:
    print(fruit)

user_fruit = input("What is your favorite fruit? ")
if user_fruit in fruits:
    print("Good job, that is a fruit.")
else:
    print("sorry, that is not a fruit. there are only 4 fruits: " + str(fruits))