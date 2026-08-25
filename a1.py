import os

print("=== Science notes ===")
with open("science.txt", "r") as f:
    for line in f:
        print(line.strip())
print()

print("=== Word Count ===")
with open("math.txt","r") as f:
    for line in f:
        words=line.split()
        print(len(words), "words ->" ,line.strip())
print()

print("=== Merging Notes ===")
if os.path.exists("all-notes.txt"):
    print("all-notes.txt already exists - overwriting")
else:
    print("all-notes.txt not found - creating now")

content = ""
with open("science.txt", "r") as f:
    content +=("--- science.txt ---\n")
    content += f.read() + "\n"
with open("math.txt", "r") as f:
    content +=("--- math.txt ---\n")
    content += f.read() + "\n"
with open("all-notes.txt", "w") as out:
    out.write(content)
print("saved to all-notes.txt")
print()

if os.path.exists("all-notes1.txt"):
    os.remove("all-notes1.txt")
    print("all-notes1.txt deleted")
else:
    print("all-notes1.txt does not exist")
