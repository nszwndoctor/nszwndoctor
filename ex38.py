ten_things = "apples oranges crows telephone light sugar"

print("wait there are no 10 things in that list. let`s fix that.")

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now")

print("there we go: ", stuff)

print("let`s do some things with stuff.")

print(stuff[1])
print([-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what ? cool!
print('#'.join(stuff[3:5])) # super stellar!   
