# Generated by Django 5.1.2 on 2024-10-18 00:16

import django.db.models.deletion
import django_jsonform.models.fields
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_comment="Stores the unique title of the instance.",
                        help_text="Enter a unique title.",
                        max_length=255,
                        unique=True,
                        verbose_name="Title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        db_comment="Stores the URL-friendly slug derived from the title.",
                        help_text="URL-friendly slug from the title.",
                        max_length=255,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        db_comment="Stores a detailed description of the instance.",
                        help_text="Enter a detailed description of the item. This can include its purpose, characteristics, and any other relevant information.",
                        verbose_name="Description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories ",
                "db_table": "sage_invoice_cat",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_comment="Stores the unique title of the instance.",
                        help_text="Enter a unique title.",
                        max_length=255,
                        unique=True,
                        verbose_name="Title",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        db_comment="Stores the URL-friendly slug derived from the title.",
                        help_text="URL-friendly slug from the title.",
                        max_length=255,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "invoice_date",
                    models.DateField(
                        db_comment="Invoice date created",
                        help_text="The date when the invoice was created.",
                        verbose_name="Invoice Date",
                    ),
                ),
                (
                    "tracking_code",
                    models.CharField(
                        db_comment="Tracking code created",
                        help_text="Enter the first 3-4 characters of the tracking code. The full code will be auto-generated as <prefix> + <date> + <random number>.",
                        max_length=255,
                        verbose_name="Tracking Code",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "DRAFT"),
                            ("overdue", "OVERDUE"),
                            ("paid", "PAID"),
                            ("unpaid", "UNPAID"),
                        ],
                        db_comment="Current status of the invoice (Paid, Unpaid)",
                        help_text="The current status of the invoice (Paid, Unpaid).",
                        max_length=50,
                        verbose_name="Status",
                    ),
                ),
                (
                    "receipt",
                    models.BooleanField(
                        db_comment="Check if this invoice is a receipt",
                        default=False,
                        help_text="Is this a receipt or an invoice",
                        verbose_name="Receipt",
                    ),
                ),
                (
                    "notes",
                    django_jsonform.models.fields.JSONField(
                        blank=True,
                        db_comment="This field stores additional dynamic content in JSON format. ",
                        help_text="\n            You can add any number of custom fields dynamically,\n            such as'Terms & Conditions', 'Technology Tips', etc.\n            ",
                        null=True,
                        verbose_name="Notes",
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("USD", "US Dollar"),
                            ("EUR", "Euro"),
                            ("GBP", "British Pound"),
                            ("JPY", "Japanese Yen"),
                            ("AUD", "Australian Dollar"),
                            ("CAD", "Canadian Dollar"),
                            ("CHF", "Swiss Franc"),
                            ("CNY", "Chinese Yuan"),
                            ("INR", "Indian Rupee"),
                            ("RUB", "Russian Ruble"),
                            ("AED", "UAE Dirham"),
                            ("SAR", "Saudi Riyal"),
                            ("TRY", "Turkish Lira"),
                            ("BRL", "Brazilian Real"),
                            ("ZAR", "South African Rand"),
                            ("NZD", "New Zealand Dollar"),
                            ("KRW", "South Korean Won"),
                            ("SGD", "Singapore Dollar"),
                            ("MXN", "Mexican Peso"),
                            ("IRR", "Iranian Rial"),
                            ("TOMAN", "Iranian Toman"),
                            ("QAR", "Qatari Riyal"),
                            ("KWD", "Kuwaiti Dinar"),
                            ("BHD", "Bahraini Dinar"),
                            ("OMR", "Omani Rial"),
                            ("EGP", "Egyptian Pound"),
                        ],
                        db_comment="Which currency is this item ",
                        default="USD",
                        help_text="Currency of unit price",
                        max_length=10,
                        verbose_name="Currency",
                    ),
                ),
                (
                    "due_date",
                    models.DateField(
                        db_comment="Due date of the invoice",
                        help_text="The date by which the invoice should be paid.",
                        verbose_name="Due Date",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        db_comment="Logo displayed on the invoice",
                        help_text="The logo displayed on the invoice.",
                        null=True,
                        upload_to="invoices/logos/",
                        verbose_name="Logo",
                    ),
                ),
                (
                    "signature",
                    models.ImageField(
                        blank=True,
                        db_comment="Signature image for the invoice",
                        help_text="The signature image for the invoice.",
                        null=True,
                        upload_to="invoices/signatures/",
                        verbose_name="Signature",
                    ),
                ),
                (
                    "stamp",
                    models.ImageField(
                        blank=True,
                        db_comment="Stamp image for the invoice",
                        help_text="The stamp image for the invoice.",
                        null=True,
                        upload_to="invoices/stamps/",
                        verbose_name="Stamp",
                    ),
                ),
                (
                    "template_choice",
                    models.CharField(
                        choices=[
                            ("quotation_1", "quotation_1"),
                            ("quotation_2", "quotation_2"),
                            ("quotation_3", "quotation_3"),
                            ("quotation_4", "quotation_4"),
                            ("receipt1", "receipt1"),
                            ("receipt2", "receipt2"),
                            ("receipt3", "receipt3"),
                        ],
                        db_comment="Template choice for the invoice",
                        help_text="The template you want for your invoice",
                        max_length=20,
                        verbose_name="Template choice",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        db_comment="Category associated with this invoice",
                        help_text="The category associated with this invoice.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoices",
                        to="sage_invoice.category",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Invoice",
                "verbose_name_plural": "Invoices",
                "db_table": "sage_invoice",
                "permissions": [
                    ("mark_as_paid", "Grants mark invoices as paid"),
                    ("mark_as_unpaid", "Grants Can mark invoices as unpaid"),
                    ("apply_discount", "Grants apply discounts to invoices"),
                    ("reject_invoice", "Grants reject invoices"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Expense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subtotal",
                    models.DecimalField(
                        db_comment="Sum of all item totals in the invoice",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The sum of all item totals.",
                        max_digits=10,
                        verbose_name="Subtotal",
                    ),
                ),
                (
                    "tax_percentage",
                    models.DecimalField(
                        db_comment="The percentage of tax applied to the invoice",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The tax percentage applied to the invoice.",
                        max_digits=5,
                        verbose_name="Tax Percentage",
                    ),
                ),
                (
                    "discount_percentage",
                    models.DecimalField(
                        db_comment="The percentage of discount applied to the invoice",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The discount percentage applied to the invoice.",
                        max_digits=5,
                        verbose_name="Discount Percentage",
                    ),
                ),
                (
                    "concession_percentage",
                    models.DecimalField(
                        db_comment="The percentage of concession applied to the invoice",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The concession percentage applied to the invoice.",
                        max_digits=5,
                        verbose_name="Concession Percentage",
                    ),
                ),
                (
                    "tax_amount",
                    models.DecimalField(
                        db_comment="The total tax amount calculated based on the subtotal and tax percentage",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The calculated tax amount.",
                        max_digits=10,
                        verbose_name="Tax Amount",
                    ),
                ),
                (
                    "discount_amount",
                    models.DecimalField(
                        db_comment="The total discount amount calculated based on the subtotal and discount percentage",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The calculated discount amount.",
                        max_digits=10,
                        verbose_name="Discount Amount",
                    ),
                ),
                (
                    "concession_amount",
                    models.DecimalField(
                        db_comment="The total concession amount calculated based on the subtotal and discount percentage",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The calculated concession amount.",
                        max_digits=10,
                        verbose_name="Concession Amount",
                    ),
                ),
                (
                    "total_amount",
                    models.DecimalField(
                        db_comment="The final total amount after tax and discount are applied",
                        decimal_places=2,
                        default=Decimal("0.00"),
                        help_text="The final total after applying tax and discount.",
                        max_digits=10,
                        verbose_name="Total Amount",
                    ),
                ),
                (
                    "invoice",
                    models.OneToOneField(
                        db_comment="Reference to the associated invoice",
                        help_text="The invoice associated with this total.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expense",
                        to="sage_invoice.invoice",
                        verbose_name="Invoice",
                    ),
                ),
            ],
            options={
                "verbose_name": "Expense",
                "verbose_name_plural": "Expenses",
                "db_table": "sage_expense",
            },
        ),
        migrations.CreateModel(
            name="CustomerProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_comment="Customer name created",
                        help_text="The name of the customer.",
                        max_length=255,
                        verbose_name="Customer Name",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True,
                        db_comment="Company name associated with the customer, if applicable.",
                        help_text="The company name of the customer (optional).",
                        max_length=255,
                        null=True,
                        verbose_name="Company Name",
                    ),
                ),
                (
                    "billing_address",
                    django_jsonform.models.fields.JSONField(
                        blank=True,
                        db_comment="Stores billing address details such as street, city, state, postal code, and country.",
                        help_text="The full billing address of the customer.",
                        null=True,
                        verbose_name="Billing Address",
                    ),
                ),
                (
                    "shipping_address",
                    django_jsonform.models.fields.JSONField(
                        blank=True,
                        db_comment="Stores shipping address details if different from the billing address.",
                        help_text="The shipping address of the customer (optional).",
                        null=True,
                        verbose_name="Shipping Address",
                    ),
                ),
                (
                    "contact",
                    django_jsonform.models.fields.JSONField(
                        blank=True, null=True, verbose_name="Customer Contacts"
                    ),
                ),
                (
                    "invoice",
                    models.OneToOneField(
                        db_comment="Link to the customer profile associated with this invoice",
                        help_text="The customer profile linked to this invoice.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer",
                        to="sage_invoice.invoice",
                        verbose_name="Customer Profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Customer Profile",
                "verbose_name_plural": "Customer Profiles",
                "db_table": "sage_invoice_customer",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        db_comment="Description of the invoice item",
                        help_text="Description of the item.",
                        max_length=255,
                        verbose_name="Description",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        blank=True,
                        db_comment="The quantity of the invoice item",
                        help_text="The quantity of the item.",
                        null=True,
                        verbose_name="Quantity",
                    ),
                ),
                (
                    "measurement",
                    models.CharField(
                        blank=True,
                        db_comment="measurement gavin more info about the item quantity",
                        help_text="measurement of the quantity.",
                        max_length=255,
                        null=True,
                        verbose_name="measurement",
                    ),
                ),
                (
                    "unit_price",
                    models.DecimalField(
                        db_comment="The price per unit of the invoice item",
                        decimal_places=2,
                        help_text="The price per unit of the item.",
                        max_digits=10,
                        verbose_name="Unit Price",
                    ),
                ),
                (
                    "total_price",
                    models.DecimalField(
                        db_comment="The total price calculated as quantity * unit price",
                        decimal_places=2,
                        help_text="Auto Generated total price for this item (quantity * unit price).",
                        max_digits=10,
                        verbose_name="Total Price",
                    ),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        db_comment="The associated invoice for this item",
                        help_text="The invoice associated with this item.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="sage_invoice.invoice",
                        verbose_name="Invoice",
                    ),
                ),
            ],
            options={
                "verbose_name": "Item",
                "verbose_name_plural": "Items",
                "db_table": "sage_invoice_items",
            },
        ),
        migrations.CreateModel(
            name="Column",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "priority",
                    models.PositiveIntegerField(
                        db_comment="Priority of the column",
                        help_text="The priority associated with each custom column.",
                        verbose_name="Priority",
                    ),
                ),
                (
                    "column_name",
                    models.CharField(
                        db_comment="Name of the custom column",
                        help_text="The name of the custom column (e.g., 'Delivery Date', 'Warranty Period').",
                        max_length=255,
                        verbose_name="Column Name",
                    ),
                ),
                (
                    "value",
                    models.TextField(
                        db_comment="Value of the custom column",
                        help_text="The value for the custom column in the specific invoice.",
                        verbose_name="Value",
                    ),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        db_comment="invoice of the custom column",
                        help_text="The invoice associated with this custom column.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="columns",
                        to="sage_invoice.invoice",
                        verbose_name="Invoice",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        db_comment="item of the custom column",
                        help_text="The item associated with this custom column.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="columns",
                        to="sage_invoice.item",
                        verbose_name="Item",
                    ),
                ),
            ],
            options={
                "verbose_name": "Column",
                "verbose_name_plural": "Columns",
                "db_table": "sage_invoice_columns",
                "ordering": ["priority"],
            },
        ),
    ]
