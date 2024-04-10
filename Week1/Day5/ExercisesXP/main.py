#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_1 = dict(zip(keys, values))
print(dict_1)

#Exercise 2
total = 0
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
fam_movie_cost= {}
for mem in family:
    if family[mem] > 12:
        fam_movie_cost[mem] = 15
        total += 15
    elif family[mem] > 3:
        fam_movie_cost[mem] = 10
        total += 10
    else:
        fam_movie_cost[family[mem]] = 0
print(f"Each family member's price is {fam_movie_cost}")
print(f"The total costs {total}")

#Exercise 3
brand_info = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color" : {"France":"blue",
    "Spain": "red",
    "US": ["pink", "green"]}
}
brand_info.update({"number_stores": 2})
print(brand_info)
print(f"Zara's clients need {brand_info["type_of_clothes"]} type of clothes")
brand_info["country_creation"] = "Spain"
for k in brand_info:
    if k == "international_competitors":
        brand_info[k].append("Desigual")
del brand_info["creation_date"]
print(brand_info["international_competitors"][-1])
print(brand_info["major_color"]["US"])
print(len(brand_info))
print(brand_info.keys())
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand_info = dict(zip(brand_info, more_on_zara))
#print(brand_info['number_stores']) ##creates keyerror, uncertain why
print(brand_info)

#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_A = {}
disney_users_B = {}
for count, user in enumerate(users):
    disney_users_A[user] = count
    disney_users_B[count] = user
print(disney_users_A)
print(disney_users_B)

disney_users_C = {}
sorted_users = sorted(users)
for count, user in enumerate(sorted_users):
    disney_users_C[user] = count
print(disney_users_C)