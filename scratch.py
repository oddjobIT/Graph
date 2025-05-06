import msal
import config
import json
import requests

app = msal.ConfidentialClientApplication(
    config.list_clientId,
    authority=config.authority,  # For Entra ID or External ID,
    #oidc_authority=config.oidc_authority,  # For External ID with custom domain
    client_credential=config.list_clientSecret,
    # token_cache=...  # Default cache is in memory only.
                       # You can learn how to use SerializableTokenCache from
                       # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
    )

result = app.acquire_token_silent(config.scope, account=None)

result = app.acquire_token_for_client(scopes=config.scope)


graph_data = requests.get(config.list_endpoint, headers={'Authorization': 'Bearer ' + result['access_token']}, ).json()



request_body = Invitation(invited_user_email_address = "boo@who.com",)

result = await graph_client.invitations.post(request_body)
