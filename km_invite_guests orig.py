""" Reads csv with guest input data of form
    <DisplayName>, <Email>, <Manager>
    to list of lists
    
    Loops through lists of lists and creates Guest accounts
    Stores responses in <date>_<time>_GuestInvite.log"""

import asyncio
import config
import csv
import requests
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.models.invitation import Invitation
import msal

tenant_id = config.tenantId
client_id = config.create_clientId
client_secret = config.create_clientSecret


async def main():
    #create an API session
    client_credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    app_client = GraphServiceClient(client_credential)

    request_body = Invitation(invited_user_display_name = 'Boo Ghost',invited_user_email_address = "boo@who.com",invite_redirect_url = "https://myapp.who.com", )
    print(f"\nrequest_body = {request_body}")
    #request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(query_parameters=query_params)
    #users = app_client.users.get(request_configuration=request_config)
    result = await app_client.invitations.post(request_body)
    print(f"\nResult = {result}")
asyncio.run(main())