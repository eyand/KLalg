#!/usr/bin/env python3

'''
K-L Algorithm
ECE428
Evan Yand
Step 1
'''

import argparse
import os
import re



def main():

        KLgraph = Graph()
        dir = "/home/evan/dd"# input("Enter file path: ")
        f = open(dir, 'r')
        readin(f, KLgraph)
        
        KLgraph.findcost()
        KLgraph.gains()

        #KLgraph.split(part1)

        KLgraph.outputgraph()


def readin(file, graph):
        first = False #First line contains total vertices and edges
        current = 1
        firstB = 0

        for line in file:
                if first is False:
                        numvertices, numedges = line.split()
                        graph.Nvertices = int(numvertices)
                        graph.Nedges = int(numedges)
                        print("There are " + str(graph.Nvertices) + " vertices and " + str(graph.Nedges) + " edges in this graph")
                        first = True

                else:
                        index = current
                        edges = []

                        for edge in line.split():
                                #print("The current edge is between " + str(current) + " and " + str(edge))
                                edges.append(int(edge)) 


                        if current <= graph.Nvertices/2:
                                graph.Part1[index] = edges      

                                #graph.vertices.append(currentvertex)
                        else:
                                graph.Part2[index] = edges



                        current += 1


class Graph(object):
        """A  mathematical graph representing a VLSI circuit"""
        def __init__(self):
                super(Graph, self).__init__()
                self.Nvertices = 0
                self.Nedges = 0
                self.Extcost = 0
                self.Intcost = 0
                # self.vertices = []
                self.Part1 = {} #Each partition is a dictionary with the index (a1, a2, b1, b2) as the key, and a list of connections as the value
                self.Part2 = {}
                
                self.Extcosts = {}
                self.Intcosts = {}
                self.Dcosts = {}

                self.Gains1 = []
                self.Gains2 = []
                self.Gains = []

                self.iteration = 0

        def findcost(self):
                extcost = 0
                intcost = 0
               

                #Reset Costs
                for ver in self.Part1.keys():
                    self.Extcosts[ver] = 0
                    self.Intcosts[ver] = 0
                for ver in self.Part2.keys():
                    self.Extcosts[ver] = 0
                    self.Intcosts[ver] = 0

                #Go through each vertex and access its connections in the form of an array
                for ver in self.Part1.keys():
                        for con in self.Part1[ver]:
                                if con in self.Part2.keys():
                                        extcost += 1
                                        self.Extcosts[con] += 1
                                        self.Extcosts[ver] += 1
                                else:
                                        intcost += 1
                                        self.Intcosts[ver] += 1
                
                for ver in self.Part2.keys():
                        for con in self.Part2[ver]:
                            if con in self.Part2.keys():
                                intcost += 1
                                self.Intcosts[ver] += 1


                #for ver in self.Part1.keys():
                 #   print("Cost of ver " + str(ver) + " is " + str(self.Extcosts[ver]))
                #  print("IntCost of ver " + str(ver) + " is " + str(self.Intcosts[ver]))
                #for ver in self.Part2.keys():
                 #   print("Cost of ver " + str(ver) + " is " + str(self.Extcosts[ver]))
                  #  print("IntCost of ver " + str(ver) + " is " + str(self.Intcosts[ver]))
                self.Extcost = extcost
                self.Intcost = intcost

                for ver in self.Part1.keys():
                    self.Dcosts[ver] = self.Extcosts[ver] - self.Intcosts[ver]

                for ver in self.Part2.keys():
                    self.Dcosts[ver] = self.Extcosts[ver] - self.Intcosts[ver]

        def gains(self):
            i = 0

            for ver in self.Part1.keys():
                for con in self.Part2.keys():
                    self.Gains1.append(ver)
                    self.Gains2.append(con)
                    self.Gains.append(self.Dcosts[ver] + self.Dcosts[con] - 2)

                    #print("The gain of " + str(ver) + " and " + str(con) + " is " + str(self.Gains[i]))

                    i += 1
            j = 0
            highest = self.Gains[0]
            selection = 0
            for g in self.Gains:
                if g > highest:
                    highest = g
                    selection = j
                j += 1
            
            print("The (first) largest possible gain is: " + str(highest) + " by swapping " + str(self.Gains1[selection]) + " and " + str(self.Gains2[selection]))



        def outputgraph(self):
                
                print()
                print("****Printing graph:****")
                #for ver in self.vertices:
                        #print("Vertex " + str(ver.index) + " is connected to " + str(ver.connections))

                print("Iteration: " + str(self.iteration))
                print()
                print("PARTITION 1")
                for ver in self.Part1.keys():
                        print(ver)

                print()
                print("PARTITION 2")
                for ver in self.Part2.keys():
                        print(ver)

                print()
                print("Final Cost:")
                print(self.Extcost)





#Exec main()
if __name__ == "__main__":
    main()
