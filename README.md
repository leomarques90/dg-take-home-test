# dg-take-home-test

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

# How to run it
add .env file according to the template.

```sh
docker-compose up --build
```

# Considerations
There is a lot to improve, but I decided to prioritize delivery as soon as possible.