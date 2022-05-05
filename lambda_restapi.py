from __future__ import print_function
import boto3
import json
import logging

logger= logging.getLogger()
logger.setLevel(logging.INFO)
def lambda_handler(event, context):
    operation = event['httpMethod']
    resource= event['path']
    employeeTable = boto3.resource('dynamodb').Table('employee')

    if(operation=='GET' and resource=='/employee'):

            response = employeeTable.get_item(
                   Key={

                       "id": event['queryStringParameters']['id']
                   });
            if 'Item' in response:
                     return {
                   "statusCode": 200,
                   "body":  json.dumps(response['Item'])}
               
            else:
                return {
                   "statusCode": 400,
                   "body": json.dumps({"message":"No Item found"})}
                

            
               
    if(operation=='GET' and resource=='/employees'):
        return {
                   "statusCode": 200,
                   "body": json.dumps(employeeTable.scan()['Items'])
            
        }

                   
    if(operation=='POST' and resource=='/employee'):
        try:
          employeeTable.put_item(Item=json.loads(event['body']))
          return {
                   "statusCode": 200,
                   "body": json.dumps(event['body'])
            
            }
        except:
             return {
                "statusCode": 406,
                "body": json.dumps({"message":"bad request"})


             }
            
    if(operation=='DELETE' and resource=='/employee'):
    
        try:
         
          employeeTable.delete_item(    
              Key={

                       "id": event['queryStringParameters']['id']
                   })
          return {
                   "statusCode": 200,
                   "body": json.dumps({"message":"the item has been deleted!"})
            
            }
        except:
             return {
                "statusCode": 404,
                "body": json.dumps({"message":"bad request"})


             }
            
             
              
    # elif(operation== 'create'):
    #           return employeeTable.put_item(event["payload"]) 
    
    # elif(operation == 'update'):
    #          return  employeeTable.update_item(id,{});
   
  



  


