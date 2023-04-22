# sqlalchemy-challenge
Module 10 Challenge

# Climate Analysis

## Part 1: Analyze and Explore the Climate Data
### The Setup
Using the given files to complete a climate analysis and data exploration, SQLAlchemy was used to connect to the hawaii.sqlite data base. This was done using the create_engine() function. The automap_base() function was used to reflect tables into classes and references to the tables were saved. A SQLAlchemy session was created to link Python to the data base which was closed at the end of the notebook. 

## Precipitation Analysis
The first step in the analysis was to create a query to retrieve the most recent date in the dataset - 8/23/2017. Next, a query was created to collect the date and precipitation for the most recent year of data. The query results were saved as a Pandas DataFrame and sorted by date. Results were plotted, and can be seen below. Summary statistics were also generated for the dataframe, which can be accessed here:

[Link to Jupyter Notebook](https://github.com/maderamel/sqlalchemy-challenge/blob/2c0cd2e3020a1a34ec076c2b4c24935623d5648c/SurfsUp/climate_starter.ipynb)

![This is a screenshot of precipitation data from the most recent year](https://github.com/maderamel/sqlalchemy-challenge/blob/2c0cd2e3020a1a34ec076c2b4c24935623d5648c/SurfsUp/Resources/year_prcp_plot.png)


## Station Analysis
To begin, a query was designed to find the number of stations within the dataset. Next, a query was created to list the stations and observation counts in descending order. This allowed the most active station to be found - USC00519281. 

Another query was created to analyze the minimum, maximum, and average temperatures for that station:

* The lowest temperature for the most active station is 54.0
* The highest temperature for the most active station is 85.0
* The average temperature for the most active station is 71.66378066378067

A query was also designed to get the previous 12 months of temperature observation data (TOBS) and filtered by station with the most number of observations. Results were saved to a Pandas DataFrame and plotted as a histogram (below).

![This is a screenshot of temperature data from the last year of data](https://github.com/maderamel/sqlalchemy-challenge/blob/2c0cd2e3020a1a34ec076c2b4c24935623d5648c/SurfsUp/Resources/yr_temp_plot.png)


## Part 2: Design Your Climate App

### API Static Routes
1. The **homepage route** (/) was created with a list of all available routes.
2. A **precipitation route** (/api/v1.0/precipitation) was created to convert the query results from the precipitation analysis to a dictionary and return the JSON representation of that dictionary.
3. A **station route** (/api/v1.0/stations) was created to return a JSON list of stations from the dataset.
4. A **tobs route** (/api/v1.0/tobs) was created to returns jsonified data for the most active station for only the last year of data.

### API Dynamic Routes
5. A **start route** (/api/v1.0/<start>) was created that accepts the start date as a parameter from the URL and returns the min, max, and average temperatures calculated from the given start date to the end of the dataset.
6. A **start/end route** (/api/v1.0/<start>/<end>) was created that accepts the start and end dates as parameters from the URL  and returns the minimum, maximum, and average temperatures calculated from the given start date to the given end date. 