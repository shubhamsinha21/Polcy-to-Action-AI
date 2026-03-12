import json
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "schemes.json")

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_schemes():

    with open(DATA_PATH, "r") as f:
        schemes = json.load(f)

    return schemes


def build_index():

    schemes = load_schemes()

    texts = [
        s["scheme_name"] + " " + s["benefit"]
        for s in schemes
    ]

    embeddings = model.encode(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, schemes


index, schemes = build_index()


def search_schemes(query, top_k=3):

    query_vector = model.encode([query])

    distances, indices = index.search(np.array(query_vector), top_k)

    results = []

    for i in indices[0]:

        results.append(schemes[i])

    return results