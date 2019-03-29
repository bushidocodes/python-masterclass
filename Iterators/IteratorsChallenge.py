teamMembers = ["Sean", "Devyani", "Alvaro"]
teamMembersIterator = iter(teamMembers)

for i in range(0, len(teamMembers)):
    print(next(teamMembersIterator))
