import json

import feedparser
import httpx
from feedparser import FeedParserDict

from constants import DATA_FILE_LOCATION

# The urls of the feeds to be parsed. We can add more feeds here.
urls = {
    "talk_python": "https://talkpython.fm/episodes/rss",
    "real_python": "https://realpython.com/podcasts/rpp/feed",
    "python_bytes": "https://pythonbytes.fm/episodes/rss",
    "profitable_python": "https://anchor.fm/s/c8df638/podcast/rss"
}


def get_parsed_feed(url: str) -> FeedParserDict:
    """
    Returns a parsed feed from the given url
    Args:
        url: The RSS url to parse

    Returns: FeedParserDict after parsing the url

    """
    with httpx.Client() as client:
        response = client.get(url)
        return feedparser.parse(response.content)


def extract_podcast_info_from_feed(top_five_entries: list) -> list:
    """
    Extracts the information from the top 5 entries in the feed
    Args:
        top_five_entries: The top 5 entries for each podcast

    Returns: List of dictionaries containing the information for each podcast
    """
    pod_cast_data = []
    for entry in top_five_entries:
        pod_casts = {
            'title': entry['title'],
            'summary': entry['summary'],
            'published': entry['published'],
            'link': entry['link'],
        }
        pod_cast_data.append(pod_casts)
    return pod_cast_data


def generate_podcasts_json() -> None:
    """
    Generates a json file containing the top 5 podcasts from each of the RSS feeds
    """
    final_data = {}
    for key, url in urls.items():
        parsed_feed = get_parsed_feed(url)
        feed = parsed_feed['feed']
        datum = {
            "title": feed['title'],
            "subtitle": feed['subtitle'],
            "publisher": feed.get('publisher', ''),
            "summary": feed.get('summary', ""),
            "image": feed['image']['href'],
        }
        top_five_entries = parsed_feed['entries'][:5]
        datum["top_five_podcasts"] = extract_podcast_info_from_feed(top_five_entries)
        final_data[key] = datum

    # Write to file for future use
    with open(DATA_FILE_LOCATION, 'w') as f:
        f.write(json.dumps(final_data))


if __name__ == '__main__':
    # This is added to run the script directly from the command line
    generate_podcasts_json()
