Data Science Project Lifecycle  

Name: Tyeshia Taylor 
Dataset: https://data.humdata.org/dataset/emdat-country-profiles 

Link to Streamlit app: https://dparicmfimwkt8bfjy8xqd.streamlit.app/ 

Aims and Objectives  
The dataset selected for this project is the EM-DAT Country Profiles dataset from the Humanitarian Data Exchange (HDX). The dataset contains information for natural disasters that have happened globally from 2000 to 2026. Each row has the year, country, and disaster subtype, and includes the following key statistics: total number of events, total people affected, total deaths, and total economic damage (both original and inflation-adjusted USD values). The dataset has 6,482 rows and 13 columns.  

The primary aim of this project is to develop an interactive Streamlit dashboard that enables people interested in the effects sustainability to explore and understand the human impact of natural weather hazards on a global scale. 
The primary aim of this project is to develop an interactive Streamlit dashboard that enables people interested in the effects sustainability to explore and understand the human impact of natural weather hazards on a global scale. 

The Key Objectives: 

To identify and visualise which countries are most affected by natural weather hazards in terms of human casualties and displacement. 

To analyze trends in disaster-related deaths and affected populations over the years 

To compare the human cost versus the economic cost of different disaster types globally. 

To provide an interactive and filterable dashboard that allows users to explore the data by year, disaster type and country. 

To highlight key insights relevant to global sustainability. 

The insights selected focus on the human effects of weather hazard. Understanding which hazard types cause the most deaths, which countries are repeatedly affected, and how trends have changed over time as it will help predict and prevent such extreme effects in the future, 

Development Methodology  
For this project, I chose to use an Agile development approach as it focuses on building software in small steps rather than planning everything at once in the start. This makes it easier to stay flexible, test things regularly, and keep improving the dashboard as it is made. Instead of following a strict, linear process, I was able to create parts of the project in sections and review how they worked then make changes before moving on. This method was the best fit because it supported the evolving nature of the project. It allowed me to gradually build, test, and refine the dashboard, making improvements as new insights emerged. 
 

Sprint 

Activity 

Outcome 

Sprint 1 

Dataset selection, approval, and initial exploration. Loading data into pandas and identifying key columns. 

Clean dataset loaded; column names confirmed; missing values identified. 

Sprint 2 

Setup of GitHub repository with main and dev branches. Creation of initial app.py with page config, sidebar filters, and KPI cards. 

Working skeleton app running locally on Streamlit. 

Sprint 3 

Development of all five chart sections: world map, trends over time, disaster type breakdown, economic vs human cost, and data explorer. 

Full dashboard with interactive charts deployed and running. 

Sprint 4 

Testing of all functional requirements, bug fixes, final deployment to Streamlit Community Cloud, and video recording. 

Live published app; completed test log; submitted report. 

 

Requirements List: 

ID 

Requirement 

Description 

FR1 

Load Dataset 

The application must load the EM-DAT Country Profiles Excel dataset and display it without errors. 

FR2 

Year Range Filter 

The user must be able to filter all visualisations by selecting a year range using a slider. 

FR3 

Disaster Type Filter 

The user must be able to filter data by one or more disaster types using a multiselect widget. 

FR4 

Disaster Subgroup Filter 

The user must be able to filter data by disaster subgroup (e.g. Hydrological, Meteorological). 

FR5 

Country Filter 

The user must be able to optionally filter data by one or more specific countries. 

FR6 

KPI Summary Cards 

The dashboard must display summary KPI cards showing total deaths, total affected, total events, and total economic damage for the filtered data. 

FR7 

Choropleth World Map 

The dashboard must display a choropleth world map coloured by the selected metric (deaths, affected, or events). 

FR8 

Map Metric Toggle 

The user must be able to switch the map colouring between Total Deaths, Total Affected, and Total Events. 

FR9 

Deaths Over Time Chart 

The dashboard must display a line chart showing total deaths per year for the filtered data. 

FR10 

Affected by Type Area Chart 

The dashboard must display a stacked area chart of people affected over time, broken down by disaster type. 

FR11 

Deaths by Type Bar Chart 

The dashboard must display a horizontal bar chart showing total deaths by disaster type. 

FR12 

Events Donut Chart 

The dashboard must display a donut chart showing the proportion of events by disaster subgroup. 

FR13 

Scatter Plot 

The dashboard must display a bubble scatter plot comparing economic damage versus deaths per country. 

FR14 

Top 10 Countries Chart 

The dashboard must display a bar chart of the top 10 most affected countries. 

FR15 

