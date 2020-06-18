# songlyrics_univeral_sentence_encoder

## Project Aim
There are differences between the lyrics of different genres and we can quantify and measure this.

## Approach

### Stage 1) Where do we get the data?
- We will scrape lyrics from Musixmatch.com. 

There is a notebook containing the scraper class [here](https://github.com/kitsamho/songlyrics_univeral_sentence_encoder/blob/master/Notebooks/SongLyrics_Scraping%20Notebook.ipynb) that has all the code in order to do this.

### Stage 2) What kind of method/metric will allow us to quantify lyrical diversity in an intuitive way?
- We will represent lyrics using high dimensional vectors from Google’s Universal Sentence Encoder
- We will apply Principal Component Analysis (PCA) to reduce these high dimensional representations to n=1,2,3 dimensions

### Stage 3) How can we visualize this in a meaningful way?
- We will use Plotly and build a combination of simple plots and more sophisticated 2d and 3d scatter plots to see where there are similarities and differences in lyrics

There is a notebook [here](https://github.com/kitsamho/songlyrics_univeral_sentence_encoder/blob/master/Notebooks/SongLyrics_Analysis%20Notebook.ipynb) containing all the project code that covers stages 1 and 2

## Results / Thoughts
We have shown that lyrics from different music genres do vary although what is interesting is that there is quite a clear relationship between lyrical content as we move from one genre to another in a stepwise fashion. I think the visualization below quite clearly brings this to life.

![Alt text](https://github.com/kitsamho/songlyrics_univeral_sentence_encoder/blob/master/assets/sim_pc1_genre.png?raw=true "Title")

The lyrics of different genres aren’t entirely mutually exclusive — unless you compare the extremes. i.e. there is a huge difference between death metal and soul/r&b but little in the way to differentiate pop and pop/rock.

These findings reflect the true nature of music in that music genres are fluid and that for each genre, there is likely to be a ‘neighbouring’ genre that is similar in its lyrical content.

## Applications

We have shown that universal sentence encoding/transfer learning is a very powerful and incredibly easy technique that can be used to pull out the differences and similarities in song lyrics across genres.

Its applications on other problems are numerous:
- Song/lyric recommender systems — using similarity metrics to find songs with similar lyrics
- Segmenting large volumes of text by finding similar documents e.g. emails, customer feedback/reviews
- Identifying plagiarism
- To be used as features for classification tasks
