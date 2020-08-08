# The survey of young people's feelings of depression
A study was conducted in an English class to compile and analyze questionnaires about the factors that make young people feel depressed as of July 2020.


## Introduction

### Aim
The aim of this study is to identify the situations and items that make young people feel depressed in a special social situation where the effects of COVID-19 require them to refrain from going out of the house.


### Motivation
The motivation for this study was that many clinical medical articles point out that psychiatric disorders are caused by stressful situations, and that the current social conditions are sufficient to accelerate this, and that we focused on people around 16-24 years of age who lack the ability to devise this situation due to their lack of life skills.


### Hypothesis
The hypothesis of this study is that "young people tend to feel depressed in proportion to their household income, wealth and ease of living.
Note that, "ease of living” is assumpted to depend on the burden of household chores and the size of the family.


## Method
In this study, data were collected through a questionnaire and a model was constructed and analyzed by decision trees.
The questionnaire items used in this study are as follows ↓. As an explanatory variable, we asked about the individual's status and how he or she has been living in the last three months. As a correct label, I asked them to use the five-point scale to see if they had experienced lethargy or mood changes in the past three months.
Fifty-six people responded to the survey, of which 47 were valid responses.

#### As explanatory variables
- Gender
- Average time of sleep
- Age
- Annual household income
- Number of meals/day
- How many hours a week do you spend out of the house?
- How much housework do you have to bear?
- Number of classes per week
- Total time to work on assignments etc. in a week
- Total part-time hours worked per week
#### As a correct label
- Lately, I'm not enjoying the things I used to enjoy anymore, I can't focus on things anymore, and I have no energy.


## Discussion
The accuracy of the decision tree model is about 93%, with three cases of high depression and two cases of low depression were obtained.

![](https://github.com/jabelic/COVID19-d8n-Analysis/blob/master/Inkedgraph_random_LI.jpg)

|DepressionLevel(x)|work|family|classes|salarry|study|meal|sleepAve|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|4&5|x > 7.5|x > 2.5||||||
|5|x <= 7.5|||x > 3.5||||
|5|x <= 7.5||x > 8.0|x <= 0.5|x <= 32.5|||
|1|x > 7.5|x <= 2.5|x > 8.5|||||
|2|x <= 7.5|||0.5 < x <= 3.5||x > 2.5|x > 5.5|


Firstly, the fifth case from the top of the table is a healthy life, and it can be interpreted that leading a life that is generally seen as low in Stress is helpful in avoiding depression. The top case is for those who work a lot and live  with their parents for a while, the second case is for those who live at home with high income families, and the third case is for those who are feeling depressed and have more lectures, lower part-time income, and are more likely to live alone.
This result shows that it is very difficult for the students with poor life skills to change the cause of their depression. 

## Conclusion

It is essential that people who are feeling depressed have friends around them to take care of them, and in these situations, it is noticeable that people who are vulnerable become weaker.
If you notice something unusual about your friends around you, try to be aware of it and take care of them as soon as possible.

## Reference

- [企業従業員における健康習慣 と抑 うつ症状の関連性](https://www.jstage.jst.go.jp/article/joh1959/29/1/29_1_55/_pdf/-char/ja)

- [ストレス度と生活習慣,ドック検査結果との関係と3年間の推移](https://www.jstage.jst.go.jp/article/ningendock2005/23/3/23_527/_pdf/-char/ja)

