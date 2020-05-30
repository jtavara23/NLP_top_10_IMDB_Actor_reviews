# Web scraping, pickle imports
import requests
from bs4 import BeautifulSoup
import pickle


def writeResults(msg):
    outFile = open("logtestResult.log", "a", encoding="utf-8")
    outFile.write(msg)

def getReviews(soup):
    reviews = [p.text for p in soup.find_all('div', class_ ='text show-more__control')]
    writeResults(str(reviews))
    #print(reviews[2])
    return reviews

# Scrapes transcript data from imdb links
def url_to_transcript(url):
    '''Returns transcript data specifically from scrapsfromtheloft.com.'''
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    reviews = getReviews(soup)
    print(url)
    return reviews
|

number_movies_per_actor = 3

#URLs of reviews in scope
# - 5 most popular movies for each actor, with reviews composed with spoilers, all ratings and sorted by votes
urls= ['https://www.imdb.com/title/tt8946378/reviews?ref_=tt_urv', # Knives Out
        'https://www.imdb.com/title/tt7979142/reviews?ref_=tt_urv', # The Night Clerk 
        'https://www.imdb.com/title/tt1856101/reviews?ref_=tt_urv', # Blade Runner 2049
        #'https://www.imdb.com/title/tt8079248/reviews?ref_=tt_urv', # Yesterday
        #'https://www.imdb.com/title/tt1833116/reviews?ref_=tt_urv',
        

        
        'https://www.imdb.com/title/tt2119532/reviews?ref_=tt_urv', #Hacksaw Ridge
        'https://www.imdb.com/title/tt2177461/reviews?ref_=tt_urv', #A Discovery of Witches 
        'https://www.imdb.com/title/tt1464540/reviews?ref_=tt_urv', #I Am Number Four
        'https://www.imdb.com/title/tt4786282/reviews?ref_=tt_urv', #Lights Out
        'https://www.imdb.com/title/tt2058673/reviews?ref_=tt_urv', #Point Break

        ]

actors = ['Ana de Armas', 
          'Sophia Lillis'
         ]

movies_reviews = [url_to_transcript(url) for url in urls]

# # Pickle files for later use

# # Make a new directory to hold the text files
!mkdir movies_reviews

for i, c in enumerate(actors):
    with open("movies_reviews/" + c + ".txt", "w") as file:
        n_movies = number_movies_per_actor * i
        for x in xrange(n_movies, n_movies + number_movies_per_actor):
            pickle.dump(movies_reviews[x], file)

