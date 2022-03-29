# Pastries to you - Pastry E-commerce
<img src="static/assets/project_images/responsiviness/responsiveness.png" width="100%">

[Live project link](https://my-recipes-ms3.herokuapp.com/all_recipes)

## **Project Introduction**

The scope of this project consists in exercise the knowledge learn up to this point with the [Code Institute](https://codeinstitute.net/all-access-coding-challenge/?utm_term=code%20institute&utm_campaign=a%26c_SEA_IRL_BR_Brand_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=539453915484&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiAvriMBhAuEiwA8Cs5lb4K7BEL5Kg1c8ZXfzdHRSPwEYkb_aMKSzaeFovYBDDbML-RP8UVoBoCyp4QAvD_BwE) -  software development course - and put in practise the conjunction of front end and Backend and also a database, in this case MONGODB, to operate the essential CRUD functionality with a functional app.
 
In this module the focus was to learn Python to work as the main language to manage the backend with the mini framework Flask and the non sequential database MongoDB.

The project idea came from a course suggestion but also a personal wish to provide a simple and functional tool for my wife who works as chef. The project scope allows the user to store her recipes in an organized, safe and accessible way from everywhere. 

Finally this project provided to me some interesting outcomes in my learning process as developer. In this project was possible to learn the fundamentals of [Python](https://www.python.org/), interact with two new frameworks - [Materialize](https://materializecss.com/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) - as it was possible as well to understand how to query and design a non-relational database - [MongoDB](https://www.mongodb.com/) - to operate CRUD operations and have access a secure informations or also manipulate them. Another important aspect was to practise basic notions in how to build a safe login and logout utilizing[Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/).
 
## **Table of Contents**
1. [UX](#ux)
    1. [User Stories](#user-stories)
    1. [Wireframe](#wireframe)
    1. [Database](#database)
1. [Features](#features)
    1. [Existing Features](#existing-features)
    1. [Features Left To Implement](#features-left-to-implement)
1. [Technologies Used](#technologies-used)
1. [Testing](#testing)
    1. [Mannual Tests and Notable Bugs](#mannual-tests-and-notable-bugs)
        - [Empty URL's Picture input form](#empty-url's-picture-input-form)
        - [Defensive Programming](#defensive-programming)
    1. [Responsiveness](#responsiveness)
1. [Deployment](#deployment)
    1. [Creating a Repository and installing Flask](#creating-a-repository-and-installing-flask)
    1. [Connecting MongoDB to your repository](#connecting-mongodb-to-your-repository)
    1. [Deploying to Heroku](#deploying-to-heroku)
    1. [Making a Local Clone](#making-a-local-clone)
1. [Credits](#credits)
    1. [Media](#media)
    1. [Acknowledgements](#acknowledgements)

## **UX**

This project borned from the idea to create a simple but functional tool - online cookbook - to help the user in their regular task to store recipes in a safe place and then have access to that information everywhere. With this in mind the UX was taught to accomplish that in an intuitive way but also keeping some visual appeal.

To help with this goal was chosen for me the Materialize framework to keep the constancy of the material design at some point that keeps the things simple and very intuitive. Materialize provides a big range of components, helpers and a good bunch of colors pre-formatat which possiblitated me to concentrate more in the functionality of the app but balancing that with good user experience.

It is important to mention the research done to understand which kind of existing website could help to understand more about the necessities of the user in this area. One website that worked as a reference was the [Jamie Oliver](https://www.jamieoliver.com/). This website sounded like a good answer for the users interested in getting an online recipe. What was noted about that was that the website uses cards with images and has a direct communication about recipe’s information which was understood by me as a good reference thinking about user experience. Normally people interested in online recipes are interested in something quick, where with a few glances at the page they will have all the information needed. For example, how much time, which ingredientes I will need and how to prepare?

<p align="center">
<img src="static/assets/project_images/references/jamie_oliver.png" width="80%">
</p>

Embeded with this concept and the user stories was possible to formulate the framework.

### **User Stories**

#### **External user’s goal**
Have their own access to a tool which would possibilitate store their own recipes in a simple, secure and intuitive manner. Also have access to the recipes everywhere they are and or whethever devices.

#### **Site owner's goal**
Initially offer satisfactory usability of the web application to allow users to keep using the tools and learning the process like a beta test. Later, collect user experience and feedback to improve functionality and eventually create a subscription service.

### **Wireframe**

As a result of the above, the concept of the website was idealised taking in consideration some research and the user stories. The wireframe was design to deliver all the functions needed to create, read, update and delete the recipes (CRUD actions) but also guaranteeing a basic secure functions just allowing the right user to have access to some of that functions as UPDATE and DELETE, but allowing access to read and create their own recipes.

The initial wireframe consist in: 

1. Navbar with the following options - All Recipes, Profile, Add Recipes, Log in, Log out and Register. Depending on the user in session or not some options will be shown or not.
2. Sidebar with the following options - All Recipes, Profile, Add Recipes, Log in, Log out and Register. Depending on the user in session or not some options will be shown or not.
3. All Recipes home pages consist of a search bar and the all cards that function as quick viewers to the recipes available to everyone. In each card there is a button to access the complete information of the recipe.
4. Each recipe page has an image, general commentary, list of ingredients, method or preparation, time estimated, food tag and who created that recipe. 
5. Add recipe consist of the same information provided in the recipe page but in format of a form to be filled and storaged, plus two buttons cancel and add to action that function.
6. Edit recipe brings all the data filled in the add page with the possibility to edit them and action this function with the addition of three buttons cancel, delete and update.
7. Register page is a form simple page to fill with the credentials to have full access to the functionalities of the website. The inputs necessary are username, password and confirm password. This option was posterior alterated along the developing process to firstname, username, password and confirm password.
8. Login page is a form to allow access and check the users credentials as username and password.
9. User profile is a page to redirect the user after the correct log in where the user has all recipes created by them in one unique space. Over this page they have the possibility to access the full recipe after selecting the recipe quick view card.

See in details clicking on this [Desktop Version](static/assets/project_images/wireframes/original_wireframes/desktop.png)
<p align="center">
<img src="static/assets/project_images/wireframes/wireframes_img/desktop.png" width="90%" height="auto">
</p>

See in details clicking on this [Tablet Version](static/assets/project_images/wireframes/original_wireframes/tablet.png)
<p align="center">
<img src="static/assets/project_images/wireframes/wireframes_img/tablet.png" width="90%" height="auto">
</p>

See in details clicking on this [Mobile Version](static/assets/project_images/wireframes/original_wireframes/mobile.png)
<p align="center">
<img src="static/assets/project_images/wireframes/wireframes_img/mobile.png" width="90%" height="auto">
</p>

## Database

The database chose for this project was the MongoDB for all well non capabilites of this resource and for fit the project requirements.

The desing or Schema was defined as bellow:

- **Database and Collections name**
```
my_recipes
    food_tags
    recipes
    users
```
### Collections

- **food_tags**
```
{
    "_id":{"ObjectId":""},
    "food_type":"Tea Treatments"
}
```
- **recipes**
```
{
    "_id":{"ObjectId":""},
    "recipe_name":"string",
    "food_type":"string",
    "estimated_time":"string",
    "url_picture":"",
    "commentary":"string",
    "ingredients_list":[Array],
    "method":[Array],
    "created_by":"string",
    "user_id":{"ObjectId":""}
}
```

- **users**
```
{
    "_id":{"ObjectId":""},
    "firstname":"string",
    "username":"string",
    "password":"werkzeug_salted_harsh"
}
```

## **Features**

The initial design suffered some fewers changes to accommodate better user experience and the overall functionality of the app. Below are all the actual functionalities that were possible to implement and those which were not possible to do it.
 
1. Navbar & Sidebar for general navigation;

2. All Recipes page - Search function, recipe quick view cards with a button to access the full recipe;

3. Individual recipe page - full visualization of the recipe, for users correct logged in and owner of the recipes Delete and Update function; 
    
4. Profile's page - Welcome message and user's own recipe quick view cards with a button to access the full recipe;

5. Add recipe page - an empty form with all the inputs to add a new recipe and one buttons to action the data insertion;

6. Edit recipe page - a filled form with with recipe’s information with two buttons cancel and update;

7. Log in page - simple form to check the user's credential username and password;

8. Log out page - a navbar link responsabile for end an user session;

9. Register page - a form to collect initial and register the initial user credentials.
    
### **Existing Features**
Below will be possible to take a look in some of the important features of this project.

#### **Base html and Extended usage**

The first important feature but one that figures just behind the scenes is the advent of [Jinja-extension](https://jinja.palletsprojects.com/en/3.0.x/templates/?highlight=extend#template-file-extension) which allows a very interesting possibility to create one base html file and then extend its use to all other html templates necessary through the project. This makes easier to implement any update in the html files.

This resource was greatly utilised during the development of this project.

It is possible to block the content you intend to not extend by following the above:

```
<main class="container">
    {% block content%}

    {% endblock %}
</main>

```

Then at the top of each new html file it is necessary to extend the base html:

```
{% extends "base.html" %}
{% block content %}
```

#### **Navbar & Sidebar**

- The **Navbar** & **Sidebar** were implemented on this project to complete their functional task to be the main form of navigation through all the possibilities offered by the website. They were designed by Materialize Framework and edited in the visual to match the identity of this project. This feature allows the user to reach links for All Recipes, Profile, Add Recipes, Log in, Log out and Register.

    - If there is no user logged in the navbar will show **All Recipes**, **Log in** and **Register** links.

    - If instead there is an user logged in the links shown will be **All Recipes**, **Add Recipes**, **Profile** and **Log out**.

    This personalised usage in accordance with an user logged or not was possible by an implementation with [Jinja-Template](https://jinja.palletsprojects.com/en/3.0.x/) which empowers the html with logic to check session user a [Flask](https://flask.palletsprojects.com/en/2.0.x/) recourse which allows archiving some information through cookies as the username of the user in question.

    ```
    {% if session.user %}
        <li><a href="{{ url_for('profile', username=session['user']) }}">Profile</a></li>
        <li><a href="{{ url_for('add_recipe') }}">Add Recipe</a></li>
    {% else %}
        <li><a href="{{ url_for('login') }}">Log in</a></li>
    {% endif %}
    {% if session.user %}
        <li><a href="{{ url_for('logout') }}">Log out</a></li>
    {% else %}
        <li><a href="{{ url_for('register') }}">Register</a></li>
    {% endif %}
    ````

#### **All Recipes page** 
 In the first place there is a search bar which will look for recipe name or tag name. It is necessary to use the buttons to complete an action such as for finding a recipe pressing the search button or clearing the result bringing back the regular recipes.

These feature was possible thanks to the use of [MongoDB indexes](https://docs.mongodb.com/manual/indexes/) that was created based in the collection recipes but more specifically with the document recipe_name and food_type. 

 ```
recipe_name_text_food_type_text
 ```

 Here it is possible to understand the logic to request the information for mongoDB and then bring the result.
 ```
 <!-- Request the value in the search bar and then replace in the syntax to search in mongodb -->
def search():
    query = request.form.get("query")
    recipes = mongo.db.recipes.find({"$text": {"$search": query}})
    food_tags = mongo.db.food_tags.find().sort("food_type", 1)
 ```

The cards utilized to show the basic information come from [Materialize](https://materializecss.com/cards.html) and they were stylised to being in consonance with the general UX idea. The idealisation of the cards was to summarise the main recipe information in a visual manner. Following this guidance the cards showed the time estimated, name, picture of the recipe, food tag or classification and a link for the full recipe.

#### **Profile's page**
This is the page where the user is redirected everytime it is log in with theirs credentials and where they can have access as a specie of a shortcut of all their own recipes making easier to, read, edit or delete any of them.
 

### **Features Left to Implement**
- What was not possible to implement due to a lack of time was a favourite option in which the user would have the possibility to hit a btn to favourite that recipe which would order those fav recipes in first place on the profile page.
- Another feature not possible to implement was the option to input an youtube recipe url and attach this to the recipe itelses utilizing an iframe the google solution to embedded video from the platform in the website.

## **Technologies Used**

All the Technologies utilised to built this web app can be found bellow with the respective links.

### **Languages**
- [HTML](https://en.wikipedia.org/wiki/HTML) to build the whole structure of the landing page.
- [CSS](https://en.wikipedia.org/wiki/CSS) to style the webiste.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript), more specifically [Jquery](https://jquery.com/) was use it to personalize some materialize components.
- [Python](https://www.python.org/) to build majority of the backend instructions on app.py file.

### **Frameworks and others**

- [Gitpod](https://www.gitpod.io/) as the code editor.
- [Materialize](https://materializecss.com/) for all the core HTML sctrucutes as for buttons, navbar, grid system and helpers to deal with less unique CSS rules and more pre built solutions.
- [Jinja-Template](https://jinja.palletsprojects.com/en/3.0.x/) was utilized in this project as placeholders in the template allowing writing similar Python code on html files to finally render the final document.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) was used in conjunction with Python to build the functional banckend logic of the web app.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) responsabile for harsh the password in secure form to be stored.
- [MongoDB](https://www.mongodb.com/) is the database for this project where the documents created by user are store as for example the recipes, the user information and food tags.
- [Git](https://git-scm.com/) was used as tool to control the version of the project.
- [Git Hub](https://github.com/) to store the project with versionament control
- [Heroku](https://pages.github.com/) to deploy the live project.
- [Balsamiq](https://balsamiq.com/) to wireframe the ideia of the website.
- [Am I responsive](http://ami.responsivedesign.is/#) to help visualize the webiste in different screens sizes and get a print of it.


## **Testing**

The automated test utilised were [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) to test general performance, [W3C Markup](https://validator.w3.org/nu/) validation service for the find any inconsistency in the HTML and  [W3C Jigsaw CSS](https://jigsaw.w3.org/css-validator/#validate_by_input) validation service for CSS and [Jshin](https://jshint.com/) for JavaScript.

All the possible erros founded by W3C validators were corrected less those ones being part of bootstrap Frameworks. The same can be said by the Jshin valitadion where there were no errors being displayed.

All the results can be seeing below.

Google Lighthouse results:
<p align="center">
<img src="static/assets/tests/lighthouse/lighthouse.png" width="90%" height="auto">
</p>

W3C Markup of all html templates. They were tested and got the same results:
<p align="center">
<img src="static/assets/tests/html_validation/home.png" width="90%" height="auto">
</p>

W3C Jigsaw CSS for style.css results:
<p align="center">
<img src="static/assets/tests/css_validation/CSS.png" width="90%" height="auto">
</p>

The only Javascript utilised in this project was to activate the Materialize components but with Jquery for that reason there is no checker result.

PEP8 Online result before correction for app.py
<p align="center">
<img src="static/assets/tests/pep8_validation/before.png" width="90%" height="auto">
</p>

PEP8 Online result after correction for app.py
<p align="center">
<img src="static/assets/tests/pep8_validation/after.png" width="90%" height="auto">
</p>

### **Mannual Tests and Notable Bugs**
The website was manually tested to check if it was working properly in all functionalities. Many attempts to run the app were executed and I can confirm in all the best of my capabilities it is working as initially was intended. All redirections, check of password, the CRUD operations, all links logged in or logged out and a big learning process with defensive programming. Above are some importants outcomes coming from those tests and meeting with my mentor that shows some important isssues that should be to tackle. 

#### **Empty URL's Picture input form**
One noticed issue is related to the URL's Picture input that is not a requirement for filling the form due to turning this experience to fill the form a little bit friendly. However, allowing the image card without an image would bring that aspect of the card empty, breaking the regular format of this Materialize component. The solution implemented was via backend through a if statement which will check the front end if that input was empty and then completing that input with a standard image. 

As it is possile to see in the add_recipe function was added two variable. One wite regular reques.form.get and other with the valueo of the standard Picture URL.
```
url_picture = request.form.get('url_picture')
url_replace = ('https://i.pinimg.com/originals/'
                'd9/55/5f/d9555f88a53f6c19ef8acbb2bd679511.jpg')
```

With that was done a simple check if that field was empty or not:
```
if url_picture:
    recipe = {
                    "recipe_name": request.form.get('recipe_name'),
                    "food_type": request.form.get('food_type'),
                    "estimated_time": request.form.get('estimated_time'),
                    "url_picture": url_picture,
                    "commentary": request.form.get('commentary'),
                    "ingredients_list": ingredients_list,
                    "method": method,
                    "created_by": session['user'],
                    "user_id": ObjectId(user['_id'])
                }
```

Or if it is false I would insert in the database the all the same structure above but replacing url_picutre key value for this:
```
"url_picture": url_replace,
```

This solutioned the issue preserving overall good visual for those cards. 

#### **Defensive Programming**

This was something really important brought from my mentor in the meetings. This is understandably an important aspect of this project because it brought light to the security aspect of the data being stored in the database by taking care of the url route and information passed through it. So in that way a two layer of security was implemented to preserve or avoid that someone could understand the route for example "delete_recipe/recipe" and or even edit the recipe without being initially authorized to do that.

The two layers implemented were first about checking if there is a user session logged and that solution was possible thanks to Flask. The second layer of protection is related to the check between the user_id logged and the user_id storaged in the recipe collection. This second form of protections works assuring the same user that is trying to delete or update or even getting access to user Profile will be redirected avoiding anyone with the right route and information to have access in something that they would not be allowed to do so.

So the logic created to implement this was as below:
```
if "user" in session:
        user = mongo.db.users.find_one({"username": session['user']})
        user_id = ObjectId(user['_id'])
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        recipe_user_id = ObjectId(recipe['user_id'])

        if user_id == recipe_user_id:
```

And for the user profile page a check was implemented to just grab a user logged to change his username for another username. The logic created check if the user session is equal to the user passed through the route:
```
def profile(username):
    if "user" in session:

        if session['user'] == username:
```

In all the cases above the user is redirected to the login page or to no_authorized page receive a flash message and a link to get back the all recipes page.

### **Responsiveness**

This project was developed to work in a diverse range of screens. All the components from Materialize and it’s Grid system are responsive and were added to them with personalized CSS to improve their capabilities in delivering a better UX and achieve satisfactory usage. With big screens more information will be shown in more comfortable form by the website having enough responsiveness to scale in small screens.

As explained this project will work fine in at least 3 different sizes Desktop,Tablet and mobile. To achieve this the website has been tested on several possible devices, from 11 "or 13" inch Macs, Google Chrome developer tools, variable Android phones of friends and relatives.

## **Deployment**

To deploy this project I utilised some of the mentioned technologies above to facilitate this process. This project was deployed on Heroku and connected with MongoDB.

### **Creating a Repository and installing Flask**

1. The first step were created a repository on GitHub with the name **my-recipes-milestone-3**
2. Installed the **Gitpod** extension for **Google Chrome**;
3. Linked **Gitpod** gaving **access** to my **GitHub profile** with my login and password;
4. After that all repositories started to showed the **Gitpod button** just next to the button Code.
5. Clicking in the **Gitpod button** you have access to the code editor linked with this repository.
6. On your recent workspace created in the terminal now it is possible to install Flask. It is necessary to input the following command pip3 Install Flask.
7. You will need to install PyMongo by using the command pip3 install flask-pymongo.
8. And also install dnspython with the command pip3 install dnspython in the terminal.
9. The next step is to create a file called requirements.txt in our root folder. The command in the terminal for that is touch requirements.txt.

### **Connecting MongoDB to your repository** 
1. First you need to create a free account with [MongoDB](https://www.mongodb.com/).
2. Once created it will be possible to create a new cluster where the database will be seated.
3. In our new cluster we then are allowed to create a database by clicking on the button create a new database.
4. With that and taking in consideration the Schema above it is possible to create all the collections clicking in the button create collection.
5. After this the next step is crucial, that is get back to the gitpod code editor to create a env.py file where sensitive information will be stored and create a secure connection with the database.
6. Create a file in the root of the project called env.py and then input those information below but replacing the key values for "SECRET_KEY", "MONGO_URI" and "MONGO_DBNAME " for their respective information.
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", ", any secure secret key)
os.environ.setdefault("MONGO_URI", link provided by Mongo DB in accordance with your database and collections information)
os.environ.setdefault("MONGO_DBNAME ", name of you database)
```
7. It will be necessary as well to create .gitignore file or utilising an already one created and list the env.py inside of this file:
```
env.py
```
8. The MONGO_URI you can get by accessing your cluster and then clicking on the connect button.
9. After that you will see an option called "connect your application".
10. In this case select Python and then copy that link and paste as a key valeu for MONGO_URI and replace **password** and **myFirstDatabase** for your Mongo database password and database name in env.py.
11. Do not forget to make the same with the respective values for "SECRET_KEY" and "MONGO_DBNAME".
12. Lastly import the following with an if statement on top of your app.py:
```
import os
if os.path.exists("env.py"):
    import env
```

### **Deploying to Heroku**

1. The next step is to deploy the project for Heroku.
2. First get back to your gitpod workspace or code editor.
3. To make sure, first save the necessary requirements in the requirements.txt through the command pip3 freeze --local > requirements.txt 
4. Create a procfile with the command 'echo web: python app.py > Procfile' without quotes.
5. Commit those changes to your repository, using git -A, then git commit -m"" and your message and finally git push.
6. Create a Heroku account.
7. On your dashboard you can create a new app hitting new and then create a new app.
8. Choose an app name with dashes -.
9. Choose a region in this case it was Europe.
10. To connect the app with Heroku I chose the option connect with Github.
11. Select the repository name of your project, in my case my-recipes-milestone-3.
12. Go to settings and in the button reveal config Vars.
13. Now the values to be filled will need to match with the values stored in env.py.
```
("IP", "0.0.0.0")
("PORT", "5000")
("SECRET_KEY", ", any secure secret key)
("MONGO_URI", link provided by Mongo DB in accordance with your database and collections information)
("MONGO_DBNAME ", name of you database)
```
14. In the repository and in app.py it it necessary to use this structure to connect finalise the connection with MonogDB, for that it is necessary to pass the informations from to env.py to app.py in a secure form as this:
```
<!-- All the imports necessary  -->
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

<!-- Instances necessary for the connection  -->

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)
```
15. Go back to Heroku and click Enable Automatic deployment, keep the main branch selected and then click in deploy and wait until it finalises the process.
It is done.


### **Making a Local Clone**

1. Log in to your [GitHub](https://github.com/), locate the repository [pedromn0/my-recipes-milestone-3](https://github.com/pedromn0/my-recipes-milestone-3).
2. Inside the repository locate the button Code and then click on "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. In your terminal open Git Bash.
5. Then you can change the current working directory to a directory that suits you in your computer.
6. Type `git clone`, and then paste the URL you copied earlier.


## **Credits**

All images utilised to fill some recipes were taken from the same source the [Jamie Oliver](https://www.jamieoliver.com/) website as the content of the recipes as well.

A significant part of the main structure code has been written following [Code institute task manager - mini project](https://learn.codeinstitute.net/)

A variety of components of this Project came from [Materialize](https://materializecss.com/) as Moodal, Grid sytem, image-cards, pallet of colours, Navbar and SideNav, Footeres, Forms and also some CSS helpers and styles.

Code instiute Slack channel was utilised as a referece to solve one bug related to how to correct populate a textarea html tag coming from my MongoDB and a collection which is stores data as an array. The ideia is keep each array index as a line inside textarea html tag.

```
<textarea placeholder="One item per line;" id="ingredients_list" name="ingredients_list" class="materialize-textarea">

<!-- This if but not the for loop -->
{%- if recipe != "NEW" -%} 
    {%- for ingredient in recipe.ingredients_list -%} 
        {{ ingredient }} &#13;&#10;
    {%- endfor -%}
{%- endif -%}</textarea>
```
The solution for login and log out was implemented utilising the same idea from the mini project which lays on [werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) to safally store the users credentials.

### **Media**

- Only one image has a different source, this pciture was utilised as an standard picture in case the user do not paste any Picture URL in the add recipe form. This is the [reference](https://www.pinterest.ie/pin/846395323697472657/) for that image as a source being Pinterest.

<p align="center">
<img src="https://i.pinimg.com/originals/d9/55/5f/d9555f88a53f6c19ef8acbb2bd679511.jpg" width="40%" height="auto">
</p>

- [FontAwesome](https://fontawesome.com/) was utilised for all small icons to enhance the visual of the webiste. 

- The Pokeball image utilised called [pokeLogo](https://www.pikpng.com/pngvi/xxRxTm_brik-pixel-art-pokemon-pokeball-clipart/) in the project came from this website https://www.pikpng.com/

### **Acknowledgements**

- It is important to note the support from my mentor Chris Quin which helped me since the beginning guiding my ideas as instruct me through some difficulties steps to implement this project.