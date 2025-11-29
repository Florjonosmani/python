

names = ["alice","bob","david","charlie"]
#print(names[2])
for name in names:
  print(name)

sentence = "Hello, world!"

for ch in sentence:
    if ch.isalpha():
      print(ch)

for number in range(1,6):
    print(number)

numbers=[12,45,6,7,94,304,34]

max = numbers[0] #12

for num in numbers:
    if num > max:
        max = num
print("Maksimumi eshte:", max)