import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import altair as alt
import time
import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.express as px
import time

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"
)

# **** HEADER ****
with st.container():
    st.markdown("<h1 style='text-align: center;'>Kejahatan Siber yang Terjadi Selama Pandemi Covid-19</h1>", unsafe_allow_html=True)
    st.markdown("---")

# **** PENDAHULUAN ****
with st.container():
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.markdown("#### Mengenal CyberCrime, Cyber Attack dan Cyber Warfare")
        st.markdown("""
            Masyarakat melakukan banyak aktivitas dengan lebih mudah dan cepat dengan menggunakan komputer dan internet. 
            Banyak aktivitas manusia sebagai individu kegiatan perusahaan, dan kegiatan pemerintahan yang sekarang sedang ditransformasikan dalam ruang maya atau yang disebut _cyberspace_.
            
            Dalam _cyberspace_, antar pengguna dapat berkomunikasi dengan menyamarkan identitasnya (_anonymous_), 
            tanpa dibatasi oleh batas wilayah (_borderless_) dan bahkan lintas negara (transnasional). Sifat cyberspace tersebut yang kemudian mendorong kejahatan-kejahatan konvensional 
            yang ada di dalam _real space_ juga ikut ditransformasikan ke dalam cyberspace dan menimbulkan banyak pelanggaran hukum karena dianggap tidak ada hukum untuk pelaku kejahatan siber.

        """)
        st.write("Beberapa dari bentuk kejahatan yang terjadi di _cyberspace_ dikenal dengan istilah _cybercrime_, _cyber attack_ dan _cyber warfare_.")
        st.markdown("""
        - _CyberCrime_ merupakan bentuk tindak pidana yang dilakukan dengan memanfaatkan teknologi komputer dan internet dalam melaksanakan tindak kejahatannya.
        - _Cyber Attack_ merupakan metode yang digunakan dalam melakukan serangan dengan menggunakan teknologi komputer dan internet.
        - _Cyber Warfare_ merupakan bentuk operasi siber (_cyber operations_) secara menyerang atau bertahan, yang dilakukan dengan tujuan untuk membuat cedera atau kematian orang 
            atau kerusakan atau kehancuran objek sasaran atau target operasi.
        """)
    with right_column:
        image = Image.open('images/cybercrime.jpg')
        st.image(image, caption='Ilustrasi Cybercrime', width=600)

with st.container():
    st.markdown("---")
    st.markdown("#### Jenis-jenis Kejahatan Siber (_CyberCrime_) yang Sering Terjadi Selama Pandemi Covid-19")
    st.caption("Menurut Interpol dan BSSN")

