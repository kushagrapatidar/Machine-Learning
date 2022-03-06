# import csv 
# import math

# def read_data(filename):
#     """ read csv file and return header and data  """
#     with open(filename, 'r') as csvfile:
#         datareader = csv.reader(csvfile, delimiter=',')
#         metadata = next(datareader)
#         traindata = []
#         for row in datareader:
#             traindata.append(row)

#     return metadata, traindata

# def calculate_entropy(attributes, lable):
#     true_indx = []

#     for index in range(len(lable)):
#         if lable[index] == 'yes':
#             true_indx.append(index)
    
#     if attributes != lable:
#         unique_attribute = []
#         for attribute in attributes:
#             if attribute not in unique_attribute:
#                 unique_attribute.append(attribute)

#         print(true_indx)
#         print(unique_attribute)

#         attribute_dict = {}
#         for attribute in unique_attribute:
#             attribute_dict[attribute + '-yes'] = 0
#             attribute_dict[attribute + '-no'] = 0 

#         print(attribute_dict)

#         for attribute_index, attribute in enumerate(attributes):
#             if attribute_index in true_indx:
#                 attribute_dict[f'{attribute}-yes'] += 1

#             else:
#                 attribute_dict[f'{attribute}-no'] += 1 
            
#         entropy = {}
#         for attribute in unique_attribute:
#             total = attribute_dict[f'{attribute}-yes'] + attribute_dict[f'{attribute}-no'] 
#             yes = attribute_dict[f'{attribute}-yes']
#             no = attribute_dict[f'{attribute}-no']

#             p1 = yes/total
#             p2 = no/total
            
#             if yes == 0:
#                 p1 = 1 
#             if no == 0:
#                 p2 = 1

#             temp_entropy = - ((yes/total)*math.log2(p1)) - ((no/total)*math.log2(p2)) 
#             entropy[attribute]=temp_entropy

#     else:
#         total = len(lable)
#         yes = len(true_indx)
#         no = total - yes    

#         p1 = yes/total
#         p2 = no/total
        
#         if yes == 0:
#             p1 = 1 
#         if no == 0:
#             p2 = 1
#         entropy = - ((yes/total)*math.log2(p1)) - ((no/total)*math.log2(p2))
#     return entropy

# def calculate_gain(entropyS, entropy, attributes):

#     unique_attributes={}
#     for attribute in attributes:
#         if attribute in unique_attributes.keys():
#             unique_attributes[attribute] += 1
#         else:
#             unique_attributes[attribute] = 1
    
#     pes = 0
#     for unique_attribute_key, unique_attribute in enumerate(unique_attributes):
#         pes += (unique_attribute/len(attributes))*entropy[unique_attribute_key]

#     gain = entropyS - pes

#     return gain

# if __name__ == '__main__':
#     metadata, traindata = read_data('decisionTree.csv')
#     col = []
#     for row in traindata:
#         col.append(row[0])

#     lable = []
#     for row in traindata:
#         lable.append(row[-1])

#     print(metadata)
#     print(traindata)
    
#     entropy = calculate_entropy(lable, lable)
#     print(entropy)
#     calculate_gain(entropyS, entropy, attributes)

import sys
import numpy as np
from numpy import *
import csv


class Node:
    def _init_(self, attribute):
        self.attribute = attribute
        self.children = []
        self.answer = ""


def read_data(filename):
    """ read csv file and return header and data  """
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        metadata = next(datareader)
        traindata = []
        for row in datareader:
            traindata.append(row)

    return (metadata, traindata)


def subtables(data, col, delete):
    dict = {}
    items = np.unique(data[:, col]) # get unique values in a particular column

    count = np.zeros((items.shape[0], 1), dtype=np.int32)   #number of row = number of values

    for x in range(items.shape[0]):#number of unique values ina column
        for y in range(data.shape[0]):# number of rows in the dataset
            if data[y, col] == items[x]:
                count[x] += 1
    #count has the data of number of times each value is present in

    for x in range(items.shape[0]):
        dict[items[x]] = np.empty((int(count[x]), data.shape[1]), dtype="|S32")##array for

        pos = 0
        for y in range(data.shape[0]):
            if data[y, col] == items[x]:
                dict[items[x]][pos] = data[y]
                pos += 1

        if delete:
           dict[items[x]] = np.delete(dict[items[x]], col, 1)
    return items, dict
