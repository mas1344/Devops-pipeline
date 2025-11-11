variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "swedencentral"
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "docker_image" {
  description = "Docker image name"
  type        = string
  default     = "katrinrylander/crypto-dashboard"
}

variable "docker_image_tag" {
  description = "Docker image tag"
  type        = string
  default     = "latest"
}

variable "coinmarketcap_api_key" {
  description = "CoinMarketCap API Key"
  type        = string
  sensitive   = true
}

variable "coinmarketcap_symbols" {
  description = "Cryptocurrency symbols to track"
  type        = string
  default     = "BTC"
}

variable "update_freq_sec" {
  description = "Update frequency in seconds"
  type        = string
  default     = "60"
}

variable "azure_subscription_id" {
  description = "Azure subscription ID"
  type        = string
  sensitive   = true
}