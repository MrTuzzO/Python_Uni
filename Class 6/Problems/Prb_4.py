counter = 0

def demonstrate_variable_scope():
    global counter
    counter += 5
    print("Global counter modified to:", counter)
    counter = 10
    print("Local counter is:", counter)


print("Initial global counter:", counter)

demonstrate_variable_scope()

print("Global counter after function call:", counter)
