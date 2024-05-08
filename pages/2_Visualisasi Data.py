import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("(1)data.csv")

st.set_page_config(
    page_title="Datmin - Deployment",
    page_icon="📊",
)

st.sidebar.success("Pilih page di atas.")

st.title("📊 Visualisasi Data")

st.write("""   
   Pada page ini ditampilkan visualisasi yang insighful berkaitan dengan faktor-faktor yang mempengaruhi prediksi minat mahasiswa 
   dalam menentukan karir berwirausaha. Selain dIberikan informasi melalui visualisasi yang memberikan gambaran terkait faktor-faktor
   yang mempengaruhi prediksi mahasiswa berpotensi menjadi seorang wirausahawan atau tidak, diberikan juga insight berupa interpretasi dan
   actionable insight.
    """)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Composition", "Relationship", "Distribution", "Comparison"])

with tab1:
   def daftar_visualisasi():
      st.header("Daftar Visualisasi 📈")
      st.write("""Berikut adalah daftar dari visualisasi terkait faktor-faktor yang mempengaruhi prediksi minat mahasiswa dalam menentukan 
               karir berwirausaha. Silahkan pilih tab untuk melihat visualisasi data!""")
      st.write("""
         1. **Composition** : komposisi dari faktor-faktor yang mempengaruhi prediksi minat mahasiswa.
         2. **Relationship** : hubungan antara faktor-faktor yang mempengaruhi prediksi minat mahasiswa.
         3. **Distribution** : distribusi dari faktor-faktor yang mempengaruhi prediksi minat mahasiswa.
         4. **Comparison** : perbandingan antara faktor-faktor yang mempengaruhi prediksi minat mahasiswa.
      """)
   daftar_visualisasi()

