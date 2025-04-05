import streamlit as st

# Set page config
st.set_page_config(page_title="Arabian Vista - Dark Theme", layout="wide", page_icon="🌙")

# Apply custom dark theme styling
dark_style = """
<style>
    body {
        background-color: #121212;
        color: #fff;
    }

    .stApp {
        background-color: #121212;
    }

    h1, h2, h3, h4, h5, h6, p {
        color: #ffffff;
    }

    .hero {
        background-image: url("https://source.unsplash.com/1600x600/?desert,dubai");
        background-size: cover;
        background-position: center;
        padding: 80px 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
    }

    .btn-custom {
        background-color: #ff9800;
        color: black;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        text-decoration: none;
    }

    .btn-custom:hover {
        background-color: #ffa726;
        color: black;
    }

    .footer {
        margin-top: 50px;
        text-align: center;
        padding: 20px;
        color: #aaa;
    }
</style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Explore the Beauty of Arabia</h1>
    <p>Luxury Desert Safaris | City Tours | Adventures</p>
    <a href="#packages" class="btn-custom">Book Now</a>
</div>
""", unsafe_allow_html=True)

# Services Section
st.markdown("## 🧭 Our Services")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🐪 Desert Safari")
    st.write("Experience thrilling dune bashing, camel rides, and BBQ dinners under the stars.")

with col2:
    st.markdown("### 🏙️ City Tours")
    st.write("Discover the modern and traditional beauty of UAE cities with our guided tours.")

with col3:
    st.markdown("### 🚘 Luxury Rides")
    st.write("Travel in style with our luxury cars and chauffeur services.")

# Tour Packages
st.markdown("## 🎒 Tour Packages")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://source.unsplash.com/400x200/?desert,safari", caption="Desert Adventure")
    st.write("Evening desert safari, camel ride, sandboarding & BBQ dinner.")

with col2:
    st.image("https://source.unsplash.com/400x200/?dubai,tour", caption="Dubai City Tour")
    st.write("Explore Burj Khalifa, Dubai Mall, Dubai Frame, and more.")

with col3:
    st.image("https://source.unsplash.com/400x200/?luxury,car", caption="VIP Experience")
    st.write("Private luxury ride, fine dining, and exclusive experiences.")

# About Section
st.markdown("## 🧾 About Us")
st.write("We are passionate about delivering unforgettable travel experiences across the UAE. From heart-pumping desert safaris to relaxing cultural tours, Arabian Vista is your gateway to adventure.")

# Contact Form
st.markdown("## 📞 Contact Us")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")
    if submit:
        st.success(f"Thank you {name}, we have received your message!")

# Footer
st.markdown("""<div class='footer'>© 2025 Arabian Vista Tourism. All Rights Reserved.</div>""", unsafe_allow_html=True)
