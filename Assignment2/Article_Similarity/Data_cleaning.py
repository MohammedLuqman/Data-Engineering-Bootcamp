import csv
import re
import numpy as np
import pickle

def cleaned_data(text):
    
    text = text.lower()
    text = re.sub(r'\d+', '', text)        
    text = re.sub(r'[^\w\s]', '', text)   
    tokens = text.split()
    return " ".join(tokens)

with open("Articles.csv", 'r') as infile, \
     open("Cleaned_Articles.csv", 'w', newline='') as outfile:
    
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    
    for row in reader:
        row['content'] = cleaned_data(row['content'])
        writer.writerow(row)

def bag_of_words():
    bag_of_words_set = set()
    with open("Cleaned_Articles.csv", 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            words_list = row['content'].split()
            bag_of_words_set.update(words_list)

    final_bag = sorted(list(bag_of_words_set))
    return final_bag 

def vectors_re(vocab, file_path="Cleaned_Articles.csv"):
    all_vectors = []
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            words = row['content'].split()
            
            vector = []
            for word in vocab:
                if word in words:
                    vector.append(1)
                else:
                    vector.append(0)
            
            all_vectors.append(vector)            
    return np.array(all_vectors)

def cosine_sim(vec1 , vec2):
    dot_product = np.dot(vec1,vec2)
    vector1 = np.linalg.norm(vec1)
    vector2 = np.linalg.norm(vec2)
    
    if vector1 == 0 and vector2 == 0 :
        return 0

    return dot_product / (vector1 * vector2)
    
def similarity_matrix(vectors):
    # Ain't lying I used AI tool to do this, I have one brain cell and it stopped here, SORRY
    dot_product = np.dot(vectors, vectors.T)
    norms = np.linalg.norm(vectors, axis=1)
    denominator = np.outer(norms, norms) + 1e-9
    return dot_product / denominator

def most_similar(article_id, sim_matrix, file_path="Articles.csv"):
    titles = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            titles.append(row['title'])

    all_scores = sim_matrix[article_id]

    scored_titles = []
    for i in range(len(titles)):
        if i != article_id:
            pair = [all_scores[i], titles[i]]
            scored_titles.append(pair)

    scored_titles.sort(reverse=True)
    top_3 = scored_titles[:3]
    

    return top_3
