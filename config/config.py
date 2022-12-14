##config.py

from pathlib import Path
import pretty_errors
import nltk
from nltk.corpus import stopwords
## directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
DATA_DIR = Path(BASE_DIR, "data")

## create dir
DATA_DIR.mkdir(parents=True, exist_ok=True)


# Assets
PROJECTS_URL = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/projects.csv"
TAGS_URL = "https://raw.githubusercontent.com/GokuMohandas/Made-With-ML/main/datasets/tags.csv"

# NLTK's default stopwords
nltk.download("stopwords")
STOPWORDS = stopwords.words("english")


# config/config.py
STOPWORDS = [
    "i",
    "me",
    "my",
    "won't",
    "wouldn",
    "wouldn't",
]

