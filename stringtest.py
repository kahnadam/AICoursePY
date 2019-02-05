list1 = ["Boston_terrier_02259.jpg","Irish_setter_2424.jpg","Big_Great_dane_242.jpg"]
list2 = []

def clean_string(name_list):
    for item in name_list:
        label = item.split("_")
        pet_name = ""
        for word in label:
            if word.isalpha():
                pet_name += word.lower() + " "
        pet_name = pet_name.strip()
        list2.append(pet_name)

clean_string(list1)
print(list2)
