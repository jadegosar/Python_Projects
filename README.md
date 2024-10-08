# Web Scraping and Converting information contained in PDFs to structured data in Python
This repository holds scipts created in Python to perform webpage scraping and converting PDFs to structured data.

## College_Sports_Web_Scraping.py

This script scrapes webpages that contain schedule information for all the sports teams from a D1 college. These webpages contained information on opponents, dates of games or competitions, location of event, and whether the outcome was a win or loss. It was requested that all schedules from 2016 forward for every varsity sports team be scraped to allow for a dataset to be created that aggregates all pertinent schedule information for all teams within the athletics program. 

**Project Description**

Webpage scraping of schedule information from all teams across an athletic program was completed as a first step to a larger project that was hoping to explore whether travel schedules and distance traveled by athletes had a relationship with specific types of injuries. To pursue this larger goal, schedule information needed to be collected from the webpages that represented the various teams and their competitions from 2016-2023. The main steps to achieve this objective were studying the html format of the webpages to understand where the pertinent information was stored in the underlying code, connecting to the target URL, and parsing the HTML content. The final step was to extract the actual data from the elements and repeat this process for the differing structures and nuances present across the various sports teams' webpages.

**Code considerations**

While many of the webpages followed a similar format, this was not true for all teams that were included. For example, there were a couple of sports that did not have varsity status in 2016 so considerations had to be made to correctly scrape the schedules of these teams such as setting different year parameters to search for in the loop that scraped all years of schedule information for a given team. Additionally, there are teams that have all games of their season in a single calendar year while others competition season will fall across multiple years (i.e. winter sports such as basketball or swimming and diving). To handle the differences in these two groups, two separate loops had to be created to support the differing format of the underlying webpages. Lastly, there was one team that had a slightly different structure to their schedule when compared to all the other sports in the athletics programs so additional code was created to handle the scraping of this team's schedules in a customized loop.

**Output**

The output of this script was datasets that contained "Team Name", "Date", and "Year". The "Team Name" column pulled the opponent from the schedule webpage, "Date" contained the date of the competition as represented on the website, and "Year" collected the year which was not represented in the date and needed to be pulled from the select option that specified the season year on the websites. The final dataset created contained an excel tab for each sports team that provided the data on opponent, date of competition, and season year for each of the sports programs across a D1 college athletic program. This file was used in the next step of a larger analysis where I scraped additional schedule information from these same webpages to get the location of the competition and denoted whether it was a home or away game for a project that was looking to explore injury rates based on miles traveled by the athletes.

## PDF converter.py

**File Description**

This Python file converts PDFs of in-game performance metrics collected by a basketball team to structured data that was usable in a larger project on team performance across a season. These PDFs were outputs from a program that the team uses to generate advanced statistics and evaluate performance of individual players and the team in the games across a season. In order to pull these metrics into a project that looked at relationships between sports science metrics and in-game performance as well as how preparation for each game may impact how well the team plays according to advanced metrics, there was a need to aggregate the data contained across the many PDFs into one usable dataset.

**Code considerations**

The main consideration that needed to be addressed when converting these PDF files was that there was both individual and team metrics contained in the file and not all metrics were available for both groups. For this reason, metrics that were collected for the individual players had to be treated differently than those that represented the performance of the team and their opponent, all of which were present in the same page of the reports. Additionally, there were '-' that needed to be replaced with NA values as they represented when there was not enough data to compute advanced metrics (i.e. effective Field Goal % if the given player did not take any shots in the game). Another major consideration when creating this script was how to make sure the metadata was getting tracked correctly so that we could link metrics from one sheet to the opponent and date of game that were given in the header of the reports. This was needed to be able to correctly identify which metrics were pulled from which game PDFs and eventually be able to merge this data with sports science metrics that were being collected by the Applied Health and Performance Science Department.

**Output**

The final output of this script was an excel file containing all relevant information from the PDF files with each tab representing a separate game across the season and both individual and team metrics represented. This data was then pulled into R and futher cleaning was performed to aggregate the individual and team data across all sheets into two distinct datasets, one that held individual statistics from all games with identifiers for opponent and date of game and another that contained team-related metrics from across the season with the same identifiers.
