app_name = "xscore_management"
app_title = "Xscore Management"
app_publisher = "Xscore Management"
app_description = "Xscore Management"
app_email = "nam.tong@xscore.me"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/xscore_management/css/xscore_management.css"
# app_include_js = "/assets/xscore_management/js/xscore_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/xscore_management/css/xscore_management.css"
# web_include_js = "/assets/xscore_management/js/xscore_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "xscore_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "xscore_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "xscore_management.utils.jinja_methods",
# 	"filters": "xscore_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "xscore_management.install.before_install"
# after_install = "xscore_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "xscore_management.uninstall.before_uninstall"
# after_uninstall = "xscore_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "xscore_management.utils.before_app_install"
# after_app_install = "xscore_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "xscore_management.utils.before_app_uninstall"
# after_app_uninstall = "xscore_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "xscore_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"xscore_management.tasks.all"
# 	],
# 	"daily": [
# 		"xscore_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"xscore_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"xscore_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"xscore_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "xscore_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "xscore_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "xscore_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["xscore_management.utils.before_request"]
# after_request = ["xscore_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["xscore_management.utils.before_job"]
# after_job = ["xscore_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"xscore_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

app_include_css = "/assets/xscore_management/css/core.css"

# fixtures = [
#     'DocType'
# ]

# fixtures = [
#     'Print Settings'
# ]

fixtures = [
    # "Address Template",
    # "Email Template",
    # "Payment Reconciliation",
    # "Notification",
    # "Notification Recipient",
    # "Print Settings",
    # "Language",
    # "Web Form",
    # "Web Form Field",
    # "Email Account",
    # "Item Attribute",
    # "Item Attribute Value",
    # "Manufacturing Settings",
    # "Mode of Payment Account",
    # "DocShare",
    # "Website Theme",
    # "Offer Term",
    # "Email Unsubscribe",
    # "Block Module",
    # "Employee Attendance Tool",
    # "Email Domain",
    # "Portal Menu Item",
    # "Portal Settings",
    # "Homepage",
    # "Salary Component",
    # "Bulk Update",
    # "OAuth Provider Settings",
    # "Lead Source",
    # "Dropbox Settings",
    # "LDAP Settings",
    # "Party Type",
    # "Custom DocPerm",
    # "Role Permission for Page and Report",
    # "Support Settings",
    # "Gender",
    # "Salutation",
    # "Domain",
    # "Domain Settings",
    # "Supplier Scorecard Variable",
    # "Supplier Scorecard Standing",
    # "Project Type",
    # "Print Style",
    # "POS Settings",
    # "Opening Invoice Creation Tool",
    # "Item Variant Settings",
    # "Role Profile",
    # "S3 Backup Settings",
    # "Activity Log",
    # "Opportunity Type",
    # "Share Type",
    # "Projects Settings",
    # "Subscription Settings",
    # "Data Export",
    # "Success Action",
    # "UOM Category",
    # "UOM Conversion Factor",
    # "Sales Partner Type",
    # "Job Applicant Source",
    # "Energy Point Rule",
    # "QuickBooks Migrator",
    # "Delivery Settings",
    # "Sales Stage",
    # "Market Segment",
    # "Route History",
    # "Plaid Settings",
    # "Dashboard Chart",
    # "Dashboard",
    # "Chart of Accounts Importer",
    # "Dashboard Chart Source",
    # "Comment",
    # "Dashboard Chart Link",
    # "Stock Entry Type",
    # "Energy Point Settings",
    # "Issue Priority",
    # "Warehouse Type",
    # "Google Settings",
    # "Session Default",
    # "Session Default Settings",
    # "Contact Email",
    # "Google Drive",
    # "Appointment Booking Settings",
    # "Global Search Settings",
    # "Quick Stock Balance",
    # "Notification Settings",
    # "Global Search DocType",
    # "Scheduled Job Type",
    # "Scheduled Job Log",
    # "DocType Action",
    # "DocType Link",
    # "Workspace Chart",
    # "Workspace Shortcut",
    # "Workspace",
    # "Dashboard Chart Field",
    # "Dashboard Settings",
    # "Onboarding Step",
    # "Number Card",
    # "Web Template Field",
    # "Web Template",
    # "Number Card Link",
    # "Module Onboarding",
    # "Onboarding Step Map",
    # "Onboarding Permission",
    # "Installed Application",
    # "Installed Applications",
    # "Payroll Settings",
    # "Navbar Item",
    # "Navbar Settings",
    # "Video Settings",
    # "System Console",
    # "Log Settings",
    # "Workspace Link",
    # "Bank Reconciliation Tool",
    # "Form Tour",
    # "Form Tour Step",
    # "DocType State",
    # "Currency Exchange Settings Details",
    # "Currency Exchange Settings Result",
    # "CRM Settings",
    # "Stock Reposting Settings",
    # "System Settings",
    # "Currency Exchange Settings",
    # "Variant Field",
    # "Workspace Quick List",
    # "Document Naming Settings",
    # "Logs To Clear",
    # "Incoterm",
    # "Workspace Number Card",
    # "RQ Job",
    # "Vehicle Service Item",
    # "Audit Trail",
    # "Bisect Accounting Statements",
    # "Process Subscription",
    # "Repost Accounting Ledger Settings",
    # "Permission Inspector",
    # "Push Notification Settings",
    # "Bulk Salary Structure Assignment",
    # "Shift Assignment Tool",
    # "Ledger Health Monitor",
    # "System Health Report",
    # "Test",
    # "Expense Claim Type",
    # "Industry Type",
    # "Authorization Control",
    # "Rename Tool",
    # "Mode of Payment",
    # "BOM Update Tool",
    # "File",
    # "Page",
    # "Website Script",
    # "Workflow State",
    # "Workflow Action Master",
    # "Role",
    # "Module Def",
    # "Property Setter",
    # "Bank Clearance",
    # "Designation",
    # "Employment Type",
    # "Leave Control Panel",
    # "SMS Center",
    # "Customer Group",
    # "UOM",
    # "Territory",
    # "SMS Settings",
    # "Sales Person",
    # "Print Heading",
    # "Supplier Group",
    # "Contact",
    # "Patch Log",
    # "Country",
    # "Fiscal Year",
    # "Print Format",
    # "Cost Center",
    # "Upload Attendance",
    # "Price List",
    # "Currency",
    # "Customize Form",
    # "Account",
    # "Department",
    # "Leave Type",
    # "Contact Us Settings",
    # "DefaultValue",
    # "DocPerm",
    # "DocField",
    # "Has Role",
    # "Activity Type",
    # "Report",
    # "Blog Settings",
    # "About Us Settings",
    # "Item Group",
    # "Website Settings",
    # "Global Defaults",
    # "Accounts Settings",
    # "Stock Settings",
    # "Selling Settings",
    # "Buying Settings",
    # "HR Settings",
    # "Version",
    # "Company",
    # "Warehouse",
    # "Custom Field",

    # "DocType",
    # "User Type",
    # "User Document Type",
    # "User Select Document Type",
    # "User Type Module",
    # "User Social Login",
    # "User"
]
