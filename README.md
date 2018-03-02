# Weibo-Social-Network-Analysis
Building Sina Microblogging 10 BIG DATA related Tag Cloud and data analysis

1 DATA SCRAPING
1. Strategies.

1.1 DATA STRUCTURE
Choose users relevant to big data.We thought of two scraping strategies for users

1.2 SCRAPING STRUCTURE
The whole scraping structure is based on Python scrapy framework as displayed in figure 1.1 .

2 STATISTICAL ANALYSIS
We want to visualize the relationship and do statistical analysis based on the data we scraped from Weibo. After referring to the Twitter Case analysis diagrams in lecture handouts 11, we decided to use Echarts to visualize all of our results and display the followingfigures.

2.1 4 ANALYSIS
1. The relationship between follow and fans
2. The relationship between fans and posts
3. The relationship between fans and posts of users having fewer than 1000 fans
4. At what time do users post weibo?
3 USER INFLUENTIAL ANALYSIS
It.s obvious that user influence is a quite complex analysis related to many factors, including user active degree, covering rate,
transmissibility and so on. So we can.t use only one quota to analyze this problem. We should approach the problem all-round. Here we
use these different methods.
3.1 PAGERANK
• Why use PageRank• Improvement• Result

3.2 DEGREE RANK
• Why still degree rank• Implementation• Result

3.3 WEIBO BEHAVIOR RANK
• Why needWeibo behavior• Implementation• Result

3.4 COMBINATION
To conclude all these three algorithm, we can generate an intersection on these three sets.Figure3.4 is the result of a Venn Graph.

4 KEYWORD EXTRACTION
4.1 TF-IDF
• introduction• problems and solutions• results and evaluation

4.2 TEXTRANK
• introduction• Why we use TextRank• Process• Results and Evaluation

4.3 WORD-CLOUD VISUALIZATION

5 COMMUNITY DETECTION ALGORITHMõFAST UNFOLDING(LOUVAIN)

5.1 INTRODUCTION

5.2 WHY WE USE LOUVAIN

5.3 RESULTS AND EVALUATION

6 REFERENCES

7 THOUGHTS AND REFLECTION
