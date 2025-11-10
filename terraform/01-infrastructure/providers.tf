terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.50.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.7.2"
    }
  }
  #required_version = "~> 1.12"
}

provider "azurerm" {
  features {

  }
}