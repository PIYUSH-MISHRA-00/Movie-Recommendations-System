![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Link to the project : [Link]()

# Movie Recommender System

This is a **Movie Recommender System** built using Streamlit, pandas, and scikit-learn. The system recommends movies based on cosine similarity of movie features such as genres, cast, overview, and more. It also fetches and displays the movie posters using the TMDb API.

## Features

- Recommends 5 movies similar to the selected movie.
- Displays the movie poster along with the movie title.
- Utilizes the TMDb API to fetch movie posters.

## Project Structure

```bash
├── app.py                      # Main Streamlit app file
├── movie_dict.pkl               # Pickle file containing movie data
├── similarity.pkl               # Pickle file containing similarity matrix
├── tmdb_5000_credits.csv        # Dataset containing movie credits
├── tmdb_5000_movies.csv         # Dataset containing movie information
├── requirements.txt             # Project dependencies
├── Dockerfile                   # Docker configuration for deployment
└── README.md                    # Project documentation (this file)
```
## Datasets

The project uses the following datasets:

TMDb 5000 Movie Dataset - Movie and credits datasets.

## Installation
Clone the Repository
```
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```
## Install Dependencies

You can install the required dependencies using pip:

```

pip install -r requirements.txt
```

## Run the Application Locally

To run the Streamlit app on your local machine:
```
streamlit run app.py
```
The app will be available at http://localhost:8501.
Running with Docker

To run the app using Docker, first build the Docker image and then run the container:

## Build the Docker Image:

```
docker build -t movie-recommender-system .
```
## Run the Docker Container:

    docker run -p 8501:8501 movie-recommender-system

## After running the container, the app will be available at http://localhost:8501.
Deployment on Render

To deploy this project on Render:

Create a new Web Service in your Render dashboard.
Connect your GitHub repository containing this project.
Select Docker as the environment in Render.
Use the free instance (512MB RAM).
Deploy the service. The app will be available at https://your-app-url.render.com.

## TMDb API Key

You will need to set up an API key from The Movie Database (TMDb) to fetch movie posters. Store the API key in a secure environment variable.
Environment Variables

To run this project, you will need to add the following environment variables:

## TMDB_API_KEY: Your TMDb API Key.

## Technologies Used

Python: For building the backend logic.
Streamlit: For creating an interactive UI.
Pandas & Numpy: For data manipulation and analysis.
Scikit-learn: For building the recommendation engine using cosine similarity.
Docker: For containerization and easy deployment.
TMDb API: For fetching movie posters.

## Acknowledgements

The movie datasets used in this project are from TMDb 5000 Movie Dataset on Kaggle.
Thanks to Streamlit for providing an easy-to-use framework to build interactive web apps.

### Key Points:
- **Features**: Highlights what the app does (recommend movies and fetch posters).
- **Project Structure**: Lists the files in the project.
- **Installation**: Provides instructions to set up and run the app locally or with Docker.
- **Deployment**: Offers guidance on deploying the app to Render.
- **TMDb API**: Notes the need for an API key.
- **Acknowledgements**: Credits the datasets and tools used.

This `README.md` will provide clear guidance for anyone visiting your GitHub project. You can customize it by adding more details if needed!



