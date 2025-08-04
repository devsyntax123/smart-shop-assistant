from graph.state import State
from graph.structure import ListOfSmartphoneReviews
import time
from graph.prompty_template import schema_mapping_prompt_template 
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from graph.model import llm
from logger import logger

def schema_mapping_node(state: State):
  max_retries = 3  # Maximum number of retries
  wait_time = 60   # Wait time in seconds between retries (1 minute)
  try:
    # Check if "blogs_content" exists in the state and is not empty
    if "blogs_content" in state and state["blogs_content"]:
            # Extract blog content from the state
            blogs_content = state["blogs_content"]
            # Define the prompt
            prompt_template=schema_mapping_prompt_template
            # Set up a parser and inject instructions into the prompt template.
            parser = JsonOutputParser(pydantic_object=ListOfSmartphoneReviews)
            # Format the prompt with the full blogs content
            prompt = PromptTemplate(
                template = prompt_template,
                input_variables = ["blogs_content"],
                partial_variables={"format_instructions": parser.get_format_instructions()}
            )
            # Retry mechanism to invoke LLM and parse the response
            for attempt in range(1, max_retries + 1):
                # try:
                    # Use LLM to process the prompt and return structured smartphone details
                    chain = prompt | llm | parser  # Invokes LLM with the prepared prompt
                    response = chain.invoke({"blogs_content": blogs_content})

                    # Check if the response contains more than one product in the schema
                    if response.get('products') and len(response['products']) > 1:
                        # If valid, store the structured schema in the state
                        return {"product_schema": response['products']}
                    else:
                        logger.info(f"Attempt {attempt} failed: Product schema has one or fewer products.")

                    # Wait for 1 minute before retrying if not successful and retry limit not reached
                    if attempt < max_retries:
                        time.sleep(wait_time)

                # except Exception as retry_exception:
                #     logger.info(f"Retry {attempt} error: {retry_exception}")
                #     if attempt < max_retries:
                #         time.sleep(wait_time)

            # Return an empty schema if all retries fail
            logger.info("All retry attempts failed to create a valid product schema with more than one product.")
            return {"product_schema": []}
    else:
      # If "blogs_content" is not present or is empty, log and return state unmodified
      logger.info("No blog content available or content is empty; schema extraction skipped.")
      return {"product_schema":[]}

  except Exception as e:
        # Error handling to catch any unexpected issues and log the error message
        logger.info(f"Error occurred during schema extraction: {e}")
        return state