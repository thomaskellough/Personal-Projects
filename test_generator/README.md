# Test Generator

This program is designed to create a random test with up to four different keys from a test bank excel file.

## Getting Started

An executable file is available for windows download. In order to run this program you need an test bank from an excel file in the proper format. A sample file is available for download [here](sample_test_bank.xlsx). <br/><br/>
You can also have pictures included in your questions. To achieve this name type the name of your image inside parentheses at the beginning of the question, then place the image inside a folder named Images within the same directory of your executable file. At this now only .png images are supported. For example: <br/><br/>

| Unique_ID	| Chapter |   Unit   |                  Question                  |           Answer            |         Incorrect1         |         Incorrect2         |         Incorrect3          |         Incorrect4          | 
| --------- | ------- | -------- | ------------------------------------------ | --------------------------- | -------------------------- | -------------------------- | --------------------------- | --------------------------- |
|     1	    |    11   |	Taxonomy |	(Taxonomy_01) Name the 3 domains of life: | Bacteria, Archaea & Eukarya | Protista, Bacteria & Fungi | Animalia, Protista & Fungi | Bacteria, Animalia & Archae | Bacteria, Archaea & Eukarya |

Then save a picture named "Taxonomy_01.png" inside your "Images" folder. <br/><br/>


### Prerequisites

This program is compatible with Windows and Mac. It has only been tested with Windows 10 and is not guaranteed to work with any previous versions. Since this program uses f-strings you must have Python 3.6 or greater installed in order to run the code. Alternately, you can edit the file to remove f-strings and format with a way that is compatible with your version. 

### Packaging
This program was packaged using PyInstaller Version 3.4. 

Instructions for Windows:
- Open the command prompt 
- Change to working directory that your script is contained in
- Ensure the Assets folder with the icon is included in the directory with your .py script

From the command line:
```
pyi-makespec --onefile --windowed --icon=Assets\\icon.ico test_generator.py
```

Edit the .spec file to look like [test_generator.spec](test_generator.spec)
Then run:

```
pyinstaller test_generator.spec
```

You should have 2-3 new folders created. 'build', 'dist', and possibly '_pycache_'
Inside the 'dist' folder will be your executable file.

## Authors

* **Thomas Kellough** - *Initial work* - [Github](https://github.com/thomaskellough)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
