dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

def find_the_redheads(dict):
    redhead_list = []

    for person in dict:
        hair_color = dict[person]

        if hair_color == "red":

            redhead_list.append(person)
    return redhead_list

redheads = find_the_redheads(dupont_family)
print(redheads)