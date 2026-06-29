# Automate CI/CD Pipeline for AWS Lambda

## Project Overview

This project demonstrates a Continuous Integration and Continuous Deployment (CI/CD) pipeline for an AWS Lambda function using GitHub and AWS CodePipeline. Whenever code is pushed to the GitHub repository, AWS CodePipeline automatically deploys the latest version of the Lambda function without any manual intervention.

## Architecture

```text
Developer
    │
git push
    │
GitHub Repository
    │
AWS CodePipeline
    │
AWS Lambda
```

## AWS Services Used

- AWS Lambda
- AWS CodePipeline
- AWS IAM
- Amazon CloudWatch
- GitHub

## Features

- Automated deployment of AWS Lambda on every GitHub push.
- Eliminates manual Lambda code uploads.
- Version-controlled Lambda source code using GitHub.
- CloudWatch integration for monitoring and debugging.
- Simple and efficient serverless CI/CD workflow.

## Project Structure

```text
lambda-cicd-demo/
│── lambda_function.py
└── README.md
```

## Workflow

1. Create an AWS Lambda function.
2. Push the Lambda source code to a GitHub repository.
3. Configure AWS CodePipeline with GitHub as the source.
4. Select the Lambda function as the deployment target.
5. Commit and push code changes to GitHub.
6. CodePipeline automatically deploys the updated Lambda function.
7. Test the Lambda function to verify the latest changes.

## Testing

Modify the Lambda function and push the changes:

```bash
git add .
git commit -m "Updated Lambda function"
git push
```

After the pipeline completes successfully, test the Lambda function from the AWS Management Console to verify that the latest code has been deployed.

## Learning Outcomes

- Implemented CI/CD for serverless applications.
- Integrated GitHub with AWS CodePipeline.
- Automated AWS Lambda deployments.
- Used CloudWatch to monitor Lambda executions.
- Gained practical experience with AWS serverless deployment workflows.

## Note

This project does **not** use AWS CodeBuild because the Lambda function is a simple Python application that does not require a build process. AWS CodePipeline directly deploys the updated source code from the GitHub repository to AWS Lambda, keeping the deployment workflow simple and efficient.
