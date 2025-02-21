import streamlit as st
import pandas as pd
from splink.exploratory import similarity_analysis as sa
import splink.comparison_library as cl
from splink import DuckDBAPI

def create_similarity_analysis_app():
    st.title("String Similarity Analysis")
    
    # Input fields
    string1 = st.text_input("Enter first string:", "Richard")
    string2 = st.text_input("Enter second string:", "iRchard")
    
    if st.button("Compare Strings"):
        # Get similarity scores
        result = sa.comparator_score(string1, string2)
        
        # Display results
        st.dataframe(result)
        
        # Show phonetic transformations
        st.subheader("Phonetic Transformations")
        ph1 = sa.phonetic_transform(string1)
        ph2 = sa.phonetic_transform(string2)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"String 1: {ph1}")
        with col2:
            st.write(f"String 2: {ph2}")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a tool:", 
        ["Similarity Analysis", "Comparison Playground", "Data Profiling"])
    
    if page == "Similarity Analysis":
        create_similarity_analysis_app()

if __name__ == "__main__":
    main()