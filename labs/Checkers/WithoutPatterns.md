In this lab, you will explore a maintenance task that does not take advantage of patterns.  While we will study design patterns that are useful to this maintanence task later in this course, **you should NOT apply design patterns while working this lab**.  The goal of this lab is for you to see some real-coding challenges that the patterns will help solve.

Please work this lab individually.  You must consult only with your instructor, not any other persons while working this lab. If you use co-pilot, please state this clearly in your reflection.

You MUST use Java 17 with JavaFX 19 for this lab. To quote [Dr. Yoder's post](https://stackoverflowteams.com/c/msoe/a/305/2) on MSOE's private Stack Overflow,

> **As of Fall 2022**, the standard instructions are on [taylorial.com](https://taylorial.com/cs1021/Install.htm), a site maintained by Dr. Taylor. You will also need to [install IntellIJ](https://www.jetbrains.com/idea/download/?ij80pr#section=windows).  Students with @msoe.edu emails can get free access to the professional version of IntelliJ.
>
> The installation process used in the freshman sequence is undoubtedly the standard.

If you don't already have one, create an empty Java project. Create a folder called `src` within this project. Download this zip and copy the folder within it as a package within the empty project's source folder. It should have a working game of checkers in which pieces can move and jump over other pieces, moving forwards only.

In checkers, ordinary pieces can move forwards but king pieces can also move backwards.
All pieces must move diagonally and can capture pieces by jumping over them.

The current implementation does not implement kings.  It only implements ordinary
pieces.

Step-by-step editing instructions
---------------------------------
These instructions walk you through the edits that are needed to add kings to the game.  Avoid making changes to the structure of the code beyond what is described here.  If you find each step requires major rewrites with multiple methods, you are likely restructuring the code too much.

1. Identify the place in the code where the type of a piece is defined.
2. Add a new isKing boolean in this place.  Add this as an optional parameter to the constructor by using 
3. two constructors and a `this` call with a default value of `false` for isKing.


3. Identify the place in the code where it determines that a black piece has reached
   the last row of the board.
4. At this position, notify the board that the old ordinary black piece was captured.
   Also create a new black king piece at this position on the board. (Pieces automatically
   add themselves to the board when created.)


5. Identify the place in the code where a black piece is drawn.
6. Update this place to draw two ellipses instead of one, with the second ellipse
   placed five pixels above the first ellipse. Be sure to also make this ellipse clickable
   as the ellipse underneath it is.


7. Identify the place in the code where the drawn piece is moved.
8. Update this place to move both ellipses.


9. Identify the place in the code where it determines if an ordinary move is valid.
10. Update this code to work for Black Kings. Kings can move backwards and forwards,
   but still only diagonally.


11. Identify the place in the code where it determines if a capture move is valid.
12. Update this code to work for Black Kings. Kings capture by jumping pieces
   backwards and forwards, but still only diagonally.


**DO NOT** redesign the provided code.  But you may optionally

* Add comments that you wish were in the code
* Rename methods or variables
* Split methods that are too long into helper methods.

Such changes are PURELY OPTIONAL, but the instructors may consider incorporating them into next year's starting code if we feel they are an improvement.

Reflections
-----------
Edit the provided file called reflections.md, replacing the parnethetical remarks with your answers.

In it, you will answer these questions:

1: What design aspects in the provided code made your work easier?
2: How do you think the design of this code could be improved to make this process easier?
3: What did you learn about design while working on this lab?

Submission instructions
--------------------------

You do **NOT** need to fix the bugs that already existed in the provide code.

All files should be placed in a single package and your code should run with them in this position.  That package should be named `checkers`.

Open the `checkers` package folder in explorer and zip this file.  Do NOT zip your IntelliJ project's root folder; zip only the package folder.

To check that your zip is correct, open it up. Inside the zip you should see the folder `checkers`, and within that folder should be all of your files, without any other folders in the zip file.

The files you should include are:

* All your .java files
* Your .fxml file
* The reflections.md file.
