from __future__ import print_function
import copy
def showMap(array2d):
    for x in range(0, 3):
        for y in range(0, 3):
            print(array2d[x][y], end='')
        print(" ")
    print("        ")
    return;
def move(array2d, srcX, srcY, drcX, drcY):
    temp = array2d[srcX][srcY]
    array2d[srcX][srcY] = array2d[drcX][drcY]
    array2d[drcX][drcY] = temp
    return array2d;
def getStatus(array2d):
    y = 0;
    for i in range(0, 3):
        for j in range(0, 3):
            for m in range(0, i + 1):
                for n in range(0, j):
                    if array2d[i][j] > array2d[m][n]:
                        y += 1;
    return y;
class Node:
    def __init__(self, array2d, g=0, h=0):
        self.array2d = array2d
        self.father = None
        self.g = g
        self.h = h
    def setH(self, endNode):
        for x in range(0, 3):
            for y in range(0, 3):
                for m in range(0, 3):
                    for n in range(0, 3):
                        if self.array2d[x][y] == endNode.array2d[m][n]:
                            self.h += abs(x * y - m * n)
    def setG(self, g):
        self.g = g
    def setFather(self, node):
        self.father = node
    def getG(self):
        return self.g
class A:

    def __init__(self, startNode, endNode):
        self.openList = []
        self.closeList = []
        self.startNode = startNode
        self.endNode = endNode
        self.currentNode = startNode
        self.pathlist = []
        self.step = 0
        return;
    def getMinFNode(self):
        nodeTemp = self.openList[0]
        for node in self.openList:
            if node.g + node.h < nodeTemp.g + nodeTemp.h:
                nodeTemp = node
        return nodeTemp
    def nodeInOpenlist(self, node):
        for nodeTmp in self.openList:
            if nodeTmp.array2d == node.array2d:
                return True
        return False
    def nodeInCloselist(self, node):
        for nodeTmp in self.closeList:
            if nodeTmp.array2d == node.array2d:
                return True
        return False
    def endNodeInOpenList(self):
        for nodeTmp in self.openList:
            if nodeTmp.array2d == self.endNode.array2d:
                return True
        return False

    def getNodeFromOpenList(self, node):
        for nodeTmp in self.openList:
            if nodeTmp.array2d == node.array2d:
                return nodeTmp
        return None

    def searchOneNode(self, node):
        if self.nodeInCloselist(node):
            return
        gTemp = self.step
        if self.nodeInOpenlist(node) == False:
            node.setG(gTemp)
            node.setH(self.endNode);
            self.openList.append(node)
            node.father = self.currentNode
        else:
            nodeTmp = self.getNodeFromOpenList(node)
            if self.currentNode.g + gTemp < nodeTmp.g:
                nodeTmp.g = self.currentNode.g + gTemp
                nodeTmp.father = self.currentNode
        return;

    def searchNear(self):
        flag = False
        for x in range(0, 3):
            for y in range(0, 3):
                if self.currentNode.array2d[x][y] == 0:
                    flag = True
                    break;
            if flag == True:
                break;
        self.step += 1
        if x - 1 >= 0:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x - 1, y)
            self.searchOneNode(Node(arrayTemp));
        if x + 1 < 3:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x + 1, y)
            self.searchOneNode(Node(arrayTemp));
        if y - 1 >= 0:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x, y - 1)
            self.searchOneNode(Node(arrayTemp));
        if y + 1 < 3:
            arrayTemp = move(copy.deepcopy(self.currentNode.array2d), x, y, x, y + 1)
            self.searchOneNode(Node(arrayTemp));
        return;

    def start(self):
        startY = getStatus(self.startNode.array2d)
        endY = getStatus(self.endNode.array2d)

        if startY % 2 != endY % 2:
            return False;
        self.startNode.setH(self.endNode);
        self.startNode.setG(self.step);
        self.openList.append(self.startNode)
        while True:
            self.currentNode = self.getMinFNode()
            self.closeList.append(self.currentNode)
            self.openList.remove(self.currentNode)
            self.step = self.currentNode.getG();
            self.searchNear();
            if self.endNodeInOpenList():
                nodeTmp = self.getNodeFromOpenList(self.endNode)
                while True:
                    self.pathlist.append(nodeTmp);
                    if nodeTmp.father != None:
                        nodeTmp = nodeTmp.father
                    else:
                        return True;
            elif len(self.openList) == 0:
                return False;
            elif self.step > 30:
                return False;
        return True;
    def showPath(self):
        for node in self.pathlist[::-1]:
            showMap(node.array2d)