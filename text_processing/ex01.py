from utilities import read_file, clean_text, wordcount

filepath = "D:\\py101\\notebooks\\hamlet.txt"

hamlet = read_file(filepath)

hamlet_cleaned = clean_text(hamlet)

hamlet_wordcount = wordcount(hamlet_cleaned)

print(hamlet_wordcount)