# Winter Table

This website was created to fix the hassle of last minute planning for a christmas table and new year table.
Project failed as imagination was greater then provided book(module) could offer ,which only offered basic database managment.
When asking for help was denied stating its self learning course.

![Responsiveness]()

## Demo

A live demo of the site can be found  [here](https://winter-table.herokuapp.com/)

## Table of contents

- [User Stories](#User-Stories)
  - [Design](#Design)
  - [Features](#Features)
- [Technologies Used](#Technologies-Used)
  - [Languages](#Languages)
  - [Programs](#Programs)
- [Testing](#Testing)
- [Bugs and Fixes](#Project Bugs and Solutions)
- [Deployment](#Deployment)
- [Credits](#Credits)
  - [Content](#Content)
  - [Media](#Media)
  - [Code](#code)

## User Stories

### Intented users

- Family
- Neighbours
- Friends
- Uninvited Guests

#### Potential Goals

1. When they visit first time, can easily navigate through the website to find the main purpose effortlessly.
2. When they visit first time, is easily find info of login property.
3. When they visit site, easily find related tables for this year,past year and future year.
4. When they visit site, are able to add new dishes and ingredients to the table.
5. When they visit site, are able to comment on tables.
6. When they see tables are able to like or dislike dishes and see the count of there and invited members vote.
7. They are able to open a new table for a new event.

#### As a Owner

1. I want to:
     - Deliver information
     - Provide links to diffrent tables
     - Show the possible benefits
     - Create, remove, update or edit a exsiting table.

### Design

Not complete Wire frames can be found [here](media/Wireframes)

#### Colour Scheme

#### Typography

#### Imagery

### Features

#### Features left to implement

On this site many updates are still to follow making it bigger and whit more options. Which includes a search option whit the help of javascript. Greater options for UX design.

### Technologies Used

- Pen and Paper wireframes.
- Figma used for more visual wrieframes.
- Git to store the code changes.
- Github used to store the repository.
- Heroku used to upload project
- Django used to build difficult settings
- Allauth used for user login since noother option known.
- Bootstrap used and then abandoned when it became clear its toxic. 
- Google fonts was used for all text on the site.
- Fontawesome used for icons.
#### Languages

- HTML
- CSS
- Pen and Paper
- Python
- Django
- Bootstrap

#### Programs

- Pen and Paper wireframes.
- Virtual code studio for code
- Git to store the code changes.
- Github used to store the repository.
- Google fonts was used for all text on the site.
- Fontawesome used for icons.
- Heroku

### Testing

Testing not done since not complete

### Project Bugs and Solutions

- Reverse related name error in modules fixed by looking for error for 4 hours then giving a uniq name for each related name.
- favicon not loading fixed by looking 8 hours through many tutorials online problem was in debug=true which did not load static files
- likes deleting tables when liked or unliked not fixed
- user cant add, delete or update since it threw a null error while it did got the dish data. 16 hours still no idea whats wrong.
- constant errors whit bootstrap collicions never did fix them
- constant errors 404 being the most usual some times 303 yet it did not fullfill the function intented
- gray screen full of text usualy on proxy server especially when trying to add picture or manipulate database

## Validator Testing

- HTML no errors were returned when passing through the official [W3C validator]
- CSS no errors were returned when passing through the official [Jigsaw validator]

## Lighthouse Testing

![Light house]

### Deployment

This site was deployed using GitHub Pages with the following the steps below:

1. Login or Sign Up to [GitHub](https://github.com/login "Link to GitHub login page")
2. Create a new repository named "medical-plant-site".
3. Once created, click on "Settings" on the navigation bar under the repository title.
4. Click on "Pages", on the left hand side below Secrets.
5. Under "Source" choose branch you wish to deploy in most cases it will be "main".
6. Choose which folder to deploy from, generally from "/root".
7. Click "Save", then wait for it to be deployed.
8. The URL will be displayed above the "source" section in GitHub Pages.

## Heroku

This App is deployed using Heroku.

Heroku depolyment steps

- Fork or clone this repository.
  - requirements.txt can be left empty as this project does not use any external libraries.
  - Create a new app in Heroku.
  - Select "New" and "Create new app".
  - Name the new app and click "Create new app".
  - In "Settings", click "Reveal Config Vars" and input the folloing.
    - CLOUDINARY_URL
    - DATABASE_URL
    - SECRET_KEY
  - Click on "Deploy" and select your deploy method and repository.
  - Click "Connect" on selected repository
  - Click "Deploy Branch" in the manual deploy section. -Heroku will now deploy the App.

### Credits

#### Content

- The fonts were taken from [Google fonts](https://fonts.google.com/).
- The icons in the footer were taken from [Fontawesome](https://fontawesome.com/).
- Help with coding was taken from [https://www.w3schools.com/]

#### Media

- The image from the landing page was taken from [Pixabay](https://pixabay.com/)
- The image from the contact me page was taken from [Freeimages](https://www.freeimages.com/)

#### Code

I looked in multiple sites in order to better understand the code i was trying to implement.

The following sites were used on a more regular basis:

- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Youtube](https://www.youtube.com/ "link to youtube pages")
- [Django](https://docs.djangoproject.com/en/4.0/ "link to django doc")

## Acknowledgement

Self taught whit no help.
