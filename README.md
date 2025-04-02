
# 🎬 Movie Recommender Using Machine Learning

Recommendation systems have become an integral part of our daily lives, assisting us in making informed choices with ease. These systems utilize advanced algorithms to personalize content recommendations, ultimately saving us time and enhancing our overall experiences. By analyzing user data, recommendation systems can predict and suggest items that align with our preferences and behaviors.

## 🌟 About This Project

This project leverages machine learning to build a movie recommendation system using Streamlit for the web application. The core concept behind this recommender system is Cosine Similarity, a metric used to measure how similar two items are. By analyzing the metadata of movies, the system provides personalized recommendations based on user interests.

## 📊 Dataset Used

The dataset used for this project is derived from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv). It contains extensive metadata for thousands of movies, which is used to train and test the recommendation algorithm.

## 🧠 Model Concept: Cosine Similarity

1. **Cosine Similarity** measures the similarity between two vectors, resulting in a value between 0 and 1.
2. This metric is used to compare document vectors in this project.
3. A value of 0 indicates complete dissimilarity, while 1 indicates perfect similarity.

For more details, check [Cosine Similarity](https://www.learndatasci.com/glossary/cosine-similarity/).

## 📓 Using Jupyter Notebooks

This project also includes a Jupyter notebook (`Movie Recommender System.ipynb`) which demonstrates the step-by-step process of building the recommendation system. The notebook is a great way to understand the data preprocessing, model training, and evaluation stages in detail.

To run the notebook:
1. Ensure you have Jupyter installed. If not, you can install it using pip:
    ```bash
    pip install jupyter
    ```

2. Launch the Jupyter notebook:
    ```bash
    jupyter notebook
    ```

3. Open the `Movie Recommender System.ipynb` notebook and follow the instructions within the notebook to execute each cell.

## 🚀 How to Run

### Steps

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd movie-recommender
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

4. **Access the web application**:
    Open your web browser and go to `http://localhost:8501` to see the app in action.

## 📈 Future Improvements

We have several ideas for future improvements to make this project even better:

1. **User Authentication**: Allow users to create accounts and save their favorite movies or recommendations.
2. **Advanced Filtering**: Add more filters (e.g., genre, release year) to refine recommendations.
3. **Enhanced UI/UX**: Improve the user interface for a more intuitive and engaging experience.
4. **Collaborative Filtering**: Implement collaborative filtering techniques for more personalized recommendations.
5. **Real-time Data Updates**: Use real-time data sources to keep the movie database up-to-date.
6. **Mobile App**: Develop a mobile version of the app using a framework like React Native.

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Scikit Learning
- **Modeling**: Cosine Similarity
- **Notebooks**: Jupyter

## 📂 Project Structure

```
- demo
  - 6.jpeg
- notebooks
  - Movie Recommender System.ipynb
- app.py
- requirements.txt
- setup.py
- .gitattributes
- README.md
```

## 📧 Contact

Author: Shamin Yasar  
Email: [shaminyasar2001@gmail.com](mailto:shaminyasar2001@gmail.com)

Check out the project live [here](https://movie-ml.streamlit.app/).
