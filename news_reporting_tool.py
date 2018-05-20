import psycopg2

DBNAME = "news"


def get_most_popular_articles():
    try:
        conn = psycopg2.connect(database=DBNAME)
        print("Connected to database...")
    except (psycopg2.Error) as e:
        print(e)

    cur = conn.cursor()
    cur.execute(
        """select articles.title, count(log.id) as views
           from articles, log
           where concat('/article/', articles.slug) = log.path
           group by articles.title
           order by views desc""")
    rows = cur.fetchall()
    for row in rows:
        print("\"" + row[0] + "\" - " + str(row[1]) + " views")
    conn.close()


get_most_popular_articles()
