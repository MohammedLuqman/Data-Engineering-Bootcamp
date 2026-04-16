import csv
import numpy as np
import Data_cleaning
import pickle

def display():
    print("\n" + "="*20, "Welcome to my ARTICLES similarity founder", "="*20)
    print("1. Calculate the cosine similarity")
    print("2. Most similar articles")
    print("3. Exit")

def main_menu():
    bag = Data_cleaning.bag_of_words()
    matrix = Data_cleaning.vectors_re(bag)
    print("Generating Similarity Matrix")
    sim_matrix = Data_cleaning.similarity_matrix(matrix)
    
    with open("similarity_matrix.pkl", "wb") as f:
        pickle.dump(sim_matrix, f)
    print("Matrix saved to similarity_matrix.pkl")

    while True: 
        display()        
        choice = input("\nSelect an option: ")  
      
        if choice == '1':
                first_id = input("Enter the first ID (0-49): ")
                second_id = input("Enter the second ID (0-49): ")
            
                if first_id.isdigit() and second_id.isdigit():
                    id1, id2 = int(first_id), int(second_id)
                    
                    if 0 <= id1 < 50 and 0 <= id2 < 50:
                        score = sim_matrix[id1][id2]
                        print(f"\nSimilarity between Article {id1} and {id2} is: {score:.4f}")
                    else:
                        print("Error: IDs must be between 0 and 49")
                else:
                    print("Please Enter an integer number")
                    
        elif choice == '2':
            while True: 
                most1 = input("Enter the ID of the article to find matches (0-49): ")
        
                if most1.isdigit():
                    id1 = int(most1)
            
                    if 0 <= id1 < 50:
                        recommendations = Data_cleaning.most_similar(id1, sim_matrix)
                        print(f"\nResults for your search:")
                        for item in recommendations:
                            print(f"{item[1]} Similarity: {item[0]:.4f}")
                        break 
                    else:
                        print("Error: ID must be between 0 and 49.")
                else:
                    print("Please enter a valid integer number.")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
     main_menu()