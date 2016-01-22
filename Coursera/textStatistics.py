def main():
    text = raw_input("Please type yor text: ")


    big_letters_amount = []
    for char in text:
        if char >= "A" and char <= "Z":
            big_letters_amount.append(char)

    sentences_amount = []
    for full_stop in text:
        if full_stop == '.':
            sentences_amount.append(full_stop)

    text_list = text.split()

    numbers_amount = []
    for char in text:
        if char.isdigit():
            numbers_amount.append(char)

    print 'numbers: %s, words: %s, sentences: %s' % (len(numbers_amount), len(text_list), len(sentences_amount))
    print 'amount of big letters is %s' % len(big_letters_amount)

if __name__ == '__main__':
    main()