with tab2:
   st.header("Composition")
   option = st.selectbox(
      "Pilih informasi apa yang ingin di dapatkan.",
      ["Komposisi Demografi dan Pengaruh", "Komposisi Karakteristik Individu", "Komposisi Sektor Pendidikan dan Karakteristik Utama"],
      help="Diberikan informasi yang mencakup visualisasi beserta insightnya."
   )
   # composition 1
   if option == "Komposisi Demografi dan Pengaruh":
      def composition_plot1():
         cols = ['Gender', 'City', 'Influenced']

         fig, axs = plt.subplots(1, len(cols), figsize=(30, 12))

         def plot_pie_chart(col, ax):
            data = df[col].value_counts(normalize=True) * 100
            max_index = data.idxmax()
            colors = ['#1e90ff' if idx == max_index else '#bfbfbf' for idx in data.index]
            data.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax, colors=colors)
            ax.set_title(f'{col}')
            ax.set_ylabel('')

         for i, col in enumerate(cols):
            plot_pie_chart(col, axs[i])

         plt.tight_layout()

         st.pyplot(fig)

         col1, col2 = st.columns(2)
         with col1.expander("Interpretasi ⓘ"):
            st.subheader("Interpretasi")
            st.write("""
               Dari visualisasi yang disajikan terlihat bahwa mayoritas mahasiswa merupakan pria, tinggal di kota, dan cenderung mudah terpengaruh. 
               Perbedaan ini menawarkan wawasan yang penting untuk mengarahkan langkah-langkah yang mendukung beragam kebutuhan mahasiswa, terutama
               dalam meningkatkan potensi mahasiswa menjadi wirausahawan.
            """)
         with col2.expander("Actionable insight ⓘ"):
            st.subheader("Actionable insight")
            st.write("""
               Dari visualisasi data yang menggambarkan mayoritas mahasiswa sebagai pria yang tinggal di kota dan cenderung mudah terpengaruh, penting 
               untuk merancang program yang spesifik untuk mendukung kebutuhan mereka dalam berwirausaha. Langkah yang bisa diambil termasuk penyediaan 
               pelatihan dalam pengembangan keterampilan kewirausahaan. Lalu, untuk mahasiswa yang tinggal di kota dapat manfaatkan workshop dan jaringan 
               lokal untuk perkembangan diri, sedangkan bagi yang tidak tinggal di kota dapat mengakses teknologi digital untuk mengembangkan diri. Kemudian,
               mahasiswa dapat sembari meminimalkan dampak negatif dari kemudahan mereka terpengaruh oleh faktor eksternal.
            """)
      composition_plot1()
   # composition 2
   elif option == "Komposisi Karakteristik Individu":
      def composition_plot2():
         numerical_cols = [
            'Age', 'Perseverance', 'DesireToTakeInitiative',
            'Competitiveness', 'SelfReliance', 'StrongNeedToAchieve',
            'SelfConfidence', 'GoodPhysicalHealth'
         ]

         fig, axs = plt.subplots(2, 4, figsize=(18, 10))
         axs = axs.flatten()

         for i, col in enumerate(numerical_cols):
            ax = axs[i]
            sns.countplot(data=df, x=col, ax=ax, color='deeppink')
            ax.set_title(f'{col}')
            ax.set_xlabel('')
            ax.set_ylabel('Count')
            ax.tick_params(axis='x', rotation=15)

            for bar in ax.patches:
               if bar.get_height() == df[col].value_counts().max():
                     continue
               bar.set_color('lightgrey')

         plt.tight_layout()

         st.pyplot(fig)

         col1, col2 = st.columns(2)
         with col1.expander("Interpretasi ⓘ"):
            st.subheader("Interpretasi")
            st.write("""
               Dari visualisasi yang disajikan disimpulkan dari rentang umur 17 hingga 26 tahun mayoritas mahasiswa di umur 20 tahun. Dan
               dapat diketahui juga bahwa mayoritas mahasiswa memiliki tingkat ketekunan, inisiatif, kemandirian, kepercayaan diri, keinginan 
               untuk berhasil, dan kesehatan fisik yang tinggi. Hal ini menunjukkan bahwa dalam populasi mahasiswa yang diamati, terdapat pola 
               umum yang menunjukkan adanya komitmen yang kuat terhadap pendidikan dan kesejahteraan fisik. Adanya mayoritas mahasiswa dengan 
               tingkat atribut positif ini dapat menjadi indikator potensial untuk kesuksesan akademik dan kesejahteraan individu di lingkungan kampus.
            """)
         with col2.expander("Actionable insight ⓘ"):
            st.subheader("Actionable insight")
            st.write("""
               Meskipun mayoritas mahasiswa menunjukkan tingkat atribut positif yang tinggi, masih penting untuk terus mendorong pengembangan keterampilan dan 
               sikap yang berkelanjutan di antara mahasiswa. Hal ini dapat dilakukan melalui program-program pembinaan dan pembelajaran yang mengedepankan 
               pengembangan karakter, keterampilan kepemimpinan, kesehatan mental, dan kesehatan fisik. Dukungan dan bimbingan dari pihak universitas serta 
               pembentukan komunitas yang mendukung juga dapat membantu meningkatkan kesejahteraan dan prestasi akademik mahasiswa secara keseluruhan.
            """)
      composition_plot2()
   # composition 3
   else:
      def composition_plot3():
         edu_categories = df['EducationSector'].unique()
         traits_categories = df['KeyTraits'].unique()

         edu_palette = ['deeppink' if x == edu_categories[0] else 'lightgrey' for x in edu_categories]
         traits_palette = ['deeppink' if x == traits_categories[2] else 'lightgrey' for x in traits_categories]

         fig, axs = plt.subplots(1, 2, figsize=(16, 6))

         sns.countplot(data=df, y='EducationSector', hue='EducationSector', ax=axs[0], palette=edu_palette, legend=False)
         axs[0].set_title('Education Sector')
         axs[0].set_ylabel('Education Sector')
         axs[0].set_xlabel('Count')

         sns.countplot(data=df, y='KeyTraits', hue='KeyTraits', ax=axs[1], palette=traits_palette, legend=False)
         axs[1].set_title('Key Traits')
         axs[1].set_ylabel('Key Traits')
         axs[1].set_xlabel('Count')

         plt.tight_layout()

         st.pyplot(fig)

         col1, col2 = st.columns(2)
         with col1.expander("Interpretasi ⓘ"):
            st.subheader("Interpretasi")
            st.write("""
               Dari visualisasi yang disajikan terlihat bahwa mayoritas mahasiswa mengambil jurusan dalam bidang ilmu Engineering Sciences. 
               Hal ini menggambarkan potensi besar dalam mengembangkan kewirausahaan di kalangan mahasiswa, terutama dalam menciptakan inovasi 
               dan solusi berkelanjutan yang dapat mendukung pertumbuhan ekonomi. Lalu, terlihat juga bahwa mayoritas mahasiswa memiliki 
               karakteristik utama Ketahanan (Resilience) yang menunjukkan sifat dalam menghadapi tantangan atau dalam mempersiapkan diri dalam berwirausaha
               pada dunia kerja.
            """)
         with col2.expander("Actionable insight ⓘ"):
            st.subheader("Actionable insight")
            st.write("""
               Dalam rangka memanfaatkan potensi wirausaha di kalangan mahasiswa, institusi pendidikan dapat mengambil langkah-langkah konkret 
               untuk mendukung pengembangan kewirausahaan. Salah satunya adalah dengan memperkuat program-program pendidikan yang menekankan pada 
               keterampilan kewirausahaan dalam bidang-bidang yang berkaitan dengan minat mahasiswa kedepannya. Selain itu, institusi juga dapat menyediakan 
               akses ke platform yang mendukung mahasiswa yang tertarik berwirausaha, seperti kelas-kelas mentoring dari profesional industri, sehingga mengembangkan
               pertumbuhan kewirausahaan di kalangan mahasiswa, yang nantinya akan memberikan kontribusi pada pembangunan ekonomi.
            """)
      composition_plot3()

