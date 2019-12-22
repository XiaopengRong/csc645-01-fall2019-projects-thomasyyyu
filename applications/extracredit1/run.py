import sys

from Function import Function
from Edge import Edge
from Node import Node


def printRoutingTable(vertexNameList, printMatrix):
    rowLength = int(len(printMatrix) / len(vertexNameList))
    outputTable = []
    firstRow = "\t"
    print("\nRouting Table: ")
    for x in vertexNameList:
        firstRow += x + "\t"

    outputTable.append(firstRow)
    indexPos = 0
    for y in vertexNameList:
        ctr = 0
        rowOutput = y
        while ctr < rowLength:
            if printMatrix[indexPos] == sys.maxsize:
                printMatrix[indexPos] = -1
            rowOutput += "\t" + str(printMatrix[indexPos])
            ctr += 1
            indexPos += 1
        outputTable.append(rowOutput)

    for z in outputTable:
        print(z)


class Run(object):

    def __init__(self):
        self.edgeInnerObjectLit = None
        self.temp = []
        self.vertexObjectList = []
        self.edgeObjectList = []
        self.edgeInnerNameList = []
        self.vertexNameList = []
        self.printMatrix = []

    def run(self):
        # vertex input
        print("Please enter list of NODES separated by comma(No less than 3 nodes)")
        isTrue = True
        while isTrue:
            Text = input("Node: ")
            self.temp = Text.split(",")
            counter = 0
            for x in self.temp:
                self.vertexObjectList.append(Node(x))
                counter += 1
            if counter < 3:
                print("Nodes num must be greater than three")
            elif counter >= 3:
                isTrue = False

        for x in self.temp:
            self.vertexNameList.append(x)

        isTrue = True
        while isTrue:
            userInput = input("Please input the start Node, finish Node and distance between them separated by comma: ")
            self.edgeInnerNameList = userInput.split(",")
            counter = 0
            for x in self.edgeInnerNameList:
                if self.edgeInnerNameList[0] and self.edgeInnerNameList[1] in self.vertexNameList:
                    counter += 1
                else:
                    print("Node not found in the list")
            if counter < 2:
                print("Please enter correct information")

            userInput2 = input("Do you want to keep enter Node? (y/n)")
            if userInput2 == 'n':
                isTrue = False
                self.edgeObjectList.append(Edge(self.vertexObjectList[0], self.vertexObjectList[1], int(self.edgeInnerNameList[-1])))
            elif userInput2 == 'y':
                isTrue = True
            else:
                print("Please enter correct selection")

        algorithm = Function()
        i = 0

        while i < len(self.vertexObjectList):
            if i > 0:
                for elements in self.vertexObjectList:
                    elements.minDistance = sys.maxsize
            algorithm.calculateShortestPath(self.vertexObjectList[i], self.vertexObjectList, self.edgeObjectList)
            i += 1
            j = 0
            while j < len(self.vertexObjectList):
                self.printMatrix.append(self.vertexObjectList[j].minDistance)
                j += 1

        printRoutingTable(self.vertexNameList, self.printMatrix)


app = Run()
app.run()
