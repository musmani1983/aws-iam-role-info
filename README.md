# AWS IAM Role Information Retrieval

This Python script allows you to retrieve and save information about AWS IAM roles, including their creation date, assume role policy document, description, and more. You can choose to save the information in either CSV or JSON format.

## Prerequisites

Before using this script, you need to have the following prerequisites:

- Python 3.x installed
- AWS CLI configured with the necessary IAM permissions
- Boto3 library installed (`pip install boto3`)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/aws-iam-role-info.git
   cd aws-iam-role-info
   ```

2. Create a virtual environment and install the required dependencies:

   ```bash
   make setup
   ```

## Usage

You can run the script to retrieve IAM role information and choose the output format (CSV or JSON). Use the following commands:

- To run the script and save the information in CSV format:

  ```bash
  make run-csv
  ```

- To run the script and save the information in JSON format:

  ```bash
  make run-json
  ```

## Testing

You can run tests for this script using the following command:

```bash
make test
```

## Cleanup

To remove the virtual environment and other generated files, you can use the following command:

```bash
make clean
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you find any issues or have suggestions for improvements.

## Acknowledgments

- Special thanks to the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library for making AWS interactions in Python easy.
