
import pandas as pd
import matplotlib.pyplot as plt
# Load the Netflix data
df = pd.read_csv('netflix_titles.csv')

# Count how many titles were released per year
release_counts = df['release_year'].value_counts().sort_index()

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(release_counts.index, release_counts.values)
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.title("Number of Netflix Titles Released per Year")
plt.tight_layout()


# Count the occurrences of each genre
genre_counts = df['listed_in'].str.split(', ').explode().value_counts() 
# This code counts the occurrences of each genre in the 'listed_in' column.
# separates the resulting lists into separate rows, and then counts the occurrences of each genre.



# Figure 2 shows the most popular genres on Netflix.
filtered_genres = genre_counts[genre_counts > 500]
top_genres = filtered_genres.sort_valhes(ascending = False).head(10)  # Get the top 10 genres
# Next, we will display filtered genres in a bar chart.

plt.figure(figsize = (24, 6))
plt.bar(top_genres.index, top_genres.values)
plt.xlabel("Genres")
plt.ylabel("Number of Titles")
plt.title("Top 10 Genres of Netflix Titles")
plt.xticks(rotation = 90)  # Rotate x-axis labels for better readability
plt.tight_layout()
# this prevents the graphs from being reran once the script is closed
# Figure 2 shows the most popular genres on Netflix.

# Figure 3: Number of shows and movies on Netflix
type_counts  = df['type'].value_counts()
# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Shows and Movies on Netflix")


# this prevents the graphs from being reran once the script is closed
if __name__ == "__main__":
    # Show the plots
    plt.show()
    plt.close('all')