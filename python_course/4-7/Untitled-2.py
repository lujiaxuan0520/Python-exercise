#!/usr/bin/python
#coding=utf-8
import random
def fill(si, sj, ei, ej, tag):
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            tag_list[i][j] = tag

def set_tag():
    global tag_list
    tag_list = [[None for x in range(29)] for y in range(29)]
    for k in (0, 7, 21, 28):
        fill(k, 0, k, 28, 'R')
        fill(0, k, 28, k, "R")
    fill(1, 1, 6, 6, "K")
    fill(1, 23, 6, 28, "K")
    fill(8, 12, 11, 16, "K")
    fill(12, 8, 16, 11, "K")
    fill(1, 8, 6, 20, "B")
    fill(8, 1, 20, 6, "B")
    fill(8, 8, 11, 11, "Y")
    fill(12, 12, 16, 16, "Y")
    fill(13, 13, 15, 15, "R")
    for i in range(29//2):
        for j in range(29):
            tag_list[28-i][j] = tag_list[i][j]
    for i in range(29):
        for j in range(29//2):
            tag_list[i][28-j] = tag_list[i][j]


def combWords(i, j, cnt):
    if visited[i][j] is True:
        return False
    if cnt == target:
        visited[i][j] = False
        return data[i][j]
    
    visited[i][j] = True

    for way in ways:
        ii, jj = i+way[0], j+way[1]
        if ii >= 0 and ii < 29 and jj >= 0 and jj < 29:
            if tag_list[ii][jj] == tag_list[i][j]:
                ret = combWords(ii, jj, cnt+1)
                if ret is not False:
                    visited[i][j] = False
                    return ret + data[i][j]
    visited[i][j] = False
    return False


def makePoem():
    global target
    poem = False
    while not poem:
        target = random.choice((4*7, 3*12, 4*6, 5*4))
        x, y = random.randint(0, 28), random.randint(0, 28)
        poem = combWords(x, y, 1)
    return poem


def addPunc(poem):
    mp = dict(zip((4*7, 3*12, 4*6, 5*4), (4, 3, 4, 5)))
    p = mp[len(poem)]
    i, k = 1, 0
    while i <= len(poem):
        if (i-k) % p == 0:
            poem.insert(i, '，')
            k += 1
            i += 1
        i += 1
    poem[len(poem)-1] = '。'
    return "".join(poem)


if __name__ == "__main__":
    global ways, jihe, visited
    visited = [[False for x in range(29)] for y in range(29)]
    ways, jihe = [(1, 0), (-1, 0), (0, 1), (0, -1)], {None}

    f = open("input.txt", 'r')
    data = f.readlines()
    data = [line.strip() for line in data]
    f.close()
    print(data)
    set_tag()
    out = open('output.txt', 'w')
    for i in range(100):
        poem = makePoem()
        while poem in jihe:
            poem = makePoem()
        out.write(addPunc(list(poem)))
        jihe.add(poem)
        out.write('\n')
