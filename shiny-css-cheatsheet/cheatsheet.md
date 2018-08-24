# If you have trouble with the inspect element trick below are some basic CSS codes that will change each element. However, it's not inclusive and there are many more options that can be changed. These are just some basics that can really help you change how your program looks. 

### [Here](https://shiny.rstudio.com/tutorial/written-tutorial/lesson3/) is a program obtained from RShiny website. 

![cap1](https://user-images.githubusercontent.com/41200583/44592448-361b1180-a786-11e8-9739-4d14a10d327d.JPG)

Let's edit a few things in your CSS file and see what happens.

## Changing the heading:
```
.h2, h2 {
font-size: 30px;
color: white;
font-family: Courier New;
background: black;
}
.h3, h3 {
font-size: 24px;
color: darkblue;
font-family: Lucida Console;
background-color: orange;
}
```
Notice that there are multiple headings that can be used in CSS. You can change them individually or in multiple. This code changes any H2 headings to have a background of black and any H3 headings to have a background of orange. It also chnges the text color to white and darkblue, respectively. You can also use hex colors instead of typing out the names. 

![cap2](https://user-images.githubusercontent.com/41200583/44592526-77abbc80-a786-11e8-860d-d3cf5ff94bc4.JPG)

## Changing the background:
```
html {
font-size: 10px;
-webkit-tap-highlight-color: rgba(0,0,0,0);
background-color: lightblue;
}
```
Here we can change the background of the entire window. The code above changes it to light blue. 

![capture](https://user-images.githubusercontent.com/41200583/44592765-25b76680-a787-11e8-8520-3065d9134edf.JPG)

## Changing the background Pt 2:
Notice how the background only changed to light blue at the bottom of the program? That's because this code contains fluidRows in the fluidPage. They have their own background. It can be edited with the code below. 

```
.container-fluid {
padding-right: 15px;
padding-left: 15px;
margin-right: auto;
margin-left: auto;
background-color: yellow;
}
```

![capture](https://user-images.githubusercontent.com/41200583/44592937-978fb000-a787-11e8-87ef-c07e09801919.JPG)

## Changing the buttons:

```
.btn-default {
color: white;
background-color: darkred;
border-color: white;
}
```

![capture](https://user-images.githubusercontent.com/41200583/44593027-e63d4a00-a787-11e8-8237-671893552638.JPG)

Notice that this changes multiple buttons, but not the submit button. That has its own code. 

### Pay attention here. Remember when we changed the fluidRow using the .container-fluid{} function? That will change the entire container that your widgets are in from RShiny. What if you want to change just the color of the rows? 

```
.row {
margin-right: -15px;
margin-left: -15px;
background-color: pink;
}
```

![capture](https://user-images.githubusercontent.com/41200583/44593870-3ddcb500-a78a-11e8-8da7-ac00f4b92bdb.JPG)

Here, the fluidRows are changed, but not the title panel. You can use this method to create banners.

## It's also possible to edit specific pieces of the widgets. This next code will change the size of the 'to' button from the date widget.

```
.input-group .form-control:not(:first-child):not(:last-child), 
.input-group-addon:not(:first-child):not(:last-child), 
.input-group-btn:not(:first-child):not(:last-child) {
border-radius: 0;
font-size: 20pt;
}
```

![capture](https://user-images.githubusercontent.com/41200583/44593999-98761100-a78a-11e8-84a8-850086035ac2.JPG)

## You can also change how things look when they are active or not active. Below is how you can change the input select items when you are activating them.

```
.selectize-control.single .selectize-input.input-active, 
.selectize-control.single .selectize-input.input-active input {
cursor: text;
color: purple;
font-size: 15pt;
}
```

![capture](https://user-images.githubusercontent.com/41200583/44594410-bb54f500-a78b-11e8-9f04-e150b11bad68.gif)


These are a few basic things to get you started. I would recommend looking up some tutorials over CSS to help you fully understand how it all works. However, if you don't want to learn it right now, but still want to style your R Shiny project, this is a good alternate solution. The code for this program is [here](https://github.com/thomaskellough/Personal-Projects/blob/add-css/shiny-css-cheatsheet/app.R) and the code for the css file is [here](https://github.com/thomaskellough/Personal-Projects/blob/add-css/shiny-css-cheatsheet/customcss.css).

Happy programming!
