# Test Generator

This program is designed to create a random test with up to four different keys from a test bank excel file.

## Getting Started

An executable file is available for windows download. In order to run this program you need an test bank from an excel file in the proper format. A sample file is available for download [here](sample_test_bank.xlsx). <br/><br/>
You can also have pictures included in your questions. To achieve this name type the name of your image inside parentheses at the beginning of the question, then place the image inside a folder named Images within the same directory of your executable file. At this now only .png images are supported. For example: <br/><br/>

| Unique_ID	| Chapter |   Unit   |                  Question                  |           Answer            |         Incorrect1         |         Incorrect2         |         Incorrect3          |         Incorrect4          | 
| --------- | ------- | -------- | ------------------------------------------ | --------------------------- | -------------------------- | -------------------------- | --------------------------- | --------------------------- |
|     1	    |    11   |	Taxonomy |	(Taxonomy_01) Name the 3 domains of life: | Bacteria, Archaea & Eukarya | Protista, Bacteria & Fungi | Animalia, Protista & Fungi | Bacteria, Animalia & Archae | Bacteria, Archaea & Eukarya |

Then save a picture named "Taxonomy_01.png" inside your "Images" folder. <br/> 
An example of the directory setup and image folder may look something like this.

![Capture1](https://user-images.githubusercontent.com/41200583/56541165-88d4e500-6530-11e9-9fe6-560aeff08af8.PNG)<br/><br/>
![Capture2](https://user-images.githubusercontent.com/41200583/56541167-8a9ea880-6530-11e9-9d85-8a541464f280.PNG)<br/><br/>
When running the program you should see this screen. Select the current unit you want the majority of your test over and the number of questions you want from that unit. The number selected for previous unit will randomly select from all other units.<br/><br/>
![Capture](https://user-images.githubusercontent.com/41200583/56541169-8c686c00-6530-11e9-9006-823e5cdfeeb6.PNG)
Create a name for your test and select how many variations you want in the "Number of keys" spinbox. Then select from 3-5 answer options in the next spin box.<br/><br/>
Once you click "Create test" the test/s will be created with the filename and keyname. Look through each test to adjust any picture sizes as well as fixing the numbering in each key at the bottom of the test. You will need to right click the first answer in the key and select "Restart numbering"


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
