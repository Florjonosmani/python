
grades = {
    ("John", "Math"):5,
    ("Alice", "Biology"):4,
    ("Eve", "Music"):3,
    ("John", "English"): 4,

      }

john_Math= grades[("John", "Math")]
print("John's grades in math is", john_Math)

grades[("Florjon", "Edukat Fizike")]= 5  #Add nre item in dictionary

print(grades)

keys = list(grades.keys())
print(keys)

student , subject = keys[0]
print(student,"'s grade in",subject,"is", john_Math)

