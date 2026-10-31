import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Hardcoded small dataset for practical demonstration
data = {
    'Weather': ['Sunny', 'Sunny', 'Cloudy', 'Rainy', 'Rainy', 'Rainy', 'Cloudy', 'Sunny'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Convert strings to numbers so the tree can read them
le = LabelEncoder()
df['Weather'] = le.fit_transform(df['Weather'])
df['Temperature'] = le.fit_transform(df['Temperature'])
df['Play'] = le.fit_transform(df['Play'])

X = df[['Weather', 'Temperature']]
y = df['Play']

# Create Decision Tree
model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

print("Decision Tree created and trained successfully.")
print("Accuracy on training data:", model.score(X, y))
