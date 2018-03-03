# Shoespotting Readme

Shoe spotting was created to entertain. It's a fun way of posting shoes from the web and commenting on them. This app allows users to comment on their own posts and also comment on the posts of others. It's a great way of tracking shoes you've discovered on the web, and optionally tracking how much they cost. It's like Pinterest for shoes!


## Getting Started Set up your virtual machine with Vagrant 


![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/setup_vagrant.png)

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/set_up_vagrant_continued.png)

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/set_up_vagrant_cont.png)



```
git clone https://github.com/GraceDurham/Shoe-Spotting.git
cd Shoe-Spotting
```
#### Create and run virtual environment on command line

```
pip install virtualenv
virtualenv VENV
source venv/bin/activate
```

#### Install system dependancies 

```
pip install -r requirements.txt
```

#### Runs flask app (start server)

```
python server.py 
```

#### Profit

open http://127.0.0.1:5000/

### The Home Page

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/home_page.png)

### Register Page 
![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/register_page.png)
```
On register page please register as a user by inputting your first name, last name, email and password 

```
### Login Page 

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/login_page.png)

```
On login page please input your email and the password you just created to login into the site. 

```

### Your Profile Page 

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/your_profile_page.png)


```
Your profile page will eventually show you all the shoes that you collected from your web search after you post them individually.  Click on the add shoe post button.

```
### Add Shoe Post Page 

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/add_shoe_post_page.png)

```
In my example above I went to Macys.com and found a pair of flats that I love. After you have found the shoe that you want to add from the web follow steps below.

1.On the image of the shoe press the control button and right click choose copy image address. Then paste this url into the image url box.

2. In the title box type the name of the shoe and the designer's name. 

3. In the website url box copy the the url of the website that you found the shoe.

4. In the text box input the price of the shoe, name of the store, the colors available and most important if they have your size.  See example above.

5. Then click on the add shoe post button. This will post onto your profile page. 

```
### Updated Profile Page After Shoe Post 

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/updated_profile_page_with_shoe_post.png)

### Comment on shoe post 

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/add_comment_shoe_post.png)
![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/add_comment_shoe_post_continued.png)

```
You can add a comment on the shoe post on the profile page by clicking the shoe image.  It will query the postgres database for that post id.  Type your comments in the add new comments box then click on the add new comment button to post your comments.  You can also add comments like this on other people's profiles.

```
### Shoe Feed Page 

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/shoe_feed_page.png)

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/shoe_feed_page_continued.png)

![alt text](https://github.com/GraceDurham/Shoe-Spotting/blob/master/shoe_feed_page_cont.png)

```
To get to the shoe feed page click on the silhouette and spot light of the black high heels in the upper left hand corner of the top nav bar. Shoe feed page displays all the shoe posts by all the users. If you see a pair that you like you can click on the image then add a comment on that user's shoe post. :)

```
