import streamlit as st
import pandas as pd
import uuid

st.set_page_config(layout="wide")
if "rows" not in st.session_state:
    st.session_state["rows"] = []

rows_collection = []
st.write(rows_collection)


def add_row():
    element_id = uuid.uuid4()
    st.session_state["rows"].append(str(element_id))


def remove_row(row_id):
    st.session_state["rows"].remove(str(row_id))


def generate_row(row_id):
    row_container = st.empty()
    row_columns = row_container.columns((1, 1, 3, 1, 1))
    row_project = row_columns[0].selectbox(
        "project", options=["EBPIT", "GM4"], key=f"prjt_{row_id}"
    )
    row_title = row_columns[1].text_input("Title", key=f"title_{row_id}")

    row_name = row_columns[2].text_input("Description", key=f"txt_{row_id}")

    row_assignee = row_columns[3].selectbox(
        "Assignee", options=["oliveirajo", "silvajo3"], key=f"assignee_{row_id}"
    )
    row_columns[4].button("🗑️", key=f"del_{row_id}", on_click=remove_row, args=[row_id])
    return {
        "proj": row_project,
        "issue_title": row_title,
        "issue_name": row_name,
        "assignee": row_assignee,
    }


st.title("Item Inventory")

for row in st.session_state["rows"]:
    row_data = generate_row(row)
    rows_collection.append(row_data)

menu = st.columns(2)

with menu[0]:
    st.button("Add Item", on_click=add_row)


if len(rows_collection) > 0:
    st.subheader("Collected Data")
    display = st.columns(2)
    data = pd.DataFrame(rows_collection)
    data.rename(columns={"proj": "Project", "issue_title": "Title"}, inplace=True)
    display[0].dataframe(data=data, use_container_width=True)
    # display[1].bar_chart(data=data, x="Project", y="Quantity")

st.write(rows_collection)


def do_somehting(lst: list):
    df = pd.DataFrame.from_dict(lst)

    return df.to_csv("teste.csv")


st.download_button(
    label="download csv", data=do_somehting, file_name="test.csv", mime="text/csv"
)
