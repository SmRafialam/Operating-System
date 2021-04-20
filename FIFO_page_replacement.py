# Id : 17201053
# input: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1

queue = input("Enter page numbers: ").split(" ")  # taking queue input
print()  # line gap

memory = ["/", "/", "/"]

hit = 0
popIndex = 0  # point on memory to replace index
for i in queue:
    if i in memory:
        print("Hit")
        hit = hit + 1
        continue

    memory[popIndex] = i
    popIndex = popIndex + 1
    if popIndex > 2:
        popIndex = 0
    print(memory)

print("Hit :", hit)
print("fault :", len(queue) - hit)





