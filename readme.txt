key.py and emails.py are used to generate yearly files for keyword usage by section and keyword usage by person (email), respectively

query_* does same as above, but prints to screen instead of to a CSV file

keyDictionary.py is used to combine results of above using python dictionaries

merge_all_keyword_counts.py takes yearly files that result from keyDictionary.py and merges them into one master CSV file

agu_queries.py has SPARQL queries used in ESIP analysis of subset_agu_by_esip.py

visualization/ contains Python code for creating heatmaps and force directed diagrams
