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
	dir = "/home/xubuntu/dd"# input("Enter file path: ")
	f = open(dir, 'r')
	readin(f, KLgraph)

	
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
		self.CurrentCost = 0
		# self.vertices = []
		self.Part1 = {} #Each partition is a dictionary with the index (a1, a2, b1, b2) as the key, and a list of connections as the value
		self.Part2 = {}
		self.iteration = 0

	def findcost(self):
		extcost = 0
		intcost = 0
		for ver in self.Part1.keys():
			for con in self.Part1[ver]:
				if con in self.Part2.keys():
					extcost += 1
					#break
				else:
					intcost += 1
		self.CurrentCost = extcost

	def outputgraph(self):
		self.findcost()
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
		print(self.CurrentCost)



				
	

#Exec main()
if __name__ == "__main__":
    main()