#
#
#
# def entropy(S):
#     """ calculate the entropy """
#     items = np.unique(S)
#     if items.size == 1:
#         return 0
#
#     counts = np.zeros((items.shape[0], 1))
#     sums = 0
#
#     for x in range(items.shape[0]):
#         counts[x] = sum(S == items[x]) / (S.size)
#
#     for count in counts:
#         sums += -1 * count * math.log(count, 2)
#     return sums
#
# def gain_ratio(data, col):
#     items, dict = subtables(data, col, delete=False)
#     #item is the unique value and dict is the data corresponding to it
#     total_size = data.shape[0]
#     entropies = np.zeros((items.shape[0], 1))
#
#     for x in range(items.shape[0]):
#         ratio = dict[items[x]].shape[0]/(total_size)
#         entropies[x] = ratio * entropy(dict[items[x]][:, -1])
#
#
#     total_entropy = entropy(data[:, -1])
#
#
#     for x in range(entropies.shape[0]):
#         total_entropy -= entropies[x]
#
#     return total_entropy
#
#
# def create_node(data, metadata):
#
#     if (np.unique(data[:, -1])).shape[0] == 1: #to check how many rows in last col(yes,no column). shape[0] gives no. of rows
#         ''' if there is only yes or only no then reutrn a node containing the value '''
#         node = Node("")
#         node.answer = np.unique(data[:, -1])
#         return node
#
#     gains = np.zeros((data.shape[1] - 1, 1))  # data.shape[1] - 1 returns the no of columns in the dataset, minus one to remove last column
#     #size of gains= number of attribute to calculate gain
#     #gains is one dim array (size=4) to store the gain of each attribute
#
#     for col in range(data.shape[1] - 1):
#         gains[col] = gain_ratio(data, col)
#
#     split = np.argmax(gains) # argmax returns the index of the max value
#
#
#     node = Node(metadata[split])
#     metadata = np.delete(metadata, split, 0)
#
#
#     items, dict = subtables(data, split, delete=True)
#
#     for x in range(items.shape[0]):
#         child = create_node(dict[items[x]], metadata)
#         node.children.append((items[x], child))
#
#     return node
#
# def empty(size):
#     """ To generate empty space needed for shaping the tree"""
#     s = ""
#     for x in range(size):
#         s += "   "
#     return s
#
# def print_tree(node, level):
#     if node.answer != "":
#
#         print(empty(level), node.answer.item(0).decode("utf-8"))
#         return
#
#     print(empty(level), node.attribute)
#
#     for value, n in node.children:
#         print(empty(level + 1), value.tobytes().decode("utf-8"))
#         print_tree(n, level + 2)
#
#
metadata, traindata = read_data("tennis.csv")
data = np.array(traindata)  # to convert the traindata to numpy array
# node = create_node(data, metadata)
# print_tree(node, 0)
#
# print(metadata)
# print(traindata)
# print(data)
# print(data.shape[0])
# print("data.shape1", data.shape[1])
# items = np.unique(data[:, 0])
# print("items", items)
# print(items.shape[0])
# count = np.zeros((items.shape[0], 1), dtype=np.int32)  # number of row = number of values
# print("count", count)
# for x in range(items.shape[0]):  # number of unique values ina column
#     for y in range(data.shape[0]):  # number of rows in the dataset
#         if data[y, 0] == items[x]:
#             count[x] += 1
# print("count1", count)
# # print(items.shape[0])
# # print(items[0])
# dict = {}
# for x in range(items.shape[0]):
#     dict[items[x]] = np.zeros((int(count[x]), data.shape[1]), dtype="|S32")  # dtype="|S32"
# #print(dict)
#     pos = 0
#     delete = False
#     for y in range(data.shape[0]):
#         if data[y, 0] == items[x]:
#             dict[items[x]][pos] = data[y]
#             pos += 1
#     if delete:
#         dict[items[x]] = np.delete(dict[items[x]], 0, 1)
# print(dict)
# items1 = np.unique(dict[items[1]][:, -1])
# print(items1)
# # # if items.size == 1:
# # #         return 0
# #
# counts = np.zeros((items1.shape[0], 1))
# print(counts)
# sums = 0
# print(sum(dict[items[1]][:, -1] == items1[0]))
# print(dict[items[1]][:, -1].size)
# print(dict[items[1]])
# for x in range(items1.shape[0]):
#     counts[x] = sum(dict[items[1]][:, -1] == items1[x]) / (dict[items[1]][:, -1].size)
# print(counts)