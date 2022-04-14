# Pastries to you - Pastry E-commerce
<img src="media/appCompleted.png" width="100%">

[Live project link](https://pastries-to-you.herokuapp.com/)

## **Project Introduction**

The scope of this project consists in practicing the knowledge learned up to this point with the [Code Institute](https://codeinstitute.net/all-access-coding-challenge/?utm_term=code%20institute&utm_campaign=a%26c_SEA_IRL_BR_Brand_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=539453915484&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=CjwKCAiAvriMBhAuEiwA8Cs5lb4K7BEL5Kg1c8ZXfzdHRSPwEYkb_aMKSzaeFovYBDDbML-RP8UVoBoCyp4QAvD_BwE) -  software development course - and make a project based on the last section of the course dedicated to use of Django in conjunction with the frontend and Backend and also a database. This project is the final outcome from the whole Knowledge accrued during the course.

The project idea came from a course suggestion but also a personal wish to learn how to build a functional e-commerce that could be the base for a future adventure to undertake a business with my wife. The project scope allows the user to store her recipes in an organized, safe and accessible way from everywhere.

This project provided to me some new interesting outcomes in my journey to become a better developer. In this project was possible to practice more of of [Python](https://www.python.org/), HTML, CSS, but mostly with [Django](https://www.djangoproject.com/) and some of the immense possibilities this framework offers. Another important aspect was to integrate a simple version of [Stripe payments](https://stripe.com/ie?utm_campaign=paid_brand-IE_en_Search_Brand_Stripe-1615558792&utm_medium=cpc&utm_source=google&ad_content=307359047676&utm_term=kwd-295607662702&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=CjwKCAjw6dmSBhBkEiwA_W-EoAMF3BDf4uNrMboFU7yCyWHTi7ndFuxxH7xc-y-oj6llv6nJ6SJaHBoCHisQAvD_BwE) in the website utilizing webhooks as well.

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

The concept of this project borned from the idea to accomplish the client, shop user and owner. The scope was thought to be functional implementing all the basic core functionalities of an e-commerce. This design from this project combines the Boutique Ado, a project from code institute, keeping the main sctruture but implementing some visual and functional aspects to match with the store idea.

Embeded with this concept and the user stories was possible to formulate the framework.

### **User Stories**

#### **Client goals**

- As a client, I want to be able to view a list of products, so that I can select some of them to purchase.

- As a client, I want to be able to view each product's details, so that I can check the price, description, ingredients, image, how much unity is included, category, allergens and if it is sweet or savory.

- As a client, I want to view the grand total of my purchases at any time so that I can check how much I am spending.

- As a client, I want to be able to sort through the list of products, so that I can identify the best different categories, priced or by sweet or savory.

- As a client, I want to be able to sort a specific product category, so that I can find the best price in each specific category and/or sort the category by name.

- As a client, I want to be able to search for a product by name and/or description, so that I can find a specific product I want to purchase.

- As a client, I want to be able to select the amount of the product I am buying.

- As a client, I want to be able to easily select the quantity of a product when purchasing it.

- As a client, I want to be able to view items in my basket to be purchased, so that I can check the total cost of my items and make sure which Items I will receive or collect.

- As a client, I want to be able to adjust the amount of individual items in my basket, so that I can easily make changes before the checkout.

- As a client, I want to be able to easily enter my payment information, so that I can check out without any problems.

- As a client, I want to be able to make sure my private payment information is safe and secure, so that I can confidently provide the needed information.

- As a client, I want to be able to view an order confirmation after the checkout, so that I can verify I haven't made any mistakes.

- As a client, I want to be able to receive a confirmation by e-mail after the checkout, so that I can keep registered the order Information for any eventuality.


#### **Shop user goal**
- As a shop user, I want to be able to easily register my account so that I can have a personal account and be able to check my profile.

- As a shop user, I want to be able to easily log in and out, so that I can access my personal information.

- As a shop user, I want to be able to reset my password, so that I can recover access to my account.

- As a shop user, I want to be able to have a personalized user profile, so that I can check my personal order history and the number of fidelity points accrued at the moment.

#### **Site owner's goal**
- As a shop owner, I want to be able to add a product, so that I can add new items to my shop.

- As a shop owner, I want to be able to edit and update the product, so that I can change product prices, amounts, images and more.

- As a shop owner, I want to be able to delete a product, so that I can remove items that are no longer for sale.

- As a shop owner, I want to be able to make sure that only I can add/edit/delete items from my shop. I want to make sure that anyone else can make changes to my products.

- As a shop owner, I want to have the possibility to communicate with my customers through a blog where I will be able to see customer’s commentaries creating a small community.


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

See in details clicking on this [Desktop Version](media/Desktop.png)
<p align="center">
<img src="media/Desktop.png" width="90%" height="auto">
</p>

See in details clicking on this [Mobile Version](media/Mobile.png)
<p align="center">
<img src="media/Mobile.png" width="90%" height="auto">
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
- [Bootstrap](https://getbootstrap.com/) was utilized in this project as the base for styling the webpage as some components which produce the final form of this project.
- [Django](https://www.djangoproject.com/) was used in conjunction with Python to build the functional banckend logic of the web app and also allow the use of built in components which accelerates the development process.
- [Stripe](https://stripe.com/) responsabile to offer an payment processor solution that was integrated within this project.
- [SQLite](https://sqlite.org/index.html) was used in the development process as builtin django solution.
- [Heroku Postgres](https://www.heroku.com/postgres) was after deployment to Heroku migrating from SQLite.
- [Git](https://git-scm.com/) was used as tool to control the version of the project.
- [Git Hub](https://github.com/) to store the project with versionament control
- [Heroku](https://pages.github.com/) to deploy the live project.
- [AmazonAWS - S3](https://aws.amazon.com/) to deploy all static files and media files.
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

### **Amazon webservice S3 and IAM**
1. First it is needed to create an account at aws.amazon.com
2. After complete this process open search for the S3 application and then create S3 bucket named - it is recommended to use the same name of your heroku app to facilitate 
3. In the section to create the bucket uncheck all options "Block All Public access setting"
4. Also in this section select ACLs enabled and keep bucket owner preferred
5. Following the next step go to the properties section, find the "Static Website Hosting" section and click to edit it
6. Set the index.html and the error.html values because in this case they will not be used.
7. Go to permission and click in edit on the CORS configuration and then set this configuration
```
[
{
"AllowedHeaders": [
"Authorization"
],
"AllowedMethods": [
"GET"
],
"AllowedOrigins": [
"*"
],
"ExposeHeaders": []
}
]
```
8. Still in the permissions section and then click to edit the bucket policy and generate and set configuration or similar
```
{
    "Version": "",
    "Id": "Policy…",
    "Statement": [
        {
            "Sid": "Stmt…",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-app/*"
        }
    ]
}

```
8. In the same section click edit on the Access control list(ACL)
9. Select the read access for the Bucket ACL to Public Access
10. This concludes the bucket creation
11. Search in the app or services for IAM application and then select it
12. Click in new user group and then name it - recommendation is keep the same name for the heroku app
13. Select "AmazonS3FullAccess" policy permission for our new user group created
14. Follow to "policies" and then click in "create new policy"
15. After that "import managed policy" and select the previous selected "AmazonS3FullAccess" and then click on 'import'.
16. You will see a JSON editor to be updated with the policy "resource" to the following
```
Resource": [
"arn:aws:s3:::your-heroku-app"
"arn:aws:s3:::your-heroku-app/*"
]
```
17. Then give the policy a name and click "create policy"
18. Attach the the new policy to the user group
19. Follow to users and create a new one
20. Include this user to for the user your user group
21. In the process select "programmatic access" for the access type
22. After that Amazon will create your access or secret keys. Take note of them, AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID. Those will be used as Heroku config variables to deploy the project.
23. In settings.py it is necessary to implement the following logic: 
```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your-heroku-and-amazon-app-name'
    AWS_S3_REGION_NAME = 'your-heroku-region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
24. These settings will establish the necessary connections between the heroku config variable.


### **Deploying to Heroku**

1. Create or login in your heroku account through heroku.com
2. After logging in, create an app and select a region most close to you
3.Install dj_database_url using the CLI with the pip3 install command
4. Install psycopg2 using the CLI with the pip3 install command
5. Import dj_database_url to your settings.py file
6. Search for postgres in Heroku and add a Postgres, free version, database
7. After setting the Postgres in your heroku app, copy the key in the config variable called DATABASE_URL and its respective key.
8. After that copy DATABASE_URL's value(Postrgres database URL) from  config variables and temporarily paste it into the default database in settings.py.
Comment temporarily the current database settings code and paste the this to make effect:
```bash 
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres key/url here>")     
    }
  ```
9. Install gunicorn using the CLI with the pip3 install command
1o. Run the command pip3 freeze > requirements.txt for both dj_database_url, psycopg2 and gunicorn being kept for the requirements.txt file
11. After that create a Procfile with the text: web: gunicorn your-heroku-app-name-wsgi:application 
12. Make sure the settings.py Databases is settled to connect with Heroku postgres database as described in the step 8.
13. Make sure the debug is set to false in the settings.py file
14. Add in settings.py:
```
ALLOWED_HOSTS = ['your-heroku-app.herokuapp.com', 'localhost']
```
15. Back to CLI run "python3 manage.py showmigrations" to check the status of the migrations. At this point all migrations will be needed again to the new Databases Postgres
16. Command "python3 manage.py migrate"
17. Command "python3 manage.py createsuperuser" to create a super/admin user to have access to Django admin
18. If you are using fixtures to populate your database now it is the right time to do it. Command "python3 manage.py loaddata products.json" for products fixtures
19. Repeat the same process for your categories fixtures or any other needed it
20. In the CLI login to Heroku through the command heroku login -i and the insert your password and user
21. Now it is necessary to disable collectstatic in Heroku prior to any code being pushed. Command “heroku config:set DISABLE_COLLECTSTATIC=1”
22. After the success from the last operations it is possible to command “git push heroku main” to push the code to Heroku
23. Make sure all the config variables are set in Heroku:

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<unique aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<unique aws secret access key>`  |
| DATABASE_URL| `<unique postgres database url>`  |
| EMAIL_HOST_PASS | `<unique email password(by Gmail)>` |
| EMAIL_HOST_USER| `<store email>`  |
| SECRET_KEY | `<unique secret key>`  |
| STRIPE_PUBLIC_KEY| `<unique stripe public key>`  |
| STRIPE_SECRET_KEY| `<unique stripe secret key>`  |
| STRIPE_WH_SECRET| `<unique stripe wh key>`  |
| USE_AWS | `True`  |

24. After that it is possible to connect you app with GitHub, and enabling the automatic deployment from main
25. After push your code to Heroku will be possible to click on the link provided to have access to you deployed application



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

Below it is all image and respective reference used in this project: 

1) File_Name: croissant
[link](https://unsplash.com/photos/sqkXyyj4WdE)
Photo by Conor Brown on Unsplash

2) File_Name: Amont croissant
[link](https://cnz.to/wp-content/uploads/2006/03/almond_croissants-2.jpg)


3) File_Name: strawberry_cake
[link](https://unsplash.com/photos/cZFU60dKB6U)
Photo by amirali mirhashemian on Unsplash

4) File_Name: choco_cake
[link](https://unsplash.com/photos/kPxsqUGneXQ)§
Photo by David Holifield on Unsplash


5) File_Name: sourdough_bread
[link](https://unsplash.com/photos/rYOqbTcGp1c)
Photo by Jude Infantini on Unsplash

6) File_Name: sweet_bread
[link](https://unsplash.com/photos/tihN043cDTQ)
Photo by Markus Winkler on Unsplash


7) File_Name: fruit_scone
[link](https://unsplash.com/photos/Kgcc8TKKEkg)
Photo by Sarah Kilian on Unsplash

8) File_Name: plane_scone
[link](https://unsplash.com/photos/WCaegqiEOCo)
Photo by Ryu Orn on Unsplash


9) File_Name: cinamon_roll
[link](https://unsplash.com/photos/MfdmKZDPAXM)
Photo by David Köhler on Unsplash

10) File_Name: almond_puff
[link](https://unsplash.com/photos/GpZGDhP5WCI)
Photo by Zach Reyes on Unsplash


11) File_Name: jam_cookie
[link](https://unsplash.com/photos/cOw_JxasssM)
Photo by amirali mirhashemian on Unsplash

12) File_Name: choco_cookie
[link](https://unsplash.com/photos/Imwgit84NGo)
Photo by Grayson Smith on Unsplash


13) File_Name: lemon_tart
[link](https://unsplash.com/photos/E8eJdYTTkMU)
Photo by Konstantinas Ladauskas on Unsplash

14) File_Name: strawberry_tart
[link](https://unsplash.com/photos/WJwHXjLjkRc)
Photo by Lili Cortez on Unsplash


15) File_Name: Brownie
[link](https://unsplash.com/photos/uG1jwfpCRhg)
Photo by Ella Olsson on Unsplash

16) File_Name: Macaroons
[link](https://unsplash.com/photos/tejecyNUUhs)
Photo by Serghei Savchiuc on Unsplash

17) Fila_Name: home_background
[link](https://unsplash.com/) the exact reference was not found but the images comes from this free website.

- [FontAwesome](https://fontawesome.com/) was utilised for all small icons to enhance the visual of the webiste. 
- [Google Fonts](https://fonts.google.com/specimen/Roboto+Serif?category=Serif&query=roboto#standard-styles) was utilised as the pincipal source of font.
- [Post-1 in the Blog](https://donalskehan.com/recipes/howth-head-seafood-chowder-2/) a snippet of the text was taken from here.
- [Post-2 in the Blog](https://www.chefspencil.com/16-most-popular-tasty-irish-cheeses/) a snippet of the text was taken from here.


### **Acknowledgements**

- It is important to note the support from my mentor Chris Quin which helped me since the beginning guiding my ideas as instruct me through some difficulties steps to implement this project.