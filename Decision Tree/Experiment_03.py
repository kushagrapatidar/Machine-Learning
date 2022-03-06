import csv 
import math

def read_data(filename):
    """ read csv file and return header and data  """
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')
        metadata = next(datareader)
        traindata = []
        for row in datareader:
            traindata.append(row)

    return metadata, traindata

def calculate_entropy(attributes, lable):
    true_indx = []

    for index in range(len(lable)):
        if lable[index] == 'yes':
            true_indx.append(index)
    
    if attributes != lable:
        unique_attribute = []
        for attribute in attributes:
            if attribute not in unique_attribute:
                unique_attribute.append(attribute)

        print(true_indx)
        print(unique_attribute)

        attribute_dict = {}
        for attribute in unique_attribute:
            attribute_dict[attribute + '-yes'] = 0
            attribute_dict[attribute + '-no'] = 0 

        print(attribute_dict)

        for attribute_index, attribute in enumerate(attributes):
            if attribute_index in true_indx:
                attribute_dict[f'{attribute}-yes'] += 1

            else:
                attribute_dict[f'{attribute}-no'] += 1 
            
        entropy = {}
        for attribute in unique_attribute:
            total = attribute_dict[f'{attribute}-yes'] + attribute_dict[f'{attribute}-no'] 
            yes = attribute_dict[f'{attribute}-yes']
            no = attribute_dict[f'{attribute}-no']

            p1 = yes/total
            p2 = no/total
            
            if yes == 0:
                p1 = 1 
            if no == 0:
                p2 = 1

            temp_entropy = - ((yes/total)*math.log2(p1)) - ((no/total)*math.log2(p2)) 
            entropy[attribute]=temp_entropy

    else:
        total = len(lable)
        yes = len(true_indx)
        no = total - yes    

        p1 = yes/total
        p2 = no/total
        
        if yes == 0:
            p1 = 1 
        if no == 0:
            p2 = 1
        entropy = - ((yes/total)*math.log2(p1)) - ((no/total)*math.log2(p2))
    return entropy

def calculate_gain(entropyS, entropy, attributes):

    unique_attributes={}
    for attribute in attributes:
        if attribute in unique_attributes.keys():
            unique_attributes[attribute] += 1
        else:
            unique_attributes[attribute] = 1
    
    pes = 0
    for unique_attribute_key, unique_attribute in enumerate(unique_attributes):
        pes += (unique_attribute/len(attributes))*entropy[unique_attribute_key]

    gain = entropyS - pes

    return gain

if __name__ == '__main__':
    metadata, traindata = read_data('decisionTree.csv')
    col = []
    for row in traindata:
        col.append(row[0])

    lable = []
    for row in traindata:
        lable.append(row[-1])

    print(metadata)
    print(traindata)
    
    entropy = calculate_entropy(lable, lable)
    print(entropy)
    calculate_gain(entropyS, entropy, attributes)