with tab3:
   st.header("Relationship")
   def relationship_plot():
      numerical_columns = df.select_dtypes(include=[np.number]).columns

      if len(numerical_columns) < 2:
         st.error("Error: At least two numerical columns are required for heatmap generation.")
      else:
         correlation_matrix = df[numerical_columns].corr()

         plt.figure(figsize=(10, 6))
         sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

         plt.xlabel("Selected Columns")
         plt.ylabel("Selected Columns")
         plt.title("Hubungan antar kolom dengan Heatmap")

         plt.xticks(rotation=45, ha="right")

         st.pyplot(plt.gcf())

      col1, col2 = st.columns(2)
      with col1.expander("Interpretasi ⓘ"):
         st.subheader("Interpretasi")
         st.write("""Hubungan kuat antara ketekunan, kepercayaan diri, inisiatif, kesehatan fisik, dan kompetitivitas menyoroti bahwa mahasiswa yang 
                     memiliki kombinasi sifat-sifat ini cenderung memiliki motivasi yang tinggi untuk mencapai kesuksesan. Kecenderungan mereka untuk 
                     gigih dalam menghadapi tantangan, kepercayaan pada kemampuan diri sendiri, serta kemauan untuk proaktif dan berada dalam kondisi 
                     fisik yang prima, memperkuat posisi mereka dalam mencapai prestasi tinggi dan bersaing di lingkungan yang kompetitif. Kualitas-kualitas 
                     ini secara keseluruhan mendukung potensi mahasiswa menjadi seorang wirausahawan, khususnya dalam situasi yang membutuhkan kemampuan 
                     untuk menonjol dan memimpin.
                  """)
      with col2.expander("Actionable insight ⓘ"):
         st.subheader("Actionable insight")
         st.write("""Untuk meningkatkan ketekunan, dorong motivasi dan semangat individu untuk mencapai keunggulan dan kompetitivitas 
                     diberikan dukungan proaktif dalam menghadapi tantangan, mengidentifikasi keinginan untuk bersaing, dan menciptakan lingkungan
                     kerja yang mendukung kemandirian. Lalu, meningkatkan kesehatan fisik melalui program kesehatan, serta mendukung pengembangan diri 
                     melalui pelatihan dan mentoring untuk membangun kepercayaan diri.
                  """)
   relationship_plot()

