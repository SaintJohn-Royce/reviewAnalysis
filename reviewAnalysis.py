data = []
totalNumber = 0
lenLine = 0

lineShorter100 = 0
dataShorter100 = []
lineGood = 0
dataGood = []

with open('reviews.txt', 'r') as file:

	for line in file:

		lenLine = len(line)

		totalNumber = lenLine + totalNumber

		data.append(line)

		# find the lines shorter than 100 characters

		if lenLine < 100:

			dataShorter100.append(line)

			lineShorter100 = lineShorter100 + 1

		# find the lines with good in them

		if 'good' in line:

			dataGood.append(line)

			lineGood = lineGood + 1

avgNum = totalNumber / len(data)

# average number of characters per comment
print('the average number of characters per line of comment is', avgNum)

print('the number of comments shorter than 100 characters is', lineShorter100)

print('the number of comments with the word "good" in them is', lineGood)