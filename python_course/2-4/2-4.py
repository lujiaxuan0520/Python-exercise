#!/usr/bin/python
#coding=utf-8
def main():
    with open('words.txt', 'r') as fp:
        words = fp.read()
    couple1 = []
    couple2 = []
    words_set=set()
    for i in words.split():
        words_set.add(i)
    for i in words.split():
        if i not in couple2:
            j = i[::-1]
            if j in words_set:
                couple1.append(i)
                couple2.append(j)
    couples = zip(couple1, couple2)
    for k in couples:
        print(k)


if __name__=='__main__':
    main()