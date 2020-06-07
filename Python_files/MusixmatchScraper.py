class MusixmatchScraper():

    """This class allows you to scrape the lyrics for an artist who has a presence on Musixmatch

    An instance of the class needs to be instantiated with an artist URL e.g.

    https://www.musixmatch.com/artist/Bob-Dylan

    The default number of songs to scrape is 50

    """

    def __init__(self,artist_url):

        self.artist_url = artist_url #artists URL as attribute

        self.artist = artist_url.split('artist/')[-1] #artist string as attribute

        self.song_l = [] #empty list to populate lyrics

    def _get_html(self,url):

        """Uses Beatiful Soup to extract html from a url. Returns a soup object """

        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

        req = Request(url, headers=headers)

        return BeautifulSoup(urlopen(req).read(), 'html.parser')

    def _multithreadCompile(self,thread_count,iteration_list,func):

        """a function that compiles an iteration list to prepare
        multi threadding"""

        jobs = []

        #distribute iteration list to batches and append to jobs list
        batches = [i.tolist() for i in np.array_split(iteration_list,thread_count)]

        for i in range(len(batches)):

            jobs.append(threading.Thread(target=func,args=[batches[i]]))

        return jobs

    def _multithreadExecute(self,jobs):

        """executes the multi-threadding loop"""

        # Start the threads
        for j in jobs:

            j.start()

        # Ensure all of the threads have finished
        for j in jobs:
            j.join()
        return

    def _getpageUrls(self,url):

        """Gets all the links from an artist page"""

        html = self._get_html(url) #gets html for current page

        songs = html.find_all('h2',{'class':'media-card-title'}) #element for song

        #loop through and extract urls for all songs in soup object
        song_urls = ['https://www.musixmatch.com'+i.find('a')['href'] for i in songs]

        #return list of song urls
        return [i for i in song_urls if 'album' not in i]


    def _getLyrics(self,song_url):

        """Extracts lyrics from a song url. Duplicated lines are removed e.g. chorus lines
        Only unique lyrics are returned"""

        html = self._get_html(song_url) #get html for current page

        #find all elements containing lyrics
        element = html.find_all('span',{'class':'lyrics__content__ok'})

        #numbe of elements to loop through
        element_loop = len(element)

        song_lyrics = [] #empty list for song lyrics

        #extract song lyrics
        song_lyrics_raw = [element[i].text.split('\n') for i in range(element_loop)]

        #flatten list of lists
        song_lyrics_raw = [i for sublist in song_lyrics_raw for i in sublist]

        #retain only unique lines in lyrics
        song_lyrics.extend(list(dict.fromkeys(song_lyrics_raw)))

        #join list and remove empty elements
        song_lyrics = ' '.join([i for i in song_lyrics if len(i) >0])

        return song_lyrics #return song lyrics

    def _getAllpageUrls(self,target=50):

        """Generates page urls for artist. There are 15 songs on each page"""

        loops = int(target/15) #specifcy how many loops needed

        #generate urls
        artist_urls = [self.artist_url+'/'+str(i+1) for i in range(loops)]

        all_song_urls = [] #empty list for all song urls

        for i in artist_urls: #loop through and get all song urls for all pages

            all_song_urls.extend(self._getpageUrls(i))

        return all_song_urls

    def _extractData(self,all_song_urls):

        """Extracts data from all song urls"""

        for i in tqdm_notebook(range(len(all_song_urls))): #loop through all song urls

            try:
                #get lyrics
                song_lyrics = self._getLyrics(all_song_urls[i])

                #get song title
                song_title = all_song_urls[i].split('/')[-1]

                #create DataFrame
                song_df = pd.DataFrame([(self.artist,song_title,song_lyrics)],columns=['artist','song','lyrics'])

                #append DataFrame to master list
                self.song_l.append(song_df)

            except:
                pass

        return

    def Run(self,target):

        """Executes all methods above"""

        self.all_song_urls = self._getAllpageUrls(target) #get page URL's to get target number of songs

        #multi-threaded scraping of all song urls
        self._multithreadExecute(self._multithreadCompile(5,self.all_song_urls,self._extractData))

        try:
            df_final = pd.concat([i for i in self.song_l]) #concatenate all song Df's

            df_final.reset_index(drop=True,inplace=True) #reset index

            self.df = df_final[df_final.lyrics.str.len() > 0] #drop any songs with no lyrics or failed scrapes

            return self.df

        except:
            pass
            return
     
