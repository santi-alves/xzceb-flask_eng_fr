""" This module is used to translate text from french to english and vice versa with IBM Watson"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """ This function is used on the endpoint "/englishToFrench" to 
    translate the input text to the specified language.
    :param str english_text: the text to be translated.
    :return str with the translated text."""

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr')
    translation = translation.get_result()[
        "translations"][0]["translation"]

    return translation


def french_to_english(french_text):
    """ This function is used on the endpoint "/frenchToEnglish" to 
    translate the input text to the specified language.
    :param str french_text: the text to be translated.
    :return str with the translated text."""

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en')
    translation = translation.get_result()[
        "translations"][0]["translation"]

    return translation
