import streamlit as st

st.title("Basic Calculator")


if "anything" not in st.session_state:
    st.session_state["anything"] = ""


st.text_input(
    label="Result",
    value=st.session_state["anything"],
    disabled=True,
    label_visibility="collapsed"
)

row1_col = st.columns(4)

with row1_col[0]:
    if st.button("7"):
        st.session_state["anything"] += "7"
        st.rerun()

with row1_col[1]:
    if st.button("8"):
        st.session_state["anything"] += "8"
        st.rerun()

with row1_col[2]:
    if st.button("9"):
        st.session_state["anything"] += "9"
        st.rerun()

with row1_col[3]:
    if st.button("/"):
        st.session_state["anything"] += "/"
        st.rerun()

row2_col = st.columns(4)

with row2_col[0]:
    if st.button("4"):
        st.session_state["anything"] += "4"
        st.rerun()

with row2_col[1]:
    if st.button("5"):
        st.session_state["anything"] += "5"
        st.rerun()

with row2_col[2]:
    if st.button("6"):
        st.session_state["anything"] += "6"
        st.rerun()

with row2_col[3]:
    if st.button("*"):
        st.session_state["anything"] += "*"
        st.rerun()

row3_col = st.columns(4)

with row3_col[0]:
    if st.button("1"):
        st.session_state["anything"] += "1"
        st.rerun()

with row3_col[1]:
    if st.button("2"):
        st.session_state["anything"] += "2"
        st.rerun()

with row3_col[2]:
    if st.button("3"):
        st.session_state["anything"] += "3"
        st.rerun()

with row3_col[3]:
    if st.button("+"):
        st.session_state["anything"] += "+"
        st.rerun()

row4_col = st.columns(4)

with row4_col[0]:
    if st.button("0"):
        st.session_state["anything"] += "0"
        st.rerun()

with row4_col[1]:
    if st.button("-"):
        st.session_state["anything"] += "-"
        st.rerun()

with row4_col[2]:
    
    if st.button("Clear"):
        st.session_state["anything"] = ""
        st.rerun()

with row4_col[3]:
    if st.button("="):
        try:
            
            if st.session_state["anything"].strip() == "":
                pass
            else:
                result = eval(st.session_state["anything"])
                st.session_state["anything"] = str(result)
        except ZeroDivisionError:
            st.session_state["anything"] = "Error: Div by 0"
        except Exception:
            st.session_state["anything"] = "Error"
        st.rerun()