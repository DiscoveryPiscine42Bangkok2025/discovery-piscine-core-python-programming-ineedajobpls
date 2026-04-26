class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

def average(dict):
    all_grades = dict.values()
    avg = sum(all_grades) / len(dict)
    return avg

print("Average for class 3B:",average(class_3B))
print("Average for class 3C:",average(class_3C))