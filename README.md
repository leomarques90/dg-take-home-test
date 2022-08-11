# DG Take Home Test
This repo was created to solve the business necessities described on the topic `The Exercise`.

# How to run it
1. Create a .env file according to the template and add API_KEY from [openweather](https://home.openweathermap.org/api_keys)

2. Run the following script:
```sh
docker-compose up --build
```

# About the solution
I developed a solution to:
- Get lat and long data from 10 cities and store it into `data/01_raw/` directory;
- Read [daily weather data](https://api.openweathermap.org/data/2.5/onecall/timemachine) from current day minus 6 until yesterday according to the day that the script is being executed.
    - Storing it on a path called `data/02_refined`;
    - Inserting its data on a table.
- Finally processing the data stored before to insert into tables that satisfy the requirements.

## Considerations
- The paths doesn't need to exist;
- The tables are created automatically;
- I implemented the idempotency on database, by choosing keys that guarantee that the data will not be duplicated;
- If the files are already presented, the API is not called. I developed in that way thinking about the limit of 1000;
- Some functions were designing thinking about a data-oriented programming approach;
- The functions of script `02_transformation.py` that stores data into the database could be improved, but I think I'm taking too long to deploy this activity;
- I choose MySQL because it is listed on job description;
- Tests could be implemented, but I think I'm taking too long to deliver this.

# The exercise

Create Workflow in Python according to the following requirements:

Extract the last 5 days of data from the free API: https://api.openweathermap.org/data/2.5/onecall/timemachine (Historical weather data) from 10 different locations to choose by the candidate.

Build a repository of data where we will keep the data extracted from the API. This repository should only have deduplicated data. Idempotency should also be guaranteed.

Build another repository of data that will contain the results of the following calculations from the data stored in step 2.

A dataset containing the location, date and temperature of the highest temperatures reported by location and month.
A dataset containing the average temperature, min temperature, location of min temperature, and location of max temperature per day.


Extra information:

The candidate can choose which kind of db, or data formats are used as a repository of data for steps 2 and 3.
The deliverable should contain a docker-compose file so it can be run by running ‘docker-compose up’ command. If the workflow relies on any database or any other middleware, this docker-compose file should have all what is necessary to make the workflow work (except passwords for the API or any other secret information)
The code should be well structured and add necessary log traces to easily detect problems. 
