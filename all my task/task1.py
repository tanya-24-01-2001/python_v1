from data_ import dataset





def addUserDish(user_name, country, dish):
    list_food=[]
    a=dataset[user_name]["country"][country]
    return a



print(addUserDish("person_1","Country_1",dataset))


dataset["peson_N"]=["country"]
#dataset["peson_N"]["country"]=["country_n"]

print(dataset)

