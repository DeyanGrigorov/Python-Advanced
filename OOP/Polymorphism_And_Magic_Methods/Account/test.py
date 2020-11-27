from account import Account

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3.transactions)


# Account of bob with starting amount: 10
# Account(bob, 10)
# 40
# 3
# 20
# -20
# 30
# -20
# [30, -20, 20]
# False
# False
# True
# True
# False
# True
# Account of bob&john with starting amount: 10
# [20, -20, 30, 10, 60]