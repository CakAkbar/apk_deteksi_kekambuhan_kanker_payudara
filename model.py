import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
import pickle

# Fungsi transformasi untuk mengubah sparse matrix menjadi dense matrix
def to_dense(x):
    return x.toarray()

# Load dataset
df_breast_cancer = pd.read_csv('data-clean.csv')

# Menambahkan kolom 'class' berdasarkan kondisi 'deg-malig'
df_breast_cancer['class'] = df_breast_cancer.apply(lambda row: 'no-recurrence-events' if row['deg-malig'] < 2 else 'recurrence-events', axis=1)

# Kolom target
target_column = 'class'

# Memisahkan fitur (X) dan label (y)
X = df_breast_cancer.drop(target_column, axis=1)
y = df_breast_cancer[target_column]

# Membagi dataset menjadi data latih dan data uji (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Mengidentifikasi kolom kategorikal dan biner
categorical_features = ['age', 'menopause', 'tumor-size', 'inv-nodes', 'breast-quad']
binary_features = ['node-caps', 'breast', 'irradiat']

# Membuat transformer untuk preprocessing
categorical_transformer = OneHotEncoder(drop='first', handle_unknown='ignore')
binary_transformer = OneHotEncoder(drop='first', handle_unknown='ignore')

# Menggabungkan transformer dalam sebuah kolom transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features),
        ('bin', binary_transformer, binary_features)
    ],
    remainder='passthrough'
)

# Pipeline untuk Naive Bayes
pipeline_nb = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('to_dense', FunctionTransformer(to_dense, accept_sparse=True)),
    ('classifier', GaussianNB())
])

# Melatih model Naive Bayes dengan data latih
pipeline_nb.fit(X_train, y_train)

# Menyimpan model ke file pickle
with open('model_nb.pkl', 'wb') as file:
    pickle.dump(pipeline_nb, file)
