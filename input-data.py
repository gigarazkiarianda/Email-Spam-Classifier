import pandas as pd
import os


data = {
    'email': [
        "Congratulations! You've won a free lottery ticket!",
        "Hello, I hope you are doing well.",
        "Limited time offer! Buy now and save 50%!",
        "Meeting at 10 AM tomorrow, don't forget to bring the report.",
        "Free Viagra now!!!",
        "Hi John, can you send me the report by tomorrow?",
        "Congratulations, you've been selected for a prize!",
        "Let's have a meeting next week to discuss the project.",
        "Earn money quickly and easily by clicking this link.",
        "Are we still on for lunch today?"
    ],
    'label': [
        1, 0, 1, 0, 1, 0, 1, 0, 1, 0
    ]
}


df = pd.DataFrame(data)


folder_path = 'dataset'
file_path = os.path.join(folder_path, 'spam_dataset.csv')


if not os.path.exists(folder_path):
    os.makedirs(folder_path)

df.to_csv(file_path, index=False)

print(f"Dataset telah disimpan di {file_path}")
