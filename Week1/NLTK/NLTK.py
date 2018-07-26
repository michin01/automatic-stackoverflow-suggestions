#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import re
import numpy as np
import nltk




def saveCSV():
    filename = 'data.csv'
    resFile = open('nltk.csv','w', newline='', encoding='utf-8')
    writer = csv.writer(resFile)
    with open(filename, encoding='utf-8') as f:
        reactTag =['react','reactjs','react-js']
        reactTg = ['NOUN','VERB','ADJ','CONJ','ADV','.','X']
        NreactTg = ['NOUN', 'VERB', 'ADJ', 'CONJ', 'ADV', '.', 'X']
        reader = csv.reader(f)
        data = list(reader)
        cnt = 0
        dr = re.compile(r'<[^>]+>', re.S)
        hasReact = False
        for lines in data:
            hasReact = False
            str = lines[8]

            str1 = dr.sub('', str)
            text = nltk.word_tokenize(str1)
            # print(text)

            tag = nltk.pos_tag(text, tagset='universal')
            res = [word for word in tag if word[0].lower() in reactTag and word[1] in reactTg]
            # res2 = [word for word in tag if word[0].lower() in reactTag and word[1] not in reactTg]
            # if not len(res2)==0:
            #     print(res)
            #     print(res2)
            #     print(str1)
            #     break
            if not len(res) == 0:
                writer.writerow(lines)
                # print(res)
                # print(str1)
                hasReact=True
            # # first=False
            # if hasReact:
            #     break
        # print(data[2])
        # print(data[2][8])
        # print(np.shape(np.asarray(list(reader))))
        # resFile.flush()
        # resFile.close()




def main():
    filename = 'data.csv'
    with open(filename, encoding='utf-8') as f:
        reactTag =['react','reactjs','react-js']
        reader = csv.reader(f)
        data = list(reader)
        cnt = 0
        dr = re.compile(r'<[^>]+>', re.S)
        hasReact = False
        for lines in data:
            hasReact = False
            str = lines[8]

            str1 = dr.sub('', str)
            text = nltk.word_tokenize(str1)
            # print(text)

            tag = nltk.pos_tag(text, tagset='universal')
            res = [word for word in tag if word[0].lower() in reactTag and (word[1]=="NOUN" or word[1]=="ADJ")]
            if not len(res) == 0:
                print(res)
                print(str1)
                hasReact=True
            # first=False
            if hasReact:
                break
        # print(data[2])
        # print(data[2][8])
        # print(np.shape(np.asarray(list(reader))))
if __name__ == '__main__':
    saveCSV()