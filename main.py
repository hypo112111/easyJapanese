import streamlit as st

import intro
import Hiragana
import Katakana
import jlptn5grammar
import jlptn4grammar
import jlptn5kanji
import jlptn4kanji

def n5next_pressed():

    current_index = n5lessons.index(st.session_state.lesson_select)

    if current_index < len(n5lessons) - 1:
        st.session_state.lesson_select = n5lessons[current_index + 1]

def n5prev_pressed():

    current_index = n5lessons.index(st.session_state.lesson_select)

    if current_index > 0:
        st.session_state.lesson_select = n5lessons[current_index - 1]

def n4next_pressed():

    current_index = n4lessons.index(st.session_state.lesson_select)

    if current_index < len(n4lessons) - 1:
        st.session_state.lesson_select = n4lessons[current_index + 1]

def n4prev_pressed():

    current_index = n4lessons.index(st.session_state.lesson_select)

    if current_index > 0:
        st.session_state.lesson_select = n4lessons[current_index - 1]

st.set_page_config(page_title="My App", layout="wide")

# Sidebar tabs
st.sidebar.title("Menu")

selected_tab = st.sidebar.radio(
    "Choose a tab",
    ["Intro",
        "Hiragana",
        "Katakana",
        "Kanji",
        "JLPT N5 Kanji",
        "JLPT N5 Grammar",
        "JLPT N4 Kanji",
        "JLPT N4 Grammar"]
)

# Display content based on selection
if selected_tab == "Intro":
    st.header("Intro")
    intro.get_content()

elif selected_tab == "Hiragana":
    st.header("Hiragana")
    Hiragana.get_content()

elif selected_tab == "Katakana":
    st.header("Katakana")
    Katakana.get_content()

elif selected_tab == "Hiragana":
    st.header("Settings")
    st.write("Here you can change settings.")

elif selected_tab == "JLPT N5 Grammar":
    prev, title, next = st.columns([0.4,2.2, 0.4])

    n5lessons = ["Lesson 1",
         "Lesson 2",
         "Lesson 3",
         "Lesson 4",
         "Lesson 5",
         "Lesson 6",
         "Lesson 7",
         "Lesson 8",
         "Lesson 9",
         "Lesson 10",
         "Lesson 11",
         "Lesson 12",
         "Lesson 13",
         "Lesson 14",
         "Lesson 15",
         "Lesson 16",
         "Lesson 17",
         "Lesson 18",
         "Lesson 19",
         "Lesson 20",
         "Lesson 21",
         "Lesson 22",
         "Lesson 23",
         "Lesson 24",
         "Lesson 25"]

    n5GrammarLesson = st.sidebar.selectbox(
        "Lesson",
        n5lessons,
        key = "lesson_select"
    )

    with prev:
        prev_pressed = st.button("←",
                                 on_click=n5prev_pressed)

    with next:
        next_pressed = st.button("→",
                                 on_click=n5next_pressed)

    with title:
        st.markdown(
            "<h1 style='text-align: center;'>JLPT N5 Grammar</h1>",
            unsafe_allow_html=True
        )

        match n5GrammarLesson:
            case "Lesson 1":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 1</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson1()
            case "Lesson 2":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 2</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson2()
            case "Lesson 3":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 3</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson3()
            case "Lesson 4":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 4</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson4()
            case "Lesson 5":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 5</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson5()
            case "Lesson 6":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 6</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson6()
            case "Lesson 7":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 7</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson7()
            case "Lesson 8":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 8</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson8()
            case "Lesson 9":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 9</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson9()
            case "Lesson 10":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 10</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson10()
            case "Lesson 11":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 11<h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson11()
            case "Lesson 12":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 12</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson12()
            case "Lesson 13":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 13</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson13()
            case "Lesson 14":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 14</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson14()
            case "Lesson 15":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 15</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson15()
            case "Lesson 16":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 16</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson16()
            case "Lesson 17":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 17</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson17()
            case "Lesson 18":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 18</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson18()
            case "Lesson 19":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 19</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson19()
            case "Lesson 20":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 20</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson20()
            case "Lesson 21":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 21</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson21()
            case "Lesson 22":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 22</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson22()
            case "Lesson 23":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 23</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson23()
            case "Lesson 24":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 24</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson24()
            case "Lesson 25":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 25</h1>",
                    unsafe_allow_html=True
                )
                jlptn5grammar.lesson25()

