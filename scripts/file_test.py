import os
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
files_to_check = [
    'lgbm_model.pkl',
    'tfidf_vectorizer.pkl', 
    'params.yaml',
    'data/interim/test_processed.csv'
]
print(root_dir)
for file in files_to_check:
    path = os.path.join(root_dir, file)
    print(path)
    print(f"{file}: {'EXISTS' if os.path.exists(path) else 'MISSING'}")