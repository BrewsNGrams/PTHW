def calculateAnswer(lhs, rhs, operator):
	if(operator == "-"):
		return lhs - rhs
	if(operator == "+"):
		return lhs + rhs
	if(operator == "*"):
		return lhs * rhs
	if(operator == "/"):
		return lhs / rhs
	raise Exception("Unknown Operator")
	
print(calculateAnswer(8, 2, "+"))
print(calculateAnswer(8, 2, "-"))
print(calculateAnswer(8, 2, "*"))
print(calculateAnswer(8, 2, "/"))
print(calculateAnswer(8, 2, "^_^"))
