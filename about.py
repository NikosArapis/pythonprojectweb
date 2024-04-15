import streamlit as st
def app():
    st.subheader('Laniteio school')
    st.write("Laniteio School, nestled in the serene environment of Knowledge City, stands as a beacon of progressive education and holistic development. Established in 1995, the school has earned a reputation for providing a robust educational experience that seeks to cultivate the innate potential of each student.")
    # Display the image
    st.image("school.png", caption="School in forest", use_column_width=True)
    with st.expander("See Philosophy:"):
        st.write(
            "The philosophy of Greenwood is deeply rooted in the belief that education should extend beyond academic excellence to include the development of character, creativity, and curiosity in every child. The school aims to foster an environment where students are encouraged to explore, inquire, and innovate, enabling them to become lifelong learners and contributors to a global society.")
    # Create three columns
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display images
    with col1:
        st.image("students1.png", caption="students playing", use_column_width=True)

    with col2:
        st.image("students2.png", caption="students playing", use_column_width=True)

    with col3:
        st.image("students3.png", caption="students playing", use_column_width=True)

    with col4:
        st.image("art_class.jpg", caption="Children learn art", use_column_width=True)

    with col5:
        st.image("science.jpg", caption="Children learn science", use_column_width=True)
