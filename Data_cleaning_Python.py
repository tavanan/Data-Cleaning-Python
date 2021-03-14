import xml.etree.cElementTree as et
import pandas as pd
import numpy as np

# Parsing xml and convert to Dataframe
def parsing(path):

    data = et.iterparse(path, events=("start", "end"))
    data = iter(data)
    lis=[]
    ev, root = next(data)
    for ev, el in data:
        if ev == 'start' and el.tag == 'row':
            lis.append(el.attrib)

            root.clear()

    return pd.DataFrame(lis)


# function for reading dataset
def readData(path):
       Posts=parsing(path+"Posts.xml")
       Comments=parsing(path+"Comments.xml")
       Badges=parsing(path+"Badges.xml")
       PostLinks=parsing(path+"PostLinks.xml")
       PostHistory=parsing(path+"PostHistory.xml")
       Tags=parsing(path+"Tags.xml")
       Users=parsing(path+"Users.xml")
       Votes=parsing(path+"Votes.xml")
       return (Posts,Comments,Badges,PostLinks,PostHistory,Tags,Users,Votes)


# reading travel dataset
path='D:Project2/travel/'
travel_Posts,travel_Comments,travel_Badges,travel_PostLinks,travel_PostHistory,travel_Tags,travel_Users,travel_Votes=readData(path)

#reading health dataset
path='D:Project2/health/'
health_Posts,health_Comments,health_Badges,health_PostLinks,health_PostHistory,health_Tags,health_Users,health_Votes=readData(path)

#reading astronomy dataset
path='D:Project2/astronomy/'
astro_Posts,astro_Comments,astro_Badges,astro_PostLinks,astro_PostHistory,astro_Tags,astro_Users,astro_Votes=readData(path)

# name of ALL Columns
print('Posts: ',list(travel_Posts.columns),'\n')
print('Comment: ',list(travel_Comments.columns),'\n')
print('Badges: ',list(travel_Badges.columns),'\n')
print('PostHistory: ',list(travel_PostHistory.columns),'\n')
print('PostLinks: ',list(travel_PostLinks.columns),'\n')
print('Tags: ',list(travel_Tags.columns),'\n')
print('Users: ',list(travel_Users.columns),'\n')
print('Votes: ',list(travel_Votes.columns),'\n')


# Creating every dataset as a list of its tables 
travel=[travel_Posts,travel_Comments,travel_Badges,travel_PostLinks,travel_PostHistory,travel_Tags,travel_Users,travel_Votes]
health=[health_Posts,health_Comments,health_Badges,health_PostLinks,health_PostHistory,health_Tags,health_Users,health_Votes]
astronomy=[astro_Posts,astro_Comments,astro_Badges,astro_PostLinks,astro_PostHistory,astro_Tags,astro_Users,astro_Votes]


# function to information about percentage of missing value
def missing(data):
  for df in data:
     name =[x for x in globals() if globals()[x] is df][0]  # get name of table
     print(name,'\n')
     for col in df.columns:
       pct_missing = np.mean(df[col].isnull()) # get percentage of every column
       print('{} - {}%'.format(col, round(pct_missing*100)))
     print('End of dataframe \n \n')



# Printing percentage of missing value per website:
missing(travel)
missing(health)
missing(astronomy)



#function to replace all missing value with NA in a given website as an argument:
def replaceNA(d):
    for df in d:
        for col in df.columns:
            df[col] = df[col].fillna('NA')



replaceNA(travel)
replaceNA(health)
replaceNA(astronomy)

# printing sample table to see the result
print(travel[0].head())




#function stats which gies some basic statistics of each column and datatype
def stats(d):
    for df in d:
        name =[x for x in globals() if globals()[x] is df][0]
        print(name,':\n')
        for col in df.columns:
            print(col)
            print(df[col].describe(),'\n\n')


# print Statistics of websites:
stats(travel)
stats(health)
stats(astronomy)




#function Repetitive which find the columns of a table of a website(given as argument to the function) 
# wich has too many rows with sme values.I specify below to show variables with over 95% rows being the same value.
def Repetitive(data):
  for df in data:  
    name =[x for x in globals() if globals()[x] is df][0]
    print(name,':\n')
    num_rows = len(df.index)
    info = [] 

    for col in df.columns:
        
        cnt = df[col].value_counts(dropna=False)
        top_pct = (cnt/num_rows).iloc[0]
    
        if top_pct > 0.95:
            info.append(col)
            print('{0}: {1:.5f}%'.format(col, top_pct*100))
            print(cnt)
            print('\n\n')




# Printing variables with over 95% repetitive rows for websites:
Repetitive(travel)
Repetitive(health)
Repetitive(astronomy)



# THE END
