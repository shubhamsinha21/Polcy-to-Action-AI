import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def load_schemes():

    with open("data/schemes.json", "r") as f:
        schemes = json.load(f)

    return schemes


def build_vector_index():

    schemes = load_schemes()

    texts = []

    for s in schemes:

        text = s["scheme_name"] + " " + s["benefit"]

        texts.append(text)

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, schemes


def search_schemes(query, k=3):

    index, schemes = build_vector_index()

    query_embedding = model.encode([query])

    distances, indices = index.search(np.array(query_embedding), k)

    results = []

    for i in indices[0]:

        results.append(schemes[i])

    return results