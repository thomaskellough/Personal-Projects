# Gene Expression

This program is designed to let users practice transcription and translation using a GUI. It allows the user to input their own DNA strands or generate random strands. Then the user can input an mRNA strand, tRNA strand, and amino acid sequence and check their answers. The user can also obtain the answers inside the program.

## Getting Started

An executable file is available for windows download. I will update an app for Mac soon. You can also run the source code directly without downloading the icon by commenting out the set_icon and resource_path functions on lines 130-145. You will also need to comment out calling the function on line 383. The program should be compatible with linux, but it has not been tested.

### Prerequisites

This program is compatible with Windows and Mac. It has only been tested with Windows 10 and is not guaranteed to work with any previous versions. Since this program uses f-strings you must have Python 3.6 installed in order to run the code. Alternately, you can edit the file to remove f-strings and format with a way that is compatible with your version. 

### Packaging
This program was packaged using PyInstaller Version 3.3.1. 

Instructions for Windows:
- Open the command prompt 
- Change to working directory that your script is contained in
- Ensure the Assets folder with the icon is included in the directory with your .py script

From the command line:
'''
pyi-makespec --onefile --windowed --icon=Assets\\icon.ico gene_expression.py
'''

Edit the .spec file to look like gene_expression.spec
Then run:

'''
pyinstaller gene_expression.spec
'''

You should have 2-3 new folders created. 'build', 'dist', and possibly '_pycache_'
Inside the 'dist' folder will be your executable file.

## Authors

* **Thomas Kellough** - [Github](https://github.com/thomaskellough)
See also the list of [contributors](https://github.com/thomaskellough/Personal-Projects/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
