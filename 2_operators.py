print(2+3)
print(3-1)
print(3//6)
print(3*2)
print(3 % 9)
print(3**6)



2/14/22, 8:37 PM 03_boxplot
file:///D:/Baba Ammar/03_boxplot.html 1/3
<AxesSubplot:xlabel='class', ylabel='fare'>
<AxesSubplot:xlabel='tip', ylabel='day'>
survived pclass sex age sibsp parch fare embarked class who adult_male deck In [2]:
import seaborn
#canvas (baloon bord)
seaborn .set(style="whitegrid")
kashti =seaborn. load_dataset("titanic")
seaborn.boxplot(x="class", y = "fare", data = kashti)
Out[2]: In [13]:
import seaborn
tip = seaborn.load_dataset("tips")
seaborn.boxplot(x="tip", y = "day", data = tip)
Out[13]: In [16]:
import seaborn as sns
import pandas as pd
import numpy as np
kashti = sns.load_dataset("titanic")
kashti.head()
Out[16]:
2/14/22, 8:37 PM 03_boxplot
file:///D:/Baba Ammar/03_boxplot.html 2/3
<AxesSubplot:xlabel='survived', ylabel='age'>
<AxesSubplot:xlabel='survived', ylabel='age'>
survived pclass sex age sibsp parch fare embarked class who adult_male deck
0 0 3 male 22.0 1 0 7.2500 S Third man True NaN
1 1 1 female 38.0 1 0 71.2833 C First woman False C 2 1 3 female 26.0 0 0 7.9250 S Third woman False NaN
3 1 1 female 35.0 1 0 53.1000 S First woman False C 4 0 3 male 35.0 0 0 8.0500 S Third man True NaN
In [21]:
import seaborn as sns
import pandas as pd
import numpy as np
kashti = sns.load_dataset("titanic")
sns.boxplot(x = "survived", y = "age", data = kashti)
Out[21]: In [22]:
sns.boxplot(x = "survived", y = "age", data = kashti, showmeans = True)
Out[22]:
2/14/22, 8:37 PM 03_boxplot
file:///D:/Baba Ammar/03_boxplot.html 3/3
Text(0.5, 1.0, 'kitny doby or kitny bachy')
In [30]:
import matplotlib.pyplot as plt
sns.boxplot(x = "survived", y = "age", data = kashti, showmeans = True, meanprops ={
 
# show lables
plt.xlabel("how many survived", size = 12)
plt.ylabel("age(years)", size = 12)
plt.title("kitny doby or kitny bachy", size =14 , weight = "bold")
Out[30]:
