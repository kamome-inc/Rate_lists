import os

print("Текущая деректория:", os.getcwd())

os.chdir("E:\!Работа\списки на сайт")
print("Текущая деректория:", os.getcwd())

# распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        print("/files/documents/ABITUR/2021_spiski/rate_lists" + os.path.join(dirpath, filename)[1:].replace('\\', r'/'))