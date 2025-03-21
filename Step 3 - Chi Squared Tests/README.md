Following the completion of factor analysis and chi-square tests, we can effectively determine which variables contribute meaningfully to the study and which do not. Step 3 (Factor Analysis) is crucial for Likert-scale items, ensuring that only reliable and internally consistent constructs are retained through Cronbach’s alpha, while Kendall’s W ranks ordinal responses appropriately. This process refines the dataset by identifying coherent groupings of variables that represent underlying constructs. Step 4 (Chi-Square Tests), on the other hand, addresses categorical, binary, and select-type variables, identifying statistically significant associations between these factors and key dependent variables. This ensures that only relevant categorical variables are retained for further analysis. By integrating the findings from these two steps, we eliminate unreliable or weakly associated factors, preventing them from introducing noise into the Gradient Boosting Machine (GBM) model. As a result, the predictive model is optimized, incorporating only the most statistically meaningful and influential variables, thereby enhancing its accuracy and interpretability.

Trying to test: Barriers to Precision Agriculture in Indonesia

Categorical: IMP2 (1-4)
alpha = 0.05
How long do you anticipate it will take to fully implement PAtechnologies on your farm?:•Less than 1 year•1-3 years•More than 3 years•Not sure

Select-Type: INO2_1, INO2_2, INO2_3, INO2_4, INO2_5 (data format, 5 cols either 1 or 0)
alpha = 0.01
What is the biggest barrier you face in adopting PA technologies(Select one)?•Lack of knowledge and/or training•High cost of implementation•Lack of infrastructure•Uncertain return on investment•Resistance from farm workers

Select-All-Type: 
COM1_1, COM1_2, COM1_3, COM1_4, COM1_5, COM1_6, COM1_7
alpha = 0.007

OUT2_1, OUT2_2, OUT2_3, OUT2_4, OUT2_5 (data format, 7 cols either 1 or 0 then 5 cols either 1 or 0, can have multiple 1s in a row)
alapha = 0.01

- How do you typically receive information about new agriculturaltechnologies (Select all that apply)?•Government extension services•Agricultural universities•Private companies/consultants•Online resources•Other farmers•Agricultural associations•Media (TV, radio, newspapers)
- What additional support would encourage you to adopt PAtechnologies (Select all that apply)?•More government subsidies•Improved internet or power infrastructure•Better access to training and knowledge•Lower costs of technology•Support from other farmers or farmer cooperatives


Binary Yes/No: SRI3 (data format, 1 cols either 1 or 0)
Do you have dedicated resources (time, money, personnel) forexploring and implementing new farming technologies?

Question that I can maybe use to help with the independence test idk?
MAD1: How willing are you to adopt Precision Agriculture technologies (1-5)?

remove ADO1_1 from likert scale questions 
only include IMP2, COM1_5 from chi squared table