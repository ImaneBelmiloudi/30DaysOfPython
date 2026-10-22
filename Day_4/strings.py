print("Thirty","Days","Of","Python")
company = ' Coding For All '
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.Cut(slice))
print(company.split())
print(company[10])
words = company.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)
print(company.index("C"))
print(company.index("F"))
print(company.index("i"))


company = "Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
list_company=company.split(",")
print(list_company)

sentence = "You cannot end a sentence with because because because is a conjuction"
position = sentence.rindex("because")
print(position)
start = sentence.find("because")
end = start + len("because because because")
phrase = sentence[start:end]
print(phrase)
cleaned = company.strip()     #remove spaces
print(cleaned)
print(len(company))
print(len(cleaned))

list = ['Django','Flask','Bottle','Pyramid','Falcon']
join = ' '.join(list)
print(join)