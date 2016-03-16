from BinaryTree import *
import sys

def readToList(file):
    newList = []
    for line in file:
        for num in line.split():
            newList.append(int(num))
    return newList

#import data
inorder = open("in-order.txt", "r")
inorderReversed = open("in-order-reverse.txt", "r")
random = open("random.txt", "r")

inorderList = readToList(inorder)
inorderReversedList = readToList(inorderReversed)
randomList = readToList(random)


#add data to the tree
inorderTree = Tree()
inorderReversedTree = Tree()
randomTree = Tree()

for element in inorderList:
    inorderTree.addNode(element)
for element in inorderReversedList:
    inorderReversedTree.addNode(element)
for element in randomList:
    randomTree.addNode(element)

sys.setrecursionlimit(100000)

#Results
print "-------------------- in-order.txt --------------------"
inorderTree.preorderTraverse()
inorderTree.inorderTraverse()
inorderTree.postorderTraverse()
inorderTree.breadthFirstSearch()


print "\n\n\n-------------------- in-order-reverse.txt --------------------"
inorderReversedTree.preorderTraverse()
inorderReversedTree.inorderTraverse()
inorderReversedTree.postorderTraverse()
inorderReversedTree.breadthFirstSearch()


print "\n\n\n-------------------- random.txt --------------------"

randomTree.preorderTraverse()
randomTree.inorderTraverse()
randomTree.postorderTraverse()
randomTree.breadthFirstSearch()
