data = []

totalNumber = 0

lenLine = 0

with open('reviews.txt', 'r') as file:

	for line in file:

		lenLine = len(line)

		totalNumber = lenLine + totalNumber

		data.append(lenLine)

avgNum = totalNumber / len(data)

# average number of characters per comment
print(avgNum)