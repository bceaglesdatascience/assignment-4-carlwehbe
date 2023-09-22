purchases = float(input("Number of purchases: "))
tax = float(input("Sales tax: "))
names = []
costs = []
i = 0
while i < purchases:
    cust = input("Customer: ")
    names.append(cust)
    cost = float(input("Cost: "))
    costs.append(cost)
    i+=1
def add_tax(cost_list, salestax):
    n_costs = []
    for cost in cost_list:
        n_cost = cost * (salestax+1)
        n_costs.append(n_cost)
    return(n_costs)
n_costs = add_tax(costs, tax)
ans = {}
for i in range(len(n_costs)):
    if names[i] in ans:
        ans[names[i]] += n_costs[i]
    else:
        ans[names[i]] = n_costs[i]
print(ans)
