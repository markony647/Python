monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12
originalBalance = balance
epsilon = 0.01

while abs(balance) > epsilon:
    balance = originalBalance
    payment = (upperBound + lowerBound) / 2
    
    for month in range(12):
        balance -= payment
        monthly_rate_money = monthlyInterestRate * balance
        balance = balance + monthly_rate_money
        
    if balance > 0:
        lowerBound = payment
    else:
        upperBound = payment
        
print "Lowest Payment:", round(payment, 2)