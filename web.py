import streamlit as st
import functions as fun

st.title("This is Title")
st.subheader("This is Sub-header")
st.write("This is write")
st.checkbox("This is checkbox")
st.checkbox("This is checkbox 2")
st.text_input(label="This is st.text_input", placeholder="this is a placeholder")
st.write('\n')


st.write("!!!!! This is a To-Do List !!!!!")


todo_list = fun.get_todos()


def add_newtodo():
    new_todo = st.session_state['key_newtodo'] + '\n'
    todo_list.append(new_todo)
    fun.write_todos("w", todo_list)


for todo in todo_list:
    st.checkbox(todo)


st.text_input(label="Add a new To-Do", placeholder="Enter a To-Do...",
              on_change=add_newtodo, key="key_newtodo")
