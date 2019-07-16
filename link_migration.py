#https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook


'''from openpyxl import load_workbook

wb = load_workbook(filename = 'mysql_tables.xlsx')
posts = wb['wp_posts']
'''


#https://stackoverflow.com/questions/51800122/using-openpyxl-to-find-rows-that-contain-cell-with-specific-value-python-3-6
import pandas as pd
import re

base_url = 'https://www.hmc.edu/cis/'
sql = pd.read_excel("mysql_tables.xlsx")
links = pd.read_excel('links.xlsx')




Link_Migrations = {}


def Iterate():
    with open ("links.txt",'w+') as f:
        for index,row in links['Links'].iteritems():

            query = re.search("?p=\d+",row).group()
            post_id = re.search("\d+", query).group()

            if post_id:

                #Conversions
                extracted_date = sql[sql['ID']== post_id]['post_date'].values[0].__str__()
                extracted_date = re.match('\d{4}-\d{2}-\d{2}',extracted_date).group()
                new_date = re.sub('-','/',extracted_date) + '/'
                slug = sql[sql['ID'] == post_id]['post_name'].values[0]


                #New Url
                url = base_url + new_date + slug

                f.write("Original| {0} | New | {1} ").format(row,url)

    f.close()

    











