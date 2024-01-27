"""
Whenever user refreshes the webpage, the script is executed from
top to bottom with any load/ refresh of the page. When a webapp
is public, it can have multiple users. Multiple users accessing
the webapp at same or different times. Each user session is
separate from other user session.

Before hosting the webapp on the server, run this command
pip freeze > requirements.txt

requirements.txt will be created in your directory.
requirements.txt is a file which will be uploaded to the server
where we host this web app. With the help of this file, the
server will know all the Python libraries the server need to
install in order to run the webapp correctly. So that the
server has python installed. If the server has Python installed
already, then the server should know what all packages or
third-party packages needed to install for you webapp to run
correctly.

With the below command,
    pip freeze
All the list of packages and their versions are displayed on the
command line.

But with the
    > requirements.txt
all the package names and their versions to the requirements.txt
file.

"""

import streamlit as st
import todo_functions

todos = todo_functions.get_todos()


def add_todo():
    # session_state is of type session_state, which is object
    # type of streamlit. Its looks like a dictionary storing
    # key-value pairs of the widgets.
    ntodo = st.session_state["new_todo"] + "\n"
    todos.append(ntodo)
    todo_functions.set_todos(todos)


# set the title of webapp
st.title("My To-do App")

for index, todo in enumerate(todos):
    # creates a checkbox and gives the existing todo name in \
    # the file as its label
    # to manipulate the checkboxes i.e., mark it as complete
    # when checked, we will need to add a key to the widget
    # if the name of the key is static or pre-defined all the
    # todos in the list will have the same key.
    # e.g. key = "todo"
    # the session state dictionary will look like
    # { "new_todo'" : "", "todo" : false }
    # so instead of static or predefined value, provide the name
    # of the to-do as the key due to which each checkbox will
    # have a different key.
    # when the checkbox gets checked, the value of the key is true
    # so we will store check checkbox value in a variable and that
    # allows ro check if checkbox is checked or not.
    checked = st.checkbox(todo, key=todo)

    # if the checkbox is checked removed the todo item from the
    # list.
    # update the list in the todo.txt file
    # also delete the checked todo from the session_state
    # finally rerun the function to rerun the code to display
    # the update todo list
    if checked:
        todos.pop(index)
        todo_functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()

# creates a text input field.
# label is required argument for text input field. It can string
# or blank (""). The label of the text input is placed on the top
# of the text input field.
# placeholder is like a hint for the user displayed inside the
# text input field indicating what should be entered.
# on_change argument will be equivalent to a callback function
# which is a custom function. "add_todo" is the name of the
# function.
# to get the value entered in the text input field, we will
# need to add the key to the widget. This key will store the value
# entered the widget in dict data-structure.

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
