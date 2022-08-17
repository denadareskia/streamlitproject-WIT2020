from unicodedata import name
from numpy import source
import requests
import streamlit as st
import pandas as pd
import altair as alt
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Cibernetica",
    page_icon=":tada:",
    layout="wide"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottieurl1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- Load Assets ----
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_8axjdnts.json")
lottie_coding1 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_96cnyxkh.json")

# ---- Header Section ----

with st.container():
    st.markdown("<h1 style='text-align: center;'>Dampak Pandemi Covid-19 pada Keamanan Siber (<i>Cybersecurity</i>)</h1>", unsafe_allow_html=True)

# ---- Opening ----

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("### Dampak Pandemi COVID-19")
        st.write(
            """
            Organisasi Kesehatan Dunia (WHO) mencatat hingga tanggal 4 Agustus 2022 ada sebanyak 570 juta kasus COVID - 19 yang terkonfirmasi, termasuk didalamnya sekitar 6 juta kematian.
            Per tanggal 1 Agustus 2022, total 12 milyar dosis vaksin telah diberikan kepada penduduk dunia dari semua negara.

            Belum berakhirnya pandemi virus corona (COVID - 19) tidak hanya berdampak kepada kondisi ekonomi dunia.
            Karantina massal para penderita COVID - 19 sebagai salah satu solusi untuk menekan angka penyebaran virus harus dilakukan dan
            keputusan untuk melakukan karantina daerah (lockdown) oleh beberapa pemerintah setempat telah menumbuhkan kebiasaan baru yang dikenal dengan 'Normal Baru'.

            'Normal Baru' (New Normal) tidak hanya terkait dengan bagaimana kita berinteraksi secara langsung dengan manusia lainnya melainkan hampir seluruh aspek kehidupan kita harus ikut terbarukan.
            Salah satunya adalah bagaimana cara kita menggunakan internet untuk bisa tetap saling terhubung dan mendukung keberlangsungan kehidupan kita.

            Masyarakat digiring untuk terbiasa dengan kehidupan berbasis teknologi yang mana pertumbuhan aktivitas siber menjadi sangat pesat
            namun tidak berjalan seiring dengan pertumbuhan pengetahuan dan kesadaran masyarakat tentang keamanan mereka dalam dunia siber.
            """
        )

    with right_column:
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",
            height=400,
            key="covid19"
        )

    with right_column:
        st.caption('Jumlah Pengguna Internet Dunia (2018- 2022)')
        source = pd.DataFrame({
            'Miliar': [3.95, 4.21, 4.42, 4.76, 4.95],
            'Tahun' : ['2018', '2019', '2020', '2021', '2022']
        })

        bar_chart = alt.Chart(source).mark_bar().encode(
            y='Miliar',
            x='Tahun',
        )
        st.altair_chart(bar_chart, use_container_width=True)
        st.caption('Sumber: DataReportal, 26 Januari 2022')

st.text(" \n")
st.text(" \n")

