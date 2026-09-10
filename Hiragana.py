import streamlit as st

def get_content():


    col1, col2 = st.columns([0.5, 0.5])

    with col1:

        st.markdown(
            """<p style='font-size:30px;'>The 46 basic hiragana characters. Each character 
            represents a sound. Japanese sounds are usually written 
            in consonant + vowel combinations.</p>""",
            unsafe_allow_html=True
        )

    with col2:


        cols = [gyo, a, ka, sa, ta, na, ma, ya, ra, wa, n] = st.columns(11)

        with cols[0]:

            st.markdown(
                """<p style='font-size:22px;'>行</p>""",
                unsafe_allow_html=True
            )

            st.markdown(
                """<p style='font-size:22px;'>a</p>""",
                unsafe_allow_html=True
            )

            st.markdown(
                """<p style='font-size:22px;'>i</p>""",
                unsafe_allow_html=True
            )

            st.markdown(
                """<p style='font-size:22px;'>u</p>""",
                unsafe_allow_html=True
            )

            st.markdown(
                """<p style='font-size:22px;'>e</p>""",
                unsafe_allow_html=True
            )

            st.markdown(
                """<p style='font-size:22px;'>o</p>""",
                unsafe_allow_html=True
            )

        with cols[1]:

            st.write("あ行")

            a_button = st.button("あ")

            i_button = st.button("い")

            u_button = st.button("う")

            e_button = st.button("え")

            o_button = st.button("お")

        with cols[2]:

            st.write("か行")

            ka_button = st.button("か")

            ki_button = st.button("き")

            ku_button = st.button("く")

            ke_button = st.button("け")

            ko_button = st.button("こ")

        with cols[3]:

            st.write("さ行")

            sa_button = st.button("さ")

            shi_button = st.button("し")

            su_button = st.button("す")

            se_button = st.button("せ")

            so_button = st.button("そ")

        with cols[4]:

            st.write("た行")

            ta_button = st.button("た")

            ti_button = st.button("ち")

            tsu_button = st.button("つ")

            te_button = st.button("て")

            to_button = st.button("と")

        with cols[5]:

            st.write("な行")

            na_button = st.button("な")

            ni_button = st.button("に")

            nu_button = st.button("ぬ")

            ne_button = st.button("ね")

            no_button = st.button("の")

        with cols[6]:

            st.write("ま行")

            ma_button = st.button("ま")

            mi_button = st.button("み")

            mu_button = st.button("む")

            me_button = st.button("め")

            mo_button = st.button("も")

        with cols[7]:

            st.write("や行")

            ya_button = st.button("や")

            yu_button = st.button("ゆ")

            yo_button = st.button("よ")

        with cols[8]:

            st.write("ら行")

            ra_button = st.button("ら")

            ri_button = st.button("り")

            ru_button = st.button("る")

            re_button = st.button("れ")

            ro_button = st.button("ろ")

        with cols[9]:

            st.write("わ行")

            wa_button = st.button("わ")

            wo_button = st.button("を")

        with cols[10]:

            st.write("ん")

            n_button = st.button("ん")




