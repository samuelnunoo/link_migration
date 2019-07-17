
#https://stackoverflow.com/questions/51800122/using-openpyxl-to-find-rows-that-contain-cell-with-specific-value-python-3-6
import pandas as pd
import re
import csv

base_url = 'https://www.hmc.edu/cis/'
sql = pd.read_excel("mysql_tables.xlsx")





def Iterates():
    with open ("links.csv",'r+') as f:
        with open('file.txt','w+') as file:
            reader = csv.reader(f, delimiter = '\n')

            for content in reader:
                content = content[0]
                query = re.search(r"p=\d+", content)
                if query:
                    post_id = re.search(r"\d+", query.group()).group()

                    if post_id:
                        print("ok",post_id)
                        extracted_date = sql[sql['ID'] == int(post_id)]['post_date'].values[0].__str__()

                        extracted_date = re.match(r'\d{4}-\d{2}-\d{2}', extracted_date).group()
                        new_date = re.sub('-', '/', extracted_date) + '/'
                        slug = sql[sql['ID'] == int(post_id)]['post_name'].values[0].__str__()

                        # New Url
                        url = base_url + new_date + slug
                        string = "Original| {content} | New | {url} \n".format(content=content, url=url)
                        file.write(string)




              




    f.close()
    file.close()









Iterates()



