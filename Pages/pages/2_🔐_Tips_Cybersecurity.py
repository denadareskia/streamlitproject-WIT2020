import streamlit as st
import streamlit.components.v1 as components
import random as _random
import string 

st.set_page_config(
    page_title="Tips Cybersecurity",
    page_icon="🔐",
    layout="wide"
)

with st.container():
    st.markdown("<h1 style='text-align: center;'>Tips Agar Terhindar dari Serangan Siber (<i>Cyber Crime</i>)</h1>", unsafe_allow_html=True)

with st.container():
    tab1, tab2 = st.tabs(["Tips Terhindar dari Cybercrime", "Password Generator"])
    with tab1:
        st.markdown("""
        Dengan semakin banyaknya negara yang mendorong warganya untuk tinggal, belajar atau bekerja dari rumah, sekaranglah saatnya untuk fokus pada keamanan siber, baik untuk diri sendiri atau tempat kerja Anda.

        - Cadangkan semua file penting Anda, dan simpan secara terpisah dari sistem Anda (misalnya di cloud, di drive eksternal)
        - Selalu verifikasi bahwa Anda berada di situs web resmi perusahaan sebelum memasukkan detail login atau informasi sensitif.
        - Pastikan Anda menginstal perangkat lunak anti-virus terbaru di komputer dan perangkat seluler Anda.
        - Perkuat keamanan jaringan kantor maupun di rumah dengan _network encription_, misalnya _Wi-Fi Protected Access 2 (WPA2)_.
        - Mengamankan gateway email untuk menggagalkan ancaman melalui spam.
        - Mengamankan kerentanan administrasi sistem yang dapat disalahgunakan oleh penyerang.
        - Unduh aplikasi seluler atau perangkat lunak lainnya hanya dari platform terpercaya.
        - Periksa dan perbarui pengaturan privasi secara teratur di akun media sosial Anda.
        - Perbarui kata sandi Anda dan pastikan kata sandinya kuat (campuran huruf besar, huruf kecil, angka, dan karakter khusus);
        - Jangan mengklik tautan atau membuka lampiran dalam email yang tidak Anda harapkan akan diterima, atau berasal dari pengirim yang tidak dikenal.
        """)

        empty1,col1,empty2=st.columns([1,3,1])
        with empty1:
                st.empty()
        with col1:
                components.iframe("""
                https://youtube.com/embed/TKB8rdYKcUE""", width=800, height= 450)
        with empty2:
                st.empty()

    with tab2:
        # ---- Password Generator ----
        with st.container():
            empty1,col1,empty2=st.columns([1,3,1])
            with empty1:
                st.empty()
                
            with col1:
                st.markdown("<h1 style='text-align: center; color: black;'>Streamlit Password Generator </h1>", unsafe_allow_html=True)
                st.markdown("""Banyak diantara kita yang tidak sadar tentang keamanan akun sosial media, terutama penggunaan password yang memakai kata-kata umum sehingga akan sangat mudah 
                disadap oleh orang-orang yang tidak bertanggung jawab. Maka dari itu, kami menyediakan fitur sederhana untuk membuat password yang aman dengan campuran huruf kapital, huruf kecil
                juga campuran simbol.
                """)
                st.text(" \n")
                st.text(" \n")

                length = st.number_input('Berapa banyak karakter password yang kamu inginkan? (8 - 16)', min_value=8, max_value=16)
                st.text(" \n")

                title = st.write('Silahkan pilih karakter yang kamu inginkan di Password kamu:')

                st.text(" \n")

                #create password variables
                lower="abcdefghijklmnopqrstvuyz"
                upper=lower.upper()
                number="0123456789"

                cb1 = st.checkbox('Numbers')
                cb2 = st.checkbox('Letters')
                cb3 = st.checkbox('Special Characters ($%?!)')

                empty = st.empty()

                if cb1 == True:
                        numbers = number
                else:
                        numbers = ""

                if cb2 == True:
                        letters = upper + lower
                else:
                        letters = ""

                if cb3 == True:
                        symbols = string.punctuation
                else:
                        symbols = ""

                if cb1 and cb1 and cb3 == None: 
                        st.write("Check")

                all = letters + str(numbers) + symbols

                try:
                        temp = _random.sample(all, length)
                except ValueError:
                        pass

                try:
                        temp2 = _random.sample(all, length)
                except ValueError:
                        pass
                                
                try:
                        password = "".join(temp)
                except ValueError and NameError:
                        pass

                try:
                        password2 = "".join(temp2)
                except ValueError and NameError:
                        pass

                try: 
                        title2 = st.write(' ')
                except:
                        NameError
                        st.write(" ")
                        
                st.text(" \n")

                try:
                        st.code(password)
                        st.code(password2)

                except ValueError and NameError:
                        st.write("Centang kotak diatas")

            with empty2:
                st.empty()
                