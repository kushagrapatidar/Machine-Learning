#Reading and Creating the dataset as a list of list
from csv import reader
file=open("candidateelim.csv", 'r')
filedata=reader(file)
data=[]
for row in filedata:
    data.append(row)
    print(row)
num_attributes=len(data[0])-1

#The initial value of hypothesis
S=['0']*num_attributes
G=['?']*num_attributes

#The most specific hypothesis S0 and most general hypothesis G0
print(S)
print(G)

# if data[0][-1]=='No':
#     idx=1
#     data[0],data[idx]=data[idx],data[0]
for i in range(num_attributes):
    S[i]=data[0][i]

#Candidate Elimination algorithm
temp=[]
for i in range(len(data)):
    #If the instance is positive this condition
    #generalize the specific hyposthesis
    if data[i][num_attributes]=='Yes':
        for j in range(num_attributes):
            if data[i][j]!=S[j]:
                S[j]='?'
        #The loop below makes the necessary changes
        #in the general hypothesis as per the above changes
        # in specific hypothesis
        for j in range(num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j]!='?' and temp[k][j]!=S[j]:
                    del temp[k]
                    
        if (len(temp)==0):
            continue
        else:
            G=temp
            
    #If the instance is negative this condition makes
    #the general hypothesis more specific
    if data[i][num_attributes]=='No':
        for j in range(num_attributes):
            if S[j] != data[i][j] and S[j]!= '?':
                G[j]=S[j]
                temp.append(G)
                G = ['?'] * num_attributes
        G=temp

#Hypothesis S and G
print("Hypothesis S:",S)
print("Hypothesis G:",G)