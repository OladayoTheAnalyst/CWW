# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt

# create a list of years form 2011-2020
years = [*range(2011, 2021, 1)]
# create a list durations of average movie lengths
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
# create a dictionary with keys years & durations
movie_dict = {"years": years, "durations": durations}
print(movie_dict)  # print the movie dictionary

# creating a Dataframe object
durations_df = pd.DataFrame(movie_dict)
print(durations_df)  # print the dataframe

# define data values
x = durations_df.years  # X-axis points
y = durations_df.durations  # Y-axis points
plt.plot(x, y)  # Plot the line graph
plt.title("Netflix Movie Durations 2011-2020")
plt.show()  # display graph

# create dataframe from netflix csv file
netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df.head(5))  # print first 5 rows of dataframe

netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']  # subset where type is Movie
# subset by columns
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]
print(netflix_movies_col_subset.head(5))  # print first 5 rows of dataframe

# define data values
x = netflix_movies_col_subset.release_year  # X-axis points
y = netflix_movies_col_subset.duration  # Y-axis points
plt.scatter(x, y)  # Draw a scatter plot
plt.title("Movie Duration by Year of Release")
plt.show()  # display plot

# movies with duration fewer than 60
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
print(short_movies.head(20))  # print first 20 rows of dataframe

colors = []
color_switcher = {
    'Children': 'red',
    'Documentaries': 'blue',
    'Stand-Up': 'green'
}
for index in netflix_movies_col_subset.index:
    colors.append(color_switcher.get(netflix_movies_col_subset['genre'][index], 'black'))

for i in range(0, 10):  # print first 10 values of colors list
    print(colors[i])

# define data values
x = netflix_movies_col_subset.release_year  # X-axis points
y = netflix_movies_col_subset.duration  # Y-axis points
plt.scatter(x, y, c=colors)  # Draw a scatter plot
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.show()  # display plot
