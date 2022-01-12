from baseball_scraper import batting_stats_range
data = batting_stats_range('2019-03-15', '2019-10-15')
data.to_csv("out.csv")