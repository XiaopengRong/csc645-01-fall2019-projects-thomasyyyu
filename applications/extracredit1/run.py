import sys

from Function import Function
from Edge import Edge
from Node import Node


class Run(object):

    def __init__(self):
        self.edgeInnerObjectLit = None
        self.vertexObjecttemp = []
        self.vertexObjectList = []
        self.edgeObjectList = []
        self.edgeInnerObjectList = []
        self.vertexNameList = []
        self.printMatrix = []

    def run(self):
        # vertex input
        print("Please enter list of NODES separated by comma(No less than 3 nodes)")
        isTrue = True
        while isTrue:
            Text = input("Node: ")
            self.vertexObjecttemp = Text.split(",")
            counter = 0
            for x in self.vertexObjecttemp:
                counter += 1
                self.vertexObjectList.append(Node(x))

            if counter < 3:
                print("Nodes num must be greater than three")
            elif counter >= 3:
                isTrue = False
        for x in self.vertexObjecttemp:
            self.vertexNameList.append(str(x))

        isTrue = True
        while isTrue:
            userInput = input("Please input the start Node, finish Node and distance between them separated by comma: ")
            self.edgeInnerObjectList = userInput.split(",")
            counter = 0
            for x in self.edgeInnerObjectList:
                counter += 1
            if counter != 3:
                print("Please enter correct information")
            if self.edgeInnerObjectList[0] and self.edgeInnerObjectList[1] in self.vertexObjectList:
                if int(self.edgeInnerObjectList[2]) > 0:
                    self.edgeObjectList.append(self.edgeInnerObjectList)
                    Edge(self.edgeInnerObjectList[0], self.edgeInnerObjectList[1], int(self.edgeInnerObjectList[2]))
            else:
                print("elements not in the Nodes, please enter again")
            userInput2 = input("Do you want to keep enter Node? (y/n)")
            if userInput2 == 'n':
                isTrue = False
            elif userInput2 == 'y':
                isTrue = True
            else:
                print("Please enter correct selection")

        algo = Function()
        i = 0

        while i < len(self.vertexObjectList):
            if i > 0:
                for _ in self.vertexObjectList:
                    _.minDistance = sys.maxsize
            algo.calculateShortestPath(self.vertexObjectList[i], self.vertexObjectList, self.edgeObjectList)
            i += 1
            j = 0
            while j < len(self.vertexObjectList):
                self.printMatrix.append(self.vertexObjectList[j].minDistance)
                j += 1

        self.printRoutingTable(self.vertexNameList, self.printMatrix)

    def printRoutingTable(self, vertexNameList, printMatrix):
        rowLength = int(len(printMatrix) / len(vertexNameList))
        outputTable = []
        firstRow = "\t"
        print("\nRouting Table: ")
        for x in vertexNameList:
            firstRow += x + "\t"

        outputTable.append(firstRow)
        indexPos = 0
        for x in vertexNameList:
            ctr = 0
            rowOutput = x
            while ctr < rowLength:
                if printMatrix[indexPos] == sys.maxsize:
                    printMatrix[indexPos] = -1
                rowOutput += "\t" + str(printMatrix[indexPos])
                ctr += 1
                indexPos += 1
            outputTable.append(rowOutput)

        for x in outputTable:
            print(x)


app = Run()
app.run()
