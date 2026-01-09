import os
print("Current folder:", os.getcwd())

print("Week4 - File Organizer")
print("Script runs successfully")

files = os.listdir()
SKIP = {"organizer.py"}
DRY_RUN = False

CATEGORIES = {
    "Images": {"jpg", "jpeg", "png", "gif", "webp"},
    "Documents": {"pdf", "doc", "docx", "txt", "cvs", "xlsx", "pptx"},
    "Audio": {"mp3", "wav", "m4a"},
    "Archives": {"zip", "rar", "7z"},
    }

print("Files in the folder:")
for f in files:
    print(f)

print("\nFiles only:")
for f in files:
    if os.path.isfile(f):
        print(f)

print("\nFolder only")
for f in files:
    if os.path.isdir(f):
        print(f)

print("\nFiles by extension:")
for f in files:
    if os.path.isfile(f):
        name, ext = os.path.splitext(f)
        print(f, "=>", ext)

def get_category(ext):
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

for f in files:
    if os.path.isfile(f) and f not in SKIP and not f.startswith("."):
        _, ext = os.path.splitext(f)
        ext = ext[1:]
        category = get_category(ext)

        if ext:
            if not os.path.exists(category):
                os.mkdir(category)
            destination = os.path.join(category, f)
            if not os.path.exists(destination):
                if DRY_RUN:
                    print(f"[DRY_RUN] Would move {f} -> {category}/")
                else:
                    os.rename(f, destination)
                    print(f"Moved {f} -> {category}/")























