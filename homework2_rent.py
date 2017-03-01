import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import r2_score

# Define the variable to store test and train data
X=[]
y=[]

def score_rent():
    # Read data from the link
    columns = ["boro","uf1_1","uf1_2","uf1_3","uf1_4","uf1_5","uf1_6","uf1_7","uf1_8","uf1_9","uf1_10","uf1_11","uf1_12","uf1_13","uf1_14","uf1_15","uf1_16","uf1_35","uf1_17","uf1_18","uf1_19","uf1_20","uf1_21","uf1_22","sc23","sc24","sc36","sc37","sc38","sc114","sc118","uf9","uf48","uf11","sc149","sc173","sc171","sc150","sc151","sc152","sc153","sc154","sc155","sc156","sc157","sc158","sc159","sc161","sc164","sc166","sc174","sc541","sc184","sc542","sc543","sc544","sc185","sc186","sc197","sc198","sc187","sc188","sc571","sc189","sc190","sc191","sc192","sc193","sc194","sc196","sc548","sc549","sc550","sc551","sc199","uf19","new_csr","rec15","sc26","uf23","rec21","rec62","rec62","rec64","rec64","rec54","rec53","cd","fw","seqno","hflag6","hflag3","hflag14","hflag16","uf17"]
    df = pd.read_csv('https://ndownloader.figshare.com/files/7586326', delimiter=",", usecols=columns)

    contcols = ["fw", "seqno", "uf17"]
    df = df[df["uf17"] != 99999]

    index = pd.Index(df.columns.tolist())
    df2 = pd.DataFrame(columns=contcols)
    indexB = pd.Index(df2.columns.tolist())

    categories = index.difference(indexB).tolist()
    dfcont = df[["fw", "seqno"]]
    dfcateg = df.drop(contcols, axis=1)
    data_dummies = pd.get_dummies(dfcateg,columns=categories)

    # Create the datasets
    Xvars = pd.concat([data_dummies, dfcont], axis=1)

    # Define the features
    X= Xvars.values

    # Define the label data
    y = df[["uf17"]].values

    # Split test and train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # Create and train the linear Regression model
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)

    # Utilize r2_score function to calculate the R^2 value between test data and predicated data
    return r2_score(regr.predict(X_test),y_test)


def predict_rent():
    # Split test and train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # Create and train the linear Regression model
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)

    # Create numpy matrix and return results
    predictedLabels = np.matrix(regr.predict(X_test))
    return X_test,y_test,predictedLabels
	
def test():
	return score_rent()	
	
if __name__ == "__main__":
    print("Check the following two functions:")
    print(score_rent())
	print(predict_rent())
