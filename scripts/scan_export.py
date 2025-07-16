import decimal
import boto3
import json
from print_log import print_log as logger
from print_log import setup_logging as setup_loggin
# Initialize the DynamoDB client
# Ensure you set the table name and region as per your AWS setup
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'Memberships'
table = dynamodb.Table(table_name)

# Configuración del logging
setup_loggin()

def scan_table(table):
    """Scan the DynamoDB table and retrieve all items."""
    response = table.scan()
    items = response.get('Items', [])
    
    # Loop to handle pagination in case of large tables
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        items.extend(response.get('Items', []))
        
    logger(f"Finalizada lectura de datos. Total de items: {len(items)}")
    return items

def save_items_as_json(items, file_name="exportedData.json"):
    with open(file_name, "w") as json_file:
        json.dump(items, json_file, indent=4, default=json_serializer, ensure_ascii=False, )
    logger(f"Data saved to {file_name}")

# Custom JSON serializer to handle decimal.Decimal types
def json_serializer(obj):
    if isinstance(obj, decimal.Decimal):
        #if value is an integer, convert to int, otherwise to float
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

if __name__ == "__main__":
    # Get all items from the table
    items = scan_table(table)
    logger(f"Exporting data from {table_name}...")
    
    # Save items as JSON data
    save_items_as_json(items, f"{table_name}-exported-data.json")
    logger(f"Data saved to '{table_name}-exported-data.json'")