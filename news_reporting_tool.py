import psycopg2

DBNAME = "news"


def get_popular_articles():
    try:
        conn = psycopg2.connect(database=DBNAME)
        print("\nPOPULAR ARTICLES...")
        print("Connected to database...")
    except (psycopg2.Error) as e:
        print(e)
    cur = conn.cursor()
    cur.execute(
        """select articles.title, count(*) as views
           from articles, log
           where concat('/article/', articles.slug) = log.path
           group by articles.title
           order by views desc""")
    rows = cur.fetchall()
    for row in rows:
        print("\"" + row[0] + "\" - " + str(row[1]) + " views")
    conn.close()


def get_popular_authors():
    try:
        conn = psycopg2.connect(database=DBNAME)
        print("\nPOPULAR AUTHORS...")
        print("Connected to database...")
    except (psycopg2.Error) as e:
        print(e)
    cur = conn.cursor()
    cur.execute(
        """select authors.name, count(*) as views
           from log, articles, authors
           where concat('/article/', articles.slug) = log.path
           and articles.author = authors.id
           group by authors.name
           order by views desc""")
    rows = cur.fetchall()
    for row in rows:
        print("\"" + row[0] + "\" - " + str(row[1]) + " views")
    conn.close()


def get_request_errors():
    try:
        conn = psycopg2.connect(database=DBNAME)
        print("\nERRORS...")
        print("Connected to database...")
    except (psycopg2.Error) as e:
        print(e)
    cur = conn.cursor()
    cur.execute(
        """select to_char(time, 'MON DD YYYY'),
           round(((errors_per_day.errors::float / total_views.views)
           * 100)::numeric, 2)
           from log, errors_per_day, total_views
           where log.time = errors_per_day.date
           and errors_per_day.date = total_views.date
           and ((errors_per_day.errors::float / total_views.views) * 100) > 1
           group by time, errors_per_day.errors, total_views.views
           order by errors_per_day.errors desc;""")
    rows = cur.fetchall()
    for row in rows:
        print("\"" + row[0] + "\" - " + str(row[1]) + "% errors")
    conn.close()


get_popular_articles()
get_popular_authors()
get_request_errors()

"""create or replace view errors_per_day as
   select date(time), count(*)
   as errors
   from log
   where status = '404 NOT FOUND'
   group by status,date
   order by errors desc;
"""

"""create or replace view total_views as
   select date(time), count(*) as views
   from log
   group by date
   order by views desc;
"""
