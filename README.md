# SSgui
A graphical user interface for Signals and Systems programs provided by professor Carlo Ciulla.

## Inspiration
For the past few weeks I have been taking Signals and Systems as well as some of you, and for every program
that we want to run in this course we have to write a significant line of text on our command prompt. 
I am sure we all have seen something like: `Laplace2019 lightSource139x139-XYpad5.img 139 139 0.5 0.5`.
The problem here, as far as I'm concerned, is that we have to run many programs like this during the semester, and I think
there is a better way to do all this.
## Dependencies
- Python 3.x, you must have python installed in your computer (I am assuming you already have it)
- PySimpleGUI, can be installed by opening cmd (<kbd>Win</kbd> + <kbd>R</kbd>, type `cmd`, hit `Enter`) and passing the command `pip install pysimplegui`
## Suggestions
1. __Use 1 main folder to contain every material that was provided by the professor__ (We will call this folder Signals_and_Systems)
2. __MAKE SURE THAT THE PATH TO THAT FOLDER DOES NOT CONTAIN ANY SPACES OR SPECIAL CHARACTERS__
    - This is essencial to run the program
    - it is advised the path must only contain letters numbers and dashes ( - ) or underlines ( _ )
        - C:\Users\Desktop\Signals and Systems\  is not considered a "good" path. Change it to: C:\Users\Desktop\Signals_and_Systems\

How to get the path of a folder
- ![picture alt](https://www.howtogeek.com/wp-content/uploads/2013/03/01_getting_directory_for_default.png "How to get path of a folder")
## How to use
1. Download ZIP 
2. Extract ZIP 
    1. Usually, do an "Extract Here"
3. Inside the folder there must me 2 python files and 1 readme file, ignore the readme
4. Open built.py with an editor of your choice (I recommend VS Code but notepad will do fine)
5. In the 9th line set the PATH variable to your desire
    - If you have for example a folder named Signals_and_Systems somewhere on your computer where you keep all the files provided by the professor
    find its path, copy it and paste it into `PATH="your-path-here"`
    - Please make sure that all the .exe files (like Laplace2019.exe or FTinvFT2018.exe) and .img files are in Signals_and_Systems folder or its subfolders.
6. Save your changes (<kbd>Ctrl</kbd> + <kbd>S</kbd>)
7. Open command prompt
8. Copy the path of the folder where gui.py is
9. In command prompt type `cd "path-you-coppied-in-step-8"`
    - Be careful because if you have it saved in another drive like drive D: you need to type `D:` in command prompt to go to the desired path
10. Type `python gui.py`

Now you must see a simple window. In the first dropdown form you can select the program you want to run. In the second one you can select which .img file you want to process
and in second and third you need to write the dimensions of that image as you do. Fifth form is reserved for additional commands you might wanna pass like we do in the Laplace2019 example.
## Limitations
The interface is designed to pass a specific type of command of the form: <..program..> <..image file..> <..image x dimension..> <..image y dimension..> <...additional arguments>.
If in the future we deal with other programs that do not follow this order we might encounter problems, but nevertheless we can modify the program to fit our needs...
## What it looks like
![App](images/App.JPG)
![dropdown](images/dropdown.JPG)

