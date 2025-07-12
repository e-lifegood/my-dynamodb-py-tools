# DynamoDB File Utilities

## Overview

This project contains a set of Python utilities designed to simplify working with files and Amazon DynamoDB. These tools are tailored for common tasks encountered during daily work, such as importing, exporting, and managing data within DynamoDB tables.

## Features

- Upload files or batches of records to DynamoDB tables.
- Export DynamoDB table data to files (CSV, JSON, etc.).
- Utility functions for bulk insert, update, and delete operations.
- Support for table scanning and querying.
- Error handling and logging for batch operations.
- Command-line usage for automation.

## Getting Started

### Prerequisites

- Python 3.7+
- AWS credentials configured (via environment variables, ~/.aws/credentials, or IAM roles)
- boto3 library

### Installation

```bash
pip install -r requirements.txt
```

### Usage

#### Example: Upload a CSV file to DynamoDB

```bash
python upload_csv_to_dynamodb.py --table MyTable --file data.csv
```

#### Example: Export DynamoDB table to JSON

```bash
python export_dynamodb_to_json.py --table MyTable --output output.json
```

## Configuration

- Update AWS credentials and region in your environment.
- Modify utility scripts for your table schema as needed.

## Contributing

Feel free to submit issues, suggest improvements, or create pull requests to add new features or fix bugs.

## License

MIT License

## Author

(Earl Downs - e-lifegood)
