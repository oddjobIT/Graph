import asyncio
import config
import requests
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
import msal

tenant_id = config.tenantId
client_id = config.list_clientId
client_secret = config.list_clientSecret

async def get_users(query_params, app_client):
    cont = 'a'
    myUsers = []
    request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(query_parameters=query_params)
    print(f"request_config = {request_config }")
    users = await app_client.users.get(request_configuration=request_config)
    for u in users.value:
        print(f"\nUser = {u}\n")
        aUser = {}
        print(users.value[0].display_name)
        print(users.value[0].mail)
        print(users.value[0].user_type)
        print(users.value[0].account_enabled)
        aUser['display_name'] = u.display_name
        aUser['mail'] = u.mail
        aUser['user_type'] = u.user_type
        aUser['account_enabled'] = u.account_enabled
        print(aUser)
        myUsers.append(aUser)
    cont = users.odata_next_link
    print(f"More data URL = {cont}")
    #users = await app_client.users.get(cont)
    #users = requests.get(cont)
    #print(users)
    #while cont != None:
    #    users = requests.get(cont)
    #    print(users)
    #    for u in users.value:
    #        aUser = {}
    #        print(users.value[0].display_name)
    #        print(users.value[0].mail)
    #        print(users.value[0].user_type)
    #        print(users.value[0].account_enabled)
    #        aUser['display_name'] = u.display_name
    #        aUser['mail'] = u.mail
    #        aUser['user_type'] = u.user_type
    #        aUser['account_enabled'] = u.account_enabled
    #        print(aUser)
    #        myUsers.append(aUser)
    print(myUsers)

async def main():
    #create an API session
    client_credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    app_client = GraphServiceClient(client_credential)

    query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(select = ['displayName', 'id', 'mail','userType','accountEnabled'],orderby= ['displayName'])
    print(f"query_params = {query_params}")
    #request_config = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(query_parameters=query_params)
    #users = app_client.users.get(request_configuration=request_config)
    await get_users(query_params,app_client)

asyncio.run(main())