"""
This module provides functions to run translation request against the Watson-Translation
Service.
"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(apikey)
WATSON_TRANSLATOR = LanguageTranslatorV3(
    version="2023-01-10", authenticator=AUTHENTICATOR
)
WATSON_TRANSLATOR.set_service_url(url)
WATSON_TRANSLATOR.set_disable_ssl_verification(True)

def english_to_french(english_text: str) -> str:
    """
    A function which requests Watson for a french translation of an
    english text.
    """
    french_text = WATSON_TRANSLATOR.translate(
        text=[english_text],
        source="en",
        target="fr"
    )
    return french_text


def french_to_english(french_text: str) -> str:
    """
    A function which requests Watson for an english translation of a
    french text.
    """
    english_text = WATSON_TRANSLATOR.translate(
        text=[french_text],
        source="fr",
        target="en"
    )
    return english_text
