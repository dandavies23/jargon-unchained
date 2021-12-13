Jargon Unchained
================

Introduction
------------

Jargon Unchained was first published as an entertaining [business jargon e-book](https://leanpub.com/jargonunchained) a seven years ago. The book’s writer and stakeholder “Len Guff” published under pseudonym as even though the book was humorous in tone, its target was the B2B industry in which he worked.

Its intended audience were people, like him, who were perhaps newly-qualifed or fresh from university and were hearing bosses and CEOs employing jargon which sounded smart but was perhaps fundamentally stupid. (This said there has been interest from business people who use the jargon but are interested in its correct etymology and correct usage….)

 

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

Priorities - New strategy
-------------------------

1.  Get people to explore and enjoy the dictionary  

2.  Raise awareness of the first volume 

3.  Get people to interact and contribute to the dictionary

4.  Build a community of contributors

5.  Compile new entry into second volume

 

User Stories
------------

### First Time Visitor Goals

1.  As a First Time Visitor, I want to understand the main purpose and tone of the site. 

2.  As a First Time Visitor, I want to find or be surprised and entertained by past entries. I want to easily navigate and sort through the dictionary.

3.  As a First Time Visitor, I want to easily interact by up or down voting entries I like. It want it to be easy to comment and even contribute my own entries. 

 

### Returning Visitor Goals

1.  As a Returning Visitor, I want to see that the site is growing and be surprised by new jargon.

2.  As a Returning Visitor, I want to see what entries are doing well.

3.  As a Returning Visitor, I want to like and comment and share on other channels.

4.  As a Returning Visitor, I want to write my own contributions and see how they are doing.

5.   As a Returning Visitor, I want to write my own definitions and see how well my previous contributions are doing. Comment on other people’s definitions.

 

### Frequent User Goals

1.  As a Frequent User, I want to see that the dictionary is growing and help it grow more

2.  As a Frequent User, I want to see what entries are doing well.

3.  As a Frequent User, I want to comment on other people’s contributions

4.  As a Frequent User, I want to fix and enhance other contributions by adding or fixing more detailed rants (editor)

5.  As a Frequent User, I want to work the site grow and getting the next volume of the ebook

 

Scope
=====

### Milestone 1 

Research look and layout the site with the 5 planes of UX (Research, ReadME, Wireframes)

 

### Milestone 2 

Sprint 1: Code out site structure, repo and basic layout

Sprint 2: Structure databases in MongoDB

Sprint 3: Add current dictionary, pull through - **Deploy to Heroku**

 

### Milestone 3

Sprint 1: Build user sign up and update pages

Sprint 2: Build dictionary, search and sort function.

Sprint 3: Build vote up vote down functionality

 

 

UX considerations
-----------------

The site is should be humorous in tone. It should be fun to use and enjoyable to lampoon business jargon. Some of the language used in the field should employ business jargon.

 

Design Ideas
------------

Humour is important. Want to be in-sympathy with the original design. Would like to use the same colour and font of the original book. I would also like the ‘boss’ character speaking to the underling in the illustration to say a “random” phrase which people could click on and that would get you into the book. The first book would also feature on the site, perhaps persistently in the footer?

 

### Colour Scheme

The main primary background colour of the site is Teal #39c2c8. White text is used for text.

 

### Typography

Header font is …

 

### Imagery

No photos are used within this project. Illustrations best fit the tone of this project as they are bring out humour. It’s important to emphasise that this is a fun project and a safe place to vent spleen.

 

 
-

 

Databases
---------

A searchable dictionary of terms which can be voted up or down - similar to Urban Dictionary or Reddit.

 

### User Database

**Business Handle** (“name” - chosen by user)

**Password** (“password” - chosen by user)

**E-Deets** (“email” - not for public but could be used - for login)

**User-level** (determined by Admin)

 

### Comment database

Requires login to comment. Users are able to debate the correctness of the jargon. And possibly suggest updates or changes. Changes can be made only by the creator of the entry or and editor or higher user.

 

### Dictionary Database

**Jargon** (“term” text: max-length:25 required)

**Definition** (“meaning” text: max-length:200 required)

**Use it in a sentence?** (“usage” text: max-length: 100)

**Why it makes the list?** (“reason” text: max-length: 200 not-required could be editorialised for e-book)

**Can we make it right?** Y/N (radio button not-required)

**Why not? / How come?** (dependant on previous answer 200 not-required // could be editorialised for e-book)

**Love to hate** (vote up) / **Hate to love** (vote down)

**Here for the long run or a flash in the pan?** (“longevity” rating 1-110%!) [perhaps not needed]

###  

 

User types
----------

[can turn this into a table…]

Role | Outline | Functions

**Visitor:** Can explore the dictionary and vote up and down (Read, Vote)

**User:** able to write contribute their own phrases and definitions, they can also update and delete their own entries. (Read, Vote, Create, Update own records, Delete own records, Comment on others)

**Editor:** able to check and update and delete other contributions. (Update, Delete others)

**Admin**: able to grant editor user level, rewrite delete other contributions, have final say on definition. (Read, Vote, Create, Update own records, Delete own records, Delete users, Prevent certain records from being altered further?)


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
