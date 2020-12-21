import submission, collections, util

def create_zebra_problem(): 
    csp  = util.CSP()
    domain = list(range(1, 6))
    variables = ['Englishmen', 'Spaniard', 'Norwegian', 'Japanese', 'Ukrainian', 'coffee', 'milk', 'orange-juice', 'tea', 'water','dog', 'horse', 'fox', 'zebra', 'snail','red','yellow' , 'blue', 'green', 'ivory','kitkats', 'snickers', 'smarties', 'hershey', 'milkyways']

    for var in variables:
        csp.add_variable(var, domain)
    
    csp.add_binary_potential('Englishmen', 'red', lambda x, y: x == y)
    csp.add_binary_potential('Spaniard', 'dog', lambda x, y: x == y)
    csp.add_unary_potential('Norwegian', lambda x: x == 1)
    csp.add_binary_potential('green', 'ivory', lambda x, y: x  == y + 1)
    csp.add_binary_potential('hershey', 'fox', lambda x, y: abs(x - y) == 1)
    csp.add_binary_potential('kitkats', 'yellow', lambda x, y: x == y)
    csp.add_binary_potential('Norwegian', 'blue', lambda x, y:  abs(x - y) == 1)
    csp.add_binary_potential('smarties', 'snail', lambda x, y: x == y)
    csp.add_binary_potential('snickers', 'orange-juice', lambda x, y: x == y)
    csp.add_binary_potential('Ukrainian', 'tea', lambda x, y: x == y)
    csp.add_binary_potential('Japanese', 'milkyways', lambda x, y: x == y )
    csp.add_binary_potential('kitkats', 'horse', lambda x, y: abs(x - y) == 1)
    csp.add_binary_potential('coffee', 'green', lambda x, y: x == y)
    csp.add_unary_potential('milk', lambda x: x == 3)

    for idx1 in range(5):
        for idx2 in range(5):
            if idx1 != idx2:
                csp.add_binary_potential(variables[idx1], variables[idx2], lambda x, y: x != y ) 

    for idx1 in range(5, 10):
        for idx2 in range(5, 10):
            if idx1 != idx2:
                csp.add_binary_potential(variables[idx1], variables[idx2], lambda x, y: x != y ) 
                
    for idx1 in range(10, 15):
        for idx2 in range(10, 15):
            if idx1 != idx2:
                csp.add_binary_potential(variables[idx1], variables[idx2], lambda x, y: x != y ) 
                
    for idx1 in range(15, 20):
        for idx2 in range(15, 20):
            if idx1 != idx2:
                csp.add_binary_potential(variables[idx1], variables[idx2], lambda x, y: x != y ) 
                
    for idx1 in range(20, 25):
        for idx2 in range(20, 25):
            if idx1 != idx2:
                csp.add_binary_potential(variables[idx1], variables[idx2], lambda x, y: x != y ) 
                
    return csp

csp = create_zebra_problem()
search = submission.BacktrackingSearch()
search.solve(csp, mcv = True, mac = True)
print(search.optimalAssignment)
houses = collections.defaultdict(list)
for var, house in search.optimalAssignment.items():
    houses[house].append(var)
print(houses)


