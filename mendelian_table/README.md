# Dihybrid Cross Mendelian Table

A dihybrid cross table is a table of potential phenotyes from two parents with two different observed traits. This program is designed to allow the user to choose the genotypes of each allele of each parent and print the results. The program prints out a grid of the possible combinations as well as the ratio of each phenotype produced. 

## Getting Started

An executable file is available for windows download. I will update an app for Mac soon. You can also run the source code directly without downloading the icon by commenting out the set_icon and resource_path functions on lines 37-52. You will also need to comment out calling the function on line 244. The program should be compatible with linux, but it has not been tested.
  

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
pyi-makespec --onefile --windowed --icon=Assets\\icon.ico mendelian_table.py
```

Edit the .spec file to look like [mendelian_table.spec](mendelian_table.spec)
Then run:

```
pyinstaller mendelian_table.spec
```

You should have 2-3 new folders created. 'build', 'dist', and possibly '_pycache_'
Inside the 'dist' folder will be your executable file.

## Authors

* **Thomas Kellough** - *Initial work* - [Github](https://github.com/thomaskellough)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
