import streamlit as st

import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To-Do app")





for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        st.session_state[todo]
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="text_input to add todo",label_visibility="hidden",placeholder="Enter a to-do here",on_change=add_todo, key ="new_todo")