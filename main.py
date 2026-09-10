import streamlit as st

import intro
import Hiragana
import Katakana
import jlptn5grammar

st.set_page_config(page_title="My App", layout="wide")

# Sidebar tabs
st.sidebar.title("Menu")

selected_tab = st.sidebar.radio(
    "Choose a tab",
    ["Home", "Hiragana", "Katakana", "Kanji", "JLPT N5 Grammar"]
)

# Display content based on selection
if selected_tab == "Home":
    st.header("Home")
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
    st.header("JLPT N5 Grammar")

    n5GrammarLesson = st.sidebar.selectbox(
        "Lesson",
        ["Lesson 1",
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
    )

    match n5GrammarLesson:
        case "Lesson 1":
            jlptn5grammar.lesson1()
        case "Lesson 2":
            jlptn5grammar.lesson2()
        case "Lesson 3":
            jlptn5grammar.lesson3()
        case "Lesson 4":
            jlptn5grammar.lesson4()
        case "Lesson 5":
            jlptn5grammar.lesson5()
        case "Lesson 6":
            jlptn5grammar.lesson6()
        case "Lesson 7":
            jlptn5grammar.lesson7()
        case "Lesson 8":
            jlptn5grammar.lesson8()
        case "Lesson 9":
            jlptn5grammar.lesson9()
        case "Lesson 10":
            jlptn5grammar.lesson10()
        case "Lesson 11":
            jlptn5grammar.lesson11()
        case "Lesson 12":
            jlptn5grammar.lesson12()
        case "Lesson 13":
            jlptn5grammar.lesson13()
        case "Lesson 14":
            jlptn5grammar.lesson14()
        case "Lesson 15":
            jlptn5grammar.lesson15()
        case "Lesson 16":
            jlptn5grammar.lesson16()
        case "Lesson 17":
            jlptn5grammar.lesson17()
        case "Lesson 18":
            jlptn5grammar.lesson18()
        case "Lesson 19":
            jlptn5grammar.lesson19()
        case "Lesson 20":
            jlptn5grammar.lesson20()
        case "Lesson 21":
            jlptn5grammar.lesson21()
        case "Lesson 22":
            jlptn5grammar.lesson22()
        case "Lesson 23":
            jlptn5grammar.lesson23()
        case "Lesson 24":
            jlptn5grammar.lesson24()
        case "Lesson 25":
            jlptn5grammar.lesson25()