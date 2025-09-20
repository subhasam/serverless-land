## Suggested AWS Policy for running AWS SAM
If you're running it on pesonal account for R & D purpose, you may choose flexibility in the policies to make the code run first and then make have a more fine grain policy following the Principles of Least Privilege. Here is a one for a `Playground` environment. If you're new to AWS IAM, start with creating user and policy on the console. Here is (AWS IAM Documentation)[https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html] to help.

*Note* : You still might need to tweak the below policy if it complains about access or oermission to resources while running the code.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DeploymentActions",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:UpdateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStacks",
                "cloudformation:DescribeStackEvents",
                "cloudformation:CreateChangeSet",
                "cloudformation:DescribeChangeSet",
                "cloudformation:ExecuteChangeSet",
                "cloudformation:DeleteChangeSet",
                "cloudformation:GetTemplate"
            ],
            "Resource": [
                "arn:aws:cloudformation:*:*:stack/*",
                "arn:aws:cloudformation:*:*:transform/Serverless-2016-10-31"
            ]
        },
        {
            "Sid": "LambdaFunctionManagement",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:AddPermission",
                "lambda:RemovePermission"
            ],
            "Resource": "arn:aws:lambda:*:*:function:*"
        },
        {
            "Sid": "S3DeploymentBucket",
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<your-deployment-bucket>",
                "arn:aws:s3:::<your-deployment-bucket>/*"
            ]
        },
        {
            "Sid": "IAMRoleManagement",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole",
                "iam:GetRole"
            ],
            "Resource": "arn:aws:iam::<your-account-id>:role/<specific-role-name>"
        },
        {
            "Sid": "CloudWatchLogManagement",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:/aws/lambda/*"
        },
        {
            "Sid": "APIGatewayManagement",
            "Effect": "Allow",
            "Action": [
                "apigateway:POST",
                "apigateway:GET",
                "apigateway:PUT",
                "apigateway:DELETE",
                "apigateway:PATCH"
            ],
            "Resource": "arn:aws:apigateway:*::/restapis/*"
        },
        {
            "Sid": "IAMRoleActions",
            "Effect": "Allow",
            "Action": [
                "iam:DetachRolePolicy",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:PassRole",
                "iam:CreateRole",
                "iam:TagRole",
                "iam:AttachRolePolicy",
                "iam:GetRole"
            ],
            "Resource": "arn:aws:iam::<your-account-id>:role/<specific-role-name>"
        }
    ]
}
```