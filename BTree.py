# !/usr/bin/python3
# coding:utf-8
class BTree:
    def __init__(self, key, lchild=None, rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild

    def addLchild(self, key):
        if self.lchild:
            node = BTree(key)
            node.lchild = self.lchild
            self.lchild = node
        else:
            self.lchild = BTree(key)

    def addRchild(self, key):
        if self.rchild:
            node = BTree(key)
            node.rchild = self.rchild
            self.rchild = node
        else:
            self.rchild = BTree(key)

    def getLchild(self):
        return self.lchild

    def getRchild(self):
        return self.rchild

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key