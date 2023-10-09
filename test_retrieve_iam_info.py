import unittest
import os
from retrieve_iam_info import retrieve_iam_info, write_to_csv

class TestRetrieveIAMInfo(unittest.TestCase):

    def test_retrieve_iam_info(self):
        # Mock AWS client or use testing profiles
        # Call your retrieve_iam_info() function
        iam_info = retrieve_iam_info()

        # Add assertions to check if the retrieved data is as expected
        self.assertIsNotNone(iam_info)
        self.assertTrue(isinstance(iam_info, list))
        self.assertTrue(len(iam_info) > 0)
        
        # Add more assertions to check the format and content of the role information
        for role_info in iam_info:
            self.assertIn('RoleName', role_info)
            self.assertIn('CreateDate', role_info)
            self.assertIn('AssumeRolePolicyDocument', role_info)
            self.assertIn('Description', role_info)
            self.assertIn('MaxSessionDuration', role_info)
            self.assertIn('AttachedPolicies', role_info)
            self.assertIn('LastUsedDate', role_info)
            self.assertIn('LastUsedRegion', role_info)

    def test_write_to_csv(self):
        # Create test IAM role data
        test_iam_info = [
            {
                'RoleName': 'TestRole1',
                'CreateDate': '2023-10-01',
                'AssumeRolePolicyDocument': 'test_policy1',
                'Description': 'Test role 1',
                'MaxSessionDuration': 3600,
                'AttachedPolicies': 'Policy1,Policy2',
                'LastUsedDate': '2023-10-05',
                'LastUsedRegion': 'us-east-1'
            },
            # Add more test IAM role data
        ]

        # Define the expected CSV file path
        expected_csv_file = 'test_iam_roles.csv'

        # Call the write_to_csv function to generate the CSV file
        write_to_csv(test_iam_info, expected_csv_file)

        # Check if the CSV file was created
        self.assertTrue(os.path.isfile(expected_csv_file))

        # Read the CSV file and verify its content
        with open(expected_csv_file, 'r') as csvfile:
            csv_content = csvfile.read()
            # Add assertions to check the content of the CSV file

        # Clean up: Delete the generated CSV file
        os.remove(expected_csv_file)

if __name__ == '__main__':
    unittest.main()
