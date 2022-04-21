# nested dictionary

sample_dictionary = {'class': {'student': {'name': 'mike', 'marks': {'physics': 70, 'history': 80}}}}
print(sample_dictionary['class']['student']['marks']['history'])

# initializing dictionary

employees = ['kelly', 'emma']
defaults = {'designation': 'Developer', 'salary': 8000}

output = dict.fromkeys(employees, defaults)
print(output)
print(output['kelly'])

# keys extraction

sample_dictionary = {'name': 'kelly', 'age': 25, 'salary': 8000, 'city': 'new york'}
keys = ['name', 'salary']

out_2 = dict()

# add current key with its value from sample dictionary;
for k in keys:
    out_2.update({k: sample_dictionary[k]})
print(out_2)