with tab4:
   st.header("Distribution")
   def distribution_plot():
      numeric_cols = [
         'Age', 'Perseverance', 'DesireToTakeInitiative',
         'Competitiveness', 'SelfReliance', 'StrongNeedToAchieve',
         'SelfConfidence', 'GoodPhysicalHealth'
      ]

      fig, axs = plt.subplots(2, 4, figsize=(14, 6))
      fig.tight_layout(pad=2.0)

      for i, col in enumerate(numeric_cols):
         ax = axs[i // 4, i % 4]
         sns.histplot(df[col], kde=False, ax=ax, color='steelblue', bins=10)
         ax.set_xlabel(col)
         ax.set_ylabel('Count')

      st.pyplot(fig) 

      col1, col2 = st.columns(2)
      with col1.expander("Interpretasi ⓘ"):
         st.subheader("Interpretasi")
         st.write("""Distribusi data ini menunjukkan bahwa data terdiri dari mahasiswa yang kebanyakan berusia antara 
                  19 hingga 22 tahun, dengan kecenderungan yang kuat dalam menunjukkan ketekunan, keinginan untuk mengambil inisiatif, 
                  dan tingkat kompetitif yang tinggi. Sebagian besar mahasiswa juga merasa mandiri dan memiliki kepercayaan diri yang 
                  tinggi, serta memiliki kesehatan fisik yang baik. Hal ini menggambarkan sebuah gambaran mahasiswa yang sangat termotivasi 
                  dan aspiratif, yang menjadikan mereka kandidat ideal untuk potensi menjadi wirausahawan.
                  """)
      with col2.expander("Actionable insight ⓘ"):
         st.subheader("Actionable insight")
         st.write("""Mengingat tingginya tingkat ketekunan, keinginan untuk mengambil inisiatif, dan kepercayaan diri yang tinggi di antar mahasiswa, 
                  institusi pendidikan dapat mengembangkan program pengembangan karir yang fokus pada penguatan kompetensi ini. Program ini bisa meliputi 
                  pelatihan khusus untuk mengasah kemampuan mahasiswa dalam berwirausaha, serta menyediakan platform untuk mengeksplorasi informasi berkaitan
                  dengan wirausaha dan dapat mengimplementasikan ide-ide inovatif.
                  """)
   distribution_plot()

with tab5:
   st.header("Comparison")
   def comparison_plot():
      numerical_cols = [
         'Perseverance', 'DesireToTakeInitiative',
         'Competitiveness', 'SelfReliance', 'StrongNeedToAchieve',
         'SelfConfidence'
      ]

      categorical_cols = ['City', 'Influenced', 'KeyTraits']

      gender_colors = {0: 'skyblue', 1: 'lightcoral'}

      fig, axs = plt.subplots(3, 4, figsize=(20, 10))
      axs = axs.flatten()

      for i, col in enumerate(numerical_cols):
         ax = axs[i]
         grouped_data = df.groupby([col, 'y'])[col].count().unstack(fill_value=0)
         grouped_data.plot(kind='bar', stacked=True, ax=ax, color=['lightcoral', 'skyblue'])
         ax.set_title(f'Comparison in {col} by y')
         ax.set_xlabel(col)
         ax.set_ylabel('Count')

      for i, col in enumerate(categorical_cols, start=len(numerical_cols)):
         ax = axs[i]
         sns.countplot(data=df, y=col, hue='y', ax=ax, palette=gender_colors)
         ax.set_title(f'Comparison in {col} by y')
         ax.set_ylabel(col)
         ax.set_xlabel('Count')

      fig.delaxes(axs[-1])
      fig.delaxes(axs[-2])
      fig.delaxes(axs[-3])

      plt.tight_layout()

      st.pyplot(fig)

      col1, col2 = st.columns(2)
      with col1.expander("Interpretasi ⓘ"):
         st.subheader("Interpretasi")
         st.write("""
            Lebih sedikit orang yang memiliki ketekunan, inisiatif, keinginan, kepercayaan diri, dan kemandirian menjadi wirausahawan 
            dibandingkan dengan yang tidak. Orang-orang yang tinggal di kota lebih cenderung menjadi wirausahawan daripada yang 
            tidak tinggal di kota. Lebih banyak orang yang tidak terpengaruh menjadi wirausahawan daripada yang mudah terpengaruh. 
            Sebagian besar wirausahawan memiliki karakteristik passion dan resilience.
         """)
      with col2.expander("Actionable insight ⓘ"):
         st.subheader("Actionable insight")
         st.write("""
            Fokus pada pengembangan keterampilan kewirausahaan yang mencakup ketekunan, inisiatif, dan kepercayaan diri, serta memberikan 
            dukungan khusus untuk wirausahawan untuk yang tidak tinggal di kota dan mengidentifikasi potensi wirausahawan yang tidak terpengaruh, 
            sambil mendorong karakteristik passion dan resilience.
         """)
   comparison_plot()
