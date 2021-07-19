from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import joblib
 
app = Flask(__name__)

filename = 'model.pkl'
reg = joblib.load(filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')  

@app.route('/result', methods = ['POST'])
def result():
    formDictionary = request.form
     
    country = request.form['country']
    accType = request.form['accType']
    headline = request.form['headline']
    followers = int( request.form['followers'] )
    mediaType = request.form['mediaType']
    post_content = request.form['post_content']
    contlen=len(post_content)
    num_links = int( request.form['num_links'] )
    num_hashtags = int( request.form['num_hastags'] )
    post_type = request.form['post_type']
    num_hash_ratio=num_hashtags/followers
    num_links_ratio=num_links/followers
    
    followers=np.sqrt(followers)
    num_hashtags=np.sqrt(num_hashtags)
    num_links=np.sqrt(num_links)
    contlen=np.sqrt(contlen)
    num_hash_ratio=np.sqrt(num_hash_ratio)
    num_links_ratio=np.sqrt(num_links_ratio)
    
    article=0
    document=0
    image=0
    poll=0
    text=0
    video=0

    if mediaType=='article':
        article=1
    elif mediaType=='document':
        document=1 
    elif mediaType=='image':
        image=1  
    elif mediaType=='poll':
        poll=1 
    elif mediaType=='text':
        text=1 
    elif mediaType=='video':
        video=1                                        

    achievement=0
    call_to_action=0
    insights=0
    job_opening=0
    other=0
    if post_type=='achievement':
        achievement=1
    elif post_type=='call to action':
        call_to_action=1 
    elif post_type=='insights':
        insights=1  
    elif post_type=='job opening':
        job_opening=1 
    elif post_type=='other':
        other=1 
    
    arr=np.array([ [followers,article,document,image,poll,text,video ,achievement, call_to_action, insights, job_opening, other,num_hashtags,num_links,contlen,num_hash_ratio,num_links_ratio] ])
    X_test = pd.DataFrame(arr,columns=[ 'followers', 'article', 'document', 'image', 'poll', 'text', 'video', 'achievement', 'call to action', 'insights', 'job opening', 'other', 'num_hashtags', 'num_links','contlen','num_hash_ratio','num_links_ratio'])
    
    post_impressions = reg.predict(X_test)
    post_impressions=post_impressions[0]
 
    import math
    post_impressions=math.exp( post_impressions )
    post_impressions=round(float(post_impressions)) 

    return render_template('result.html', post_impressions=post_impressions  )        



if __name__=='__main__':
    app.run()
