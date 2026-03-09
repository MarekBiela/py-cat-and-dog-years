def get_human_age(cat_age: int, dog_age: int) -> list:
    result_list = []
    for animal, age in (("cat", cat_age), ("dog", dog_age)):
        if age < 15:
            result_list.append(0)
        elif 15 <= age < 24:
            result_list.append(1)
        else:
            if animal == "cat":
                result_list.append((age - 24) // 4 + 2)
            if animal == "dog":
                result_list.append((age - 24) // 5 + 2)
    return result_list
