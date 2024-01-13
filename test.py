import json

number_persian_dic = {
    "۰" : 0,
    "۱" : 1,
    "۲" : 2,
    "۳" : 3,
    "۴" : 4,
    "۵" : 5,
    "۶" : 6,
    "۷" : 7,
    "۸" : 8,
    "۹" : 9,
}



def Jread(address):
   jfile = open(address)
   jobj = json.load(jfile)
   return jobj

obj = Jread("DB/db.json")
print(obj)

