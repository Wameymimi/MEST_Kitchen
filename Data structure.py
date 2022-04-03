my_list = [ "clothes","shoes", "handbags", "sneakers"]
print(my_list[1])
my_list.append("wrist watch")
print(my_list)
my_list.insert(1, "head band")
print(my_list)
my_list[0]="iphone"
my_list.remove("wrist watch")
print(my_list)


#To acess last item in list
#step 1:Get length or count of list items 
length = len(my_list)
#step 2: Deduct 1 from length to get the last index
last_index = length - 1
#step 3:Access the last item with the last_index 
last_item=my_list[last_index]
print(last_item)


my_dict = {
    "id":1,
    "name":"wamey",
    "is_programmer":True,
    "salary":1.2

}
print(my_dict.get("id"))

my_dict = {
    "id":1,
    "name":"wamey",
    "is_programmer":True,
    "salary":1.2,
    "loans":[{"package":"Student loan", "amount": 1000}],
    "languages": [{"lang":"french", "proficiency":100},
                  {"lang":"spanish", "proficiency":100},
                  {"lang":"portuguese", "proficiency":80}]

}
# print(my_dict.get("name"))
# print(my_dict["languages"])

# print(my_dict.get("loans")[0].get("amount"))
print(my_dict.get("languages")[0].get("proficiency"))