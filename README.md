# Database News Reporting Tool

## Created by Justin Schlump

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

