import pandas as pd
import numpy as np
import sklearn as sk
from sklearn import linear_model
def Calc(age_input,bmi_input,smoker_input):
    df = pd.read_csv('dataset/insurance.csv')

    df["smoker"]=map_smoking(df["smoker"])

    mean_features = calc_mean(df[["age","bmi"]]) 
    #mean_target = calc_mean(df[["charges"]]) 

    sd_features = calc_mean(df[["age","bmi"]]) 
    #sd_target = calc_mean(df[["charges"]]) 

    df = normalise(df, mean_features,sd_features)

    x= df[["age","bmi","smoker"]].to_numpy()
    y = df["charges"].to_numpy()
    
    reg = linear_model.LinearRegression()
    reg.fit(x,y)

    age_input = (age_input-mean_features[0])/sd_features[0]
    bmi_input = (bmi_input-mean_features[1])/sd_features[1]
    if smoker_input=="yes":
        s=1
    else:
        s=0
    
    inputs = np.array([age_input,bmi_input,s])

    return reg.predict([inputs])[0]




def map_smoking(column):
    mapped=[]
    
    for row in column:
        
        if row=="yes":
            mapped.append(1)
        else:
            mapped.append(0)
        
        
    return mapped


def calc_mean(x):
      return x.mean().to_numpy()



def calc_sd(x):
      return x.std().to_numpy()


def normalise(df, mean_features,sd_features):
    list = [["age","bmi"]]
    for i in list:
        df[i] = (df[i]-mean_features[list.index(i)])/sd_features[list.index(i)]
    return df








