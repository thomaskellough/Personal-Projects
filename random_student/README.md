# Random Student Generator

This program is designed to randomly select either a student, pair of students, or group of four students and display it onto the screen. A random image is also displayed on the screen next to the name(s).  

## Getting Started

An executable file is available for windows download. In order to run this program you need the exectuable file, at least one txt file with names in the format "period_(number).txt" from periods 1 - 8, and a folder of images you want to display. The executable file needs to be in the same folder as the txt files, while the pictures need to be in their own folder named 'pictures' which is in the same directory as the exectuable file. Below is an example of how your directory may look. 

 ![pic1](https://user-images.githubusercontent.com/41200583/43981208-7c078f14-9cb6-11e8-9250-d3cf8b2455ee.JPG)
 
You may have additional files in the directory without causing any problems, but at minimum, one txt file in the correct format, the exe file, and picture folder with at least one picture. This is done so you can edit names and pictures without having to edit the script itself and refreeze the script. 

When running the program you should see something similar to this:

![pic2](https://user-images.githubusercontent.com/41200583/43981491-ad6a7c78-9cb7-11e8-84d2-2abfc2aa84ce.JPG)


### Prerequisites

This program is compatible with Windows and Mac. It has only been tested with Windows 10 and is not guaranteed to work with any previous versions. Since this program uses f-strings you must have Python 3.6 installed in order to run the code. Alternately, you can edit the file to remove f-strings and format with a way that is compatible with your version. 

### Packaging
This program was packaged using PyInstaller Version 3.3.1. 

Instructions for Windows:
- Open the command prompt 
- Change to working directory that your script is contained in
- Ensure the Assets folder with the icon is included in the directory with your .py script

From the command line:
```
pyi-makespec --onefile --windowed --icon=Assets\\icon.ico random_student.py
```

Edit the .spec file to look like [random_student.spec](random_student.spec)
Then run:

```
pyinstaller random_student.spec
```

You should have 2-3 new folders created. 'build', 'dist', and possibly '_pycache_'
Inside the 'dist' folder will be your executable file.

## Authors

* **Thomas Kellough** - *Initial work* - [Github](https://github.com/thomaskellough)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
