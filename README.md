# 3.6 Snyk Scan - Serverless Lambda with Security Scanning

This repository contains a Terraform configuration to deploy a simple "Hello, World!" AWS Lambda function with comprehensive CI/CD security scanning using GitHub Actions and Snyk.

## Architecture

- **AWS Lambda Function**: Python-based function that prints "Hello, World!"
- **Terraform Infrastructure**: Complete IaC setup with IAM roles, CloudWatch logs
- **GitHub Actions**: Automated CI/CD with terraform checks and Snyk security scans
- **Security Scanning**: Multiple Snyk security scans (IaC, Code, Open Source, Container)

## Files Structure

```
.
├── lambda_function.py          # Python Lambda function code
├── main.tf                     # Main Terraform configuration
├── variables.tf                # Terraform input variables
├── outputs.tf                  # Terraform outputs
├── .terraform-version          # Terraform version specification
├── .tflint.hcl                # TFLint configuration
├── .github/workflows/ci.yaml   # GitHub Actions workflow
└── README.md                   # This file
```

## Prerequisites

1. **AWS Account**: Configure AWS credentials for deployment
2. **Terraform**: Version 1.6.0 or later
3. **Snyk Account**: Get a Snyk token for security scanning

## Setup Instructions

### 1. Configure GitHub Secrets

Add the following secrets to your GitHub repository:

- `SNYK_TOKEN`: Your Snyk authentication token

### 2. Local Development

```bash
# Initialize Terraform
terraform init

# Format Terraform files
terraform fmt

# Validate configuration
terraform validate

# Plan deployment (optional)
terraform plan

# Deploy infrastructure
terraform apply
```

### 3. GitHub Actions Workflow

The CI/CD pipeline runs on:
- Push to `main` branch
- Pull requests to `main` branch

The workflow includes:

#### Terraform Checks
- ✅ Format verification (`terraform fmt`)
- ✅ Configuration validation (`terraform validate`)
- ✅ TFLint static analysis
- ✅ Security best practices

#### Snyk Security Scans
- 🔒 Infrastructure as Code (IaC) scanning
- 🔒 Static code analysis
- 🔒 Open source dependency scanning
- 🔒 Container scanning (if applicable)

## Lambda Function

The deployed Lambda function:
- **Runtime**: Python 3.9
- **Handler**: `lambda_function.lambda_handler`
- **Memory**: Default (128 MB)
- **Timeout**: 60 seconds
- **Function**: Prints "Hello, World!" and returns JSON response

## Security Features

- ✅ IAM least privilege access
- ✅ CloudWatch logging enabled
- ✅ Terraform state security
- ✅ Automated security scanning
- ✅ Infrastructure as Code validation
- ✅ Static code analysis
- ✅ Dependency vulnerability scanning

## Outputs

After deployment, you'll get:
- Lambda function ARN
- Lambda function name
- Lambda invoke ARN
- IAM role ARN

## Clean Up

```bash
terraform destroy
```

## CI/CD Status

The GitHub Actions workflow ensures:
1. All Terraform configurations are properly formatted and valid
2. Security scans pass with acceptable risk levels
3. No high-severity vulnerabilities in code or dependencies
4. Infrastructure follows security best practices

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and ensure all checks pass
4. Submit a pull request

The automated CI/CD pipeline will run all terraform and security checks before merge.