# **** KONTEN ****
with st.container():
    selected = option_menu(
            menu_title=None,  # required
            options=["", "Phishing", "Ransomware", "Trojan", "SQL Injection"],  # required
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

if selected == "":
    with st.container():
        st.markdown("---")
        st.markdown("#### Laporan Kasus Kejahatan Siber Selama Pandemi Covid-19")
        st.write("""
        Serangan siber terjadi selama pandemi, di seluruh dunia, termasuk di Indonesia. Badan Siber dan Sandi Negara merilis 
        sebuah laporan tahunan yang dikumpulkan dari pantauan Pusat Operasi Keamanan Siber 
        Nasional BSSN (BSSN, 2021) , dengan data sebagai berikut:
        """)


        # ---- Grafik
        "Tren Aduan Siber Tahun 2021"
        source = pd.DataFrame({
            'Jumlah Kejadian': [55, 21, 15, 23, 29, 21, 20, 37, 43, 24, 28, 16],
            'Bulan': pd.date_range('2021-01-01', freq='M', periods=12)
        })
    
        line_chart = alt.Chart(source).mark_line().encode(
            y='Jumlah Kejadian',
            x=alt.X('month(Bulan):O')
        )
        st.altair_chart(line_chart, use_container_width=True)

        labels=['IIVN', 'PEMERINTAH PUSAT', 'EKONOMI DIGITAL', 'PEMERINTAH DAERAH', 'LAINNYA']
 
        values = [12, 23, 15, 25, 25]

        #The plot
        fig = go.Figure(
            go.Pie(
            labels = labels,
            values = values,
            hoverinfo = "label+percent",
            textinfo = "value"
        ))

        st.header("Sebaran Sektor")
        st.plotly_chart(fig)

        st.write("""
        **Dengan rincian:**

        IIVN: 43 Aduan, Pemerintah Pusat: 75 Aduan, Ekonomi Digital: 51 Aduan, Pemerintah Daerah: 81 Aduan, Lainnya: 81 Aduan. Total 332 Aduan.
        """)

        st.write("")
        "Sebaran Jenis Serangan Pada Aduan Siber Tahun 2021"
        source = pd.DataFrame({
            "Banyak Aduan": [79, 56, 46, 33, 17, 12, 11, 11, 5],
            "Jenis Serangan": ["SQL Injection", "Ransomware", "XSS", "Konten Negatif", "Information Disclosure", "Phising", "Web Defacement", "Pengaduan dan Konsultasi Kejahatan Dunia Maya", "Bypass Admin"]

        })

        bar_chart = alt.Chart(source).mark_bar().encode(
            x="Banyak Aduan:Q",
            y=alt.Y("Jenis Serangan:N", sort="-x")
        )

        st.altair_chart(bar_chart, use_container_width=True)

        st.caption("Sumber: Laporan Tahunan Monitoring Keamanan Siber 2021")

# ---- Phishing ----
if selected == "Phishing":
    st.markdown(f"<h1 style='text-align: center; margin-bottom: 10px;'>Mengenal {selected}</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.markdown("### Definisi dan Tujuan Phishing")
        st.write("""
        Phishing adalah upaya untuk mendapatkan informasi data seseorang dengan teknik pengelabuan.
        Data yang menjadi sasaran phishing adalah data pribadi (nama, usia, alamat), data akun (username dan password), 
        dan data finansial (informasi kartu kredit, rekening).
        
        Istilah phishing berasal dari kata _fishing_ yaitu memancing.

        Kegiatan phishing memang bertujuan memancing orang untuk memberikan informasi pribadi secara sukarela tanpa disadari. 
        Padahal informasi yang dibagikan tersebut akan digunakan untuk tujuan kejahatan. 
        94 persen malware dikirimkan melalui email menggunakan teknologi rekayasa sosial untuk dapat mengelabui pengguna agar membuka lampiran atau tautan yang berbahaya.""")
        
    with right_column:
        image = Image.open('images/phising.jpg')
        st.image(image, caption='Ilustrasi Phishing', width=400)

        
    with st.container():
        st.markdown("<h3 style='margin-bottom: 20px;'>Jenis-jenis Phishing</h3>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            image = Image.open('images/email-phising.png')
            st.image(image, caption='Email Phishing')
        with col2:
            image = Image.open('images/spear-phising.jpg')
            st.image(image, caption='Spear Phishing')
        with col3:
            image = Image.open('images/web-phising.png')
            st.image(image, caption='Web Phishing')
        with col4:
            image = Image.open('images/whaling.jpg')
            st.image(image, caption='Whaling')

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("---")
            st.write("""
            **Email phishing**
            
            Jenis yang pertama adalah email phishing.
            Sesuai dengan namanya, phishing ini menggunakan email atau surat elektronik sebagai media untuk menipu korbannya.
            Email ini dibuat semirip mungkin dengan email asli dari sebuah instansi atau lembaga dan dikirimkan secara masif.
            """)
        with col2:
            st.markdown("---")
            st.write("""
            **Spear phishing**

            Spear phishing ini mirip dengan email phishing, tetapi ada perbedaan dalam cara mengirimkan emailnya. 
            Email phishing dikirimkan secara masif dan acak, sedangkan spear phishing akan menarget korban tertentu. 
            Phishing jenis ini dilakukan setelah pelaku memiliki informasi dari korban.
            """)
        with col3:
            st.markdown("---")
            st.write("""
            **Web phishing**

            Pelaku akan membuat website yang terlihat mirip baik dari tampilan maupun nama domain dengan website resminya. 
            Web phishing juga dikenal dengan istilah domain spoofing.
            """)
        with col4:
            st.markdown("---")
            st.write("""
            **Whaling**

            Jenis phishing yang terakhir ini mirip seperti spear phishing, yaitu menargetkan satu orang yang memiliki kewenangan tinggi dalam suatu organisasi atau institusi secara spesifik. 
            Dengan whaling, pelaku mendapatkan banyak keuntungan dari akses yang didapatkan.
            """)

    st.markdown("### Bagaimana Phishing Bekerja?")
    col1, col2 = st.columns((1,2))
    with col1:
        option = st.selectbox(
        'Ilustrasi Phishing',
        ('Pilih salah satu', 'Ilustrasi dengan Video', 'Ilustrasi dengan Gambar'))

    if option == "Ilustrasi dengan Video":
        components.iframe("""
        https://youtube.com/embed/pGFr4lkidVM""", width=800, height= 450) 
    if option == "Ilustrasi dengan Gambar":
        image = Image.open('images/ilustrasi-phising.png')
        st.image(image, caption='Ilustrasi Phishing', width=800)

    st.markdown("***")
    st.markdown("### Kasus Phishing Selama Pandemi Covid-19")
    
    #Data Set
    name = ['Email Phishing', 'Web Phising']
    
    values = [9, 90]

    #The plot
    fig = go.Figure(
        go.Pie(
        labels = name,
        values = values,
        hoverinfo = "label+percent",
        textinfo = "percent"
    ))

    st.markdown("##### Jenis Aktivitas Phishing di Indonesia Tahun 2021")
    st.plotly_chart(fig)
    st.caption("Sumber: Laporan Tahunan Monitoring Keamanan Siber 2021")

# ---- ransomware ----
if selected == "Ransomware":
    st.markdown(f"<h1 style='text-align: center; margin-bottom: 10px;'>Mengenal {selected}</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.markdown("### Definisi Ransomware")
        st.write("""
        Ransomware adalah salah satu jenis malware (_malicious software_) yang bekerja dengan metode enkripsi––mengolah data menjadi kode yang tidak dapat dibaca oleh perangkat. 
        Sehingga, menyebabkan korban tidak dapat mengakses perangkatnya sebelum data tersebut didekripsi––diolah kembali dari bentuk yang sudah dienkripsi agar dapat dibaca oleh perangkat.
        
        Untuk dapat mendekripsi data pada perangkat yang terinfeksi Ransomware, kamu memerlukan kode dekripsi yang akan ditawarkan oleh peretas dengan membayar tebusan. 
        Jika dalam waktu tertentu kamu belum dapat mendekripsikan perangkatmu, maka data-data yang ada di perangkat akan hilang.
        """)
        
    with right_column:
        image = Image.open('images/ransomware.jpg')
        st.image(image, caption='Ilustrasi Ransomware', width=500)

    st.markdown("### Jenis-jenis Ransomware")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        1. Encrypting Ransomware
        Ransomware jenis ini menginfeksi perangkat dengan cara mengenkripsi file maupun folder penting yang ada di perangkat korban. 
        Setelah target berhasil terkunci dan terenkripsi, akan muncul notifikasi mengenai tebusan yang harus dibayarkan untuk membuka kembali data yang telah terkunci.

        Contoh Encrypting Ransomware:
        - WannaCry
        - CryptoWall
        - CryptoLocker
        - Locky
        """)
    with col2:
        st.write("""
        2. Locker Ransomware
        Ransomware jenis ini tidak bekerja dengan cara mengenkripsi file maupun folder milik korban, melainkan mengunci akses korban ke perangkat. 
        Biasanya, target Locker Ransomware adalah penguncian file maupun perangkat. Tapi terkadang, malware jenis ini juga menyasar hardware milik korban seperti keyboard atau mouse.

        Locker Ransomware termasuk gangguan tingkat rendah yang masih bisa ditangani cukup dengan menghapus script, dsb. 
        Sehingga, tebusan yang dibayarkan untuk malware jenis ini bisa dibilang lebih sedikit.

        Contoh Locker Ransomware:
        - Winlocker
        - Reveton
        """)

    empty1,col1,empty2,col2,empty3=st.columns([0.3,1.2,0.3,1.2,0.3])
    with empty1:
        st.empty()
    with col1:
        image = Image.open('images/wannacry-ransomware.jpg')
        st.image(image, caption='Contoh WannaCry Attack', width=500)
    with empty2:
        st.empty()
    with col2:
        image = Image.open('images/ransomware-reveton.png')
        st.image(image, caption='Contoh Reveton Attack', width=500)


    st.markdown("### Bagaimana Ransomware Bekerja?")
    col1, col2 = st.columns((1,2))
    with col1:
        option = st.selectbox(
        'Ilustrasi Ransomware',
        ('Pilih salah satu', 'Ilustrasi dengan Video', 'Ilustrasi dengan Gambar'))

    if option == "Ilustrasi dengan Video":
        components.iframe("""
        https://youtube.com/embed/-KL9APUjj3E?t=104""", width=800, height= 450) 
    if option == "Ilustrasi dengan Gambar":
        image = Image.open('images/ilustrasi-ransomware.jpg')
        st.image(image, caption='Ilustrasi Ransomware', width=800)

    st.markdown("***")
    st.markdown("### Statistik Kasus Ransomware Global Selama Pandemi Covid-19")
    
    #Data Set
    source = pd.DataFrame({
    'US$': [325000000, 5000000000, 11500000000, 20000000000],
    'Tahun' : ['2015', '2017', '2019', '2021']
    })

    bar_chart = alt.Chart(source).mark_bar().encode(
        x='Tahun',
        y='US$',
    )
    st.altair_chart(bar_chart, use_container_width=True)
    st.caption('Sumber: Cybersecurity Ventures')
    st.write("""Dengan rincian: 
    
    2015: US$325 Juta, 2017: US$5 Miliar, 2019: US$11.5 Miliar, 2021: US$20 Miliar
    """)

# ---- Trojan ----
if selected == "Trojan":
    st.markdown(f"<h1 style='text-align: center; margin-bottom: 10px;'>Mengenal {selected}</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.markdown("### Definisi Trojan")
        st.write("""
        Trojan adalah sebuah file, program, atau kode khusus yang terlihat aman, namun sebenarnya ini cukup berbahaya karena bagian dari jenis malware. 

        Trojan sendiri mengadaptasi dari cerita Yunani kuno, di mana kuda Troya tampak tidak berbahaya, 
        namun sebenarnya berisi tentara di dalamnya yang menjarah kota Troy setelah orang-orang membawanya masuk. 

        Trojan ini berada di dalam perangkat lunak yang sah dan umumnya dirancang untuk memata-matai seseorang atau mencuri data. Trojan biasanya juga akan sesuai 
        dengan tujuan saat peretas membuatnya seperti menghapus data di perangkat, salin data untuk dicuri dan dijual, mengubah data, memblokir akses ke data, hingga mengganggu kinerja komputer atau jaringan target. 
        """)
        
    with right_column:
        image = Image.open('images/trojan.jpg')
        st.image(image, caption='Ilustrasi Kuda Trojan', width=500)

    st.markdown("### Jenis-jenis Trojan")
    st.write("""
    1. Banking Trojan
    Trojan perbankan ini akan menyusup ke perangkat dan mencuri kredensial login finansial. Peretas menggunakannya untuk meretas banking milikmu dan akun keuangan lainnya. 

    2. DDoS Trojan
    Jenis DDoS Trojan bertujuan untuk memaksa perangkat menjadi botnet yaitu jaringan perangkat yang tertaut dapat dikendalikan dari jarak jauh oleh peretas. 

    Mereka akan menggunakan botnet untuk melakukan Distributed Denial of Service (DDoS) yang dapat mematikan situs web dan layanan internet lainnya. 

    3. Dropper atau downloader Trojan
    Dropper adalah tahap pertama dalam sebuah serangan malware yang biasanya terdiri dari tiga bagian yaitu dropper, loader, dan maware atau rootkit. 

    Trojan jenis ini nantinya akan menginfeksi perangkat dan mengatur untuk loader yang pada gilirannya menginstal rootkit secara otomatis. 

    Dengan begitu dapat memberikan akses peretas ke perangkat milikmu. Downloader Trojan akan menginstal malware jenis lain.

    4. Exploit Trojan
    Trojan ini menggunakan exploit yaitu trik perangkat lunak yang sengaja dirancang untuk memanfaatkan sistem perangkat lunak atau perangkat keras yang lemah sehingga dapat menginfeksinya. 

    5. Trojan antivirus palsu
    Trojan antivirus yang palsu ini akan berpura-pura mendeteksi virus dan malware di perangkat, kemudian memaksa untuk membayar perangkat lunak keamanan.

    6. Backdoor Trojan
    Malware backdoor memberikan kendali penuh device kepada pelakunya. Sehingga, pelaku bisa melakukan apapun pada seluruh data dalam device korbannya.
    """)

    empty1,col1,empty2,col2,empty3=st.columns([0.3,1.2,0.3,1.2,0.3])
    with empty1:
        st.empty()
    with col1:
        image = Image.open('images/banking-trojan.jpg')
        st.image(image, caption='Contoh Banking Trojan dengan Popup Gmail', width=500)
    with empty2:
        st.empty()
    with col2:
        image = Image.open('images/trojan-alert.png')
        st.image(image, caption='Trojan Terdeteksi oleh Antivirus', width=500)

    st.markdown("### Bagaimana Trojan Bekerja?")
    col1, col2 = st.columns((1,2))
    with col1:
        option = st.selectbox(
        'Ilustrasi Trojan',
        ('Pilih salah satu', 'Ilustrasi dengan Video', 'Ilustrasi dengan Gambar'))

    if option == "Ilustrasi dengan Video":
        components.iframe("""
        https://youtube.com/embed/pzOM8sc2RPU""", width=800, height= 450) 
    if option == "Ilustrasi dengan Gambar":
        image = Image.open('images/ilustrasi-trojan.png')
        st.image(image, caption='Ilustrasi Trojan', width=800)


if selected == "SQL Injection":
    st.markdown(f"<h1 style='text-align: center; margin-bottom: 10px;'>Mengenal {selected}</h1>", unsafe_allow_html=True)
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.markdown("### Definisi SQL Injection")
        st.write("""
        _SQL Injection_ merupakan suatu teknik eksploitasi dengan cara memodifikasi perintah _sql_ pada _form_ input aplikasi yang memungkinkan penyerang untuk dapat mengirimkan sintaks ke database aplikasi.
        _SQL Injection_ juga bisa didefinisikan sebagai suatu teknik mengeksploitasi celah keamanan pada _layer_ _database_ untuk mendapatkan _query_ data pada suatu aplikasi.
        """)

        st.write("""
        _SQL Injection_ dapat terjadi karena pengembang aplikasi tidak mengimplementasikan filter terhadap metakarakter (&, ;, ', ", |, *, ?, <, >, ^, (, ), [, ], {, }, atau $) yang digunakan
        dalam sintaks _sql_ pada form input aplikasi sehingga penyerang dapat menginput metakarakter tersebut menjadi instruksi pada aplikasi untuk mengakses _database_.
        """)
        
        st.write("""
        Kemudian bisa juga diakibatkan oleh pengembang bagian _back end_ yang tidak mengimplementasikan atau tidak melakukan pengaturan _Web Application Firewall (WAF)_ atau _Intrusion Prevention System (IPS)_
        pada arsitektur jaringan dengan baik sehingga _database_ bisa diakses langsung melalui celah kerawanan yang ditemukan oleh penyerangnya.
        """)

    with right_column:
        image = Image.open('images/ilustrasi-SQL-Injection.jpeg')
        st.image(image, caption='Ilustrasi SQL Injection', width=500)

    st.markdown("### Bagaimana _SQL Injection_ Bekerja?")
    col1, col2 = st.columns((1,2))
    with col1:
        option = st.selectbox(
        'Ilustrasi SQL Injection',
        ('Pilih salah satu', 'Ilustrasi dengan Video', 'Ilustrasi dengan Gambar'))

    if option == "Ilustrasi dengan Video":
        components.iframe("""
        https://www.youtube.com/embed/Yqu93GXx0vI""", width=800, height= 450) 
    if option == "Ilustrasi dengan Gambar":
        image = Image.open('images/SQL-injection.jpeg')
        st.image(image, caption='Ilustrasi SQL Injection', width=600)