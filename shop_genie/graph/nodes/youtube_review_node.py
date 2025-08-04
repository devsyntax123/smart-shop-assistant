from graph.state import State
from graph.model import youtube
from logger import logger

def youtube_review_node(state: State):
    best_product_name = state.get("best_product", {}).get("product_name")

    if not best_product_name:
        logger.info("Skipping YouTube search: No best product found.")
        return {"youtube_link": None}

    try:
        search_response = youtube.search().list(
            q=f"{best_product_name} review",
            part="snippet",
            type="video",
            maxResults=1
        ).execute()

        video_items = search_response.get("items", [])
        if not video_items:
            logger.info("No YouTube videos found for the best product.")
            return {"youtube_link": None}

        video_id = video_items[0]["id"]["videoId"]
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"
        return {"youtube_link": youtube_link}

    except Exception as e:
        logger.info(f"Error during YouTube search: {e}")
        return {"youtube_link": None}
