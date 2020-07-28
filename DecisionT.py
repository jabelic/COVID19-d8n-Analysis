import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pydotplus
from sklearn.externals.six import StringIO
from sklearn import tree

# ------DataParse----

df = pd.read_csv('data/English3A.csv')

salarytxt = 'おおよその世帯年収（一人暮らしの方はご自身の収入(+仕送り)をお答えください）'
df.loc[df[salarytxt] == '～500万円', salarytxt] = 0
df.loc[df[salarytxt] == '500万円～800万円', salarytxt] = 1
df.loc[df[salarytxt] == '800万円～1200万円', salarytxt] = 2
df.loc[df[salarytxt] == '1200万円～1600万円', salarytxt] = 3
df.loc[df[salarytxt] == 'それ以上', salarytxt] = 4

sleeptxt = '平均睡眠時間'
for i in range(4, 11):
    df.loc[df[sleeptxt] == str(i) + '時間', sleeptxt] = i
df.loc[df[sleeptxt] == 'それ以上', sleeptxt] = 13

sextxt = '性別(保険証記載の方)'
df.loc[df[sextxt] == '男', sextxt] = 1
df.loc[df[sextxt] == '女', sextxt] = 0

familytxt = '同居している人数(自分除いて)は何人ですか？'
df.loc[df[familytxt] == 'それ以上', familytxt] = 6

del df["タイムスタンプ"]
del df['高校生/高専生/専門学生/短大生/大学生/大学院生ですか？']

df_ = df.dropna(how='any')
df_.to_csv("data/dataEng3A.csv")
df_ = df_.astype(float)

dfstd = df_.iloc[:, :].apply(lambda x: (x-x.mean())/x.std())
dfstd.to_csv("dataEng3Astd.csv")

dfs = df_.iloc[:, :12].apply(lambda x: (x-x.mean())/x.std())
dfs.head()


X = np.array(df_.iloc[:, :11])
Y = np.array(df_.iloc[:, 11:12]).T
for item in np.array(Y):
    Y = item

'''
X, Y = make_classification(n_samples=100, n_features=11,
                           n_informative=5, n_redundant=5,
                            random_state=0, shuffle=False)
'''
X = np.array(list(X)*80)
Y = np.array(list(Y)*80)

(train_x, test_x ,train_y, test_y) = train_test_split(X, Y, test_size = 0.3, random_state = 42)

clf = tree.DecisionTreeClassifier(max_depth=6)
clf = clf.fit(train_x, train_y)

predicted = clf.predict(test_x)

judge = []

for i in range(len(test_y)):
    if predicted[i] == test_y[i]:
        judge.append(1)


print(sum(judge)/len(test_y))
#np.shape(X)


dot_data = StringIO()
labels = ['gender', 'sleepAve', 'age', 'salary', 'meal', 'family', 'housework','outgoing', 'classes', 'study', 'work']

graph = tree.export_graphviz(clf, out_file=None,
                         feature_names=labels,
                         class_names=None,
                         filled=True, rounded=True)
graph = pydotplus.graph_from_dot_data(graph)
graph.write_png("graph_random.png")