with st.container():
    st.markdown("<h1 style='text-align: center;'>Pendahuluan tentang Cybersecurity</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Cybersecurity", "Konsep Cybersecurity", "Penerapan Cybersecurity", "Landasan Hukum Cybercrime di Indonesia"])

    with tab1:
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("### Apa itu Cybersecurity?")
            st.write(
                """
                Dilansir dari **CISCO**, cybersecurity adalah proses perlindungan sistem, data, jaringan, dan program dari ancaman atau serangan digital.

                Jika mengacu pada **International Telecommunication Unit (ITU)**, cyber security adalah aktivitas yang meliputi kebijakan dan konsep keamanan dan berfungsi melindungi aset organisasi.
                
                Perlindungan terhadap organisasi dan aset pengguna termasuk perangkat komputasi, aplikasi, layanan dan informasi yang dikirimkan dan / atau disimpan di lingkungan cyber.

                Dengan menerapkan cyber security, Anda dapat mengurangi resiko ancaman yang menyasar sistem komputer Anda. Sedikit info, cyber security adalah bagian dari website development.
                """
            )
        with right_column:
            st_lottie(lottie_coding1, height=300, key="cybersecurity")
    
    with tab2:
        st.markdown("### Mengenal Konsep Cybersecurity")
        st.write("""
        Cyber security mengacu pada praktik memastikan **Confidentiality (kerahasiaan), Integrity (integritas), dan Availability (ketersediaan)** informasi. Tiga poin di barusan dikenal sebagai CIA Triad.

        **CIA Triad** sebenarnya adalah model keamanan yang dikembangkan untuk membantu manusia memikirkan berbagai bagian keamanan teknologi informasi. 
        Model inilah yang menjadi konsep cyber security.
        """)
        components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        
        <div class="card">
            <div class="card-body">
                <table class="table">
                    <thead class="thead-light">
                        <tr>
                            <th>Nama Konsep</th>
                            <th>Definisi</th>
                            <th>Penerapan</th>
                            <th>Contoh Kasus</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><i>Confidentiality</i> (Kerahasiaan)</td>
                            <td>Usaha untuk merahasiakan atau menyimpan data.</td>
                            <td>Terdapat sejumlah langkah yang dapat dipergunakan untuk melindungi kerahasiaan data seperti dengan 
                            menerapkan autentikasi dua faktor, penggunaan password yang kuat, enkripsi, dan lain-lain. </td>
                            <td>Salah satu caranya dengan membatasi wewenang akses kepada pihak yang tidak
                                berkepentingan.
                                Contohnya, hanya karyawan bagian penggajian yang memiliki akses ke database
                                penggajian perusahaan.
                                Karyawan di luar bagian itu hanya bisa melihat struktur perusahaan yang berisi nama
                                dan jabatan.</td>
                        </tr>
                        <tr>
                            <td><i>Integrity</i> (Integritas)</td>
                            <td>Upaya memberikan data yang konsisten, akurat, dan terpercaya.</td>
                            <td>Beberapa cara menjaga integritas data diantaranya enkripsi, tanda tangan digital,
                                hingga <i>certificate authority (CA)</i> digital.
                                CA seperti SSL/TLS berguna untuk verifikasi identitas pengguna situs website.</td>
                            <td>Misalnya Anda punya bisnis toko online. Anda harus memberikan informasi produk yang
                                jelas dan harga yang akurat.
                                Hal ini membuat pelanggan Anda percaya pada integritas toko online Anda.</td>
                        </tr>
                        <tr>
                            <td><i>Availability</i> (Ketersediaan)</td>
                            <td>Mengacu pada ketersediaan data Anda.</td>
                            <td>Untuk menjaga aspek availability ini, terdapat beberapa upaya yang bisa dilakukan, seperti:
                                menggunakan layanan pelindung DDoS,
                                menggunakan <i>redundancy, firewall,</i> dan <i>proxy servers</i>
                                memastikan bahwa <i>bandwidths</i> yang digunakan mencukupi
                                penggunaan <i>access controls.</i> </td>
                            <td>Misal pengguna <i>mobile banking</i>harus melakukan transfer mendadak. Dia akan kecewa
                                ketika aplikasinya tiba-tiba down.
                                Hal tersebut dapat mengurangi kepercayaan pengguna kepada bank bersangkutan.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """,
        height=600,
    )

    with tab3:
        st.markdown("### 3 Penerapan Cybersecurity")
        st.markdown("""
        Penerapan cyber security terbagi menjadi tiga jenis, yaitu _**cloud security, network security,**_ dan _**application security.**_
        """)
        components.html(
        """
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        
        <div class="card">
            <div class="card-body">
                <table class="table">
                    <thead class="thead-light">
                        <tr>
                            <th>Nama</th>
                            <th>Definisi</th>
                            <th>Penerapan</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Cloud Security</td>
                            <td>Merupakan upaya perlindungan data yang tersimpan di cloud dengan melibatkan teknologi, kebijakan kontrol, dan layanan pendukung keamanan cloud.</td>
                            <td>Dapat dilakukan dengan menggunakan firewall, <i>two factor authentication</i>, VPN hingga enkripsi data.</td>
                        </tr>
                        <tr>
                            <td>Network Security</td>
                            <td>Merupakan praktik perlindungan jaringan internal dengan cara memberikan keamanan jaringan.</td>
                            <td>Network security dapat dilaksanakan dengan penggunaan antivirus atau firewall, <i>two factor authentication</i>, dan mengganti atau memperbaharui password secara berkala.</td>
                        </tr>
                        <tr>
                            <td>Application Security</td>
                            <td>Merupakan usaha melindungi keamanan aplikasi dari berbagai ancaman <i>cyber crime.</i></td>
                            <td>Beberapa hal yang dapat dilakukan pada tahapan application security meliputi autentikasi, otorisasi atau pemberian wewenang, enkripsi, perekaman informasi (<i>logging</i>), dan uji keamanan aplikasi.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """,
        height=600,
        )

    with tab4:
        st.markdown("### Landasan Hukum Penanganan _Cyber Crime_ di Indonesia")
        st.caption("Sumber: https://business-law.binus.ac.id/2019/06/30/konsep-kejahatan-siber-dalam-sistem-hukum-indonesia/")
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""
            Indonesia tidak memiliki definisi hukum untuk kejahatan siber. Sebenarnya, Undang-Undang Nomor 11 Tahun 2008 sebagai amandemen dengan Undang-Undang Nomor 19 Tahun 2016 
            tentang Informasi dan Transaksi Elektronik (UU ITE) adalah undang-undang administratif. Namun, legislator memasukkan beberapa ketentuan tentang tindak pidana. 
            
            Definisi kejahatan siber dapat disimpulkan dari artikel tentang kejahatan tersebut. Anatomi kejahatan siber berdasarkan UU ITE dapat dibagi menjadi dua kelompok.

            Pertama, kejahatan yang menargetkan internet, komputer, dan teknologi terkait. Di bawah Undang-Undang Informasi dan Transaksi Elektronik, 
            ada tujuh jenis kejahatan yang diklasifikasikan sebagai kejahatan yang menargetkan internet, komputer, dan teknologi terkait.
            """)
            st.markdown("---")
    
            components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
                integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
            </script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
                integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
            </script>

            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th>Jenis Kejahatan</th>
                        <th>Ketentuan dalam UU ITE</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Melakukan Akses Ilegal (<i>Hacking</i>)</td>
                        <td>Pasal 30</td>
                    </tr>
                    <tr>
                        <td>Intersepsi atau Penyadapan Ilegal</td>
                        <td>Pasal 31 Ayat (1) dan Pasal 31 Ayat (2)</td>
                    </tr>
                    <tr>
                        <td>Mengotori (<i>Defacing</i>)</td>
                        <td>Pasal 32</td>
                    </tr>
                    <tr>
                        <td>Pencurian Elektronik</td>
                        <td>Pasal 32 Ayat (2)</td>
                    </tr>
                    <tr>
                        <td>Interference</td>
                        <td>Pasal 33</td>
                    </tr>
                    <tr>
                        <td>Memfasilitasi Tindak Pidana Terlarang</td>
                        <td>Pasal 34</td>
                    </tr>
                    <tr>
                        <td>Pemalsuan Informasi atau Dokumen Elektronik</td>
                        <td>Pasal 35</td>
                    </tr>
                </tbody>
            </table>
            """,
            height=380,
            )
            st.caption("Tabel 1. Jenis Kejahatan siber Kelompok Pertama")

        with right_column:
            # image = Image.open('images/police.jpg')
            # st.image(image, caption='Ilustrasi Penanganan Kejahatan Siber', width=600)
            st.write("""
            Kelompok kedua adalah konten ilegal dengan menggunakan internet, komputer dan teknologi terkait untuk melakukan kejahatan. 
            Di bawah UU ITE, ada tujuh jenis kejahatan yang diklasifikasikan sebagai kejahatan yang menargetkan internet, komputer, dan teknologi terkait. 
            Kejahatan ini terkait dengan publikasi dan distribusi konten ilegal. 
            
            Faktanya, pelanggaran UU ITE didominasi oleh publikasi dan distribusi kasus konten ilegal. 
            
            Menurut Divisi Kejahatan Siber Kepolisian Nasional Indonesia pada tahun 2017, 
            Kepolisian Nasional Indonesia telah menyelidiki 1.763 laporan. Dari jumlah itu, penipuan adalah yang tertinggi dengan 767 kasus diikuti oleh pencemaran nama baik dengan 
            528 kasus dan pornografi dengan 100 kasus. Kalau tidak, peretasan adalah yang terendah yang hanya satu kasus. Selama tahun pemilu 2018, 
            pelanggaran UU ITE didominasi oleh konten ilegal terutama pidato kebencian dan konten tipuan. Ini menunjukkan bahwa pelanggaran konten ilegal masih mendominasi pelanggaran UU ITE.
            """)

            st.markdown("---")

            components.html(
            """
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
                integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous">
            </script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
                integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous">
            </script>

            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th>Jenis Kejahatan</th>
                        <th>Ketentuan dalam UU ITE</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Kesusilaan/Pornografi</td>
                        <td>Pasal 27 Ayat (1)</td>
                    </tr>
                    <tr>
                        <td>Perjudian</td>
                        <td>Pasal 27 Ayat (2)</td>
                    </tr>
                    <tr>
                        <td>Penghinaan dan/atau Pencemaran Nama Baik</td>
                        <td>Pasal 27 Ayat (3)</td>
                    </tr>
                    <tr>
                        <td>Pemerasan dan/atau Pengancaman</td>
                        <td>Pasal 27 Ayat (4)</td>
                    </tr>
                    <tr>
                        <td>Berita Bohong yang Menyesatkan dan Merugikan Konsumen</td>
                        <td>Pasal 28 Ayat (1)</td>
                    </tr>
                    <tr>
                        <td>Menimbulkan rasa Kebencian Berdasarkan SARA</td>
                        <td>Pasal 28 Ayat (2)</td>
                    </tr>
                    <tr>
                        <td>Ancaman Kekerasan Terhadap Orang Lain</td>
                        <td>Pasal 29</td>
                    </tr>
                </tbody>
            </table>
            """,
            height=380,
            )
            st.caption("Tabel 2. Jenis Konten Ilegal Menurut UU ITE")


        st.write("---")
        st.markdown("### Cara Melapor Jika Mengalami Kejahatan Siber")
        agree = st.checkbox('Tampilkan Gambar')

        if agree:
            col1, col2, col3 = st.columns(3)
            with col1:
                image = Image.open('images/lapor1.jpg')
                st.image(image, width=500)

            with col2:
                image = Image.open('images/lapor2.jpg')
                st.image(image, width=500)
                
            with col3:
                image = Image.open('images/lapor3.jpg')
                st.image(image, width=500)

        st.write("")
        st.markdown("### Kontak Aduan Kejahatan Siber BSSN")
        st.write("🖥️ [Website BSSN Aduan Siber](https://bssn.go.id/aduan-siber/)")
        st.write("☎️ (021) 78833610")
        st.write("📧 bantuan70@bssn.go.id")

st.sidebar.success("Pilih salah satu halaman diatas")