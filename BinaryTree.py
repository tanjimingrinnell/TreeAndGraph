from __future__ import print_function
from Queue import *

"""Binary Tree Node"""
class TreeNode:

    leftNode = None
    rightNode = None
    value = 0

    def __init__(self, inputValue):
        self.leftNode = None
        self.rightNode = None
        self.value = inputValue

    def __repr__(self):
        return str(self.value)



"""Binary Tree"""
class Tree:

    rootNode = None
    queue = Queue()

    def __init__(self):
        rootNode = None

    def addNode(self, inputValue):
        self.queue.clear()
        if self.rootNode is None:
            self.rootNode = TreeNode(inputValue)
        else:
            self.queue.enqueue(self.rootNode)
            self.addNodeRecurse(inputValue)

    def addNodeRecurse(self, inputValue):
        currentNode = self.queue.dequeue()
        if currentNode.leftNode is None:
            currentNode.leftNode = TreeNode(inputValue)
        elif currentNode.rightNode is None:
            currentNode.rightNode = TreeNode(inputValue)
        else:
            self.queue.enqueue(currentNode.leftNode)
            self.queue.enqueue(currentNode.rightNode)
            self.addNodeRecurse(inputValue)


    def preorderTraverse(self):
        print ("Preorder traversal: ", end = " ")
        self.preorderTraverseRecurse(self.rootNode)
        print ("\n")

    def inorderTraverse(self):
        print ("Inorder traversal:  ", end = " ")
        self.inorderTraverseRecurse(self.rootNode)
        print ("\n")

    def postorderTraverse(self):
        print ("Postorder traversal:", end = " ")
        self.postorderTraverseRecurse(self.rootNode)
        print ("\n")

    def preorderTraverseRecurse(self, node):
        if node is None:
            return
        else:
            print (node.value, end = " ")
            self.preorderTraverseRecurse(node.leftNode)
            self.preorderTraverseRecurse(node.rightNode)

    def inorderTraverseRecurse(self, node):
        if node is None:
            return
        else:
            self.inorderTraverseRecurse(node.leftNode)
            print (node.value, end = " ")
            self.inorderTraverseRecurse(node.rightNode)

    def postorderTraverseRecurse(self, node):
        if node is None:
            return
        else:
            self.postorderTraverseRecurse(node.leftNode)
            self.postorderTraverseRecurse(node.rightNode)
            print (node.value, end = " ")


    def breadthFirstSearch(self):
        print ("Breadth first search (left to right):", end = " ")
        self.queue.clear()
        self.queue.enqueue(self.rootNode)
        self.breadthFirstSearchRecurse()
        print ("\n", end = "\n")

    def breadthFirstSearchRecurse(self):
        #if Queue is empty return
        if self.queue.count() == 0:
            return
        node = self.queue.dequeue()
        #if the element pulled from the queue is null then do nothing
        if node != None:
            print (node.value, end = " ")
            self.queue.enqueue(node.leftNode)
            self.queue.enqueue(node.rightNode)
        self.breadthFirstSearchRecurse()