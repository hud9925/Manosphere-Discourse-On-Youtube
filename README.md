# YouTube Comment Analysis: Red Pill & Manosphere Discourse

## Project Overview
This project analyzes YouTube comments related to Red Pill and manosphere discourse to uncover key themes, sentiment distribution, and community structures. The dataset consists of comments extracted from relevant videos, which are preprocessed and analyzed using various NLP techniques.

## Analysis Workflow

### 1. Data Collection
- YouTube API is used to scrape comments from selected videos.
- Metadata such as `video_id`, `comment_id`, `timestamp`, and `likes` are stored in an SQLite database.

### 2. Preprocessing
- **Text Cleaning:** Remove HTML tags, emojis, and unnecessary whitespace.
- **Lemmatization:** Using SpaCy's BERT-based model to normalize words.
- **Tokenization & Stopword Removal:** Ensures high-quality data for analysis.
- Cleaned data is stored in the `LemmatizedComments` table.

### 3. Community Detection
- **TF-IDF Vectorization:** Represents comment similarity.
- **Cosine Similarity Matrix:** Used to create a comment graph.
- **Louvain Clustering (NetworkX):** Identifies discussion communities.
- **Visualization:** Network graph showing discussion clusters.
- Results stored in `CommunityDetection`.

### 4. Topic Modeling
- **Latent Dirichlet Allocation (LDA)** for extracting dominant themes.
- **Word Cloud** highlights frequently used terms.
- **pyLDAvis** interactive visualization.

### 5. Sentiment Analysis
- **VADER Sentiment Classifier:** Labels comments as Positive, Neutral, or Negative.
- **Radar Chart** visualizing sentiment distribution.

### 6. Emotion Analysis (Lexicon-Based)
- Uses **NRC Emotion Lexicon** to detect:
  - Anger, Joy, Sadness, Fear, Trust, Surprise, Anticipation, Disgust.
- **Heatmap** displays the emotional intensity of comments.

## Results & Insights
- Community detection reveals distinct discussion clusters—topics like self-improvement, masculinity, and dating advice.
- Sentiment analysis shows overwhelmingly positive reactions, likely due to engagement bias (commenters supporting content creators).
- Topic modeling suggests common manosphere themes, such as "success," "status," "relationships," and "self-improvement."
- Emotion analysis indicates higher levels of distrust and anger in certain communities, aligning with manosphere rhetoric.

## Technologies Used

| Category               | Tools / Libraries |
|------------------------|------------------|
| **Programming**       | Python           |
| **Data Storage**      | SQLite           |
| **NLP Processing**    | spaCy, NLTK      |
| **Vectorization**     | TF-IDF, scikit-learn |
| **Topic Modeling**    | gensim (LDA)     |
| **Community Detection** | networkx        |
| **Visualization**     | matplotlib, tableau |
