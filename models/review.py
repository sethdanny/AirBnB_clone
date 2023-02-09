#!/usr/bin/python3
"""Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        review_text (str): The text of the review.
    """

    place_id = ""

    user_id = ""

    review_text = ""
