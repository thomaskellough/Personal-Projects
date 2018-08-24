#### The first thing you need to do is create your folder to contain your CSS file. This will be a folder named 'www' inside the same directory as your add.R file. Then you'll create a new text file and re-name it to contain a .css extension. You can now put all of your CSS code inside of this file. To edit the CSS file, simply right-click and click 'edit'. I use Notepad++ for this, but you can edit it with any text editor of your choosing. 

![createcssgif](https://user-images.githubusercontent.com/41200583/44587595-0a455f00-a779-11e8-8e17-e53ba567ccf4.gif)

#### If you want to find how to edit your CSS file for your project it only takes a couple of steps. Once you have your project run it in your browser or your window. Right click the content you want to change, click 'inspect' search throught the CSS styling in the new window that pops up. You can then edit specific contents inside this window to see what the change will look like. 

![buttongif](https://user-images.githubusercontent.com/41200583/44591075-5ba61c00-a782-11e8-90b1-1e5dc88ae091.gif)

#### Now how do you save it? Whatever you do here is not a permanent solution. You need to now add this code inside your CSS file. 

![savecss](https://user-images.githubusercontent.com/41200583/44589641-a9b92080-a77e-11e8-8446-bb8e20f01190.gif)


#### Using them css file inside your program is very easy. It's only one line of code. Inside your fluidPage, type in 

```theme = ('customcss.css')```

The code to create the above gif is here.

```
library(shiny)


ui <- fluidPage(
  
  theme = 'customcss.css',
  
  mainPanel(
    actionButton('action', 'Click me')
    )
)



server <- function(input, output, session) {
  
}

shinyApp(ui, server)```
