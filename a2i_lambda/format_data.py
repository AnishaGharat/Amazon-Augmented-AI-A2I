import json


def format_data(data):
    """ Args:
        ---
        > data: (string) JSON object fetched from the S3 file

        Returns:
        ---
        > JSON of input to the A2I
    """

    data = json.loads(data)
    images = data["file_data"]["image_paths"]
    file_type = data['file_data']['file_type']
    key_values = data["keyValuePairs"]
    filtered_content = []
    
    for pair in key_values:
        if int(pair["confidence"]) < 90:
            filtered_content.append(pair)
    return {
        'filtered_content': key_values,
        'images': images,
        'file_type': file_type
    }