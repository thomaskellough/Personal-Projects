library(shiny)
library(dplyr)
library(tidyverse)
library(DT)
library(shinydashboard)
library(shinyjs)
library(lubridate)
library(rsconnect)
library(readxl)

plotTheme <- function(){
  theme(plot.background = element_rect(fill = 'lightgray', color = 'lightgray'),
        panel.border = element_rect(color = 'black', fill = NA),
        title = element_text(color = 'midnightblue', size = 28),
        axis.title = element_text(color = 'blue', size = 24),
        axis.text = element_text(face = 'bold', size = 14),
        legend.text = element_text(size = 16),
        legend.background = element_rect(fill = 'lightblue', color = 'black'),
        legend.title = element_text(color = 'darkred'),
        strip.text = element_text(size = 12, face = 'bold'),
        strip.background = element_rect(fill = 'lightblue', color = 'black')
  )
}

ui <- fluidPage(
  
  useShinyjs(),
  theme = 'custom.css',
  
  dashboardPage(
    dashboardHeader(title = 'Student Grades', titleWidth = 235),
    dashboardSidebar(
      width = 235,
      fileInput(inputId = 'file', label = 'Select a file...'),
      uiOutput('periodSelection'),
      uiOutput('studentSelection'),
      dataTableOutput('individualSummary'),
      img(src='lhimg.JPG', width = '100%')
    ),
    
    dashboardBody(
      fluidRow(uiOutput('topbox')),
      fluidRow(
      tabBox(
        id = 'tabset1',
        width = '100%',
        tabPanel('Grades Graph', plotOutput('individualGraph')),
        tabPanel('Grades Table', dataTableOutput('summaryDT')),
        tabPanel('Summary by Unit', plotOutput('summaryBarGraph'), br(), dataTableOutput('summaryUnitDT')),
        tabPanel('Class Averages', plotOutput('classAverageGraph'), br(), dataTableOutput('classAverageTable'))
        )
      )
    )
  )
)


