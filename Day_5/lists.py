# list = ["Machine Learning","Deep Learning","Computer vision","Generative AI","Data Science"]

# first_item = list[0]
# middle_item = list[len(list) // 2]
# last_item = list[-1]

# print(first_item)
# print(middle_item)
# print(last_item)

mixed_data_types = ["Imane",20 , 160, "Student", "i.belmiloudi@gmail.com"]
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
# print(mixed_data_types)
print(len(it_companies))
first = it_companies[0]
middle = it_companies[len(it_companies) // 2]
last = it_companies[-1]
print(first)
print(middle)
print(last)
it_companies[0]="Instagram"
it_companies.append("Oracle")
it_companies[4] = it_companies[4].lower()
join = '#;'.join(it_companies)
print(join)
it_companies.reverse(-1,0)
print(it_companies)