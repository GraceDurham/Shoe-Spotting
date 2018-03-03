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


