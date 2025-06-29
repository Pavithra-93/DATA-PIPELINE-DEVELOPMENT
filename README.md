# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PAVITHRA K

*INTERN ID*: CT04DF2827

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

##DESCRIPTION:In this project, I developed a complete data preprocessing pipeline using Python and the PyCharm integrated development environment (IDE). The goal was to create an end-to-end ETL (Extract, Transform, Load) workflow that prepares raw tabular data for machine learning tasks in a clean, automated, and reproducible way. The pipeline was implemented in a single Python script, demonstrating how modern data science libraries can be combined to solve practical data preparation challenges efficiently.

The process begins with the Extract step. In this phase, the pipeline reads a CSV file containing raw data using the Pandas library. Pandas is a widely used Python library for data manipulation, offering powerful tools to load, inspect, and process data stored in different formats. The script loads the file into a DataFrame, which makes it easy to explore column types, detect missing values, and separate features from the target variable. This initial extraction is crucial for understanding the structure of the dataset and identifying which transformations are needed to prepare it for modeling.

Once the data has been loaded, the Transform phase applies several preprocessing steps. The script first separates the dataset into features (input variables) and the target (the output variable to predict). It then identifies numeric columns, such as integers or floating-point numbers, and categorical columns containing text labels or other discrete categories. Each of these requires a specific strategy for cleaning and encoding.

For numeric columns, the pipeline uses scikit-learn’s SimpleImputer to fill in any missing values with the column mean. This ensures no information is lost due to incomplete data and keeps the dataset consistent. After imputation, numeric features are scaled using StandardScaler, transforming them to have zero mean and unit variance. Standardization is an important step for many machine learning algorithms, as it helps improve convergence and ensures that all features contribute equally to the model’s performance.

Categorical columns are processed differently. The pipeline imputes missing categorical values by replacing them with the most frequent category in each column. This approach prevents data loss and avoids introducing bias through arbitrary replacements. Then, the categorical columns are encoded with OneHotEncoder, converting each unique category into a binary vector. This transformation allows machine learning models to interpret categorical information correctly without assuming any ordinal relationship among categories.

Both numeric and categorical transformations are combined in a ColumnTransformer, a flexible scikit-learn utility that applies each transformation to the appropriate subset of columns. The ColumnTransformer is then integrated into a Pipeline object, ensuring all preprocessing steps can be executed in a single call. This design promotes reproducibility and reduces the risk of inconsistent transformations across training and testing datasets.

In the Load step, the transformed data is converted back into a Pandas DataFrame. If the transformation output is a sparse matrix, the script converts it to a dense format for compatibility with CSV export. Finally, the transformed features and target variable are combined and saved as processed_data.csv in an automatically created output directory. The script prints informative messages throughout the process to confirm successful completion.

The project was developed entirely in PyCharm, using Python 3.10, Pandas, and scikit-learn. This approach demonstrates a practical, professional workflow for data preparation, enabling efficient and repeatable pipelines for machine learning.

###OUTPUT:

![Image](https://github.com/user-attachments/assets/187cc1a6-7321-44b8-9798-f2fa2f85577d)
