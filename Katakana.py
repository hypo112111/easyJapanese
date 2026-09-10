import streamlit as st

def get_content():


    col1, col2 = st.columns([0.5, 0.5])

    with col1:

        st.markdown(
            """<p style='font-size:30px;'>Katakana (カタカナ) is one of the three writing systems used in Japanese. 
            It has 46 basic characters, and each character represents a sound, just like Hiragana. Katakana is mainly 
            used for foreign words, foreign names, loanwords, and sometimes for emphasis. For example, “computer” is 
            written as コンピューター (konpyūtā), and “coffee” is コーヒー (kōhī). Katakana characters are usually more 
            angular than Hiragana. Learning Katakana is important because it helps you read many common Japanese 
            words.</p>""",
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

            a_button = st.button("ア")

            i_button = st.button("イ")

            u_button = st.button("ウ")

            e_button = st.button("え")

            o_button = st.button("オ")

        with cols[2]:

            st.write("か行")

            ka_button = st.button("カ")

            ki_button = st.button("キ")

            ku_button = st.button("ク")

            ke_button = st.button("ケ")

            ko_button = st.button("コ")

        with cols[3]:

            st.write("さ行")

            sa_button = st.button("サ")

            shi_button = st.button("シ")

            su_button = st.button("ス")

            se_button = st.button("セ")

            so_button = st.button("ソ")

        with cols[4]:

            st.write("た行")

            ta_button = st.button("タ")

            ti_button = st.button("チ")

            tsu_button = st.button("ツ")

            te_button = st.button("テ")

            to_button = st.button("ト")

        with cols[5]:

            st.write("な行")

            na_button = st.button("ナ")

            ni_button = st.button("二")

            nu_button = st.button("ヌ")

            ne_button = st.button("ネ")

            no_button = st.button("ノ")

        with cols[6]:

            st.write("ま行")

            ma_button = st.button("マ")

            mi_button = st.button("ミ")

            mu_button = st.button("ム")

            me_button = st.button("メ")

            mo_button = st.button("モ")

        with cols[7]:

            st.write("や行")

            ya_button = st.button("ヤ")

            yu_button = st.button("ユ")

            yo_button = st.button("ヨ")

        with cols[8]:

            st.write("ら行")

            ra_button = st.button("ラ")

            ri_button = st.button("リ")

            ru_button = st.button("ル")

            re_button = st.button("レ")

            ro_button = st.button("ロ")

        with cols[9]:

            st.write("わ行")

            wa_button = st.button("ワ")

            wo_button = st.button("ヲ")

        with cols[10]:

            st.write("ん")

            n_button = st.button("ン")




