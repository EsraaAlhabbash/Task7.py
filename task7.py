names = ["Tarteel", "Asmaa", "Ahmed"]

def add_item_start(lst, item):
    lst.insert(0, item)
    return lst

new_names = add_item_start(names, "Sabrin")
print(new_names)

def remove_last_item(lst):
    lst.pop()
    return lst

new_names = remove_last_item(new_names)
print(new_names)

def add_item_end(lst, item):
    lst.append(item)
    return lst

new_names = add_item_end(new_names, "Hamda")
print(new_names)

def remove_third_item(lst):
    lst.pop(2)
    return lst

new_names = remove_third_item(new_names)
print(new_names)


friends = ["Adel", "Ahmed"]
employees = ["Samah", "Amjad"]
school = ["Ali", "Basma"]

def merge_lists(lst1, lst2, lst3):
    merged_list = lst1 + lst2 + lst3
    return merged_list

final_list = merge_lists(friends, employees, school)
print(final_list)


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

def merge_dicts(d1, d2, d3):
    merged_dict = {**d1, **d2, **d3}
    return merged_dict

final_dict = merge_dicts(dic1, dic2, dic3)
print(final_dict)

def print_squared_dict():
    squared_dict = {}
    for i in range(1, 16):
        squared_dict[i] = i ** 2
    print(squared_dict)
print_squared_dict()


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 150, 'b': 200, 'd': 400}

def combine_dicts(d1, d2):
    combined_dict = {}
    for key in d1.keys() | d2.keys():
        if key in d1 and key in d2:
            combined_dict[key] = d1[key] + d2[key]
        elif key in d1:
            combined_dict[key] = d1[key]
        else:
            combined_dict[key] = d2[key]
    return combined_dict

final_dict = combine_dicts(d1, d2)
print(final_dict)

def create_dict(keys, values):
    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = create_dict(keys, values)
print(result)


def get_history_score(sample_dict):
    return sample_dict['Class']['Student']['marks']['history']

sample_dict = {
    "Class": {
        "Student": {
            "name": "Mike",
            "marks": {
                "Physics": 70,
                "history": 80
            }
        }
    }
}

history_score = get_history_score(sample_dict)
print(history_score)


def print_dict_values_less_than_10(my_dict):
    values_less_than_10 = [value for key, value in my_dict.items() if key < 10]
    print("->".join(values_less_than_10))

my_dict = {1: "Alaa", 5: "Hadel", 7: "Hanin", 13: "Malak"}

print_dict_values_less_than_10(my_dict)
