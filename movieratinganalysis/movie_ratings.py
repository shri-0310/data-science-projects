# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Step 1: Load the Dataset
file_path = 'movie_ratings.csv'  # Replace with your file path
movie_data = pd.read_csv(file_path)

# Inspect the dataset
print("First 5 rows of the dataset:")
print(movie_data.head())
print("\nDataset Info:")
print(movie_data.info())

# Step 2: Data Cleaning
# Remove duplicates
movie_data.drop_duplicates(inplace=True)

# Handle missing values
movie_data.fillna({'Rating': 0}, inplace=True)

# Confirm the cleaning process
print("\nCleaned Dataset:")
print(movie_data.head())

# Step 3: Analyze Genres
# Find the most popular genres by frequency
popular_genres = movie_data['Genre'].value_counts()
print("\nMost Popular Genres:")
print(popular_genres)

# Calculate average ratings for each genre
average_ratings = movie_data.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
print("\nAverage Ratings by Genre:")
print(average_ratings)

# Step 4: Visualize Trends in Movie Ratings Over Time
# Ensure 'Release_Date' is in datetime format
movie_data['Release_Date'] = pd.to_datetime(movie_data['Release_Date'], errors='coerce')

# Calculate average ratings per year
movie_data['Year'] = movie_data['Release_Date'].dt.year
ratings_over_time = movie_data.groupby('Year')['Rating'].mean()

# Plot trends in movie ratings
plt.figure(figsize=(10, 6))
ratings_over_time.plot(kind='line', marker='o', color='green')
plt.title('Trends in Movie Ratings Over Time')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.grid()
plt.show()

# Step 5: Optional - Word Cloud for Keywords in Movie Titles
# Combine all movie titles into a single string
title_text = ' '.join(movie_data['Movie_Title'].dropna())

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(title_text)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Frequent Keywords in Movie Titles')
plt.show()