import reflex as rx
from enum import Enum
from .fonts import Font as Font
from .colors import TextColor, Color 

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Signika+Negative:wght@300:500&display=swap",
    "https://fonts.googleapis.com/css?family=Poppins:wght@500&display=swap"
    "https://fonts.googleapis.com/css?family=Teko:wght@400&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value, 
    "color": TextColor.PRIMARY.value,
    "background": Color.DEFAULT.value
}

class Size(Enum):
    DEFAULT = "1em"
    SMALL = "0.5em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    
    

class Spacing(Enum):
    DEFAULT = "1em"
    SMALL = "0.5em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"