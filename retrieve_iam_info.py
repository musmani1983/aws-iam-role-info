import os
import boto3
import csv
import json
import argparse

def retrieve_iam_info():
    # Read AWS credentials and configuration from environment variables
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    aws_session_token = os.environ.get('AWS_SESSION_TOKEN')
    aws_region = os.environ.get('AWS_REGION')

    # Initialize a boto3 session with the provided credentials and region
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        aws_session_token=aws_session_token,
        region_name=aws_region
    )

    # Initialize the AWS IAM client
    iam_client = session.client('iam')

    # Retrieve and process IAM roles
    response = iam_client.list_roles()

    role_info_list = []

    for role in response['Roles']:
        role_name = role['RoleName']
        creation_date = role['CreateDate']
        assume_role_policy_document = role['AssumeRolePolicyDocument']
        description = role.get('Description', 'N/A')
        max_session_duration = role.get('MaxSessionDuration', 'N/A')

        # Retrieve attached policies for the role
        attached_policies = []
        attached_policy_response = iam_client.list_attached_role_policies(RoleName=role_name)
        for policy in attached_policy_response['AttachedPolicies']:
            attached_policies.append(policy['PolicyName'])

        # Retrieve last used information for the role
        role_last_used = role.get('RoleLastUsed', {})
        last_used_date = role_last_used.get('LastUsedDate', 'N/A')
        last_used_region = role_last_used.get('Region', 'N/A')

        role_info = {
            'RoleName': role_name,
            'CreateDate': creation_date,
            'AssumeRolePolicyDocument': assume_role_policy_document,
            'Description': description,
            'MaxSessionDuration': max_session_duration,
            'AttachedPolicies': ', '.join(attached_policies),  # Convert to a comma-separated string
            'LastUsedDate': last_used_date,
            'LastUsedRegion': last_used_region,
            # Add more key-value pairs for additional role information
        }

        role_info_list.append(role_info)

    return role_info_list

def write_to_csv(data, file_name):
    # Define the CSV file headers based on your data structure
    headers = [
        'RoleName',
        'CreateDate',
        'AssumeRolePolicyDocument',
        'Description',
        'MaxSessionDuration',
        'AttachedPolicies',
        'LastUsedDate',
        'LastUsedRegion',
        # Add more header fields as needed
    ]

    with open(file_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def write_to_json(data, file_name):
    with open(file_name + '.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieve and save IAM role information.')
    parser.add_argument('--format', choices=['json', 'csv'], default='csv', help='Output format (default: csv)')
    args = parser.parse_args()

    iam_info = retrieve_iam_info()
    base_file_name = 'iam_role_info'

    if args.format == 'csv':
        write_to_csv(iam_info, base_file_name)
        print(f'IAM role information saved to {base_file_name}.csv')
    elif args.format == 'json':
        write_to_json(iam_info, base_file_name)
        print(f'IAM role information saved to {base_file_name}.json')
