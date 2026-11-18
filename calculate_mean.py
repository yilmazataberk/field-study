# Water temperature readings (C)

measurements=[16.0, 18.0, 19.0, 30.0]

def calculate_mean(values):
	return sum(values)/len(values)

print(f"Mean water temperature: {calculate_mean(measurements)} C")
