import os

filePath = os.path.join(os.getcwd(), "days", "28-30-regex", "practice", "testContent.html")
# print(filePath)

with open(filePath, 'r') as f:
    
    fileContent = f.read()

    matches = fileContent.findall(r'\(\d+:\d+\)')

print(matches)
