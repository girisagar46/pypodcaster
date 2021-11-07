# The Podcaster API

This is a FastAPI application that provides a RESTful API for the Podcasts from different podcast's RSS feeds.
The API response is in JSON format and only contains top 5 podcasts from the source.

## Running it locally

1. [Install Poetry](https://python-poetry.org/docs/#installation) on your local machine.
2. Go into the root directory of the project and run the following command to install the dependencies:

   ```bash
   poetry install
   ```

3. Run the application:

   ```bash
   uvicorn main:api --host localhost --port=8000 --log-config log_config.json --reload
   ```

4. Visit [localhost:8000](http://localhost:8000) in your browser.

This is what index page looks like:

![index](demo_images/index.png)

Play around with the API to see the response.
