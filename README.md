Jargon Unchained
================

![Jargon Unchained Mockup](readme/JargonUnchainedMockUp.png)


Introduction
------------

Jargon Unchained 2.0 is the online app version of a business jargon dictionary. It is [deployed on Heroku](https://jargon-unchained.herokuapp.com/).

Jargon Unchained was first published as an entertaining [business jargon e-book](https://leanpub.com/jargonunchained) a seven years ago. The book’s writer and stakeholder “Len Guff” published under pseudonym as even though the book was humorous in tone, its target was the B2B industry in which he worked.

Its intended audience were people, like him, who were perhaps newly-qualifed or fresh from university and were hearing bosses and CEOs employing jargon which sounded smart but was perhaps fundamentally stupid. This said there has been interest from business people who use the jargon but are interested in its correct etymology and correct usage.

 

Former strategy
---------------

In interview the author claimed his intended growth strategy was to:

1.  Largely give volume 1 away for free and build on a word-of-mouth reputation

2.  Volume 2 would be free in exchange for email or a nominal fee

3.  A growing and interested audience could then be nudged pay more to but volume 3 outright.

Now nearly 8 years after it was conceived the author admits that it has been difficult to maintain momentum and grow Jargon Unchained’s customer base. Also as a largely solo practice of collation and compilation, new words for the further volumes has taken longer than first estimated. The author pointed out that some original words have changed, disappeared or been more broadly adopted. This web app should revitalise interest, ease the burden of compilation and nurture a community who are interested in taking the next ebook further. 

Competitor research
-------------------

Many of Jargon Unchained’s competitors are similarly the product of sole-operators.

The stakeholder’s initial research discovered [World Wide Words](http://www.worldwidewords.org/) an archive of newsletter articles and word Index written by a Cambridge graduate and Oxford dictionary reader. He ‘ceased writing’ World Wide Words in 2017. There is no search function and the site is poorly structured.

![Worldwide words index](readme/competitors/WorldWideWordsIndex.png)

Larger resources such as [Online Etymology Dictionary](http://www.etymonline.com/) are more robust with larger word lists largely compiled from other printed etmology books. It’s well researched by an American scholar and self-confessed early online amateur. But it is enthusiastically maintained with even a Google Chrome extension with an academically authoritative layout which is also functional. The search and letter navigation are easy to understand.

![Online Etymology Dictionary](readme/competitors/OnlineEtymologyDictionary.png)

A similarly large resource by a British academic Gary Martin is [The Phrase Finder](https://www.phrases.org.uk/). It’s scope is even broader but from a UX perspective the home page suffers from feature creep. With a flattened word cloud dominating the right hand side, the alphabet on the left is most useful search. The most interesting homepage function is the 'most popular today’ section.

![Phrase Finder Home](readme/competitors/PhraseFinderHome.png)

The full list and well using the well structured taxonomy is the best way to navigate.

![Phrase Finder Full List](readme/competitors/PhraseFinderFullList.png)

Clicking on the ‘Work’ category does take you to around [30 of business jargon words](https://www.phrases.org.uk/meanings/business-and-work-related-phrases.html). It’s also worth pointing out that whilst in terms of tonally it’s a much more serious site. Once you’ve stepped through the navigation and reached the database - the UI is clean, fast focussed and learnable.

Much more inline with the humorous tone of Jargon Unchained is[The Business Jargon Dictionary](http://www.theofficelife.com/business-jargon-dictionary-A.html) created by The Office Life. Navigation is via the rounded alphabet old school typwriter letters. It has a moustachioed water-cooler and the brevity of the entries encourages contribution and makes them easily shareable.

![Business Jargon Dictionary](readme/competitors/BusinessJargonDictionary.png)

Although it’s worth noting that the social share buttons don’t work and the site’s [Twitter account](https://twitter.com/jargondujour) stopped retweeting in 2017. Contribution is done through a contact form which prevents a fluid and active community.

In terms of simple and effective UI nurturing a strong community Jargon Unchained can learn a lot from [Urban Dictionary](https://www.urbandictionary.com/). Its is easy to contribute and interact, from visitors who can upvote and easily contribute, with simple search bar, shuffle function and login, through to a democratic contribution function.

![Urban Dictionary](readme/competitors/UrbanDictionary.png)

UX Priorities
-------------

1.  Get people to explore and enjoy the dictionary

2.  Raise awareness of the first ebook

3.  Get people to interact and contribute to the dictionary

4.  Build a community of contributors

5.  Compile new entries into second volume

 

User Stories
------------

### First Time Visitor Goals

1.  As a First Time Visitor, I want to understand the main purpose and tone of the site.

2.  As a First Time Visitor, I want to find or be surprised and entertained by past entries. I want to easily navigate and search and sort through the dictionary.

3.  As a First Time Visitor, I want to easily interact by up or down voting entries I like. I want it to be fairly frictionless to contribute my own entries.

 

### Returning Visitor Goals

1.  As a Returning Visitor, I want to see that the site is growing and be surprised by new jargon.

2.  As a Returning Visitor, I want to see what entries are doing well.

3.  As a Returning Visitor, I want to write my own contributions and see how they are doing.

4.  As a Returning Visitor, I want to write my own definitions and see how well my previous contributions are doing. 

 

### Frequent User Goals

1.  As a Frequent User, I want to see that the dictionary is growing and help it grow more

2.  As a Frequent User, I want to see what entries are doing well.

3.  As a Frequent User, I want to work the site grow and getting the next volume of the ebook published.

 

Scope
=====

### Sprint 1: Scope  (1.5 weeks)

1.  Research look and layout the site with the 5 planes of UX (Research, ReadME, Wireframes) 

2.  Planning out work process deadlines, work structure and testing implementation

3.  GitHub’s project Kanban used to track development, improvements and bug fixes.

 

### Sprint 2: Structure (2 weeks)

1.  Code out site structure, repo and basic layout

2.  Structure databases in MongoDB

3.  Add current dictionary, pull through - **Deploy to Heroku**

 

### Sprint 3 Structure / Skeleton

1.  Build user sign up and update pages

2.  Build dictionary, search and sort function.

3.  Build vote up vote down functionality (2nd meeting with mentor)

 

### Sprint 4 Skeleton and Surface

1.  Testing and Bug fixes

2.  Navbar fixing FA icons in place (3rd mentor meeting)

3.  Styling of the site

4.  Final testing

 

Out of scope
------------

The intention of this first milestone is to achieve a working Minimal Viable Product (MVP). Energy and time was focussed on creating a database, it being functional from a user perspective.

 

Tone considerations
-------------------

The site is should be humorous in tone. It should be fun to use and enjoyable to lampoon business jargon. Some of the language used in the field should employ business jargon. Research touchpoints for this are a blend between The Business Jargon Dictionary and Urban Dictionary.

 

Design Ideas
------------

Humour is important to how this page is pitched. It is in-sympathy with the original design. This is the influenced the colour choices of the original book. Materialize was well suited to the project as the dropshadow and other features are a little bit dated now. This became a bit of an issue with the site validation see: **TestingBugs.**

Another out-of-scope feature was the home page. This would have had the the ‘boss’ character speaking to the underling in the illustration to say a “random” phrase which people could click on and that would get you into the book. 

![Home page](readme/wireframes/Second Draft/Homescreen Desktop.png)

My other wireframe considerations can be [accessed here](readme/wireframes) with more explanation why other choices weren't made in Bugs and Fixes.

 

### Colour Scheme

The main primary background colour of the site is Cyan #39c2c8. The navbar is this custom color. Elsewhere in the site the [Materialize color scale](https://materializecss.com/color.html) is used and with secondary color “blue" as a sympathetic  better-defined contrast. Elsewhere Materialize’s dark green and red are used to signify access buttons/links or delete/quite.

 

### Imagery

No photos are used within this project. Illustrations best fit the tone of this project as they are bring out humour. It’s important to emphasise that this is a fun project and a safe place to vent spleen.

 

Database rationale
------------------

 ![Relational Diagram](readme/JUC_Relational_Diagram.png)

### Category Collection

*Another way to group entries - used in search function for this Sprint iteration. *

Category (category_name): Nouns as verbs

\- Tortured metaphors

\- Overcomplicated

\- Plain nonsense

\- -ise

 

### Jargon Collection

**Jargon** (jargon_name) (“Jargon" String: max-length:25 required)

**Definition** (definition) “What does it really mean?" String: max-length:200 required)

**Example sentence** (usage) **"**Use it in a sentence?“ String max-length: 100)

**Optional rant: **(editorialise) "Why is it here? Why do you love and hate it? Can you make it right? Is it going to last?” String: 200 not-required could be editorialised for e-book) END of input field

**Category** (category_name) from category collection

**Love percentage** (love_percent) triggered by voting thumbs up / thumbs down (originally intended to be out of 110% but left uncapped for now)

 

### User Collection

**Business Handle** (“name” - chosen by user)

**Password** (“password” - chosen by user)

**E-Deets** (“email” - not for public but could be used - for login) Not in scope for this sprint

**User-level** (determined by Admin)

In discussion with my mentor it was decided for this MVP that email grab wasn’t needed as verification protocol and technology isn’t in place. Further down the line it will be.

 

 

### Comment collection (Out of scope)

Requires login to comment. Users are able to debate the correctness of the jargon. And possibly suggest updates or changes. Changes can be made only by the creator of the entry or and editor or higher user.

 

User types
----------

 

**Visitor:** Can explore the dictionary and vote up and down (Read, Vote)

**User:** able to write contribute their own phrases and definitions, they can also update and delete their own entries. (Read, Vote, Create, Update own records, Delete own records, Comment on others)

**Editor:** able to check and update and delete other contributions. (Update, Delete other entries) - not in scope for this MVP.

**Admin**: able to grant editor user level, rewrite delete other contributions, have final say on definition. (Read, Vote, Create, Update own records, Delete own records, Delete users)

These roles were kept in mind for development but there wasn’t enough development time to implement. In this current sprint editor is currently frontend admin is backend and more complex administration is done in MongoDB. 

 
## Testing and Bugs
Testing and further details on compenents and features can be [found here](readme/TestingBugs.md).

Tools
-----

 

Languages Used
--------------

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)

-   [CSS3](https://en.wikipedia.org/wiki/CSS)

-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

-   [jQuery](https://en.wikipedia.org/wiki/JQuery)

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

Frameworks, Libraries & Programs Used
-------------------------------------

-   [Materialize 1.0.0](https://materializecss.com/) Used to provide the responsiveness and styling of the website as well as navigation bar, buttons, panel cards, scrollspy and cards reveal.

-   [jQuery](https://jquery.com/) jQuery comes with Materialize to make the navbar and the application in a whole responsive.

-   [Flask](https://flask.palletsprojects.com/en/1.1.x/) Flask is the web framework for the app.

-   [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) Is used for the Python template.

-   [Heroku](https://dashboard.heroku.com/) The cloud platform for deploying the app.

-   [MongoDB](https://www.mongodb.com/1) The application data platform

-   [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) Used for the for password hashing/authentication as well as authorization.

-   [Git](https://git-scm.com/) Used Git for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

-   [GitHub](https://github.com/) GitHub stored the projects code after being pushed to Heroku via Flask

-   [Balsamiq](https://balsamiq.com/) To create initial wireframes for the project design - full wireframes can be seen here.

- [DB Diagram](https://dbdiagram.io/d/6297ea0054ce26352742e082) To create database schema

-   [Photoshop](https://www.adobe.com/uk/products/photoshop/) Used to crop, resize and optimise main illustration

-   [W3C Markup Validation Service](https://validator.w3.org/) service for testing HTML

-   [W3C CSS Validation Service](https://jigsaw.w3.org/) Used to test CSS

-   [PEP8 online](http://pep8online.com/) I used this service for possible errors identification in the Python code

-   [Autopep8](https://pypi.org/project/autopep8/) used to clean

-   [Lighthouse](https://developers.google.com/web/tools/lighthouse) I used it to audit performance of the application

-   [Chrome DevTools ](https://developer.chrome.com/docs/devtools/)I used this service to test code changes and responsivity of landing page.

 

# Deployment
1. Connecting the Application to MongoDB
2. Logged into my MongoDB account.
3. With the "Clusters" tab selected, click on "Connect"
4. Select "Connect your application"
5. Select "Python" as the "Driver" and "Version" "3.6 or later".

## Heroku Deployment
Before following the steps listed below, a requirements.txt file and a Procfile were created and pushed to GitHub from Gitpod using the following commands:

    pip3 freeze --local > requirements.txt
    echo web: python app.py > Procfile

Then to integrate APScheduler into the application to automate the awards() & new competition processess I added a second dyno to my Procfile --> clock: python jobs.py Referring to the jobs.py file where the scheduled jobs are listed.

Use the Heroku CLI to scale up the clock process using the command: heroku ps:scale clock=1

The application was deployed via Heroku using this process:
Navigated to Heroku
Signed into my Heroku account.
Selected "New" on the dashboard and then "Create new application" option as below:


Selected a name for my application, selected "Europe" as the region and clicked "Create app".

5. With the "Deploy" tab selected, "GitHub - Connect to GitHub" was chosen as the deployment method. 


6. Make GitHub profile is, click "connect" next to the GitHub repository for this project.


7. Navigate to the "Settings" tab and clicked on "Reveal Convig Vars".
Added configuration variables to Heroku.
Navigated back to the "Deploy" tab and selected "Enable Automatic Deploys" with the master branch selected from the dropdown box.

10. Then clicked on "Deploy Branch" also with master selected.

11. Site is deployed and any changes are automatically deployed each time they are updated and pushed to GitHub during development.

_NOTE: Due to a security issue, Heroku disabled automated deployments from GitHub during the development of this app. On [30th May 2022](https://status.heroku.com/incidents/2413) this was resolved but on 3rd June 2022 it was still disabled for this app. The following additional steps are needed to push to both repositories. There are additional steps if you have MFA/2FA authentication activated you need to retrieve the API key from the dashboard and use this when prompted._ 

1. Open terminal in Gitpod.
2. Get your app name from Heroku:
Enter the following command in the terminal: heroku apps
4.   Set the Heroku remote. (Replace <app_name> with your actual app name and remove the <> characters)
Enter the following command in the terminal: heroku git:remote -a <app_name>
5.   Add and commit any changes to your code, if applicable.
Enter the following command in the terminal: 
```git add . && git commit -m "Deploy to Heroku via CLI"``` 
 6.   Push to both GitHub and Heroku
Enter the following command in the terminal: ```git push origin main```
Enter the following command in the terminal: ```git push heroku main```

_Whilst the problem persistes must do this every time you push to ensure that both repo's are the same_

_In order to push to Heroku you will need to login through the CLI for every Gitpod session. ``` heroku login -i ``` using your email as login and Heroku API as password._

Other thanks and acknowledgments
--------------------------------

Jargon Unchained was originally conceived by ‘Len Guff’ original copyright rests with him 2014 otherwise it’s me and the contributors. Illustration was by Dave Whittle. Thanks to Code Institute support including my mentor Antonio and Tutors Jo, Johan and Igo.I’m thankful for the support, and advice and tolerance from Jon Kennard, Juliet Spare, Tim Stacey and Darren Legore plus CI Slack and Stack Overflow communities. 
