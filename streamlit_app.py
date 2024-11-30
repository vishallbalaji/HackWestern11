import streamlit as st
from streamlit.components.v1 import html
from PIL import Image



# pg = st.navigation([st.Page("out.py"), st.Page("cook.py")])

# pg.run()


def nav_page(page_name, timeout_secs=1):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

#removes side bar
st.set_page_config(initial_sidebar_state="collapsed", page_title="Design the Meal for Me Please", layout="centered")
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: black; line-height: 60%;'>Design a meal for me please</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: grey; line-height: normal;'>Maximize your ingredients, minimize waste, and simplify meal planning</h4>", unsafe_allow_html=True)

# Layout with icons and buttons
col1, col2 = st.columns(2)

#button
st.markdown(
    """
<style>
button {
    height: 30px;
    padding: 10px 38px !important
}
</style>
""",
    unsafe_allow_html=True,
)

with col1:
    with st.container():
        image = Image.open("./Baking.png")
        new_image = image.resize((388, 388))
        st.image(new_image)
with col2:
    with st.container():
        image = Image.open("./Restaurant.png")
        new_image = image.resize((388, 388))
        st.image(new_image)



col11, col22, col33, col44, col55 = st.columns(5)

with col11:
    pass
with col22:
    cook = st.button("Cook", key="cook_button", type="primary")
with col33:
    pass
with col44:
    eat_out = st.button("Eat Out", key="eat_out_button", type="primary")
with col55:
    pass

if cook:
    nav_page("cook", 1)
if eat_out:
    nav_page("out", 1)