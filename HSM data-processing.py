# HSM data-processing
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df1 = pd.read_csv('./data/Happy.csv')
df2 = pd.read_csv('./data/Sad.csv')

df = pd.concat([df1,df2])
dataset = df.values
print(len())