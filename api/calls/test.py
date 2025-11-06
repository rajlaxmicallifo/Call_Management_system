import json

def handler(request):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Calls API is working!',
            'status': 'success',
            'data': ['call1', 'call2', 'call3']
        })
    }