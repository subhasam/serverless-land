# Building Lambda Function with AWS SAM(Serverless Access Model)
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
3. **Python 3.13+**: [Install Python](https://www.python.org/downloads/) (AWS is suggesting on EOL of Python 3.9)
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
## AWS Policy for Lambda
Here is a [sample IAM policy](/lambda-sam/AWS_Policy.md) for your AWS `Playground` that is a pre-requisite before you run the function from your local workstation.

---
## Getting started 🚀
### 1. Clone the Repository
If you're getting started on you local, without a remote repo, you can ignore this step.

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
Building codeuri: /Users/subha_sam/dev_playground/serverless-land/lambda-sam/src runtime: python3.13 architecture: x86_64 functions: HelloWorldFunction           
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
### Lambda Function Output on your Local terminal
```bash
lambda-sam % sam local invoke HelloWorldFunction
Invoking app.lambda_handler (python3.13)                                                                                                        Local image was not found.                                                                                                                                       
Removing rapid images for repo public.ecr.aws/sam/emulation-python3.13                                                                                           
Building image...............................................................................................................................................................................
Using local image: public.ecr.aws/lambda/python:3.13-rapid-x86_64.                                                                                               
Mounting /Users/subha_sam/dev_playground/serverless-land/lambda-sam/.aws-sam/build/HelloWorldFunction as /var/task:ro,delegated, inside runtime container        
START RequestId: a122f5ea-102a-454a-ab1f-80647de8c87c Version: $LATEST
END RequestId: acece483-53da-4e77-817e-ed83b89e2c46
REPORT RequestId: acece483-53da-4e77-817e-ed83b89e2c46  Init Duration: 0.34 ms  Duration: 241.62 ms     Billed Duration: 242 ms Memory Size: 128 MB     Max Memory Used: 128 MB
{"statusCode": 200, "body": "{\"message\": \"Hello!! We offer supports for all Digital Wallets and Payment Methods.\", \"input\": {}}"}
```
---
## Testing
Run unit tests:
```bash
cd tests
pytest
```

## Some Troubleshooting Tips
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

