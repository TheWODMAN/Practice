with open("cleaningSections.txt", "r") as sections:
    for line in sections:
        sectionList = line.rsplit()
        print(sectionList)

sections.close()