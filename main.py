from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
dict_list = []
result_list = []
keys = contacts_list[0]
for i in contacts_list:
    j = ", ".join(map(str,i))
    pattern = re.compile(r"(\w+)?[,\s]*(\w+)?[,\s]*(\w+)?[,\s]*(\w+)?[,\s]+([–\sа-яёА-ЯЁa-zA-Za-zA-Z]+)?[,\s]+((\+7|8)?\s*\(?(\d{3})\)?[-\s*]?(\d{3})[-\s*]?(\d{2})[-\s*]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d+)?\)?|[,\s]+)[,\s]+([\d,@.+a-zA-Z]+|[,\s]+)")
    number1 = pattern.sub("+7(\\8)\\9-\\10-\\11", j)
    if number1.strip() != "+7()--":
        number1 = "+7(\\8)\\9-\\10-\\11"
    else:
        number1 = ""
    number2 = pattern.sub("\\14", j)
    if number2.strip() != "":
        number2 = "Доб.\\14"
    else:
        number2 = ""
    result = pattern.sub(f"\\1,\\2,\\3,\\4,\\5,{number1} {number2},\\15", j)
    temp_list = []
    for t in result.split(","):
        temp_list.append(t.strip())
    result_list.append(temp_list)
for items in result_list:
    temp_dict = {}
    for num, val in enumerate(items):
        if val != "":
            temp_dict.setdefault(keys[num], val)
    for n, d in enumerate(dict_list):
        if d["lastname"] == temp_dict["lastname"] and d["firstname"] == temp_dict["firstname"]:
            temp_dict.update(d)
            dict_list.pop(n)
    dict_list.append(temp_dict)
result_list = []
for list in dict_list:
    temp_list = []
    temp_list.append(list.get("lastname", " "))
    temp_list.append(list.get("firstname", " "))
    temp_list.append(list.get("surname", " "))
    temp_list.append(list.get("organization", " "))
    temp_list.append(list.get("position", " "))
    temp_list.append(list.get("phone", " "))
    temp_list.append(list.get("email", " "))
    result_list.append(temp_list)
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result_list)
