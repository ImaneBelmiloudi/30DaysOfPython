# dict = {'key':'value','key':'value'}
empty_dict ={}
dog = {'name':'zack','color':'black','breed':'white','legs':'small','age':10}
student = {'first_name':'imane',
    'last_name':'belmiloudi',
    'gender':'female',
    'marital_status':'unmarried',
    'skills':'computer science',
    'country':'Morocco',
    'city':'khémisset',
    'address':'lotissement n° 24'
}
# print(len(student))
# student['skills']='Marketing'
# print(student)
# keys= student.keys()
# print(keys)
# list = student.values()
# print(list)
# print(student.items())
student.pop('address')
print(student)
del student