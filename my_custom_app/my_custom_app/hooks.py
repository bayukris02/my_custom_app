app_name = "my_custom_app"
app_title = "My Custom App"
app_publisher = "Bayu Krisna"
app_description = "Custom app for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bayukrisna02@example.com"
app_license = "MIT"

doc_events = {
    "Sales Order": {
        "validate": "my_custom_app.sales_order.validate"
    },
    "Purchase Order": {
        "validate": "my_custom_app.purchase_order.validate"
    }
}
