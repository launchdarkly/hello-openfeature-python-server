from openfeature import api
from openfeature.evaluation_context import EvaluationContext
from ldclient import Config
from ld_openfeature import LaunchDarklyProvider
from os import getenv

sdk_key = getenv("LAUNCHDARKLY_SERVER_SDK", "")
flag_key = getenv("LAUNCHDARKLY_FLAG_KEY", "")

if sdk_key == "":
    print("*** Set the 'LAUNCHDARKLY_SERVER_SDK' environment variable before running this script")
    exit(1)
elif flag_key == "":
    print("*** Set the 'LAUNCHDARKLY_FLAG_KEY' environment variable before running this script")
    exit(1)

provider = LaunchDarklyProvider(Config(sdk_key))

api.set_provider(provider)
client = api.get_client()

# Set up the evaluation context. This context should appear on your LaunchDarkly
# contexts dashboard soon after you run the demo.
context = EvaluationContext("example-user-key", {"name": "Sandy"})

flag_value = client.get_boolean_value(flag_key, False, context)
print(f"*** Feature flag '{flag_key}' is {flag_value} for this context")
