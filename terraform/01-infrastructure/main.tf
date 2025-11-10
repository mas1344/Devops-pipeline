############################################################
# Resource Group
############################################################

# Create a resource group using the generated random name
resource "azurerm_resource_group" "crypto_rg" {
  name     = "rg-crypto-dashboard-${random_string.suffix.result}"
  location = var.location

  tags = {
    Environment = var.environment
    Project     = "crypto-dashboard"
    ManagedBy   = "terraform"
  }
}

############################################################
# App Service Plan
############################################################

resource "azurerm_service_plan" "crypto_asp" {
  name                = "asp-crypto-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.crypto_rg.name
  location            = azurerm_resource_group.crypto_rg.location
  os_type             = "Linux"
  sku_name           = "F1"  # Free tier for development

  tags = {
    Environment = var.environment
    Project     = "crypto-dashboard"
  }
}

############################################################
# Web App
############################################################

resource "azurerm_linux_web_app" "crypto_webapp" {
  name                = "app-crypto-dashboard-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.crypto_rg.name
  location            = azurerm_resource_group.crypto_rg.location
  service_plan_id     = azurerm_service_plan.crypto_asp.id

  site_config {
    always_on = false  # Required for Free tier
    
    application_stack {
      # CORRECT SYNTAX FOR DOCKER HUB IMAGES:
      docker_image_name = "${var.docker_image}:${var.docker_image_tag}"
    }
  }

  app_settings = {
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "WEBSITES_PORT"                       = "8501"  # Streamlit default port
    "COINMARKETCAP_API_KEY"              = var.coinmarketcap_api_key
    "COINMARKETCAP_SYMBOLS"              = var.coinmarketcap_symbols
    "UPDATE_FREQ_SEC"                    = var.update_freq_sec
  }

  tags = {
    Environment = var.environment
    Project     = "crypto-dashboard"
  }
}