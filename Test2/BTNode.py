
class BTNode:

    def __init__(self, parent=None, key=0, lc=None, rc=None):
        self.__parent = parent
        self.__key = key
        self.__rightChild = rc
        self.__leftChild = lc

    def getParent(self):
        return self.__parent
    def setParent(self, p):
        self.__parent = p
        
    def getKey(self):
        return self.__key
    def setKey(self, k):
        self.__key = k

    def getRightChild(self):
        return self.__rightChild
    def setRightChild(self, rc):
        self.__rightChild = rc

    def getLeftChild(self):
        return self.__leftChild
    def setLeftChild(self, lc):
        self.__leftChild = lc

    def isLeftChild(self):
        if self.__parent is None:
            return False
        else:
            return self is self.getParent().getLeftChild()
    def isRightChild(self):
        if self.__parent is None:
            return False
        else:
            return self is self.getParent().getRightChild()

    def __str__(self):
        b = 'BTNode(key=' + str(self.__key)
        if self.__parent != None:
            b += ', p=' + str(self.__parent) + ', '
        else:
            b += ', p=NULL, '
        if self.__leftChild != None:
            b += ', lc=+, '
        else:
            b += ', lc=NULL, '
        if self.__rightChild != None:
            b += 'rc=+'
        else:
            b += 'rc=NULL'
        b += ')'
        return b

    @staticmethod
    def __heightOf(node):
        if self is None:
            return -1
        else:
            return 1+max(node.getLeftChild(), node.getRightChild())
        
    def heightOf(self):
        return BTNode.__heightOf(self)
