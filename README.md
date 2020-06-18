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
