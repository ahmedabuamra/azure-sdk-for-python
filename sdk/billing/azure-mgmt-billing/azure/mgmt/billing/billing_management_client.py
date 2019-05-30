# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.billing_accounts_operations import BillingAccountsOperations
from .operations.payment_methods_operations import PaymentMethodsOperations
from .operations.billing_accounts_validate_address_operations import BillingAccountsValidateAddressOperations
from .operations.available_balances_operations import AvailableBalancesOperations
from .operations.billing_profiles_operations import BillingProfilesOperations
from .operations.invoice_sections_operations import InvoiceSectionsOperations
from .operations.departments_operations import DepartmentsOperations
from .operations.enrollment_accounts_operations import EnrollmentAccountsOperations
from .operations.invoices_operations import InvoicesOperations
from .operations.price_sheet_operations import PriceSheetOperations
from .operations.billing_subscriptions_operations import BillingSubscriptionsOperations
from .operations.products_operations import ProductsOperations
from .operations.transactions_operations import TransactionsOperations
from .operations.policies_operations import PoliciesOperations
from .operations.billing_property_operations import BillingPropertyOperations
from .operations.transfers_operations import TransfersOperations
from .operations.recipient_transfers_operations import RecipientTransfersOperations
from .operations.operations import Operations
from .operations.billing_permissions_operations import BillingPermissionsOperations
from .operations.billing_role_definitions_operations import BillingRoleDefinitionsOperations
from .operations.billing_role_assignments_operations import BillingRoleAssignmentsOperations
from .operations.agreements_operations import AgreementsOperations
from .operations.line_of_credits_operations import LineOfCreditsOperations
from . import models


class BillingManagementClientConfiguration(AzureConfiguration):
    """Configuration for BillingManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(BillingManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-billing/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class BillingManagementClient(SDKClient):
    """Billing client provides access to billing resources for Azure subscriptions.

    :ivar config: Configuration for client.
    :vartype config: BillingManagementClientConfiguration

    :ivar billing_accounts: BillingAccounts operations
    :vartype billing_accounts: azure.mgmt.billing.operations.BillingAccountsOperations
    :ivar payment_methods: PaymentMethods operations
    :vartype payment_methods: azure.mgmt.billing.operations.PaymentMethodsOperations
    :ivar billing_accounts_validate_address: BillingAccountsValidateAddress operations
    :vartype billing_accounts_validate_address: azure.mgmt.billing.operations.BillingAccountsValidateAddressOperations
    :ivar available_balances: AvailableBalances operations
    :vartype available_balances: azure.mgmt.billing.operations.AvailableBalancesOperations
    :ivar billing_profiles: BillingProfiles operations
    :vartype billing_profiles: azure.mgmt.billing.operations.BillingProfilesOperations
    :ivar invoice_sections: InvoiceSections operations
    :vartype invoice_sections: azure.mgmt.billing.operations.InvoiceSectionsOperations
    :ivar departments: Departments operations
    :vartype departments: azure.mgmt.billing.operations.DepartmentsOperations
    :ivar enrollment_accounts: EnrollmentAccounts operations
    :vartype enrollment_accounts: azure.mgmt.billing.operations.EnrollmentAccountsOperations
    :ivar invoices: Invoices operations
    :vartype invoices: azure.mgmt.billing.operations.InvoicesOperations
    :ivar price_sheet: PriceSheet operations
    :vartype price_sheet: azure.mgmt.billing.operations.PriceSheetOperations
    :ivar billing_subscriptions: BillingSubscriptions operations
    :vartype billing_subscriptions: azure.mgmt.billing.operations.BillingSubscriptionsOperations
    :ivar products: Products operations
    :vartype products: azure.mgmt.billing.operations.ProductsOperations
    :ivar transactions: Transactions operations
    :vartype transactions: azure.mgmt.billing.operations.TransactionsOperations
    :ivar policies: Policies operations
    :vartype policies: azure.mgmt.billing.operations.PoliciesOperations
    :ivar billing_property: BillingProperty operations
    :vartype billing_property: azure.mgmt.billing.operations.BillingPropertyOperations
    :ivar transfers: Transfers operations
    :vartype transfers: azure.mgmt.billing.operations.TransfersOperations
    :ivar recipient_transfers: RecipientTransfers operations
    :vartype recipient_transfers: azure.mgmt.billing.operations.RecipientTransfersOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.billing.operations.Operations
    :ivar billing_permissions: BillingPermissions operations
    :vartype billing_permissions: azure.mgmt.billing.operations.BillingPermissionsOperations
    :ivar billing_role_definitions: BillingRoleDefinitions operations
    :vartype billing_role_definitions: azure.mgmt.billing.operations.BillingRoleDefinitionsOperations
    :ivar billing_role_assignments: BillingRoleAssignments operations
    :vartype billing_role_assignments: azure.mgmt.billing.operations.BillingRoleAssignmentsOperations
    :ivar agreements: Agreements operations
    :vartype agreements: azure.mgmt.billing.operations.AgreementsOperations
    :ivar line_of_credits: LineOfCredits operations
    :vartype line_of_credits: azure.mgmt.billing.operations.LineOfCreditsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = BillingManagementClientConfiguration(credentials, subscription_id, base_url)
        super(BillingManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-11-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.billing_accounts = BillingAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.payment_methods = PaymentMethodsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_accounts_validate_address = BillingAccountsValidateAddressOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.available_balances = AvailableBalancesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_profiles = BillingProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.invoice_sections = InvoiceSectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.departments = DepartmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.enrollment_accounts = EnrollmentAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.invoices = InvoicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.price_sheet = PriceSheetOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_subscriptions = BillingSubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.products = ProductsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.transactions = TransactionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_property = BillingPropertyOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.transfers = TransfersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recipient_transfers = RecipientTransfersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_permissions = BillingPermissionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_role_definitions = BillingRoleDefinitionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.billing_role_assignments = BillingRoleAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.agreements = AgreementsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.line_of_credits = LineOfCreditsOperations(
            self._client, self.config, self._serialize, self._deserialize)