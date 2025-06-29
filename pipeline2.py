import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import os

# ------------------ Step 1: Extract ------------------
def extract_data(file_path):
    print("Extracting data...")
    return pd.read_csv(file_path)

# ------------------ Step 2: Transform ------------------
def transform_data(df):
    print("Transforming data...")

    # Separate features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # Identify column types
    num_features = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_features = X.select_dtypes(include=['object']).columns.tolist()

    # Define transformers
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine transformers
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_features),
            ('cat', categorical_transformer, cat_features)
        ]
    )

    # Final pipeline
    full_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor)
    ])

    # Apply transformations
    X_transformed = full_pipeline.fit_transform(X)

    return X_transformed, y

# ------------------ Step 3: Load ------------------
def load_data(X, y, output_dir='output'):
    print("Loading data...")
    os.makedirs(output_dir, exist_ok=True)

    # Convert to DataFrame (after transformation, X may be sparse matrix)
    X_df = pd.DataFrame(X.toarray() if hasattr(X, 'toarray') else X)
    y_df = pd.DataFrame(y, columns=['target'])

    final_df = pd.concat([X_df, y_df], axis=1)
    final_df.to_csv(os.path.join(output_dir, 'processed_data.csv'), index=False)
    print(f"Processed data saved to {output_dir}/processed_data.csv")

# ------------------ Main Function ------------------
def run_etl_pipeline(input_file):
    df = extract_data(input_file)
    X_transformed, y = transform_data(df)
    load_data(X_transformed, y)

# ------------------ Entry Point ------------------
if __name__ == "__main__":
    # Replace 'your_data.csv' with your actual data file
    run_etl_pipeline("my_data.csv")