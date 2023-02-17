# SPACE-QUIZ

SPACE-Quiz is a Project 3 for Code Institute Full-stack development program: Python Essentials.
Made with passion for anyone interested in space, astronomy and anything related to it.
The whole project is dedicated to Mr. Carl Sagan, whose books, TV shows and science communication continues to inspire today.

<!--Webpage image -->

Visit the live site [Here.](https://space-quiz.herokuapp.com/ "Link to Budget Calculator")

---

## CONTENTS

* [Project Overview](#project-overview)
  * [Project Goals](#project-goals)

* [User Experience](#user-experience)
  * [User Expectations](#user-expectations)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Imagery](#imagery)
  * [Structure](#structure)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Intro](#intro)
  * [Name input](#name-input)
  * [Guide](#guide)
  * [Quiz](#quiz)
  * [More knowledge](#more-knowledge)
  * [Quiz end messages](#quiz-end-messages)
  * [Leaderboard update message and display](#leaderboard-update-message-and-display)
  * [Quiz replay](#quiz-replay)
  * [Secret username](#secret-username)
  * [Front-end features](#front-end-features)

* [Future Implementations](#future-implementations)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Programs Used](#programs-used)

* [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code used and adapted](#code-used-and-adapted)
  * [Acknowledgments](#acknowledgments)

---

## **Project Overview**
The idea of developing space-themed quiz was in author's mind for a long time, since starting the Code Institute Full-stack development program.
As soon as the Python lessons were finished, the author knew that space themed quiz will be developed if able. After research the wireframes and the flowchart were developed and the project fully made-up conceptually.
The idea to dedicate the project came after first quote from Mr. Sagan was inserted.
The quiz-based game explains itself but there are numerous features that (hopefully) set it apart:
 - Error checking throughout the quiz
 - Feedback on every input ( right or wrong )
 - Evenly and nicely spaced text
 - Text output in typewriter style
 - Interesting secret hidden within the quiz
 - Ability to know more about question/answer, no matter if question is answered right or wrong 
 - Get a hint, sometimes rather funny
 - Get your name on leaderboard
 - Restart the quiz without using mouse and keep your username if you want
 - Enjoy simple and relaxing space-themed webpage

The project also uses Google Worksheet API for:
 - Questions
 - Answers
 - Hints
 - More knowledge
 - Updating and displaying top 10 players on a leaderboard
 - This is the [Google worksheet](https://docs.google.com/spreadsheets/d/1-mEIbGDZpEof_4VUdDmKuQsoC3czJN-EKm6sUlSruns/edit#gid=0 "Link to Google sheets page") used to hold the data

 Some of the features present in the project were conceived in the planning stages (error checking, feedback etc) and some were developed as the project grew in scope (more knowledge, secret username etc). The final result is an amalgam of what the author considers to be a good, interesting and educational quiz.

### **Project Goals**
 - Develop CLI based quiz game using Python
 - Present the quiz in a clean and easy to understand manner
 - Keep good UX principles regarding layout/colours/interaction
 - Robust Python code without issues/bugs

[Back to top ⇧](#space-quiz)

---

## **User Experience**

### **User Expectations**
 - Able to quickly understand what the purpose of the site is
 - Find additional info/rules if needed
 - Every interaction has feedback
 - Get a hint if stuck
 - Get more info about question/answer, right or wrong 
 - Get name on/see the leaderboard
 - Good looking and theme adjusted look of the project
 - No errors with the game logic

### **User Stories**

 - I want to know what is this site for
 - I want to find additional info/instructions
 - I want to have numbers in my username
 - I want to know more about the answer I got wrong
 - I want to restart the quiz and keep my username
 - I want no bugs or issues with the game

[Back to top ⇧](#space-quiz)

---

## **Design**

### **Colour Scheme**

<!-- Colour Palette image -->

There are just a few colors used in the CLI, by installing/importing TERMCOLOR and CPRINT. The red colored text signifies wrong answer/input, green is used for the right answer, light cyan for leaderboard, guide and more knowledge display. The blue is used for intro/outro quote and quiz logo/intro.
Aside for CLI itself, on the webpage the colors used are blue for quiz title and its variations for hover color change on the 'run program' button.
This was not mandatory but the author felt necessary to include simple but nice colours to pair with the project theme.

### **Imagery**

<!-- Stars GIF -->
<!-- Favicon -->

Only two images (image and GIF) were used for the project. The Interstellar Dream GIF was obtained from Youtube [Here](https://www.youtube.com/watch?v=Hh816wRR2hc&list=PLNZfrta02FkM15KMNlB24dDz68EPa22lD&index=27&ab_channel=AllBackgroundVideos "Link to Youtube"). The author used [GifCap](https://gifcap.dev/ "Link to GifCap page") to capture the GIF, then [XConvert](https://www.xconvert.com/compress-gif "Link to GifCap page") to resize and compress the GIF.
The GIF's purpose is to make the UX better and add something dynamic outside the CLI. 
The other image used is favicon 'galaxy' which pairs nicely with the project.

### **Structure**

<!-- flowchart img -->

Flowchart was designed at the start of the project along with the wireframes.
The final result differs from the flowchart slightly on account of implementing changes for better UX.

Some of the thing different to the flowchart:
 - Need help/guide? ==> leads straight into first round of the quiz instead asking if ready ==> loop back to asking need help/guide
 - Added hints display after user is asked the question and presented with answers ('H' input)
 - Added 'more knowledge' text after the answer is resolved. No matter the outcome (correct or wrong) the user can input 'Y' to learn more or 'N' to go to next round
 - Question about 'Wanna go to Leaderboard' removed, the user is entered into the leaderboard automatically
 - Add 'secret' username input, more about this feature in 'Features' section of this README
 
### **Wireframes**

Wireframes for Assessment Guide and Project Planning & Ux were made before the ones for the content of the project itself.
<details>
<summary>Assessment guide wireframe</summary>

<!-- img -->
</details>

<details>
<summary>Project planning wireframe</summary>

<!-- img -->
</details>

There are three wireframes for the project, each one corresponding to the level of learning outcome (grade); Pass Performance, Merit Performance and Distinction Performance.

Differences between outcomes were considered early as to allow flexibility when working on the project. Personal, work, family, dependants and health situations were considered to have impact on time available for the project.
Ideally, maximum time was to be taken to finish the project making the scope bigger.

<details>
<summary>Pass Performance wireframe</summary>

<!-- img -->
</details>

<details>
<summary>Merit Performance wireframe</summary>

<!-- img -->
</details>

<details>
<summary>Distinction Performance wireframe</summary>

<!-- img -->
</details>

Mobile wireframe was not considered as there was no instructions that making the project responsive was necessary. Upon checking other student's projects on Slack and their respective GitHub accounts, the author concluded this was not necessary. Also checked with mentor, confirming this.

[Back to top ⇧](#space-quiz)

---

## **Features**

### **Intro**
 - Intro clear screen, quote and ASCII art
 <!-- image -->

### **Name input**
 - Name input ok, capitalize name
 <!-- image -->
 - Name input errors
 <!-- img -->

### **Guide**
 - Guide/rulebook question ok input and display
 <!-- img -->
 - Guide/rulebook input error
 <!-- img -->

### **Quiz**
 - Question/answers display, answer correct
 <!-- img -->
 - Question/answers display, answer wrong
 <!-- img -->
 - Question/answers display, hint input
 <!-- img -->
 - Question/answers display, input error
 <!-- img -->

### **More knowledge**
 - Know more display, 'Y' input
  <!-- img -->
 - Know more display, 'N' input
 <!-- img -->
 - Know more display input error
 <!-- img -->
 - Know more last question message
 <!-- img -->

### **Quiz end messages** 
 - Quiz over message and score
 <!-- img -->
 - Score colour and message change
 <!-- img -->

### **Leaderboard update message and display**
 - Updating leaderboard
 <!-- img -->
 - Leaderboard display
 <!-- img -->

### **Quiz replay**
 - Quiz replay 'N' input, outro quote
 <!-- img -->
 - Quiz replay error input
 <!-- img -->
 - Quiz replay 'Y' input, username question
 <!-- img -->
 - Quiz replay 'Y', username question 'Y' input
 <!-- img -->
 - Quiz replay 'Y', username question 'N' input
 <!-- img -->
 - Quiz replay 'Y', username question error input

### **Secret username**
The secret username is a throwback to a very popular Sci-Fi movie, '2001: A Space Odyssey. In the movie, the AI by the name HAL 9000 is the main antagonist.
The secret username is first hinted in the guide/rulebook = '3 LETTERS = ASCII'.
At first this means nothing, but as the user finishes the quiz the leaderboard is presented. The rules clearly say there are maximum of 100 points but somehow there is an user by the name 'HAL_9000' with a score of 105 points (present at the time of writing this README). That should give the user incentive to see the rules and replay the quiz again to see what is going on. Upon rechecking the clue '3 LETTERS = ASCII', the user should assume the need to change only the letters of 'HAL_9000' into ASCII code and input that as the username. As there are checks in place for name input against using special characters, meaning '_', the user should not consider '_9000' for input. As ASCII code can be triple or double digits, both 'secret' usernames are allowed:
<details>
<summary>=====SPOILER=====</summary>

072065076 and 726576
</details>
If the user enters the secret username, special message prints with change of score calculation. Also, if the user scores more than 100 points, which is possible only using secret username, a special message will display at the end of the quiz.

 - Secret username input result
<details> 
<summary>=====SPOILER=====</summary>

<!-- img -->
</details>

 - Secret username score message
<details>
<summary>=====SPOILER=====</summary>

<!-- img -->
</details>

### **Front-end features**
- Favicon and dynamic background/GIF
<!-- img -->
- GitHub and Youtube icon, 'Run Program' button hover colour change
<!-- img -->
- GitHub icon opening page in new tab
<!-- img -->
- Youtube icon opening page in new tab
<!-- img -->

---

## **Future Implementations**
The author would like to implement random question order and add a lot more questions/answers/more knowledge. Also, give the user option to use various 'game modes' like easy, medium and hard and corresponding questions. Implement timer that the user can turn on/off for added challenge and more score points.

[Back to top ⇧](#space-quiz)

---

## **Technologies Used**

### **Languages Used**

- [HTML](https://en.wikipedia.org/wiki/HTML "Link to html Wikipedia page") - The website content was adjusted using HTML language.
- [CSS](https://en.wikipedia.org/wiki/CSS "Link to css Wikipedia page") - The webpage was styled using custom CSS internally using 'style' in the head of layout.html.
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wikipedia page") - The project logic and operations inside CLI were developed using Python language.

### **Programs Used**

- [GitHub](https://github.com/ "Link to GitHub page") - Source code hosted on GitHub, deployed using Git Pages.
- [GitPod](https://www.gitpod.io/ "Link to GitPod page") - Used to commit, comment and push code during the development process.
- [Font Awesome](https://fontawesome.com/ "Link to Font Awesome page") - GitHub icon was obtained from Font Awesome.
- [Balsamiq](https://balsamiq.com/ "Link to Balsamiq page") - Used to create wireframes and website structure map for the project.
- [Visual Studio Code + Spell Checker add on](https://code.visualstudio.com/ "Link to Visual Studio page") - Used to spell-check the html and css code
- [Google Keep](https://keep.google.com/ "Link to Google Keep page") - Used to make notes during the project duration
- [LanguageTool](https://languagetool.org/ "Link to Language Tool page") - Used to spell-check the contents of README.md
- [Google Fonts](https://fonts.google.com/ "Link to Google fonts page") - Used to import fonts to the project
- [GifCap](https://gifcap.dev/ "Link to GifCap page") - used to capture gif-s of the project 
- [Heroku](https://www.heroku.com/ "Link to Heroku page") - used to deploy the project
- [XConvert](https://www.xconvert.com/compress-gif "Link to XConvert page") - used to compress GIF file
- [Imgur](https://imgur.com/ "Link to Imgur page") - used to host the background image and favicon
- [Patorjk](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20 "Link to Patorjk page") - used to convert text into ASCII art
- [Google worksheet](https://www.google.com/sheets/about/ "Link to Google sheets page") - used to host the worksheet to hold data
- [Lucidchart](https://www.lucidchart.com/pages/examples/flowchart-maker "Link to Lucidchart page") - used to make the flowchart for the project

[Back to top ⇧](#space-quiz)

---

## **Deployment**
The project was written and hosted on [GitHub](https://github.com/ "Link to GitHub page"). The author used GitHub's terminal output with command 'python3 run.py' to run the program logic/game. After the project was developed enough, it was deployed on [Heroku](https://www.heroku.com/ "Link to Heroku page") using the following method:

1. Add dependencies in GitPod to requirements.txt file with command "pip3 freeze > requirements.txt"
2. Commit and push to GitHub
3. Go to the Heroku Dashboard
4. Click "Create new app"
5. Name app and select location
6. Add Config Vars for Creds and Port in Settings tab
7. Add the buildbacks to Python and NodeJS in that order
8. Select appropriate deployment method, GitHub
9. Connect to Github and link to repository
10. Enable automatic deployment and/or deploy manually
11. Click on Deploy

[Back to top ⇧](#space-quiz)

---

## **Testing**

Testing information can be found in a separate testing file [TESTING.md](/TESTING.md).

[Back to top ⇧](#space-quiz)

---

## **Credits**

### **Code used and adapted**

 - The author used his previous projects, [Boudoir Studio](https://boiann.github.io/boudoir-studio/index.html "Link to Boudoir Studio home page") ( GithHub repository [here](https://boiann.github.io/boudoir-studio/index.html "Link to Boudoir Studio home page") ), and [Budget Calculator](https://boiann.github.io/budget-calculator/ "Link to Budget Calculator") ( GithHub repository [here](https://github.com/Boiann/budget-calculator "Link to Budget Calculator GitHub repository") ) as a source for looking up the code for CSS and README purposes mainly.
 - [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template "Link to CI Python template") was used to start the project.
 - Using [Google worksheet](https://www.google.com/sheets/about/ "Link to Google sheets page") to manipulate questions and answers was seen during  Code Institute [Love Sandwiches](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/58d3e90f9a2043908c62f31e51c15deb/ "Link for Love Sandwiches project") project, ( GithHub repository [here](https://github.com/Code-Institute-Org/python-essentials-template "Link to CI Python template") ).
 - [Pub Quiz Challenge](https://pub-quiz-challenge.herokuapp.com/ "Link to Pub Quiz Challenge") ( GithHub repository [here](https://github.com/CI-Tom/pub-quiz-challenge "Pub Quiz Challenge repository page") ) was studied in depth to get a sense of how a quiz game in Python would work, and to get a sense of the quiz layout itself. It has also provided the solution for pairing the questions with the right answers.
 - [Football Quiz](https://football-quiz-game.herokuapp.com/ "Link to Football Quiz") ( GithHub repository [here](https://github.com/mikyrenato/3rd_Project_Quiz_Game "Football Quiz repository page") ) was taken note of because the CLI was centered and the image background was applied. This is also where the author learned about tabular display of the leaderboard.
 - [Wheel of Fortune](https://the-wheel-of-fortune.herokuapp.com/ "Link to Wheel of Fortune") ( GithHub repository [here](https://github.com/LudovicLeGuen/Wheel-of-Fortune "Wheel of Fortune repository page") ) was studied and this is where the author noticed and learned about clearing the screen in CLI.
 - [Harry Potter Adventure Game](https://harry-potter-adventure-game.herokuapp.com/ "Link to Harry Potter Adventure Game") ( GithHub repository [here](https://github.com/AlexaH88/harry-potter-adventure-game "Harry Potter Adventure Game repository page") ) was studied to fix the background issue in HTML, more on this in BUGS section in [TESTING.md](/TESTING.md).
 - [Carl Sagan quotes webpage](https://www.goodreads.com/author/quotes/10538.Carl_Sagan "Link to Carl Sagan quotes webpage") was used to copy Mr. Sagan's quotes for intro/outro.
 - [Space Trivia Questions](https://conversationstartersworld.com/trivia-questions/space-trivia-questions/ "Link to Space Trivia Questions") was where the author copied the questions, answers and 'more knowledge' info from.

### **Websites visited to gather knowledge**
There were many sites visited during the duration of the project.
[Google](https://google.com/ "Google home page") was used to produce results of the specific query, and [Stack Overflow](https://stackoverflow.com/ "Stack Overflow home page") proved to be the best source of information for various queries/issues. 

The standout webpages are:
- [This](https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside "Link to Sorting a string") website was used to learn about sorting a string.
 - [This](https://pypi.org/project/tabulate/ "Link to tabulate") website was used to learn about tabulating the leaderboard.
 - [This](https://www.geeksforgeeks.org/clear-screen-python/ "Link to sleep") website was used to learn about sleep.
 - [This](https://www.101computing.net/python-typing-text-effect/ "Link to typing print and clear screen") website was used to learn about typing print, input and clear screen.
 - [This](https://stackoverflow.com/questions/46112605/python3-issue-with-calling-execopen-read-inside-a-function "Link to restart program") website was used to learn about restarting the program.
 - [This](https://www.codingem.com/python-print-on-the-same-line/ "Link to print on the same line") website was used to learn about printing on a same line.

###  **Acknowledgments**
This whole project is dedicated to Carl Sagan, astronomer, planetary scientist, cosmologist, astrophysicist, astrobiologist, author, and science communicator.
His book 'Cosmos' inspired me as a child and geared me towards sciences and astronomy.

Without support I got from other people, this project would never be realized. I'll try and remember to thank everyone and everything I can!

- Mirjana, my wife, thank you for your support and cheering me on, lifting me 
back up when it got hard. Thank you for taking care of all the housework and food, children and numerous other responsibilities while I was busy with full time job and doing this project on the side. Without you this journey into career change would never be possible.
- A., G. and V., my three beautiful girls. Thank you for being so understanding during the project work. Thank you from the bottom of my heart for being who you are, wonderful and delightful souls. You make me proud to be your dad.
- Boris, my brother, thank you for testing my project so thoroughly, and for your support.
- Marija and Boris, my mother and father, thank you for making me feel like a superstar when I announced I'm starting this journey.
- John, my friend, thank you for starting me on this path, and for your support, chats and sharing the things you learned.
- Helen from Code Institute, thank you believing in me and making this change possible.
- Slack community, thank you for being a constant source of good information.
Special mentions are Sirinya_5P, Kate L_5P and Tomislav_5P, whose praise lifted my spirits and reinforced the notion that I can do this.
- Koko, my mentor, thank you for being an incredible source of solutions and good advice, your support meant a great deal during the project.
- C8H10N4O2 in a cup. Thank you for existing.

[Back to top ⇧](#space-quiz)

***