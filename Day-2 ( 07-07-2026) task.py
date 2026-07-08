
# Name: Yug Patel

print("----- LIST METHODS -----")

numbers = [10, 20, 30]

# append
numbers.append(40)
print(numbers)

# insert
numbers.insert(1, 15)
print(numbers)

# remove
numbers.remove(20)
print(numbers)

# pop
numbers.pop()
print(numbers)

# reverse
numbers.reverse()
print(numbers)


print("\n----- DICTIONARY METHODS -----")

student = {
    "name": "Yug",
    "age": 20,
    "city": "Bardoli"
}

# keys
print(student.keys())

# values
print(student.values())

# items
print(student.items())

# get
print(student.get("name"))

# update
student.update({"age": 21})
print(student)


print("\n----- TUPLE METHODS -----")

t = (5, 10, 15, 10, 20)

# count
print(t.count(10))

# index
print(t.index(15))

# len
print(len(t))

# max
print(max(t))

# min
print(min(t))


print("\n----- SET METHODS -----")

s = {1, 2, 3}

# add
s.add(4)
print(s)

# remove
s.remove(2)
print(s)

# discard
s.discard(10)
print(s)

# pop
s.pop()
print(s)

# copy
new_set = s.copy()
print(new_set)


print("\n----- IF -----")

num = 10

if num > 5:
    print("Number is greater than 5")


print("\n----- IF ELSE -----")

age = 17

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


print("\n----- IF ELIF ELSE -----")

marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


print("\n----- NESTED IF ELSE -----")

number = 8

if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")


print("\n----- BREAK -----")

for i in range(1, 6):
    if i == 4:
        break
    print(i)


print("\n----- CONTINUE -----")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


print("\n----- PASS -----")

for i in range(1, 4):
    if i == 2:
        pass
    print(i)


print("\n----- INPUT -----")

name = input("Enter your name: ")
print("Welcome", name)


print("\n----- RANGE -----")

for i in range(5):
    print(i)


print("\n----- LEN -----")

word = "Python"
print(len(word))


print("\n----- TYPE -----")

a = 100
print(type(a))


print("\n----- FOR LOOP -----")

for i in range(1, 6):
    print(i)


print("\n----- WHILE LOOP -----")

count = 1

while count <= 5:
    print(count)
    count = count + 1