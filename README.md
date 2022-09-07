<pre>
  Django Basic Project
</pre>
<pre>
This website allows user who is photographer to uplaod there photos by filling up a form which is displayed on the home page of the website.

This website as functionality of SignUp and SignIn and user can contact us by filling up a form which response is been stored into the database.
SQLite3 Database is been used.

Whenever the photo is uploaded by the user to database we call it as media.
all this images will be in media folder
---------------------------------------------------------------------------------------------------------------------------------------------------
Step 01: To make project called photography we write command into terminal as: django-admin startproject photography
Step 02: To make app called photographer for the project we use command:       python manage.py startapp photographer
Step 03: Set up URL dispatching or pipeline for the peoject.
Step 04: Register the app into setting.py.
As because we are dealing with static files and media (media: the data which is been uplaoded to the database by the user is called media)
so we have to set up the static and medial root. (For url dispatching)
Step 05: Setting up of static and media url and root in setting.py
Step 06: Model design into models.py
Step 07: Registering the models into admin.py
Step 08: after registering the model make migrations by using python manage.py makemigrations command (this command save all the change made to model)
Step 09: after migrations apply all the changes to database tables. By follwing command:- python manage.py migrate
Step 10: Open admin panel and see the changes
</pre>
---------------------------------------------------------------------------------------------------------------------------------------------------
Once the username is choosen that username cannot be used by other user/guest.

Our HOME Page:
You can see two button called "Be Part Of Us Join Us" when we click this we get the signup page
when we click on the button called "contrubite your work" this takes to the upload form from where user can upload his/her images to the database.
![Screenshot (48)](https://user-images.githubusercontent.com/86867746/188710316-6a650c73-47bf-4870-aa69-ea6ca1b7da9d.png)
![Screenshot (55)](https://user-images.githubusercontent.com/86867746/188711347-bcfc932c-7b60-471c-98c8-b926ab583d09.png)
Now this tumbnails are those images which are fetched from the database.
<pre>----------------------------------------------------------------------------------------------------------------------------------------------------</pre>
Our About Page:
![Screenshot (54)](https://user-images.githubusercontent.com/86867746/188711618-ca9ee206-28ba-4cf3-b6db-4d65a9772922.png)

<pre>----------------------------------------------------------------------------------------------------------------------------------------------------</pre>
Our Contact Page:
If user got any queries he/she can fill up the form that will be seen by admin in admin portal when you click on submit button the data goes to database and success meesage is shown below the nav bar.
![Screenshot (49)](https://user-images.githubusercontent.com/86867746/188711987-034f053d-c450-4cd9-8b54-fcd4eeb996c3.png)
![Screenshot (50)](https://user-images.githubusercontent.com/86867746/188869438-2aeccef2-6167-4144-92b3-391e55720e46.png)
<pre>----------------------------------------------------------------------------------------------------------------------------------------------------</pre>
SingUp Page:
TO Add a user: Registration form is been used and the data is stored in the user table which is in built given by the framework, after user account is created the success message is shown in home page refer second screenshot.
![Screenshot (56)](https://user-images.githubusercontent.com/86867746/188712636-effa3ac7-330c-4461-bb60-ebab82afaf0b.png)
![Screenshot (57)](https://user-images.githubusercontent.com/86867746/188712647-9eeac663-17c0-4ee0-945a-5424fbb75fd9.png)

<pre>----------------------------------------------------------------------------------------------------------------------------------------------------</pre>
Our SignIn/Login Page:
Django feature which is authentication it checks for the user has right credentials or not.
If the user or password are wrong it shows a warning message. Below the password section.
When all the credentials are coorect user gets logged in and redirected to the home page showing success message in home page refer second screenshot.
![Screenshot (51)](https://user-images.githubusercontent.com/86867746/188712176-fd6d241f-6338-44e6-baef-544a5cb0cf9f.png)
![Screenshot (52)](https://user-images.githubusercontent.com/86867746/188712914-a46c292f-5ff2-450d-83a8-ba38ce6a4441.png)

When Contact form is filled and submit button is clicked then:
![Screenshot (49)](https://user-images.githubusercontent.com/86867746/188713235-f3897e2e-590b-4415-a98f-6d467b234aed.png)
![Screenshot (50)](https://user-images.githubusercontent.com/86867746/188713257-f7fe15fc-5cd8-4eb0-9de3-8c0490c7a6b1.png)

When the photo is uploded by the user:
![Screenshot (53)](https://user-images.githubusercontent.com/86867746/188714127-742b84ee-2290-486f-9995-561acc558d6c.png)
Admin portal:
![Screenshot (62)](https://user-images.githubusercontent.com/86867746/188872321-71fbde5a-a9ce-4abf-9ca2-b5d3ddab988c.png)
Fetching images from the database: image, description of photo & time and date is fetched and displayed.
![Screenshot (55)](https://user-images.githubusercontent.com/86867746/188872588-16336678-c6d0-4b89-8552-5302a33a7d6e.png)
----------------------------------------------------------------------------------------------------

When user is not logged in or anonymous user vistis to the website it will go to the home page where in nav bar you get an account drop down menu where you can find login button (This login button shows only when the user is not logged in)
![Screenshot (60)](https://user-images.githubusercontent.com/86867746/188871275-7b74ceb6-be7c-43a8-93d4-57786e28b4c0.png)
After login then in the account drop down menu you can see the username who is logged in and the logout button.(logout button and username is shown only when the user is logged in)
![Screenshot (59)](https://user-images.githubusercontent.com/86867746/188871658-e7d3f335-d69f-4bd4-a041-6e885bbcb692.png)
----------------------------------------------------------------------------------------------------
Admin Panel By Django:
To create a super user we use command: python manage.py createsuperuser admin

To create a super user we use command: python manage.py createsuperuser admin
![Screenshot (35)](https://user-images.githubusercontent.com/86867746/188714538-55406e91-1621-4014-9ab7-e49e9119f21b.png)

To create a super user we use command: python manage.py createsuperuser sufiyan
![Screenshot (36)](https://user-images.githubusercontent.com/86867746/188714523-ff4a4c2e-3d3b-4508-94b4-61804b46233c.png)

----------------------------------------------------------------------------------------------------


