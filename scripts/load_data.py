import os
import boto3
import json
from botocore.exceptions import BotoCoreError, ClientError
from boto3.dynamodb.types import TypeDeserializer
from print_log import print_log as logger
from print_log import setup_logging as setup_loggin

# set up logging
setup_loggin()

def load_data_to_dynamodb(json_file_path, table_name):
    """
    EARL DOWNS guiding to CHATGPT
    Loads data from a JSON file into a specified DynamoDB table.

    Args:
        json_file_path (str): the JSON file path to load data from.
        table_name (str): the table name in DynamoDB to load data into.

    Returns:
        None
    """
    try:
        # Inicializar cliente DynamoDB
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(table_name)

        # read JSON file
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            items = json.load(json_file)

        if not isinstance(items, list):
            logger(f"File must contains a object list.", type='error')
            raise ValueError("Json file must contain a list of objects.")

        # Initialize TypeDeserializer to convert DynamoDB types
        deserializer = TypeDeserializer()
        
        formato = "plain" #plain (json plano) o raw (json formato dynamodb crudo)
        
        # Cargar elementos a la tabla
        for item in items:
            # Convertir al formato plano esperado por boto3
            if formato == "plain":
                item_plain = item
            
            if formato == "dynamoraw":
                item_plain = {key: deserializer.deserialize(value) for key, value in item.items()}

            table.put_item(Item=item_plain)
            logger("Item updated with success.")

        logger("Data file loaded successfully.")

    except (BotoCoreError, ClientError) as error:
        logger(f"Error al interactuar con DynamoDB: {error}", "error")
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as error:
        logger(f"Error al procesar el archivo JSON: {error}", "error")
    except Exception as e:
        logger(f"Ocurrió un error inesperado: {e}", "error")

if __name__ == "__main__":
    # Favor indicar tabla física DynamoDB a actualizar
    TABLE_NAME = "Memberships"
    
    while True:        
        OPTION_TABLE = input("Please enter table to update (1 = Memberships, 2 = Other): ") 
        
        if OPTION_TABLE == "1":
            TABLE_NAME = "Memberships"
        elif OPTION_TABLE == "2":
            TABLE_NAME = "Other"
        else:                        
            if input("Please confirm to start (y/n): ").lower() != "y":
                break
            
        # request JSON file path
        JSON_FILE_PATH = input("Enter json file path with data: ")
        
        if not JSON_FILE_PATH or not os.path.exists(JSON_FILE_PATH):
            logger(f"File does not exists: {JSON_FILE_PATH}", type='error')
        else:        
            load_data_to_dynamodb(JSON_FILE_PATH, TABLE_NAME)
            print("\nProcess finished with success.")
                    
        print("¿Load again? (y/n)")    
        respuesta = input()
        if respuesta.lower() != "y":
            break        