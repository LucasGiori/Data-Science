import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

train=pd.read_csv('e:/Users/lucas.cesconetto/Desktop/Data Sciense/dreanalisecsv.csv')
test=pd.read_csv('e:/Users/lucas.cesconetto/Desktop/Data Sciense/dreanalisecsv.csv')
train['Type']='Train' #Cria uma bandeira para o conjunto de dados de treino e de teste
test['Type']='Test'
fullData = pd.concat([train,test],axis=0) #Combina ambos conjuntos de dados de treino e de teste