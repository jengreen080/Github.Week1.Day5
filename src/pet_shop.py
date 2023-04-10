# WRITE YOUR FUNCTIONS HERE

# TEST 1
def get_pet_shop_name(type_of_shop):
    return type_of_shop["name"]

# TEST 2
def get_total_cash(type_of_shop):
    return type_of_shop["admin"]["total_cash"]

# TEST 3
def add_or_remove_cash(type_of_shop, amount_to_add_or_remove):
    type_of_shop["admin"]["total_cash"] = get_total_cash(type_of_shop) + amount_to_add_or_remove
    
# TEST 4
# same as TEST 3

# TEST 5
def get_pets_sold(type_of_shop):
    return type_of_shop["admin"]["pets_sold"]

# TEST 6
def increase_pets_sold(type_of_shop, additional_pets):
    type_of_shop["admin"]["pets_sold"] = get_pets_sold(type_of_shop) + additional_pets

# TEST 7
def get_stock_count(type_of_shop):
    counter = 0
    for each_pet in type_of_shop["pets"]:
        counter = counter + 1
    return counter

# TEST 8 (COULDN"T WORK THIS AS AN INT)
def get_pets_by_breed(type_of_shop, pet_breed):
    total_of_breed = []
    for pet in type_of_shop["pets"]:
        if pet["breed"] == pet_breed:
            total_of_breed.append(1)
    return total_of_breed

# TEST 9
# as above (TEST 8)

# # TEST 10    
def find_pet_by_name(type_of_shop, pet_name):
    # go through ["pets"] array, checking petname
    for pet in type_of_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# TEST 11
# as above (TEST 10)

# TEST 12
def remove_pet_by_name(type_of_shop, pet_name):
    for pet in type_of_shop["pets"]:
        if pet["name"] == pet_name:
            pet["name"] = None


#CODE BELOW DOES NOT WORK, WAS OTHER ATTEMPTS
# def remove_pet_by_name(type_of_shop, pet_name):
#     new_list_of_pets = type_of_shop["pets"].remove(pet_name)
#     return new_list_of_pets

# def remove_pet_by_name(type_of_shop, pet_name):
#     if "name" in type_of_shop["pets"] == pet_name:
#         type_of_shop["pets"][pet_name] = None
#     return type_of_shop["pets"]



# TEST 13
def add_pet_to_stock(type_of_shop, new_pet):
    type_of_shop["pets"].append(new_pet)
    get_stock_count(type_of_shop)

# TEST 14
def get_customer_cash(customer):
    return customer["cash"]

# TEST 15
def remove_customer_cash(customer, amount_customer_hands_over):
    customer["cash"] = customer["cash"] - amount_customer_hands_over
    return customer["cash"]

# TEST 16
def get_customer_pet_count(customer):
    return len(customer["pets"])

# TEST 17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)



# TEST 18
# TEST 19
# TEST 20
# TEST 21
# TEST 22
# TEST 23
