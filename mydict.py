mydict= {
    "dhruv":"a coder",
    "mango":"king of fruits",
    "lion":"king of jungle",
    "dob":[18,10,2001]
}

print(mydict['dhruv'])
print(mydict['dob'])
print(mydict.get("mango"))

print(mydict.keys())
print(type(mydict.keys()))
print(mydict.values())

updatedict= {
    "mirage 2000":"Balakot hero",
    "SU 30 MKI":"a fighter",
    "mig":{
        'mig 21':'a warrior'}

    }


mydict.update(updatedict)
print(mydict)