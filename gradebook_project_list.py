last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics','calculus','poetry','history']
grades = [98,97,85,88]

subjects_grades = zip(subjects,grades)

gradebook =list(subjects_grades)

gradebook.append('visual arts')
gradebook.append(93)
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
###
string1 = "The quick brown"
string2 = "fox jumps over"
string3 = string1+string2
print(string3+" the lazy dog.")
