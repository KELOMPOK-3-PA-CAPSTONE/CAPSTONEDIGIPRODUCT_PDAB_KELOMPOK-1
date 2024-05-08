import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
from knn import KNeighborsClassifier

model = joblib.load('knn.pkl')

st.set_page_config(
    page_title="Datmin - Deployment",
    page_icon="📊",
)

st.sidebar.success("Pilih page di atas.")

st.title("📝 Analisis Prediksi")

st.write("""
         
    Pada page ini memiliki tujuan untuk memprediksi apakah seorang mahasiswa berpotensi menjadi seorang wirausahawan atau tidak berdasarkan 
    faktor-faktor yang mempengaruhi analisis prediksi yang dilakukan. Prediksi dapat dilakukan dengan memasukkan data yang
    relevan dengan mahasiswa. Silahkan masukkan data-data dibawah.

    """)

st.subheader("Pilih Opsi 💡")

def user_input_features():
    inputs = {}
    col1, col2 = st.columns(2)

    with col1:
        inputs['EducationSector'] = st.selectbox(
            'Education Sector',
            options=[0, 1, 2, 3, 4, 5, 6, 7, 8],
            format_func=lambda x: ["Engineering Sciences", "Economic Sciences, Business Studies, Commerce and Law", "Art, Music or Design", 
                                "Humanities and Social Sciences", "Medicine, Health Sciences", "Teaching Degree (e.g., B.Ed)",
                                "Mathematics or Natural Sciences", "Language and Cultural Studies", "Others"][x],
            help="Pilih sektor edukasi yang sesuai."
        )
        inputs['Gender'] = st.selectbox(
            'Gender',
            options=[0, 1],
            format_func=lambda x: ["Male", "Female"][x],
            help="Pilih gender yang sesuai."
        )
        inputs['City'] = st.selectbox(
            'City',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda tinggal di daerah perkotaan?"
        )
        inputs['Influenced'] = st.selectbox(
            'Influenced',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda mudah terpengaruh dengan orang lain?"
        )
        inputs['KeyTraits_Passion'] = st.selectbox(
            'Key Traits: Passion',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda memiliki semangat kuat untuk usaha Anda?"
        )
        inputs['KeyTraits_Positivity'] = st.selectbox(
            'Key Traits: Positivity',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda umumnya orang yang positif?"
        )
        inputs['KeyTraits_Resilience'] = st.selectbox(
            'Key Traits: Resilience',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda memiliki ketahanan yang kuat dalam menghadapi kesulitan?"
        )
        inputs['KeyTraits_Vision'] = st.selectbox(
            'Key Traits: Vision',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda memiliki visi yang jelas mengenai tujuan Anda?"
        )
        inputs['KeyTraits_Work Ethic'] = st.selectbox(
            'Key Traits: Work Ethic',
            options=[0, 1],
            format_func=lambda x: ["No", "Yes"][x],
            help="Apakah Anda memiliki etos kerja yang kuat?"
        )  
    
    with col2:
        inputs['Age'] = st.slider(
            'Age', 17, 30, 17,
            help="Pilih umur yang sesuai."
        )
        inputs['Perseverance'] = st.slider(
            'Perseverance', 1, 5, 1,
            help="Nilai tingkat ketekunan Anda dari 1 (Rendah) hingga 5 (Tinggi)."
        )
        inputs['DesireToTakeInitiative'] = st.slider(
            'Desire To Take Initiative', 1, 5, 1,
            help="Nilai keinginan Anda untuk mengambil inisiatif dari 1 (Rendah) hingga 5 (Tinggi)."
        )
        inputs['Competitiveness'] = st.slider(
            'Competitiveness', 1, 5, 1,
            help="Nilai tingkat kompetitif Anda dari 1 (Rendah) hingga 5 (Tinggi)."
        )
        inputs['SelfReliance'] = st.slider(
            'Self Reliance', 1, 5, 1,
            help="Nilai tingkat kemandirian Anda dari 1 (Rendah) hingga 5 (Tinggi)."
        )
        inputs['StrongNeedToAchieve'] = st.slider(
            'Strong Need To Achieve', 1, 5, 1,
            help="Nilai kebutuhan Anda untuk mencapai kesuksesan dari 1 (Rendah) hingga 5 (Tinggi)."
        )
        inputs['SelfConfidence'] = st.slider(
            'Self Confidence', 1, 5, 1,
            help="Nilai kepercayaan diri Anda dari 1 (Rendah) hingga 5 (Tinggi)."
        )
        inputs['GoodPhysicalHealth'] = st.slider(
            'Good Physical Health', 1, 5, 1,
            help="Nilai kesehatan fisik Anda dari 1 (Rendah) hingga 5 (Tinggi)."
        )

    return pd.DataFrame(inputs, index=[0])

def make_prediction(input_data):
    prediction = model.predict(input_data)
    return prediction

def main():
    input_data = user_input_features()
    
    if st.button('Prediksi'):
        result = make_prediction(input_data)
        st.info(f'Hasil prediksi: {result[0]}')
        if result == 0:
            st.error(f'Mahasiswa tidak berpotensi menjadi seorang wirausahawan 😞')
        else:
            st.success(f'Mahasiswa berpotensi menjadi seorang wirausahawan 🤩')

if __name__ == '__main__':
    main()
