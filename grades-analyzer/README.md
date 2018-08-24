# Student Grade Analyzer

This program is designed to quickly and efficiently analyze student grades. It creates tables and graphs that can hep quickly assess where a student may be struggling and where they are exceeding expectations. It also creates boxplots of entire class averages.

## Getting Started

The easiest way to use this program is by going directly my the shinyapps.io website. [Here](https://tkellough.shinyapps.io/grades/) is a direct link. As of right now, this program is free to use with a limited number of individuals. 

You will need either an excel or CSV file to upload in a specific format. You can download my sample files [here](assets).

| Date	    | Student	| Unit	        | Period	| Type	    | Grade	| Weight |
| --------- | ------- | ------------- | ------- | --------- | ----- | ------ |
| 8/30/2017	| Andy	  | Biochemistry	| 2	      | Homework	| 98	  | 15     |
| 8/31/2017	| Andy	  | Biochemistry	| 2	      | Homework	| 99    | 15     |


The other method is by coping the [source code](app.R) and running it through your R interpreter. Note: you will also need the [CSS](www/custom.css) file and the [logo](www/lhimg.JPG) to run the code. Or you can comment them out in the app.R file. 

When running the program you should see something similar to this:

![capture](https://user-images.githubusercontent.com/41200583/44596990-ca3fa580-a793-11e8-959d-a739d524e46b.JPG)
![capture](https://user-images.githubusercontent.com/41200583/44597071-12f75e80-a794-11e8-9a5e-859ea8b6076e.JPG)
![capture1](https://user-images.githubusercontent.com/41200583/44597076-1559b880-a794-11e8-9bab-fca0685cdda2.JPG)
![capture2](https://user-images.githubusercontent.com/41200583/44597077-17237c00-a794-11e8-981a-1a97cb2e9bc5.JPG)
![capture3](https://user-images.githubusercontent.com/41200583/44597084-1a1e6c80-a794-11e8-89ae-65e713213667.JPG)

You can quickly change the period and student with dropdown boxes on the side panel. You can also select which type of grades are shown and which units are shown witht the collapsable box above the graphs/tables. It can take an import from CSV or Excel files.

### Prerequisites

This program is compatible with Windows and Mac. It has only been tested with Windows 10 and is not guaranteed to work with any previous versions. The browsers it has has been tested on is Safari, Chrome (Version 68.0.3440.106 (Official Build) (64-bit)), Internet Explorer (Version 11.228.17134.0), and FireFox (Version 61.0 (64-bit)). Internet access is needed to use this program on shinyapps.io.

## Authors

* **Thomas Kellough** - *Initial work* - [Github](https://github.com/thomaskellough)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
