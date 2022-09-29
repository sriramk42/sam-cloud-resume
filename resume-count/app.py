import boto3
import os

dynamodb = boto3.resource('dynamodb')
ddbTable = os.environ['databaseName']
table = dynamodb.Table(ddbTable)

def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'id': 'Counter'
        },
        UpdateExpression='ADD hits :value',
        ExpressionAttributeValues={
            ':value': 1
        },
        ReturnValues="ALL_NEW"
    )

    visitCount = int(response["Attributes"]['hits'])

    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "Access-Control-Allow-Credentials" : True
        },
        "body": visitCount
    }

    return apiResponse