elif selected_tab == "JLPT N4 Grammar":
    prev, title, next = st.columns([0.4,2.2, 0.4])

    n4lessons = ["Lesson 26",
         "Lesson 27",
         "Lesson 28",
         "Lesson 29",
         "Lesson 30",
         "Lesson 31",
         "Lesson 32",
         "Lesson 33",
         "Lesson 34",
         "Lesson 35",
         "Lesson 36",
         "Lesson 37",
         "Lesson 38",
         "Lesson 39",
         "Lesson 40",
         "Lesson 41",
         "Lesson 42",
         "Lesson 43",
         "Lesson 44",
         "Lesson 45",
         "Lesson 46",
         "Lesson 47",
         "Lesson 48",
         "Lesson 49",
         "Lesson 50"]

    n4GrammarLesson = st.sidebar.selectbox(
        "Lesson",
        n4lessons,
        key = "lesson_select"
    )

    with prev:
        prev_pressed = st.button("←",
                                 on_click=n4prev_pressed)

    with next:
        next_pressed = st.button("→",
                                 on_click=n4next_pressed)

    with title:
        st.markdown(
            "<h1 style='text-align: center;'>JLPT N4 Grammar</h1>",
            unsafe_allow_html=True
        )

    match n4GrammarLesson:
        case "Lesson 26":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 26</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson26()
        case "Lesson 27":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 27</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson27()
        case "Lesson 28":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 28</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson28()
        case "Lesson 29":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 29</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson29()
        case "Lesson 30":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 30</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson30()
        case "Lesson 31":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 31</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson31()
        case "Lesson 32":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 32</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson32()
        case "Lesson 33":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 33</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson33()
        case "Lesson 34":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 34</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson34()
        case "Lesson 35":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 35</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson35()
        case "Lesson 36":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 36</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson36()
        case "Lesson 37":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 37</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson37()
        case "Lesson 38":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 38</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson38()
        case "Lesson 39":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 39</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson39()
        case "Lesson 40":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 40</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson40()
        case "Lesson 41":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 41</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson41()
        case "Lesson 42":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 42</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson42()
        case "Lesson 43":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 43</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson43()
        case "Lesson 44":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 44</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson44()
        case "Lesson 45":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 45</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson45()
        case "Lesson 46":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 46</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson46()
        case "Lesson 47":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 47</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson47()
        case "Lesson 48":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 48</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson48()
        case "Lesson 49":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 49</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson49()
        case "Lesson 50":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 50</h1>",
                unsafe_allow_html=True
            )
            jlptn4grammar.lesson50()

elif selected_tab == "JLPT N5 Kanji":

    st.markdown("""
        <style>
        button {
            height: auto;
            padding-top: 20px !important;
            padding-bottom: 20px !important;
            font-size: 24px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    prev, title, next = st.columns([0.4, 2.2, 0.4])

    n5lessons = ["Lesson 1",
                 "Lesson 2",
                 "Lesson 3",
                 "Lesson 4",
                 "Lesson 5",
                 "Lesson 6",
                 "Lesson 7",
                 "Lesson 8",
                 "Lesson 9",
                 "Lesson 10",
                 "Lesson 11"]

    n5KanjiLesson = st.sidebar.selectbox(
        "Lesson",
        n5lessons,
        key="lesson_select"
    )

    with prev:
        prev_pressed = st.button("←",
                                 on_click=n5prev_pressed)

    with next:
        next_pressed = st.button("→",
                                 on_click=n5next_pressed)

    with title:
        st.markdown(
            "<h1 style='text-align: center;'>JLPT N5 Kanji</h1>",
            unsafe_allow_html=True
        )

        match n5KanjiLesson:
            case "Lesson 1":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 1</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson1()
            case "Lesson 2":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 2</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson2()
            case "Lesson 3":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 3</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson3()
            case "Lesson 4":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 4</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson4()
            case "Lesson 5":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 5</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson5()
            case "Lesson 6":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 6</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson6()
            case "Lesson 7":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 7</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson7()
            case "Lesson 8":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 8</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson8()
            case "Lesson 9":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 9</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson9()
            case "Lesson 10":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 10</h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson10()
            case "Lesson 11":
                st.markdown(
                    "<h1 style='text-align: center;'>Lesson 11<h1>",
                    unsafe_allow_html=True
                )
                jlptn5kanji.lesson11()

elif selected_tab == "JLPT N4 Kanji":

    st.markdown("""
        <style>
        button {
            height: auto;
            padding-top: 20px !important;
            padding-bottom: 20px !important;
            font-size: 24px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    prev, title, next = st.columns([0.4, 2.2, 0.4])

    n4lessons = ["Lesson 1",
         "Lesson 2",
         "Lesson 3",
         "Lesson 4",
         "Lesson 5",
         "Lesson 6",
         "Lesson 7",
         "Lesson 8",
         "Lesson 9",
         "Lesson 10",
         "Lesson 11",
         "Lesson 12",
         "Lesson 13",
         "Lesson 14",
         "Lesson 15",
         "Lesson 16",
         "Lesson 17",
         "Lesson 18",
         "Lesson 19",
         "Lesson 20"]

    n4KanjiLesson = st.sidebar.selectbox(
        "Lesson",
        n4lessons,
        key="lesson_select"
    )

    with prev:
        prev_pressed = st.button("←",
                                 on_click=n4prev_pressed)

    with next:
        next_pressed = st.button("→",
                                 on_click=n4next_pressed)

    with title:
        st.markdown(
            "<h1 style='text-align: center;'>JLPT N4 Kanji</h1>",
            unsafe_allow_html=True
        )

    match n4KanjiLesson:
        case "Lesson 1":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 1</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson1()
        case "Lesson 2":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 2</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson2()
        case "Lesson 3":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 3</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson3()
        case "Lesson 4":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 4</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson4()
        case "Lesson 5":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 5</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson5()
        case "Lesson 6":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 6</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson6()
        case "Lesson 7":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 7</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson7()
        case "Lesson 8":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 8</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson8()
        case "Lesson 9":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 9</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson9()
        case "Lesson 10":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 10</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson10()
        case "Lesson 11":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 11</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson11()
        case "Lesson 12":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 12</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson12()
        case "Lesson 13":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 13</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson13()
        case "Lesson 14":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 14</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson14()
        case "Lesson 15":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 15</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson15()
        case "Lesson 16":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 16</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson16()
        case "Lesson 17":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 17</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson17()
        case "Lesson 18":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 18</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson18()
        case "Lesson 19":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 19</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson19()
        case "Lesson 20":
            st.markdown(
                "<h1 style='text-align: center;'>Lesson 20</h1>",
                unsafe_allow_html=True
            )
            jlptn4kanji.lesson20()
