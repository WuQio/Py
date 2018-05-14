#!/usr/bin/python3
# coding:utf-8
import sqlite3

bookList = []
with open("chapters", mode="r", encoding="UTF-8") as chapters:
    bookList = chapters.readlines()
    for idx, e in enumerate(bookList):
        bookList[idx] = bookList[idx].strip()

conn = sqlite3.connect("E:\\sqlite\\和合本.db")
cursor = conn.cursor()
bible = open("bible.txt", "w", encoding="utf-8")

for book in range(66):  # book[0, 65]
    sql = "select * from Bible where Book=" + str(book + 1)
    resList = cursor.execute(sql).fetchall()
    cpt = 0
    # write every verse in each Book. Book means "卷" in Chinese
    bible.write("\n"+bookList[book])
    for e in resList:
        # write chapter info
        if e[2] != cpt:
            bible.write("\n第" + str(e[2]) + "章" + "\n")
            cpt = e[2]
        bible.write(str(e[3]) + "."+e[4])

bible.close()
cursor.close()
conn.close()
