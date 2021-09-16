### Objective

Determine whether the author is male or not (True:1; unknown or False:0) based on his/her posts published on the forum.
LGBTQ is out of the scope of this project because of technical limitations. 
We could not classify whether a post was written by homosexual men or women yet according to their writing style. 
Thus, posts on "rainbow" forum on Dcard would not be considered to be part of our dataset.

- - -
### Required knowledge and skills

Concept of machine learning. [Introduction to Machine Learning.md](Introduction%20to%20Machine%20Learning.md) is for your reference.

- - -
### Data Collection 

- **Rule of Labeling**

    Only keep posts whose content are informative about gender of its author. *i.e. There must be clear correspondence between content and label(target).*


- **Data Source**: *MySQL database named "forum_data"* <p>Notice: Some posts have null value or incomplete pattern in the column named "content". <p> We need below columns:

    
    id, s_id, s_area_id, title, content_type, author, page_url, post_time, content
    
    
- - -
### Model Building and Training
Although this is the most interesting and valuable work in the whole project, I was not responsible for this part. My advice is to
go check Prof.Hung-Yi Lee's YouTube video and learn for yourself. Also, google for more resources if you need :) 
- - -
### Performance Evaluation
Visit [Performance Evaluation.md](Performance%20Evaluation.md) for further information.

    
