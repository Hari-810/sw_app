import streamlit as st

# Create an empty list to store user data (initialize as a list)
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = []

# Define a simple admin password
ADMIN_PASSWORD = "admin123"

# Function to display form for users to enter Question and Fun Fact
def user_input():
    st.header("Submit Your Details")
    question = st.text_input("Enter your question")
    fun_fact = st.text_area("Enter a fun fact about yourself")
    
    if st.button("Submit"):
        if question and fun_fact:
            # Append the user's details to the list
            st.session_state['user_data'].append({
                "Question": question,
                "Fun Fact": fun_fact
            })
            st.success("Your details have been submitted!")
        else:
            st.error("Please fill in all fields.")

# Function to display data for Admin
def admin_view():
    st.header("Admin Dashboard")
    password = st.text_input("Enter Admin Password", type='password')
    
    if password == ADMIN_PASSWORD:
        if st.session_state['user_data']:
            st.write("### Submitted User Data")
            for idx, details in enumerate(st.session_state['user_data']):
                st.write(f"**Entry {idx + 1}:**")
                st.write(f"- **Question**: {details['Question']}")
                st.write(f"- **Fun Fact**: {details['Fun Fact']}")
                st.write("---")
        else:
            st.info("No user data available.")
    elif password:
        st.error("Incorrect password. Please try again.")

# Main logic for the Streamlit app
st.title("Fun Fact & Question App")

# Select whether user or admin
role = st.radio("Are you a User or Admin?", ('User', 'Admin'))

if role == 'User':
    user_input()
elif role == 'Admin':
    admin_view()
