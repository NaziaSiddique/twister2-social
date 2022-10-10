# <h1 align="center">TWISTER</h1>

<img width="905" alt="Screenshot 2022-09-05 at 20 36 22" src="https://user-images.githubusercontent.com/36114589/188505848-0e0b41b3-58b4-4ef3-9b7f-8b0dec1d61ed.png">

Twister is a social media platform, similar to Twitter, specifically to connect businesses with their end users. Business owners and consumers can register for a free account, share, manage, re-post other users post (twist and re-twist!), as well as creating and managing their own social profile online. The focus being to create a focussed and transparent conversation/link between business-to-business owners, business-to-consumers, and consumers-to-consumers.  

[Link to the deployed project](https://twister-social.herokuapp.com/)

## Project Overview

 Twister is a social media application built using Python, Flask+SQLAlchemy, Flask+PyMongo, Bootstrap 5, Jinja2 and JavaScript. This Application is a hybrid database project using both MongoDB and PostgreSQL.   
 
•	User Registration is handled using relational-backed database: PostgreSQL using Flask+SQLAlchemy

•	Standard CRUD data manipulation i.e., user posts, re-posts etc is handled using a nonrelational-backed database: MongoDB using Flask+PyMongo 
 
Twister is the third and my personal favourite project created for the Code Institute’s Level 5 Diploma in Web Application Development (Full Stack Software Development). To make an app to rival Twitter’s was very challenging, but something I felt confident I could take on. Twitter is my most used social media platform, with some great features that I really wanted to incorporate into Twister. Features including the ability to re-post, follow live conversations, chime in on existing threads, scroll through timelines, explore what’s trending using hashtags on topics that matter to the user, join communities, track what’s happening around the business world and find a platform to voice consumer opinions/reviews on the latest gadgets and products. The Twister app also allows users to build their own customisable profiles, add a profile picture, description, location, and a background photo.   


# User Experience

## Project Goals

 
• To develop a social media App specifically to connect businesses with other businesses and consumers (B2B, B2C & C2C)

• Users have to register to enter the app and be able to use it 

• Registered users will be able to set up their own profiles, connect with other users/businesses, post, re-post, follow conversations, use hashtags to see what’s trending, all the while allowing open communication between businesses and their customers 

• Make the app easy to access, with a single registration/login page 

• Make the app user friendly and engaging using fun colours and keeping the fonts neat  

• Use Mobile First design principle in building a responsive App 

• Ensure all registered users (members and superadmin) have access to a full CRUD functionality 

• Ensure that registered users (members and superadmin) have access to a custom user dashboard with read functionality 

• App should include defensive programming (Bcrypt) to make encryption stronger and guard against threats/hackers 
 
## Consumer Demographics 
 
• Ages 16 and above for registering and contributing to the Twister community 

• Visitors who are interested in a platform that will connect them directly to businesses and other consumers 

• Users who are looking for a quick way to access product launches/news 

• Users who are looking for a one stop platform that focusses on bringing businesses and consumers together 

• Registered users who want to an easy way to set up their own profile 

• Registered users who want to able to follow relevant trends and company business profiles 

• Registered users who want to be able to join live conversations on topics of interest 

• Registered users who want to share their opinions and reviews on products/businesses etc   

• Registered users who want to able to view latest deals/offers on products 

• Registered users who want to be able to connect with other consumers to share ideas or have their voice heard 
 
 
## Businesses Demographics 
 
• Small, medium, large-scale businesses internationally  

• Businesses who want a social media platform to solely focus on brand awareness/growth 

• Businesses who are looking for a one stop platform with tools to help with product marketing, promotion, and latest trends  

• Businesses that want great analytics to help with current and future launches 

• Businesses who are looking to liaise directly with their consumers and understand what they need  

# User Stories

## First Time Visitor Goals (a first-time user/business who has not created an account). 

 I want to be able to:
• Immediately understand the main purpose and use of the application

• Have the ability to register/create a user account easily

• Easily navigate to the site to get the information that I need

## Registered User Goals (Consumers) 

I want to be able to:
• Learn more about what I can do on the Twister App 

• Add, edit, retrieve, and delete my own data 

• Add my own profile picture and set up my own profile  

• Be able to add additional information about myself onto my profile page 

• Have privacy options to allow me to choose what information other users can view 

• Be able to create, post and delete Twists 

• Upload an image to post 

• Have access to tools I may need to add, update, or delete my posts 

• Search and view specific posts using hashtags 

• Search and view other users profiles (consumers and businesses) 

• Be able to view trending posts/hashtags easily 

• Be able to follow other users/business profiles/groups/posts 

• Have my own member user dashboard (read functionality) 

• Registered User Goals (Businesses) 

• Have a business login/registration page 

• Have the ability to set up a profile with business information/links to business website  

• Be able to get verified business status  

# Design

# Wireframes

Sign up

![Business Profile Sign Up](https://user-images.githubusercontent.com/36114589/194953510-aa325bec-ee19-4749-9491-d6d97ffb529b.png)

![Consumer Sign Up Page](https://user-images.githubusercontent.com/36114589/194953532-9e58e5b4-9661-4907-83b4-4c8afbb54432.png)

![Sign Up Page](https://user-images.githubusercontent.com/36114589/194953703-82fb995d-1de8-4f1e-b6a0-89b2a268ed52.png)

Home Page

![Home Page_Main Feed](https://user-images.githubusercontent.com/36114589/194953584-f1c5283a-d3df-4515-ab4a-ca2be9cc064b.png)

Landing Page

![Landing Page](https://user-images.githubusercontent.com/36114589/194953623-3542c9e4-c87d-4eb0-97c9-2a8904137a0a.png)

Log In Page

![Log In Page](https://user-images.githubusercontent.com/36114589/194953764-b53bc4df-3ae2-4bf6-8c23-2ef1f0b68622.png)

Mobile Landing Page

![Mobile Landing Page](https://user-images.githubusercontent.com/36114589/194953816-d7b3bd04-0236-4b89-8487-2b4b589773b3.png)


# Features

Existing Features Overview (Non-Registered Users) 

 

Header Logo - Exists on every page and allows all users to easily navigate back to the home page by clicking on it 

 

Header Navigation Bar –Not visible on the landing page, but if users navigate away from it to other pages, it will appear and  will allow all users to easily navigate from any page back to the landing page 

 

Call to Action Buttons – This feature is available on the landing page, where potential users can click on either the ‘Sign Up’ or ‘Log In’ buttons to access the Twister site itself after signing up/logging in 

 

Sign Up Page – Allows users to sign up as either a Business or Consumer Profile 

 

Log In Page – Allows existing users to log in using their credentials. The site has the ability for users to click the ‘Remember Me’ check box for faster log ins 

 

About Page - Allows potential clients to quickly get an overview of the website, visible on the ‘Sign Up’ and ‘Log In’ pages 

 

*Landing Page: the landing page of the website features a orange modar with three lines of text in white describing what the site can be used for. The right-hand side of the landing page is white and split down the middle to separate it from the orange modar. Towards the middle of the right-hand side of the landing page, the orange logo is featured, with the site tagline ‘Explore what’s happening in the world of business’, followed by ‘Join Twister Today’. There are two call to action buttons ‘Sign up’ and ‘Log In’, which will navigate users to the relevant pages to access the site.  

 

* The colours used on the landing page reflect the branding that is used consistently throughout the website: orange, white and black. The logo is also featured on every page once the user enters the site.  

 

*All call-to-action buttons that link to a different page of the website and are fully responsive on both desktop mobile/tablet devices.  

 

 

* Log In Page: This page features a nav bar with links to the Home and About pages. The logo appears next to the Home button on the nav bar. On the right-hand side of the nav bar there is an option to change the language of the site, default language is set to English. The page features the text ‘Log in to Twister’, followed by two log-in boxes; one for the username and one for the password. This is followed by an orange call to action ‘Log In’ button and a check box feature to ‘Remember Me’ to save username and password, as well as a ‘Forgot Password?’ hyperlink to reset password. In smaller text there’s also the option for new users to the site, with the hyperlink option to ‘Sign up now’, which will re-navigate users to the Sign-Up page. The top nav bar features a small Twister logo on the left side. It also has two call to action buttons: ‘Home’ – when clicked, it takes users back to the landing page & ‘About’ – which takes the users to an information page. On the right-hand side of the nav bar, there is an option to choose the Language, which is pre-set to English.  

 

* Sign Up Page: This page features a nav bar with links to the Home and About pages. The logo appears next to the Home button on the nav bar. On the right-hand side of the nav bar there is an option to change the language of the site, default language is set to English. The page features the text ‘Sign Up to Twister’, followed by boxes to input the following data fields: full name, username, email, Password and Repeat Password. This is followed by an orange call to action ‘Sign Up’ button and a check box feature ‘Business Profile’ to allow the creation of a business profiles on Twister.  

 

* Consumer Sign Up – After filling in the basic information as mentioned above, users will be navigated to another page, prompting them to upload a profile pic, enter their address and contact number. They will then click ‘Save & Next’ to gain access to the Twister site.  

 

* Business Sign Up - After filling in the basic information as mentioned above, business users will be navigated to another page, prompting them to upload a profile pic, enter their business name, address, website URL, social media URL and contact number. They will then click ‘Save & Next’ to gain access to the Twister site.  

## Features for Registered Users (Consumers) 

Existing Features Overview (Non-Registered Users) 

 

Header Home Icon- Exists on most pages and allows all users to easily navigate back to the home page (main feed) by clicking on it 

 

Header Navigation Bar – Appears on the home page to allow quick access to search the site and view profile/account information 

 

Comment/Like Posts – Allows users to comment/like on any post on their news feed 

 

Share Posts – Allows users to share posts to various social media platforms, as well as email, what’s app and skype 

 

Change Profile Picture/Information – Allows existing users to change/update profile pictures and profile information  

 

Delete Profile - Allows users to delete profiles  

 

Main Page: Once users log in, they land on the main homepage of the site. The nav bar running across the top of the page has an orange ‘Home’ icon, when clicked will re-navigate users back to the main homepage. The nav bar also has a grey search bar, which will allow users to type and search for keywords and with further development search for users/businesses. The right-hand side of the nav bar has a profile picture icon, alongside the username and a drop-down arrow, which brings up a drop-down menu. The drop-down menu options provide information on the account and is aptly named ‘Account info’, followed by a mini user profile picture, the username and their @username. It will also show how many accounts the user is following and how many followers the account has. The action buttons  The homepage has a similar layout to many social media sites, featuring a main feed which will allow users to view updates from their connections/businesses they follow. It also has several action buttons, which gives users quick licks to access their profile information, view their posts/bookmarked posts, change their passwords, delete their account, log out or change from light to dark mode.  Consumers have the ability to comment on posts, share posts and ‘like’ them using the heart icon present on all posts.  Next to main feed, there’s a white box which will give users suggestions on ‘Who to follow’, this will be based on their current following/users they may be interested in. Currently this feature only allows users to view that particular profile, but with further development, they will have the ability to follow.  

 

The posts on main feed appear with the name of the user who has posted them, a small icon of their profile picture, as well as their @username and a time stamp of how many hours ago the post was posted. If posts have pictures, they appear under the text. Under the picture/text, there are three icons: comment bubble (with a number of how many comments appear under that particular post), love heart (to like the post) and a share icon (share to social media handles/emails/what’s app, skype). There is also a text input bar to add a comment.  

 

One of the most noticeable features of the homepage is the clear font and a simplistic layout. I wanted the homepage to feel clean and simple, with the same orange, white & black colour scheme running throughout the side. An additional feature, users can choose between a  classic white interface and a dark mode option.  

 

 

Features for Registered Users (Businesses) 

Header Home Icon- Exists on most pages and allows all users to easily navigate back to the home page (main feed) by clicking on it 

 

Header Navigation Bar – Appears on the home page to allow quick access to search the site and view profile/account information 

 

Post – Business users are able to share posts and information for other users to view  

 

Upload Images – Business users can share images to their posts as well images of products 

 

Comment/Like Posts – Allows users to comment/like on any post on their news feed 

 

Share Posts – Allows users to share posts to various social media platforms, as well as email, what’s app and skype 

 

Change Profile Picture/Information – Allows existing users to change/update profile pictures and profile information  

 

Additional Profile Information - have the options to view their Lists, Ads, Analytics and Products (which have been added, but due to time restrictions are not yet available) 

 

Delete Profile - Allows users to delete profiles  

 

Main Page: The homepage for business users is very similar layout to that of consumers, again, featuring a main feed which will allow users to view updates from the connections they follow. Business profiles have all the features available to consumers and some additional functionalities. Business users have the ability to post and upload pictures to posts as part of their user access levels. This is available in two different ways, one way is by typing directly into the text input box just above the main feed, businesses can upload pictures and then click the post button to post. Alternatively, there are two floating orange action buttons towards the bottom of the page, on the right-hand side, ‘+Post’ and ‘+Product’, which will allow businesses to not only post, but also upload products to their product catalogues. Businesses can also comment on posts, like and share.  

 

Like the consumer profiles, businesses also have the ability to access their account info by clicking on the on the mini profile picture icon on the right-hand side of the nav bar. The drop-down menu also has several action buttons, which gives business users quick licks to access their profile information, view their posts/bookmarked posts, change their passwords, delete their account, log out or change from light to dark mode.  For business users, they also have the options to view their Lists, Ads, Analytics and Products (which have been added, but due to time restrictions are not yet available). 

 
 
Log-in page:  
  
![login-page](https://user-images.githubusercontent.com/36114589/188512116-81a62b50-e719-4ebe-bd96-eac92121cc94.PNG) 
  
How a new post looks: 
  
![one-post](https://user-images.githubusercontent.com/36114589/188512155-c115a948-2966-4fed-b48e-eadcb65aaec1.PNG) 
  
When registering: 
  
![register](https://user-images.githubusercontent.com/36114589/188512264-08b4d796-028b-4691-9a39-6db931913b53.PNG) 
 
## Future Implementation 

* Ability for Consumers to Post – currently only have ability to comment/like/share posts, so this will be a great addition 

* Build In-App Messaging Tool– this will allow users (businesses and consumers) to send private messages 

* Search and View Specific Posts Using Hashtags 

A* nalytics Dashboard for Business Users 

* Trending posts 

* Chargeable Business Profile Features – set up an additional cost for registration  

* FAQ Page – this will give potential clients answers to the most asked questions via a table with FAQs and dropdown buttons to view answers 

* Add CAPTCHA to Contact Form – this will protect the site from being spammed  

* GDPR Compliant Pop-Up Screen – this will ensure that the company complies with the EU data protection laws, by enabling visitors to the website to approve or deny the processing of their personal data 

* Site Privacy Information – this will set out clear guidelines about what language restrictions there are in place, what behaviour is expected online and what actions will lead to accounts being blocked 

## Structure 

Database Schema and Structure 


The Twister Application uses a combination of two databases, PostgreSQL and MongoDB,  


All User Authentication and the list of Categories are handled using relational-backed database (PostgreSQL using Flask+SQLAlchemy).   

All the Standard CRUD data manipulation is handled using a nonrelational-backed database (MongoDB using Flask+PyMongo). The diagram below show the structure and schema used in the Postgres database. The Mongo db has all information for the content that is posted, such as the posts, the products information, the comments and any likes. 

 
 ![Entity](https://user-images.githubusercontent.com/36114589/194945939-f5b02e66-9bbc-460e-bd4d-2a5b17637039.jpg)


## CRUD

# CREATE:
         - All businesses can create new posts.
         - Consumers & Businesses can create their own accounts
# READ
         - All businesses can read all posts
         - All Consumers can read all posts
# UPDATE 
         - All business users can update their profiles
         - All consumers can update their details
# DELETE
         - All consumers can delete their accounts
         - All business users can delete their accounts
         
## KNOWN PROBLEMS

- The like icon counts the likes and is working but currently not showing the number of likes on the user interface.
- The search feature can be temperamental and not provide results every time a search is made.
- Some features have had to be removed due to not working any mre such as the hash tag search
- The site is not finished/polished the way I originally intednded it to look. Draft 1 which was just the front end, looked like this: https://github.com/NaziaSiddique/project3 Which is what I wanted this website to look like.
- The deployment was done in Heroku, a few days ago, however, it seems to stop working from time to time and then starts working again.
- The language is currently set to English and will be developed at a later stage.
- 

## Technologies Used

This app/website is programmed in the following languages: 
• HTML5/CSS3 were used for the content, styling and structure of the site 

• JavaScript was used for the dynamic elements if the site

• Python was used for the back end programming of the site 

• Flask – this was used to handle the templating for the site 

• Postgres – this is relational database used to store the user profiles, avatars, profile, user registrations, login and authentication 

• MongoDB – this is the nonrelational database used to store less structured data such as content that users post 

• Flask-PyMongo – this provides MongoDB support for Flask applications 

• Dnspython - this is a DNS toolkit for Python 

• Werkzeug – this is a Web Server Gateway Interface web application library 

• Jinja - this is a templating engine for Python, used to write Flask and other templating services 

• Bcrypt – password-hashing function used as a security feature 

• Click – Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.  

• Flask-Bcrypt – this is a Flask extension that provides bcrypt hashing utilities for the site 

• Flask-Login - provides the user session management for Flask. It handles the common tasks of logging in, logging out, and remembering users’ sessions over prolonged periods of time 

• Flask-SQLAlchemy – this is an extension for Flask that adds support for SQLAlchemy to the site. It simplifies processes to make it easier to accomplish common tasks 

• greenlet –  these are lightweight coroutines for in-process concurrent programming

• itsdangerous –this enables data to be signed cryptographically to ensure that a token has not been tampered with 

• pymongo – this is a Python distribution containing tool for working with MongoDB 

• SQLAlchemy –  this is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL

• gunicorn –  this is a Python Web Server Gateway Interface HTTP server. It allows the site to run any Python application concurrently by running multiple Python processes within a single dyno

• Balsamiq - balsamiq was used to create the wireframes for this project 

• Git - Git was used for version control and saving work in the repository 

• Gitpod – Gitpod was used as the IDE to develop and code this website 

• GitHub – used to host the site 

• Heroku – where the live site is deployed 

• Chrome - was used as the default testing browser 

## Deployment & Local Development

This project was built using Gitpod and pushed to GitHub using the in-built functionality to commit and push (source control). 
 
To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken: 
Log into GitHub 
From the list of repositories on the screen, select NaziaSiddique/twister2-social 
From the menu items near the top of the page, select Settings 
Scroll down to the GitHub Pages section 
Under Source click the drop-down menu labelled None and select Main 
By selecting Main the page is automatically refreshed and the website is now deployed 
Scroll back down to the GitHub Pages section to retrieve the link to the deployed website 
 
## Deployment to Heroku 
 
To deploy this project, I used Heroku. The deployed version is the same as in the repository. These are the steps used for deployment to Heroku: 
 
In GitPod CLI,  in root directory of the project, run: pip3 free --local > requirements.txt to create a requirements.txt file containing project dependencies 
In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'. Open the Procfile. Inside the file, check that web: python3 app.py has been added when creating the file. Continue on to save the file 
Login to Heroku, select ‘Create New App’, then add the desired name for your app, without any spaces and choose your closest region 
Navigate to the ‘Deploy’ tab on Heroku dashboard and select Github, search for your repository and click 'Connect' 
Navigate to the settings tab, click reveal config vars and input: 
 
CLOUD_NAME: mycloudinaryname 
API_KEY:	myapikey 
API_SECRET:	myapisecret 
IP: 0.0.0.0 
PORT:	5000 
MONGO_DBNAME:	mongodb_name mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER>- 
MONGO_URI:	4g3i1.mongodb.net/<DATABASE>?retryWrites=true&w=majority 
SECRET_KEY:	mysecretkey 
DATABASE_URL: postgresql 
 
Go back to the ‘Deploy’ tab and enable ‘Automatic Deploys’ 
Click ‘Deploy Branch’ 
Once the build is complete, click ‘Open App’  
 
 
## How to run this project locally 
 
To clone this project into Gitpod you will need: 
 
A Github account. Create a Github account  
Use the Chrome browser 
 
Then follow these steps: 
 
Install the Gitpod Browser Extentions for Chrome 
After installation, restart the browser 
Log into Gitpod with your Gitpod account 
Navigate to the Project GitHub repository 
Click the green "Gitpod" button in the top right corner of the repository 
This will trigger a new gitpod workspace to be created from the code in GitHub, where it can be worked on locally 
 
To work on the project code within a local IDE such as VSCode, Pycharm etc: 
 
Go to the link of the Project GitHub repository 
Under the repository name, click "Clone or download" 
In the Clone with HTTPs section, copy the clone URL for the repository 
In your local IDE open the terminal 
Change the current working directory to the location where you want the cloned directory to be made 
Type git clone, and then paste the URL you copied in Step 3 
git clone https://github.com/USERNAME/REPOSITORY 
Press Enter and your local clone will be created 
  

# Testing

![html](https://user-images.githubusercontent.com/36114589/188511829-49db3cc9-018d-403a-9d5f-adcab5bf40f3.png)

 The error above was fixed.
 
 ![css-validaton](https://user-images.githubusercontent.com/36114589/188511876-811e3999-db27-4a12-bc22-a82d9d7b72a1.PNG)

 No errors were found.
 
 Create Post:
 ![create-post](https://user-images.githubusercontent.com/36114589/188511971-e8cdc798-54bb-43aa-911f-7c85d5f26b60.PNG)

 The color contrast issue was fixed
 
 ![image](https://user-images.githubusercontent.com/36114589/188512034-bfb61257-9705-4f7e-9eaa-a3e864624f0c.png)

 No JS errors were found:
 
 ![js-validation](https://user-images.githubusercontent.com/36114589/188512067-23845082-124c-4402-a61c-9d2d1b57f58a.PNG)

 
 
# Credits

## Content 

The text for all the pages of the website was created by me 
 
The text was proof-read/edited by me 
 
 
## Media 
The logo (to be used) used on this site was designed by me 
 
 
## Code 
 
All code on this app/website is my own 
 
 
## Acknowledgements 
 
My inspiration for this website was from my own experience of using Twitter and other social media platforms 
 
My course administrator Jo Bowden, who has helped and supported me throughout the development of this project. Her support has been invaluable! 
 
A special shoutout to my fellow student, Joy Zadan, so glad to have you around for your technical knowledge as well as your daily support. 

Thank you to Laravanth, a neighbour and friend, who borrowed me their laptop when my laptop stopped working in the last 48 hours.
 
 
## Disclaimer 
 
The content of this app is intended for my third project at the Code Institute only 
