import json
import logging

from jsonifyx.config import NAME

logger = logging.getLogger(NAME)


def jsonify(json_input):
    """
    Beautify json input.
    :param json_input: json.
    :return: formatted json.
    """
    formatted_json = json.dumps(json.loads(json_input), indent=4)
    logger.info(f"Formatted json: {formatted_json}")
    return formatted_json
