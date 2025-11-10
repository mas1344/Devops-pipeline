output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.crypto_rg.name
}

output "web_app_name" {
  description = "Name of the web app"
  value       = azurerm_linux_web_app.crypto_webapp.name
}

output "web_app_url" {
  description = "URL of the deployed web app"
  value       = "https://${azurerm_linux_web_app.crypto_webapp.default_hostname}"
}

output "app_service_plan_name" {
  description = "Name of the app service plan"
  value       = azurerm_service_plan.crypto_asp.name
}

output "location" {
  description = "Azure region"
  value       = azurerm_resource_group.crypto_rg.location
}