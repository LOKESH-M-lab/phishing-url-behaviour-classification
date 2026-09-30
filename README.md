# Phishing URL Behaviour Classification Using Machine Learning

## 1. Project Overview

This project implements a machine learning-based system for **Phishing URL Behaviour Classification**.

The goal is to classify website-related records as either:

- **Legitimate**
- **Phishing**

The project uses structural URL/webpage behaviour features from the **UCI Phishing Websites dataset** and evaluates multiple machine learning models. A Streamlit application is also provided as a simple prototype for making predictions.

> **Important:** The current Streamlit prototype accepts the 30 engineered feature values used by the dataset. It is a feature-input classifier, not a raw URL scanner.

---

## 2. Problem Statement

Phishing websites are designed to deceive users and may attempt to obtain sensitive information. This project studies whether machine learning can classify website records as legitimate or phishing using structural and behavioural features.

The project focuses on a binary classification task without relying on paid security APIs.

---

## 3. Objectives

- Load and inspect the UCI Phishing Websites dataset.
- Perform data cleaning and exploratory data analysis.
- Analyse relationships between features and the target.
- Train multiple classification models.
- Evaluate the models using standard classification metrics.
- Save the trained model for reuse.
- Build a Streamlit prototype for prediction.
- Provide project documentation and reproducible setup instructions.

---

## 4. Dataset

### UCI Phishing Websites Dataset

**Source:** UCI Machine Learning Repository  
**Dataset:** Phishing Websites  
**DOI:** 10.24432/C51W2X

The original dataset contains:

- **11,055 instances**
- **30 features**
- **Target column:** `result`

The original target encoding is:

- `1` = Legitimate
- `-1` = Phishing

For machine learning in this project, the target is remapped to:

- `0` = Legitimate
- `1` = Phishing

### Dataset Citation

Mohammad, R. & McCluskey, L. (2012). *Phishing Websites*. UCI Machine Learning Repository. DOI: 10.24432/C51W2X.

---

## 5. Features Used

The project uses the following 30 engineered features:

1. `having_ip_address`
2. `url_length`
3. `shortining_service`
4. `having_at_symbol`
5. `double_slash_redirecting`
6. `prefix_suffix`
7. `having_sub_domain`
8. `sslfinal_state`
9. `domain_registration_length`
10. `favicon`
11. `port`
12. `https_token`
13. `request_url`
14. `url_of_anchor`
15. `links_in_tags`
16. `sfh`
17. `submitting_to_email`
18. `abnormal_url`
19. `redirect`
20. `on_mouseover`
21. `rightclick`
22. `popupwindow`
23. `iframe`
24. `age_of_domain`
25. `dnsrecord`
26. `web_traffic`
27. `page_rank`
28. `google_index`
29. `links_pointing_to_page`
30. `statistical_report`

---

## 6. Data Preprocessing

The original dataset was inspected for missing values and duplicate records.

Project cleaning steps included:

- Combining the feature and target data.
- Removing exact duplicate rows.
- Identifying feature records with conflicting target labels.
- Removing conflicting feature groups from the cleaned dataset.
- Checking for remaining duplicates and missing values.

### Cleaning Result

| Stage | Rows | Columns |
|---|---:|---:|
| Original data | 11,055 | 31 |
| After exact duplicate removal | 5,849 | 31 |
| Final cleaned dataset | 5,721 | 31 |

The final cleaned dataset contained:

- **5,721 rows**
- **30 features + target**
- **0 remaining duplicate rows**
- **0 missing values**

> The duplicate/conflicting-label removal described above is a project-specific preprocessing decision and is not a requirement of the original UCI dataset.

---

## 7. Exploratory Data Analysis

The project includes:

- Target/class distribution analysis.
- Feature correlation analysis.
- Identification of features with stronger observed association with the target.
- Model performance visualisation.

The ten features with the highest absolute correlation values observed in the cleaned dataset were:

| Feature | Absolute Correlation |
|---|---:|
| `sslfinal_state` | 0.709765 |
| `url_of_anchor` | 0.687107 |
| `prefix_suffix` | 0.386242 |
| `having_sub_domain` | 0.302746 |
| `web_traffic` | 0.286628 |
| `sfh` | 0.286143 |
| `links_in_tags` | 0.248927 |
| `request_url` | 0.242663 |
| `domain_registration_length` | 0.223581 |
| `google_index` | 0.119731 |

These values describe observed statistical association in this dataset; they should not be interpreted as causal effects.

---

## 8. Machine Learning Models

Three classification models were trained:

### 1. Logistic Regression

A scaled Logistic Regression pipeline was used.

### 2. Decision Tree

A Decision Tree classifier was trained with:

- `max_depth = 10`
- `random_state = 42`

### 3. K-Nearest Neighbours (KNN)

A scaled KNN pipeline was used with:

- `n_neighbors = 5`

---

## 9. Train-Test Split

The cleaned dataset was divided into:

- **80% training data**
- **20% testing data**
- `random_state = 42`
- Stratified split

Dataset sizes:

- Training set: **4,576 rows**
- Test set: **1,145 rows**
- Features: **30**

---

## 10. Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

### Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 91.27% | 91.82% | 91.20% | 91.51% | 97.71% |
| Decision Tree | 93.97% | 94.24% | 94.08% | 94.16% | 97.18% |
| KNN | 92.40% | 91.72% | 93.74% | 92.72% | 97.65% |

On this held-out test split, the Decision Tree recorded the highest observed Accuracy, Precision, Recall and F1-Score among the three tested models. Logistic Regression recorded the highest observed ROC-AUC.

These are results on the project's test split and should not be interpreted as guaranteed performance on future websites.

---

## 11. Confusion Matrices

The observed confusion matrices on the test set were:

### Logistic Regression

```text
[[506, 48],
 [ 52, 539]]
```

### Decision Tree

```text
[[520, 34],
 [ 35, 556]]
```

### KNN

```text
[[504, 50],
 [ 37, 554]]
```

The rows and columns correspond to the project ML labels:

- `0` = Legitimate
- `1` = Phishing

---

## 12. ROC-AUC

The observed ROC-AUC values were:

- Logistic Regression: **0.9771**
- Decision Tree: **0.9718**
- KNN: **0.9765**

ROC curves were generated to compare the classification behaviour of the models across different decision thresholds.

---

## 13. Streamlit Prototype

A Streamlit application was developed to provide an interactive prediction interface.

### Application Features

- Displays project information.
- Accepts the 30 dataset feature values.
- Uses the saved Decision Tree model.
- Produces a Legitimate or Phishing prediction.
- Displays estimated class probabilities.
- Displays the input feature values used for prediction.

### Target Encoding in the Application

```text
0 = Legitimate
1 = Phishing
```

### Run the Application

Open a terminal in the project folder and run:

```bash
py -m streamlit run app.py
```

Then open the local Streamlit address shown in the terminal, normally:

```text
http://localhost:8501
```

---

## 14. Prototype Validation

A real sample from the held-out test set was entered into the Streamlit application.

### Validation Sample

- Test sample index: `1501`
- Actual class: `0`
- Actual meaning: **Legitimate**
- Streamlit prediction: **Legitimate**
- Displayed legitimate probability: **100.00%**

This confirms that the saved model and Streamlit prediction pipeline worked correctly for this particular test sample.

> A single validation example demonstrates that the prototype pipeline is functioning for that sample; it does not establish generalisation performance.

---

## 15. Project Structure

```text
Phishing/
│
├── app.py
├── phishing_cleaned.csv
├── phishing_decision_tree_model.pkl
├── phishing_feature_names.pkl
├── requirements.txt
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `app.py` | Streamlit application |
| `phishing_cleaned.csv` | Cleaned project dataset |
| `phishing_decision_tree_model.pkl` | Saved Decision Tree model |
| `phishing_feature_names.pkl` | Saved feature-name list |
| `requirements.txt` | Python package requirements |
| `README.md` | Project documentation |

---

## 16. Installation

### Step 1: Install Python

The project was developed and tested using Python 3.13.x.

Check your Python installation:

```bash
py --version
```

### Step 2: Open the Project Folder

```bash
cd C:\Phishing
```

### Step 3: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

### Step 4: Run Streamlit

```bash
py -m streamlit run app.py
```

---

## 17. Reproducibility

The saved model and feature-name file are included so that the Streamlit application can load the trained model without retraining it.

The notebook used for data loading, preprocessing, analysis, training and evaluation is:

```text
Phishing_URL_Behaviour_Classification.ipynb
```

---

## 18. Limitations

- The current application does not accept a raw URL and automatically extract all 30 features.
- Several dataset features represent webpage/domain characteristics and cannot be reliably determined from a URL string alone without additional processing or external/network access.
- The reported model results are based on the project's cleaned dataset and one held-out test split.
- The duplicate/conflicting-label cleaning procedure changes the original dataset size and is a project-specific preprocessing choice.
- A model's performance on this dataset does not guarantee performance against new or evolving phishing techniques.

---

## 19. Future Scope

Possible future improvements include:

- Building automatic feature extraction from raw URLs.
- Testing additional machine learning models.
- Hyperparameter tuning and cross-validation.
- Evaluating the system on newer phishing datasets.
- Adding stronger real-world validation.
- Improving the Streamlit interface.
- Adding model monitoring and periodic retraining.
- Exploring explainable AI methods to show why a URL/webpage record was classified as phishing.

---

## 20. References

1. Mohammad, R. & McCluskey, L. (2012). *Phishing Websites*. UCI Machine Learning Repository. DOI: 10.24432/C51W2X.
2. Pedregosa, F., et al. (2011). “Scikit-learn: Machine Learning in Python.” *Journal of Machine Learning Research*, 12, 2825–2830.
3. Streamlit Documentation.
4. Learn Depth Academy LLP. *Track 1 Final Capstone – Problem 02: Phishing URL Behaviour Classification*, 2026.

---

## 21. Disclaimer

This project is developed for educational and academic purposes. The classification output should not be treated as a complete security verdict for real-world websites.

---

## Author

**Lokesh M**  
B.E. Computer Science and Engineering  
Phishing URL Behaviour Classification – Machine Learning Capstone Project
