from pandadataframe import create_dataframe
import numpy

df = create_dataframe()

# print df['country_name']
# print df[['country_name', 'gold']]
# print df.loc[5]
# print df[df['gold'] > 5]  # more than 5 gold medals
# print df[['country_name', 'gold']][df['gold'] < 5]  # more than 5 gold medals
# print df[['gold', 'silver']].apply(numpy.mean)  3 calculate the mean gold and silver medals resp.
# print df['bronze'].map(lambda x: x >= 5)  # has 5 or more bronze medals? boolean true/false
# print df[df['bronze'].map(lambda x: x >= 5)]  # has 5 or more bronze medals? whole df
# print df.applymap(lambda x: x >= 5)  # has 5 or more of each column? boolean true/false columns
# print df[df.applymap(lambda x: x >= 5)]  # has 5 or more of each column? boolean true/false or NaN


