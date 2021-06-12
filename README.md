

![Screenshot (110)](https://user-images.githubusercontent.com/58565264/119225748-5d63c080-bb23-11eb-9bc3-a6775ed13e5b.png)

Team Members:Shreya Sajal,Vineet Agarwal,Saman Ghous,Siddharth Shankar Pandey,Rishika Patwa

## Aim:
Often important linkedin posts by organizations don’t get the required reach due to poor post designing or use of inaccurate community hashtags.Our project, PredictIn aims at solving this problem by predicting a popularity score for a post beforehand and help the organizations in designing the posts in an effective way that maximizes their popularity.

# DEMO

https://user-images.githubusercontent.com/58565264/119225905-1cb87700-bb24-11eb-9e4d-6d417cd7c9e8.mp4

## Data:
* The data has been obtained by scraping the linkedin pages of companies and influencers.Information like Number of followers,company size,post content,number of likes,number of comments,comments’ content,etc are being used as the features.
* We have used selenium and beautifulsoup for scraping 


## Working Approach:
* After the data was collected ,a popularity metric using the features( Number of followers,company size,post content,number of likes,number of comments,length of post,type of post,number of hashtags) was made.These were made after proper research on LinkedIn metrics .
 
* The most suitable Machine learning model with proper hyperparameter tuning was then fitted on our training set and used to predict the popularity score of any test post.
 
* The model was then deployed.
 



