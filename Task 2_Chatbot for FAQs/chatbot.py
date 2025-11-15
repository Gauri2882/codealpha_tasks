import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# -----------------------------
# 1. SAMPLE FAQ DATA
# -----------------------------
faqs = [
    {
        "question": "What is ChatGPT?",
        "answer": "ChatGPT is an AI language model created by OpenAI for generating human-like text."
    },
    {
        "question": "How do I reset my password?",
        "answer": "To reset your password, go to the account settings and choose 'Forgot Password'."
    },
    {
        "question": "What is your refund policy?",
        "answer": "We offer a 7-day refund policy for all customers."
    },
    {
        "question": "How can I contact support?",
        "answer": "You can contact support via email at support@example.com."
    }
]

# Extract FAQ questions
faq_questions = [faq["question"] for faq in faqs]

# -----------------------------
# 2. PREPROCESSING FUNCTION
# -----------------------------
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()                       # lowercase
    tokens = word_tokenize(text)              # tokenization
    tokens = [w for w in tokens if w not in stop_words and w not in string.punctuation]
    return " ".join(tokens)


# Preprocess all FAQ questions
processed_questions = [preprocess(q) for q in faq_questions]

# -----------------------------
# 3. TF-IDF VECTORIZE
# -----------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

# -----------------------------
# 4. MATCHING FUNCTION
# -----------------------------
def get_best_answer(user_query):
    processed_query = preprocess(user_query)
    query_vec = vectorizer.transform([processed_query])

    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    best_idx = similarities.argmax()
    best_score = similarities[best_idx]

    if best_score < 0.2:
        return "Sorry, I couldn't understand your question. Could you rephrase it?"

    return faqs[best_idx]["answer"]


# -----------------------------
# 5. CHAT LOOP
# -----------------------------
print("Chatbot is ready! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    response = get_best_answer(user_input)
    print("Chatbot:", response)