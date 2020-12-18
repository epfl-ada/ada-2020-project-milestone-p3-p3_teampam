import networkx as nx
import pandas as pd
import numpy as np
import itertools

'''
TO KNOW BEFORE READING THE CODE : 
- p1 denote P(+|+)
- p2 denote P(-|+)
- p3 denote P(+|-)
- p4 denote P(-|-)
'''

def count_p(dataframe, name_data):
    ''' Returns the number of edges satisfying the p1, p2, p3 and p4 relations in a graph G'''
    df_copy = dataframe.copy()
    p1 = 0 #initialisation of the p1 count
    p2 = 0 #initialisation of the p2 count
    p3 = 0 #initialisation of the p3 count
    p4 = 0 #initialisation of the p4 count
    iteration = 0
    for index, row in df_copy.iterrows():
        if iteration%2 == 1:
            iteration+=1
            continue #we only check the values every 2 iterations (A couple of reciprocated edges is found every 2 lines)
        else : 
            if name_data == 'wikipedia' :
                from_node = row['FromNodeId']
                to_node = row['ToNodeId']
                sign = row['Sign']
                #we find the sign of the reciprocation manually (actually it's the next line in the dataframe, but this is a naive try)
                sign_reci = df_copy.loc[(df_copy['FromNodeId'] ==to_node) & (df_copy['ToNodeId']==from_node)]['Sign'].values[0]
            else :
                from_node = row['SOURCE_SUBREDDIT']
                to_node = row['TARGET_SUBREDDIT']
                sign = row['Sign']
                sign_reci = df_copy.loc[(df_copy['SOURCE_SUBREDDIT'] ==to_node) & (df_copy['TARGET_SUBREDDIT']==from_node)]['Sign'].values[0]

            if (sign == 1) and (sign_reci == 1) :
                p1 +=1

            if (sign == 1) and (sign_reci == -1) :
                p2 +=1

            if (sign == -1) and (sign_reci == 1) :
                p3 +=1

            if (sign == -1) and (sign_reci == -1) :
                p4 +=1

            iteration+=1
        
    return p1, p2, p3, p4


def create_table4(dataframe, name_data):
    '''Creates table 4
    Input : - dataframe : the dataframe for which we replicate table 4
            - name_data : 'reddit' or 'wikipedia' : name of the dataset, for filling the table 4 but also for handling the different column names 
            
    Output : - table : table4
    '''
    #create the table and fill the first column
    table = pd.DataFrame(columns = [name_data, 'Count', 'Fraction'])
    table[name_data] = ['P(+|+)', 'P(-|+)', 'P(+|-)', 'P(-|-)']
        
    #count p1, p2, p3 and p4 :
    p1,p2,p3,p4 = count_p(dataframe, name_data)
    
    #compute the fractions :
    f_p1 = p1/(p1+p2)
    f_p2 = p2/(p1+p2)
    f_p3 = p3/(p3+p4)
    f_p4 = p4/(p3+p4)
    
    #fill the table
    table['Count'] = [p1, p2, p3, p4]
    table['Fraction'] = [f_p1, f_p2, f_p3, f_p4]
    
    return table
    
    
    
    
    
''' Function  to print examples of link p2'''
def print_p2(dataframe, name_data, nb_ex):
    ''' Prints nb_ex examples of couples of subreddits that satisfy P(-|+)'''
    
    print('Examples of subreddits (A,B) satisfying P(-|+) : A link positive to B, B link negative to A ')
    df_copy = dataframe.copy()
    iteration = 0
    nb_ex_found =0 #number of examples that satsfies P(-|+) we found
    for index, row in df_copy.iterrows():
        if iteration%2 == 1:
            iteration+=1
            continue #we only check the values every 2 iterations (A couple of reciprocated edges is found every 2 lines)
        else : 
            if name_data == 'wikipedia' :
                from_node = row['FromNodeId']
                to_node = row['ToNodeId']
                sign = row['Sign']
                #we find the sign of the reciprocation manually (actually it's the next line in the dataframe, but this is a naive try)
                sign_reci = df_copy.loc[(df_copy['FromNodeId'] ==to_node) & (df_copy['ToNodeId']==from_node)]['Sign'].values[0]
            else :
                from_node = row['SOURCE_SUBREDDIT']
                to_node = row['TARGET_SUBREDDIT']
                sign = row['Sign']
                sign_reci = df_copy.loc[(df_copy['SOURCE_SUBREDDIT'] ==to_node) & (df_copy['TARGET_SUBREDDIT']==from_node)]['Sign'].values[0]

            if (sign == 1) and (sign_reci == -1) :
                nb_ex_found+=1 #we increase the number of examples we found
                print('example {} :\nA : {}\nB : {}\n'.format(nb_ex_found, from_node, to_node))

            if nb_ex_found==nb_ex:
                break

            iteration+=1
            
