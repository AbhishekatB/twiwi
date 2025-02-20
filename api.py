import json
import logging

logging.basicConfig(level=logging.INFO)

def handler(request):
    logging.info("Request: %s", request)
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            input_value = data.get('input', '')
            result = input_value[::-1]  # Example: reverse input
            return {
                "statusCode": 200,
                "body": json.dumps({"result": result})
            }
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method Not Allowed"})
        }
    except Exception as e:
        logging.error("Error occurred: %s", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
