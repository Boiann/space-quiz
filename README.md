<!-- Code for readme adapted from author's own project (Portfolio 2),
https://github.com/Boiann/budget-calculator -->

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

 Some of the features present in the project were concieved in the planning stages (error checking, feedback etc) and some were developed as the project grew in scope (more knowledge, secret username etc). The final result is an amalgam of what the author considers to be a good, interesting and educational quiz.

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

I want to know what is this site for
I want to find additional info/instructions
I want to have numbers in my username
I want to know more about the answer I got wrong
I want to restart the quiz and keep my username
I want no bugs or issues with the game

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

Mobile wireframe was not considered as there was no instructions that making the project responsive was neccessary. Upon checking other student's projects on Slack and their respective GitHub accounts, the author concluded this was not neccessary. Also checked with mentor, confirming this.

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

- [HTML](https://en.wikipedia.org/wiki/HTML "Link to html wikipedia page") - The website content was adjusted using HTML language.
- [CSS](https://en.wikipedia.org/wiki/CSS "Link to css wikipedia page") - The webpage was styled using custom CSS internally using 'style' in the head of layout.html.
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python wikipedia page") - The project logic and operations inside CLI were developed using Python language.

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

[Back to top ⇧](#space-quiz)

---

## **Testing**

Testing information can be found in a separate testing file [TESTING.md](/TESTING.md).

[Back to top ⇧](#space-quiz)

---

## **Credits**

### **Code used and adapted**

* 

### **Websites visited to gather knowledge**

  
###  **Acknowledgments**


[Back to top ⇧](#space-quiz)

***