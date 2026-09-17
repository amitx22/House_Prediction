import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(
    "house_price_model.pkl"
)

model_columns = joblib.load(
    "model_columns.pkl"
)


# ============================================================
# TITLE
# ============================================================

st.title("🏠 House Price Prediction")

st.write(
    "Enter house details to predict the estimated house price."
)


# ============================================================
# USER INPUT
# ============================================================

square_footage = st.number_input(
    "Square Footage",
    min_value=100,
    max_value=10000,
    value=2000
)

num_bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

num_bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10,
    value=2
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2010
)

lot_size = st.number_input(
    "Lot Size",
    min_value=0.1,
    max_value=20.0,
    value=2.5
)

garage_size = st.number_input(
    "Garage Size",
    min_value=0,
    max_value=5,
    value=1
)

neighborhood_quality = st.slider(
    "Neighborhood Quality",
    min_value=1,
    max_value=10,
    value=8
)


# ============================================================
# CREATE INPUT DATA
# ============================================================

input_data = pd.DataFrame({
    "Square_Footage": [square_footage],
    "Num_Bedrooms": [num_bedrooms],
    "Num_Bathrooms": [num_bathrooms],
    "Year_Built": [year_built],
    "Lot_Size": [lot_size],
    "Garage_Size": [garage_size],
    "Neighborhood_Quality": [neighborhood_quality]
})


# ============================================================
# PREDICTION
# ============================================================

if st.button(
    "🔮 Predict House Price",
    use_container_width=True
):

    prediction = model.predict(
        input_data
    )[0]

    st.success(
        "Prediction completed successfully!"
    )

    st.metric(
        "Estimated House Price",
        f"${prediction:,.2f}"
    )

    st.info(
        "This is an ML-based estimated price."
    )