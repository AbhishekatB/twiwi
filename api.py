import json

def handler(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        input_value = data.get('input', '')
        result = input_value[::-1]  # Example logic: reverse the input
        return {
            "statusCode": 200,
            "body": json.dumps({"result": result})
        }
    return {
        "statusCode": 405,
        "body": json.dumps({"error": "Method not allowed"})
    }
