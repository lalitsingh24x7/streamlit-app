# Import the Streamlit library
import streamlit as st


# Function to simulate an API call (replace with actual API call)
def get_api_response(input_data):
    return """
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    """


# Streamlit code for the UI
def main():
    st.title("Streamlit App")

    # User input: Text input box
    input_text = st.text_input("Question:")

    # Submit button
    if st.button("Submit"):
        # Input validation
        if not input_text:
            st.warning("Please enter a question.")
            return

        # Simulate an API call
        response_data = get_api_response(input_text)

        # Display API response with formatting
        if response_data:
            st.markdown("## Response:")
            st.info(response_data)
        else:
            st.error("Error fetching API data. Please try again.")


if __name__ == "__main__":
    main()
