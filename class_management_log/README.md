# Class Management Log

This program is designed to log any interactions with your students related to class management. It reads students names from a text file, creates Excel workbooks for each period along with one page per student, then allows you to quickly document infraction, consequence level, and notes.

## Getting Started

An [executable file](management_log.exe) is available for windows download. In order to run this program you need the exectuable file, at least one txt file with student names in the format "period_(number).txt" for periods 1 - 8, and Microsoft Excel. The executable file needs to be in the same folder as the txt file(s).

When running the program you should see something similar to this:

![capture](https://user-images.githubusercontent.com/41200583/45598202-85c3b600-b99d-11e8-89f1-9d6eedc8363d.JPG)

### Prerequisites

This program is compatible with Windows, Mac, and Linux. It has only been tested with Windows 10 and is not guaranteed to work with any previous versions. Since this program uses f-strings you must have Python 3.6 installed in order to run the code. Alternately, you can edit the file to remove f-strings and format with a way that is compatible with your version. You will also need Microsoft Excel installed.

### Packaging
This program was packaged using PyInstaller Version 3.3.1. 

Instructions for Windows:
- Open the command prompt 
- Change to working directory that your script is contained in
- Ensure the Assets folder with the icons are included in the directory with your .py script

From the command line:
```
pyi-makespec --onefile --windowed --icon=Assets\\icon.ico management_log.py
```

Edit the .spec file to look like [management_log.spec](management_log.spec)
Then run:

```
pyinstaller management_log.spec
```

You should have 2-3 new folders created. 'build', 'dist', and possibly '_pycache_'.
Inside the 'dist' folder will be your executable file.

## Authors

* **Thomas Kellough** - *Initial work* - [Github](https://github.com/thomaskellough)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
