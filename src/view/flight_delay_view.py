import streamlit as st
import pandas as pd

# View
class FlightDelayView:
    """
    The View component for the Flight Delay Prediction App.

    This class handles the display of the Streamlit web application.
    """

    @staticmethod
    def display_input_form():
        """Displays the input form on the Streamlit app."""
        st.title("Flight Delay Prediction App")
        st.write("This app predicts the extent of flight delay in minutes.")
        st.sidebar.header("User Input")

    @staticmethod
    def display_selected_inputs(selected_data):
        """
        Displays selected user inputs.

        Args:
            selected_data (dict): User-provided input data.
        """
        input_data = pd.DataFrame([selected_data])
        st.write("Selected Inputs:")
        st.write(input_data)
        return input_data

    @staticmethod
    def display_predicted_delay(flight_delay):
        """
        Displays the predicted flight delay.

        Args:
            flight_delay (float): Predicted flight delay in minutes.
        """
        st.write("Predicted Flight Delay (minutes):", round(flight_delay[0], 2))
