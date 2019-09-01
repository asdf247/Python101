from utilities import read_file, clean_text, wordcount_counter, wordcount_dd, word_count_err_handling
filepath = "D:\\py101\\notebooks\\hamlet.txt"

def main():
    hamlet = read_file(filepath)

    hamlet_cleaned = clean_text(hamlet)

    #hamlet_wordcount = wordcount(hamlet_cleaned)
    #hamlet_wordcount = wordcount_counter(hamlet_cleaned)
    #hamlet_wordcount = wordcount_dd(hamlet_cleaned)
    hamlet_wordcount = word_count_err_handling(hamlet_cleaned)

    #print(hamlet_wordcount.most_common(50))
    print(hamlet_wordcount)


if __name__ == "__main__":
    main()