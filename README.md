# Movie-Recommender-System-ContentBased
This is a Content Based Recommender System built based on Python and uses Streamlit (open source app framework in Python) for WebApp.


Dataset - https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
(Also both the csv files are added in the GitHub LFS)

## How to Host the Web Application?
1. Clone the repository into your local environment using command git clone https://github.com/Balakrishnan000/Movie-Recommender-System-ContentBased.git <br>
2. On the terminal, run pip install -r requirements.txt All the required packages will now be installed.<br>
3. On the terminal, run py -m streamlit run app.py <br>

The web app will now be hosted on your localhost.
<br>
(OR)<br>
Hosted Version on Herouku:<br>
Link: https://movie-rec-sys-bala.herokuapp.com/

## Project Flow:

1. Import and Structurize Data from csv file
2. Do Preprocessing of Data
3. Do Vectorization
4. Do Model Building
5. Convert the result as a .pkl file using pickle module
6. Deploy the WebApp on Heroku.
   Note: Used TMDB API for fetching the poster of the movie.

## Final Output: 
![image](https://user-images.githubusercontent.com/70379877/175554131-dfc35a5b-3381-4473-ae9c-1d5ecdd80169.png)