server <- function(input, output, session) {

  grades <- reactive({
    req(input$file)
    inFile <- input$file
    if (endsWith(inFile$name, '.xlsx')){
      gradesTbl <- read_excel(inFile$datapath)
      gradesTbl <- gradesTbl %>% 
        arrange(Period, Student, Date, Type) %>% 
        mutate(Date = as.Date(Date))
      return(gradesTbl)
    } else if (endsWith(inFile$name, 'csv')){
      gradesTbl <- read_csv(inFile$datapath)
      gradesTbl <- gradesTbl %>% 
        arrange(Period, Student, Date, Type) %>% 
        mutate(Date = mdy(Date))
      return(gradesTbl)
    }
  })
  

  findAverages <- function(data, student, period){
    data %>% 
      filter(Student == student, Period == period) %>% 
      group_by(Type) %>% 
      mutate(Average = round(mean(Grade), 2)) %>% 
      ungroup() %>% 
      select(Type, Average, Weight) %>% 
      unique() %>% 
      ungroup()
  }
  
  output$topbox <- renderUI({
    req(input$file)
    box(
    splitLayout(uiOutput('type'), uiOutput('unit')),
    solidHeader = T,
    status = 'success',
    collapsible = T)
  })
  
  # Allow student choices to be dependent on Period
  output$periodSelection <- renderUI({
    df <- data.frame(grades())
    req(input$file)
    selectInput(inputId = 'periodVar', 
                label = 'Select Period',
                choices = unique(df$Period))
  })
  output$studentSelection <- renderUI({
    df <- data.frame(grades())
    selectInput(inputId = 'studentVar', 
                label = 'Select Student', 
                choices = unique(df[df$Period==input$periodVar, 'Student']))
  })
  
  # Selection box to display type of grades
  output$type <- renderUI({
    df <- data.frame(grades())
    choices <- unique(pull(df, Type))
    checkboxGroupInput(inputId = 'typeVar',
                label = 'Select Type',
                choices = choices,
                selected = choices)
  })
  
  # Selection box to display different units
  output$unit <- renderUI({
    df <- data.frame(grades())
    choices <- unique(pull(df, Unit))
    checkboxGroupInput(inputId = 'unitVar',
                       label = 'Select Unit',
                       choices = choices,
                       selected = choices)
  })

  # Sidebar - Individual Summary
  output$individualSummary <- renderDataTable({
    req(input$studentVar)
    req(input$periodVar)
    # Get weighted average to add to datatable
    df <- data.frame(grades())
    studentAverage <- findAverages(df, input$studentVar, input$periodVar)  
    wm <- weighted.mean(studentAverage$Average, studentAverage$Weight)
    DT::datatable(
      df %>% 
        filter(Student == input$studentVar & Period == input$periodVar) %>% 
        group_by(Type) %>% 
        mutate(Average = round(mean(Grade), 2)) %>%
        ungroup() %>% 
        select(Type, Average) %>% 
        unique() %>% 
        ungroup() %>% 
        add_row(Type = 'Overall', Average = wm),
      options = list(dom = 't'),
      rownames = F,
      filter = 'none'
    )
  })

  
  # Tab 1 - Individual Grades Graph
  output$individualGraph <- renderPlot({
    req(input$studentVar)
    req(input$periodVar)
    df <- data.frame(grades())
    df %>% 
      filter((Student == input$studentVar) & (Period == input$periodVar) & (Type %in% input$typeVar) & (Unit %in% input$unitVar)) %>% 
      ggplot(aes(x = Date, y = Grade, 
                 color = Type, shape = Unit)) +
      geom_point(size = 4) + 
      ggtitle(paste(input$studentVar, "'s Individual Grades", sep = '')) +
      plotTheme() +
      scale_shape_manual(values = 1:10) +
      facet_wrap(Unit~.) +
      scale_color_manual(values = c('#E51A1D', '#377DB9', '#4EAE4A'))
  })
  
  # Tab 2 - Individual Full Data Table
  output$summaryDT <- renderDataTable({
    req(input$studentVar)
    req(input$periodVar)
    df <- data.frame(grades())
    DT::datatable(
      df %>% 
        filter((Student == input$studentVar) & (Period == input$periodVar) & (Type %in% input$typeVar) & (Unit %in% input$unitVar)),
      options = list(paging = F),
      rownames = F)
  })
  
  # Tab 3 - Individual Average By Unit Graph
  output$summaryBarGraph <- renderPlot({
    req(input$studentVar)
    req(input$periodVar)
    df <- data.frame(grades())
    df %>% 
      filter((Student == input$studentVar) & (Period == input$periodVar) & (Type %in% input$typeVar) & (Unit %in% input$unitVar)) %>% 
      group_by(Unit, Type) %>% 
      mutate(Average = round(mean(Grade), 2)) %>%
      ungroup() %>% 
      select(Unit, Type, Average) %>% 
      unique() %>% 
      ggplot(aes(x = Unit, y = Average, fill = Type)) +
      geom_bar(position = 'dodge', stat = 'identity', color = 'black') +
      geom_text(aes(label = Average), 
                position = position_dodge(width = 0.87), 
                vjust = 3.0,
                color = 'white',
                fontface = 'bold') +
      ggtitle(paste(input$studentVar, "'s Averages by Unit", sep = '')) +
      plotTheme() +
      scale_fill_brewer(palette = 'Set1')
  })
  
  # Tab 3 - Individual Average by Unit Data Table
  output$summaryUnitDT <- renderDataTable({
    req(input$studentVar)
    req(input$periodVar)
    df <- data.frame(grades())
    DT::datatable(
      df %>% 
        filter((Student == input$studentVar) & (Period == input$periodVar) & (Type %in% input$typeVar) & (Unit %in% input$unitVar)) %>% 
        group_by(Unit, Type) %>% 
        mutate(Average = round(mean(Grade), 2)) %>% 
        ungroup() %>% 
        select(Unit, Type, Average) %>% 
        unique(),
      options = list(paging = F),
      rownames = F)
  })
  
  # Tab 4 - Class Averages by Unit Graph
  output$classAverageGraph <- renderPlot({
    req(input$periodVar)
    df <- data.frame(grades())
    df %>% 
      filter((Period == input$periodVar) & (Type %in% input$typeVar) & (Unit %in% input$unitVar)) %>% 
      select(Unit, Type, Grade) %>% 
      unique() %>% 
      ggplot(aes(x = Type, y = Grade, fill = Type)) +
      geom_boxplot() +
      coord_flip() +
      facet_wrap(Unit~.) +
      ggtitle('Class Averages by Unit') +
      plotTheme() +
      scale_fill_brewer(palette = 'Set1')
  })
  
  # Tab 4 - Class Averages by Unit Data Table
  output$classAverageTable <- renderDataTable({
    req(input$periodVar)
    df <- data.frame(grades())
    DT::datatable(
      df %>% 
        filter((Period == input$periodVar) & (Type %in% input$typeVar) & (Unit %in% input$unitVar)) %>% 
        group_by(Type, Unit) %>%
        mutate(Average = round(mean(Grade)), 2) %>% 
        ungroup() %>% 
        select(Unit, Type, Average) %>% 
        unique(),
      rownames = F,
      options = list(paging = F)
    )
  })
}

shinyApp(ui = ui, server = server)
