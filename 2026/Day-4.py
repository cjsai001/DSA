def calculate_total_price(item_price, tax_rate):
    total = item_price + (item_price * tax_rate)
    return total  
# Calling the function
final_bill = calculate_total_price(item_price=100, tax_rate=0.18)
print(f"Your final bill is: {final_bill}")


def my_function():
    local_message = "I am inside the function!"
    print(local_message)  
my_function()


global_username = "DevOpsLearner"
def greet_user():
    print(f"Welcome back, {global_username}!")
greet_user() 
print(global_username)
