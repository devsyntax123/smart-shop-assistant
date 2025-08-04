from graph.model import tavily_client
from graph.model import load_blog_content
from tavily.errors import InvalidAPIKeyError, UsageLimitExceededError
from logger import logger
def tavily_search_node(state):
    try:
        # Use the user-provided query from the state
        query = state.get('query', state['query'])
        
        # Check if Tavily client is available
        if not tavily_client:
            logger.info("Error: Tavily client not initialized. Please check your TAVILY_API_KEY.")
            return {"blogs_content": []}
        
        # Perform the search with Tavily to retrieve multiple blog links
        response = tavily_client.search(query=query, max_results=3)  # Increased to 3 for better coverage

        if "results" not in response or not response["results"]:
            logger.info("No search results found for the given query.")
            return {"blogs_content": []}
            
        # Initialize an empty list to store each blog's content
        blogs_content = []
        
        # Iterate over the search results
        for blog in response['results']:
            blog_url = blog.get("url", "")
            if blog_url:
                # Load and store content from each URL using WebBaseLoader
                content = load_blog_content(blog_url)
                if content and len(content.strip()) > 100:  # Only include meaningful content
                    # Append blog details to blogs_content
                    blogs_content.append({
                        "title": blog.get("title", ""),
                        "url": blog_url,
                        "content": content,  # Use loaded content
                        "score": blog.get("score", "")
                    })
                else:
                    logger.info(f"Skipping {blog_url} - content too short or blocked")

        # Store all blog contents in the state
        if len(blogs_content) > 0:
            logger.info(f"Successfully extracted content from {len(blogs_content)} blogs")
            return {"blogs_content": blogs_content}
        else:
            logger.info("No usable blog content found after filtering.")
            return {"blogs_content": []}

    except InvalidAPIKeyError:
        logger.info("Error: Invalid Tavily API key. Please verify your key.")
        return {"blogs_content": []}
    except UsageLimitExceededError:
        logger.info("Error: Tavily usage limit exceeded. Check your plan or limits.")
        return {"blogs_content": []}
    except Exception as e:
        logger.info(f"Error with Tavily API call: {e}")
        return {"blogs_content": []}
