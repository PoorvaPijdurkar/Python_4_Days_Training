# Frozenset :: same as set only but immutable

print(dir(frozenset), end="\n\n")

# OR
# print(dir(my_frozenset_1))

print("#"*40, end="\n\n")
####################################

print("frozenset PART-3")
print("union, intersection, difference methods")
print("-"*20)
# --------------------

sb_acc_customers = frozenset({"cust-1", "cust-2", "cust-3", "cust-4"})
loan_acc_customers = frozenset({"cust-3", "cust-4", "cust-5", "cust-6"})

print("sb_acc_customers:", sb_acc_customers)
print("loan_acc_customers:", loan_acc_customers, end="\n\n")

# union
all_customers = sb_acc_customers.union(loan_acc_customers)
print("all_customers:", all_customers)

# intersection
customers_having_both = sb_acc_customers.intersection(loan_acc_customers)
print("customers_having_both:", customers_having_both)

# Difference
customers_not_having_loan = sb_acc_customers.difference(loan_acc_customers)
print("customers_not_having_loan:", customers_not_having_loan)

print("#"*40, end="\n\n")
####################################