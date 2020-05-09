# Quickstart
1. Install requirements (Unavaliable Now)   
cd to current path and run `pip install -r requirement.txt`

2. Set up env var   
In linux
```bash
export AZURE_TENANT_ID=""
export AZURE_CLIENT_ID=""
export AZURE_CLIENT_SECRET=""
export SUBSCRIPTION_ID=""
```
About how to create app registration, see here: https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app

3. Start sample
```bash
python create_a_namespace.py
python create_an_eventhub.py
```