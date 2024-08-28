<p align="center">
  <img src="https://github.com/walkxcode/dashboard-icons/blob/main/png/terraform.png?raw=true" alt="Header" width="100" height="100"><br>

<h3 align="center"> Learning Terraform </h3>


<h2> :memo: Table of Contents </h2>

+ [Module 2: What you need to know about Iac.](#module-2-what-you-need-to-know-about-iac)
  + [Infrastructure as Code Benefits](#infrastructure-as-code-benefits)
+ [Module 3: Deploying your first Terraform configuration.](#module-3-deploying-your-first-terraform-configuration)

## Module 2: What you need to know about Iac.

### Infrastructure as Code Benefits
- Reusable components
- Automated deployment
- Repeatable process

## Module 3: Deploying your first Terraform configuration.

**The Terraform Commands**

- `terraform init` - Initializes to terraform configs by looking in the current directory for terraform config files.
- `terraform plan` - Saves the current configs to a file to deploy later if needed.
- `terraform apply` - applies the current config to put them into motion.
- `terraform destroy` - Destroys the current terraform config. This does not delete the files just what was deployed.

**Example of Terraform Provider Config**:

```tf

terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

# Configure the GitHub Provider
provider "github" {
      token = var.GITHUB_TOKEN # or `GITHUB_TOKEN`
}
```



