from requests import get
from webbrowser import open
from typing import Optional


class InvalidAPIKey(Exception):
    """Api Key not valid"""
    pass


def _check_type(_value, expected_type) -> None:
    """raises Value Error if given type is not expected type"""
    if not isinstance(_value, expected_type):
        def __type(value) -> str:
            """
            returns type of value in string format
            """
            if isinstance(value, int):
                return 'int'
            elif isinstance(value, str):
                return 'str'
            elif isinstance(value, list):
                return 'list'
            elif isinstance(value, tuple):
                return 'tuple'
            elif isinstance(value, bool):
                return 'bool'

        raise ValueError(f"expected {__type(expected_type)} got {__type(_value)}")

class Channel(object):
    """
    gets info about a channel
    """
    def __init__(self, channel_id, api_key:str) -> None:
        pass


class Video(object):
    """
gets info about a channel
"""
    def __init__(self, video_id, api_key:str) -> None:
        pass


class Youtube(object):
    """main class of youtube.py library"""
    def __init__(self, api_key: str) -> None:
        """
        :param api_key: api key of youtube
        to get an api key use get_api_key() function of this library
        """
        self.Api_Key = api_key
        _check_type(self.Api_Key,str)
        self._check_api_key(self.Api_Key)

    def _check_api_key(self, api_key):
        """
        checks given api key
        :param api_key: api key
        """

    def get_channel(self, channel_id):
        _check_type(channel_id,str)
        return Channel(channel_id=channel_id,api_key=self.Api_Key)

    def get_video(self, video_id):
        _check_type(video_id,str)
        return Video(video_id=video_id,api_key=self.Api_Key)


# clean up
del (get, open, _check_type)
