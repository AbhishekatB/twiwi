
import json

def handler(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            input_value = data.get('input', '')
            result = input_value[::-1]  # Example: reverse input string
            return {
                "statusCode": 200,
                "body": json.dumps({"result": result})
            }
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method Not Allowed"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
