import streamlit as st
import pandas as pd
import joblib
import os


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Phishing URL Behaviour Classification",
    page_icon="🔐",
    layout="wide"
)


# ---------------------------------------------------------
# Load Model and Feature Names
# ---------------------------------------------------------

MODEL_FILE = "phishing_decision_tree_model.pkl"
FEATURE_FILE = "phishing_feature_names.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_FILE)


@st.cache_data
def load_features():
    return joblib.load(FEATURE_FILE)


model = load_model()
feature_names = load_features()


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.title("🔐 Phishing URL Behaviour Classification")

st.write(
    "This application uses a trained Decision Tree machine learning "
    "model to classify URL/webpage behaviour as Legitimate or Phishing."
)

st.info(
    "Enter the 30 dataset feature values below. "
    "The UCI dataset uses encoded feature values of -1, 0 and 1."
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

st.sidebar.header("About the Project")

st.sidebar.write(
    """
    **Problem:** Phishing URL Behaviour Classification

    **Machine Learning Task:** Binary Classification

    **Model:** Decision Tree

    **Input:** 30 engineered URL/webpage features

    **Output:**
    - Legitimate
    - Phishing
    """
)

st.sidebar.markdown("---")

st.sidebar.write("Target encoding:")
st.sidebar.write("0 = Legitimate")
st.sidebar.write("1 = Phishing")


# ---------------------------------------------------------
# Feature Input Form
# ---------------------------------------------------------

st.subheader("Enter Feature Values")

st.write(
    "Select the encoded value for each feature. "
    "Use the dataset's original encoding: -1, 0 or 1."
)


feature_values = {}

with st.form("prediction_form"):

    columns = st.columns(3)

    for index, feature in enumerate(feature_names):

        column = columns[index % 3]

        with column:
            feature_values[feature] = st.selectbox(
                feature,
                options=[-1, 0, 1],
                index=1,
                key=feature
            )

    submitted = st.form_submit_button(
        "🔍 Predict URL Behaviour",
        use_container_width=True
    )


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------

if submitted:

    input_data = pd.DataFrame(
        [feature_values],
        columns=feature_names
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    # Find probability of phishing
    phishing_index = list(model.classes_).index(1)
    phishing_probability = probability[phishing_index] * 100

    legitimate_probability = 100 - phishing_probability

    st.markdown("---")
    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("🚨 PHISHING URL BEHAVIOUR")

        st.write(
            f"Estimated phishing probability: "
            f"**{phishing_probability:.2f}%**"
        )

    else:

        st.success("✅ LEGITIMATE URL BEHAVIOUR")

        st.write(
            f"Estimated legitimate probability: "
            f"**{legitimate_probability:.2f}%**"
        )

    # Probability display
    st.subheader("Prediction Probability")

    probability_data = pd.DataFrame(
        {
            "Class": ["Legitimate", "Phishing"],
            "Probability (%)": [
                legitimate_probability,
                phishing_probability
            ]
        }
    )

    st.bar_chart(
        probability_data.set_index("Class")
    )

    # Show submitted values
    with st.expander("View Input Features"):

        st.dataframe(
            input_data.T.rename(
                columns={0: "Value"}
            )
        )


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

st.markdown("---")

st.caption(
    "Phishing URL Behaviour Classification | "
    "Machine Learning Capstone Project"
)