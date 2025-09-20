# Building Lambda Function with AWS SAM(Serverless Application Module)
This project demonstrates how to build, deploy, and test a "Hello World" Lambda function using the AWS Serverless Application Model (SAM). It is designed to be simple yet professional, making it accessible to college students and experienced professionals alike.
## Features
- **Serverless Architecture**: Built using AWS Lambda and SAM.
- **Python Implementation**: The Lambda function is written in Python.
- **Unit Testing**: Includes tests to ensure code quality.
- **Step-by-Step Instructions**: Detailed guide for setup, deployment, and testing.
---
## Prerequisites
Ensure the following software is installed:
1. **AWS CLI**: [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
2. **AWS SAM CLI**: [Install SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
3. **Python 3.13+**: [Install Python](https://www.python.org/downloads/)
4. **Docker**: [Install Docker](https://www.docker.com/get-started)
---
#### Using Homebrew for installation
To install the AWS SAM CLI using `Homebrew`
```bash
brew install aws-sam-cli
```
Post installation, verify the installed version:
```bash
sam --version
```


## Project Structure
```
your-app/
├── src/
│   ├── app.py
│   ├── requirements.txt
│   └── __init__.py
├── tests/
│   ├── test_app.py
│   └── __init__.py
├── template.yaml
├── .gitignore
├── LICENSE
├── README.md
```

---
## Step-by-Step Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/hello-world-lambda-sam.git
cd hello-world-lambda-sam
```
### 2. Install Dependencies
```bash
cd src
pip install -r requirements.txt
```
### 3. Build the Application
```bash
sam build
```
### Suggested Command after successful build
```bash
subha_sam@Mac lambda-sam % sam build
Building codeuri: /Users/subha_sam/dev_playground/serverless-land/lambda-sam/src runtime: python3.13.7 architecture: x86_64 functions: HelloWorldFunction           
 Running PythonPipBuilder:ResolveDependencies                                                                                                                    
 Running PythonPipBuilder:CopySource                                                                                                                             

Build Succeeded

Built Artifacts  : .aws-sam/build
Built Template   : .aws-sam/build/template.yaml

Commands you can use next
=========================
[*] Validate SAM template: sam validate
[*] Invoke Function: sam local invoke
[*] Test Function in the Cloud: sam sync --stack-name {{stack-name}} --watch
[*] Deploy: sam deploy --guided
```
### 4. Deploy the Application
```bash
sam deploy --guided
```
Follow the prompts to configure the deployment.
---
### 5. Test the Lambda Function
Invoke the function locally:
```bash
sam local invoke HelloWorldFunction
```
---
## Testing
Run unit tests:
```bash
cd tests
pytest
```

## Troubleshooting
Problem: Error: AWS Region was not found.
Cause:
The AWS CLI is not configured with a default region.

Fix:
Run the following command to configure the AWS CLI and provide required infor from your AWS account.
```bash
aws configure
```

## Best Practices
### 1. Follow the Principle of Least Privilege: 
Grant only the necessary permissions to IAM roles and users.

### 2. Use Environment Variables: 
Store sensitive information (e.g., API keys) in environment variables instead of hardcoding them.

### 3. Write Unit Tests: 
Ensure all critical functionality is covered by unit tests.

### 4. Monitor Lambda Logs: 
Use CloudWatch Logs to monitor and debug Lambda function executions.

### 5. Keep Dependencies Minimal: 
Only include necessary dependencies in requirements.txt to reduce the deployment package size.

