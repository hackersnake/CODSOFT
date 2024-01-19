import numpy as np

book_names = ["The Silent Observer", "Eternal Echoes", "Whispers of the Wind", "Midnight Serenade", "Shadows in the Moonlight"]

book_descriptions = [
    "A gripping thriller about a silent observer.",
    "An exploration of eternal themes and timeless echoes.",
    "Poetic tales that capture the whispers of the wind.",
    "A mysterious midnight serenade that will keep you on the edge.",
    "Shadows in the moonlight reveal hidden secrets."
]

def tfidf_vectorizer(book_descriptions):
    unique_words = set(word for description in book_descriptions for word in description.lower().split())
    word_to_index = {word: i for i, word in enumerate(unique_words)}
    
    tf_matrix = np.zeros((len(book_descriptions), len(unique_words)))
    for i, description in enumerate(book_descriptions):
        for word in description.lower().split():
            tf_matrix[i, word_to_index[word]] += 1
    
    idf_vector = np.log(len(book_descriptions) / (1 + np.sum(tf_matrix > 0, axis=0)))
    
    tfidf_matrix = tf_matrix * idf_vector
    
    return tfidf_matrix, word_to_index

def cosine_similarity(user_preferences_text, tfidf_matrix, word_to_index):
    user_vector = np.zeros(len(tfidf_matrix[0]))
    for preference in user_preferences_text:
        if preference and preference.lower() in word_to_index:
            user_vector += tfidf_matrix[:, word_to_index[preference.lower()]]
    
    user_vector = user_vector / (np.linalg.norm(user_vector) + 1e-10)  # Add a small value to avoid division by zero
    
    cosine_similarities = np.dot(user_vector, tfidf_matrix.T) / (np.linalg.norm(user_vector) * np.linalg.norm(tfidf_matrix, axis=1))
    return cosine_similarities.flatten()

def content_based_filtering(user_preferences_text, tfidf_matrix, word_to_index, book_names):
    cosine_similarities = cosine_similarity(user_preferences_text, tfidf_matrix, word_to_index)
    recommended_books_indices = np.argsort(cosine_similarities)[-2:][::-1]
    recommended_books = [book_names[i] for i in recommended_books_indices]
    return recommended_books

# Take user input for preferences
user_preferences_text = input("Enter your book preferences (separated by spaces): ").split()

# Process user input and make recommendations
tfidf_matrix, word_to_index = tfidf_vectorizer(book_descriptions)
recommended_books = content_based_filtering(user_preferences_text, tfidf_matrix, word_to_index, book_names)

# Display recommended books
if recommended_books:
    print("Recommended books for you:")
    for i, book in enumerate(recommended_books, start=1):
        print(f"{i}. {book}")
else:
    print("Sorry, no recommendations based on your preferences.")