Data Explorer Table 

The dashboard must include an expandable section showing the full filtered dataset as a table. 

 

Non-functional requirements describe the quality and operational characteristics of the dashboard. 

ID 

Requirement 

Description 

NFR1 

Performance 

The dashboard must load and render all charts within 5 seconds on a standard internet connection. 

NFR2 

Usability 

The dashboard must have a clear, intuitive layout that requires no prior training to navigate. 

NFR3 

Accessibility 

All charts must include clear titles and axis labels so that data can be interpreted without additional explanation. 

NFR4 

Reliability 

The application must not crash or produce errors under normal usage with the provided dataset. 

NFR5 

Compatibility 

The dashboard must be accessible via a standard web browser without requiring any software installation by the user. 

NFR6 

Maintainability 

The source code must be version-controlled using Git and hosted on a public GitHub repository with meaningful commit messages. 

Test Cases: 

The following five test cases cover the core functional requirements of the dashboard. Each test case has been designed to verify a specific interactive element of the application. 

TC1 — Dataset Loading 

Field 

Detail 

Description 

Verify that the application successfully loads the EM-DAT dataset on startup with no errors. 

Steps and Input Data 

1. Navigate to the deployed Streamlit app URL. 2. Wait for the app to fully load. 3. Observe the KPI cards at the top of the dashboard. 

Dependencies 

The Excel file must be present in the data/ directory. openpyxl must be installed. 

Expected Result 

The dashboard loads fully with no error messages. KPI cards display numeric values for deaths, affected, events, and damage. 

  

TC2 — Year Range Filter 

Field 

Detail 

Description 

Verify that adjusting the year range slider correctly filters all charts to the selected time period. 

Steps and Input Data 

1. Open the sidebar. 2. Move the year range slider to 2010–2015. 3. Observe the deaths over time line chart and KPI cards. 

Dependencies 

FR2 — Year Range Filter. Dataset must be loaded successfully (TC1 must pass). 

Expected Result 

The line chart displays only data from 2010 to 2015. KPI card values update to reflect only that time period. 

  

TC3 — Disaster Type Filter 

Field 

Detail 

Description 

Verify that selecting a specific disaster type correctly filters all visualisations. 

Steps and Input Data 

1. In the sidebar, deselect all disaster types. 2. Select only ‘Flood’. 3. Observe the world map, bar chart, and KPI cards. 

Dependencies 

FR3 — Disaster Type Filter. TC1 must pass. 

Expected Result 

All charts update to show flood data only. The donut chart shows 100% Hydrological. The KPI cards reflect flood-only totals. 

  

TC4 — Map Metric Toggle 

Field 

Detail 

Description 

Verify that the map metric radio button correctly updates the choropleth map colouring. 

Steps and Input Data 

1. Observe the world map with default setting (Total Deaths). 2. Click ‘Total Affected’ radio button. 3. Click ‘Total Events’ radio button. 

Dependencies 

FR7, FR8 — Choropleth Map and Map Metric Toggle. TC1 must pass. 

Expected Result 

The map colour scale updates each time the radio button is changed. Countries with higher values for the selected metric appear darker. 

  

TC5 — Data Explorer Table 

Field 

Detail 

Description 

Verify that the data explorer expander displays the correctly filtered dataset as a table. 

Steps and Input Data 

1. Set the country filter to ‘India’ only. 2. Scroll to the bottom of the dashboard. 3. Click ‘View filtered dataset’ expander. 4. Check that only India rows are shown. 

Dependencies 

FR5, FR15 — Country Filter and Data Explorer Table. TC1 must pass. 

Expected Result 

The table displays only rows where Country is India. No rows from other countries are visible. 

 

Test Log: 

 All tests were executed by me. 

TC 

Date 

Result 

Pass/Fail 

Notes 

TC1 

28/04/2026 

Dashboard loaded successfully. All four KPI cards displayed correct numeric values. No errors observed. 

Pass 

No issues. 

TC2 

28/04/2026 

Adjusting the year slider to 2010–2015 updated the line chart and all KPI values correctly. 

Pass 

Charts updated within 2 seconds. 

TC3 

28/04/2026 

Selecting only ‘Flood’ updated all charts to show flood data only. Donut chart showed Hydrological only. 

Pass 

No issues. 

TC4 

28/04/2026 

Switching map metric between Total Deaths, Total Affected, and Total Events updated the choropleth colours correctly each time. 

Pass 

No issues. 

TC5 

28/04/2026 

Setting country filter to India and opening the data explorer showed only India rows in the table. 

Pass 

No issues. 


