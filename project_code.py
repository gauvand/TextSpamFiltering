'''
Authors: Gaurav Anand, John Zhang, Summer Chambers, Vasudha Manikandan
Class: DS6014
'''

try:
    import nltk, re, pprint
except:
    import os
    os.system('pip install nltk')
finally:
    import nltk, re, pprint
    import numpy as np
    import pandas as pd
    from nltk import word_tokenize
    nltk.download('punkt')


class NaiveBayesClassifier:
    def __init__(self,df,alpha):
        '''
        :param df: Pandas DataFrame containing a `class` column ('ham' or 'spam') and a `text` column
        '''
        self.data = df
        self.n = len(df)    
        self.table = self.generate_table()   
        self.priors = self.generate_priors() 
        self.train(alpha)

    def generate_table(self):
        '''
        Generates a word table for each topic (in this case, ham and spam)
        '''
        self.data['word'] = self.data.text.apply(word_tokenize)
        table = self.data.explode('word')
        table = table.groupby(['type','word']).count().rename({'text':'count'},axis=1).reset_index()
        table = table.pivot_table(columns='type',index=['word'],values='count',fill_value=0)
        return table

    def table_to_csv(self,path):
        '''
        Writes the word table to a csv 

        :param path: path to the file directory
        '''
        table = self.generate_table()
        table.to_csv(path)
        print(f"Wrote to {path}!")

    def generate_priors(self):
        '''
        Create informed priors for ham and spam
        '''
        ham_length = len(self.data.query('type=="ham"'))
        spam_length = self.n - ham_length
        priors = [ham_length/self.n, spam_length/self.n]
        return priors        
    
    def train(self,alpha):
        '''
        Create probability table based on the value of alpha (the smoothing parameter)
        
        :param alpha: smoothing parameter :type float
        '''
        table = self.generate_table()
        WordSums = table.sum()
        Pword = np.zeros([len(table.index), len(table.columns)])
        v = len(table.index)
        for i in range(len(table.index)):
            for j in range(len(table.columns)):
                Pword[i,j] = (table.iloc[i,j] + alpha)/(WordSums[j] + v*alpha)
        self.prob_table = pd.DataFrame(data=Pword, index = table.index, columns = table.columns)

    def predict(self,NewReview):
        WordsIndex = list()
        for i in range(len(NewReview)):
            for j in range(len(self.table.index)):
                if NewReview[i] == self.table.index[j].strip():
                    WordsIndex.append(j)

        # Likelihoods

        likelihoods = np.ones(len(self.table.columns))
        for j in range(len(self.table.columns)):
            for i in WordsIndex:
                likelihoods[j] = likelihoods[j]*self.prob_table[i,j]

        # Posterior Probabilities

        numerator = likelihoods * self.priors
        postprob = np.round(numerator/numerator.sum(), 4)
        return postprob
            
if __name__ == '__main__':
    pass