''' Function  to print examples of link p3'''
def print_p3(dataframe, name_data, nb_ex):
    ''' Prints nb_ex examples of couples of subreddits that satisfy P(+|-)'''
    
    print('Examples of subreddits (A,B) satisfying P(+|-) : A link negative to B, B link positive to A ')
    df_copy = dataframe.copy()
    iteration = 0
    nb_ex_found =0 #number of examples that satsfies P(+|-) we found
    for index, row in df_copy.iterrows():
        if iteration%2 == 1:
            iteration+=1
            continue #we only check the values every 2 iterations (A couple of reciprocated edges is found every 2 lines)
        else : 
            if name_data == 'wikipedia' :
                from_node = row['FromNodeId']
                to_node = row['ToNodeId']
                sign = row['Sign']
                #we find the sign of the reciprocation manually (actually it's the next line in the dataframe, but this is a naive try)
                sign_reci = df_copy.loc[(df_copy['FromNodeId'] ==to_node) & (df_copy['ToNodeId']==from_node)]['Sign'].values[0]
            else :
                from_node = row['SOURCE_SUBREDDIT']
                to_node = row['TARGET_SUBREDDIT']
                sign = row['Sign']
                sign_reci = df_copy.loc[(df_copy['SOURCE_SUBREDDIT'] ==to_node) & (df_copy['TARGET_SUBREDDIT']==from_node)]['Sign'].values[0]

            if (sign == -1) and (sign_reci == 1) :
                nb_ex_found+=1 #we increase the number of examples we found
                print('example {} :\nA : {}\nB : {}\n'.format(nb_ex_found, from_node, to_node))

            if nb_ex_found==nb_ex:
                break

            iteration+=1

            
''' Function  to print examples of link p4'''
def print_p4(dataframe, name_data, nb_ex):
    ''' Prints nb_ex examples of couples of subreddits that satisfy P(-|-)'''
    
    print('Examples of subreddits (A,B) satisfying P(-|-) : A link negative to B, B link positive to A ')
    df_copy = dataframe.copy()
    iteration = 0
    nb_ex_found =0 #number of examples that satsfies P(-|-) we found
    for index, row in df_copy.iterrows():
        if iteration%2 == 1:
            iteration+=1
            continue #we only check the values every 2 iterations (A couple of reciprocated edges is found every 2 lines)
        else : 
            if name_data == 'wikipedia' :
                from_node = row['FromNodeId']
                to_node = row['ToNodeId']
                sign = row['Sign']
                #we find the sign of the reciprocation manually (actually it's the next line in the dataframe, but this is a naive try)
                sign_reci = df_copy.loc[(df_copy['FromNodeId'] ==to_node) & (df_copy['ToNodeId']==from_node)]['Sign'].values[0]
            else :
                from_node = row['SOURCE_SUBREDDIT']
                to_node = row['TARGET_SUBREDDIT']
                sign = row['Sign']
                sign_reci = df_copy.loc[(df_copy['SOURCE_SUBREDDIT'] ==to_node) & (df_copy['TARGET_SUBREDDIT']==from_node)]['Sign'].values[0]

            if (sign == -1) and (sign_reci == -1) :
                nb_ex_found+=1 #we increase the number of examples we found
                print('example {} :\nA : {}\nB : {}\n'.format(nb_ex_found, from_node, to_node))

            if nb_ex_found==nb_ex:
                break

            iteration+=1