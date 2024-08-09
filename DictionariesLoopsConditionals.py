# Exercise 1 : Convert lists into dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# zipped = zip(keys, values)
# print(set(zipped))

# Exercise 2 : Cinemax #2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# family = []
# another_member = "y"
# while another_member == "y":
#     total_bill = 0
#     member = dict()
#     name = input("what is your name?")
#     age = input("how old are you?")
#     member['name'] = name
#     member['age'] = age
#     family.append(member)
#     for member in family:
#         member['age'] = int(member['age'])
#         if member['age'] >= 12:
#             total_bill += 15
#         elif member['age'] > 3:
#             total_bill += 10
#         elif member['age'] < 3:
#             total_bill += 0
#     another_member = input("would you like to add another member? if yes type 'y' else type 'n' and get the bill :-) ")
# else:
#     print(f"total bill needed to pay {total_bill}")


# Exercise 3: Zara
# brand = {
#     'name': 'Zara',
#     'creation_date': 1975,
#     'creator_name': 'Amancio Ortega Gaona',
#     'type_of_clothes': ["men", "women", "children", "home"],
#     'international_competitors': ["Gap", "H&M", "Benetton"],
#     'number_stores': 7000,
#     'major_color': {
#     'France': 'blue',
#     'Spain': 'red',
#     'US': ["pink", "green"]
#     }
# }
# brand['number_stores'] = 2
# brand['Zara_Clients'] = 'Touse how seek for perfection'
# brand['country_creation '] = 'Spain'
# brand['international_competitors'].append("Desigual")
# del brand['creation_date']
# print(brand['international_competitors'][-1])
# print(brand['major_color']['US'])
# print(len(brand))
# print(brand.keys())
# brand.update(more_on_zara = {
#     'creation_date': 1975,
#     'number_stores': 10000
# })
# print(brand['number_stores'])
# print(brand['more_on_zara']['number_stores'])























