people = {
    "grace": "mallory",
    "william": "butcher",
    "bojack": "horseman",
    "madelyn": "stillwell"
}

def array_of_names(dict):
    full_names_list = []

    for first_name in dict:
        last_name = dict[first_name]
    
        full_name = first_name + " " + last_name

        full_name = full_name.title()

        full_names_list.append(full_name)

    return full_names_list

result = array_of_names(people)
print(result)