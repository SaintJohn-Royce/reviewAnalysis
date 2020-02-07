data = []

totalNumber = 0

lenLine = 0

lineShorter100 = 0

dataShorter100 = []

with open('reviews.txt', 'r') as file:

	for line in file:

		lenLine = len(line)

		totalNumber = lenLine + totalNumber

		data.append(line)

		if lenLine < 100:

			dataShorter100.append(line)

			lineShorter100 = lineShorter100 + 1

avgNum = totalNumber / len(data)

# average number of characters per comment
print('the average number of characters per line of comment is', avgNum)

print('the number of comments shorter than 100 characters is', lineShorter100)

print(dataShorter100[0])