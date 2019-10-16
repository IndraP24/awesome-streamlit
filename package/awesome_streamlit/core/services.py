"""Organizes and shares business logic, data and functions with different
pages of the Streamlit App.

  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations
"""
import urllib.request

import streamlit as st


@st.cache
def get_file_content_as_string(url: str) -> str:
    """The url content as a string

    Arguments:
        url {str} -- The url to request

    Returns:
        str -- The text of the url
    """
    data = urllib.request.urlopen(url).read()
    return data.decode("utf-8")
