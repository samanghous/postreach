

Creator: Saman Ghous

Project-Deployment: https://predictin-deployment.herokuapp.com/

## Aim:
Often important linkedin posts by organizations don’t get the required reach due to poor post designing or use of inaccurate community hashtags.This project, Linkedin Post Reach Predictor aims at solving this problem by predicting reach i.e total impressions in linkedin community for a post beforehand and help the organizations in designing posts in an effective way that maximizes their reach.

# DEMO

https://user-images.githubusercontent.com/58565264/119225905-1cb87700-bb24-11eb-9e4d-6d417cd7c9e8.mp4

## Data:
* The data has been obtained by scraping the linkedin pages of companies and influencers.Information like Number of followers,company size,post content,number of likes,number of comments,comments’ content,etc are being used as the features.
* We have used selenium and beautifulsoup for scraping 


## Working Approach:
* After the data was collected major variables which could affect post's reach was then shortlisted and processed. 
 
* The most suitable Machine learning model which was votingRegressor i.e combination of various regressor, with proper hyperparameter tuning was then used to fit our training set and used to predict the reach of any test post.
 
* The model was then deployed.
 



