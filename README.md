# <h1 align="center">TWISTER</h1>

<img width="905" alt="Screenshot 2022-09-05 at 20 36 22" src="https://user-images.githubusercontent.com/36114589/188505848-0e0b41b3-58b4-4ef3-9b7f-8b0dec1d61ed.png">

Twister is a social media platform, similar to Twitter, specifically to connect businesses with their end users. Business owners and consumers can register for a free account, share, manage, re-post other users post (twist and re-twist!), as well as creating and managing their own social profile online. The focus being to create a focussed and transparent conversation/link between business-to-business owners, business-to-consumers and consumers-to-consumers. 

[Link to the deployed project](https://twister3-ms3.herokuapp.com/)

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

• Be able to comment on conversation threats 

• Be able to join communities/group that I am interested in 

• Be able to follow other users/business profiles/groups/posts 

• Be forewarned on any activity that I am about to do on the app, such as deleting posts, or re-posting images etc.  

• Have my own member user dashboard (read functionality) 

• Registered User Goals (Businesses) 

• Have all the features available to Consumers 

• Have a business login/registration page 

• Have the ability to set up a profile with business information/links to business website  

• Be able to get verified business status  

• Have a business dashboard with the relevant analytical features useful for marketing 

## Design

* Colour Scheme
* Typography
* Imagery
* Wireframes
* Database Structure

## Features

* General Features of Each Page
* Future Implementations
* Accessibility

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

• SQLAlchemy –  

• gunicorn –  this is a Python Web Server Gateway Interface HTTP server. It allows the site to run any Python application concurrently by running multiple Python processes within a single dyno

• Balsamiq - balsamiq was used to create the wireframes for this project 

• Git - Git was used for version control and saving work in the repository 

• Gitpod – Gitpod was used as the IDE to develop and code this website 

• GitHub – used to host the site 

• Heroku – where the live site is deployed 

• Chrome - was used as the default testing browser 

## Deployment & Local Development

* Deployment
* Local Development
* How to Fork
* How to Clone

# Testing

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
