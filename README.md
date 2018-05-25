# Database News Reporting Tool

## Created by Justin Schlump

### About
This script contains 3 queries from a news article database.  The first query
is for the most popular news articles of all time.  The second query is for
the most popular article's author of all time.  The third query is for the
days in which over 1% of requests led to errors.

### Running it
1. Open your terminal/console of choice.
2. Ensure the news database and "newsdata.sql" file are in active directory.
3. Connect to the news database and add the sql views shown below.
4. Run the script("news_reporting_tool.py").
5. Enjoy results.


### SQL View Code:
   ```
   create or replace view total_views as
   select date(time), count(*) as views
   from log
   group by date
   order by views desc;
   ```
   ```
   create or replace view errors_per_day as
   select date(time), count(*)
   as errors
   from log
   where status = '404 NOT FOUND'
   group by status,date
   order by errors desc;
   ```

