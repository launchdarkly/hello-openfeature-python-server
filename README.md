# LaunchDarkly Sample OpenFeature Python Server application

[![Build and run](https://github.com/launchdarkly/hello-openfeature-python-server/actions/workflows/ci.yml/badge.svg)](https://github.com/launchdarkly/hello-openfeature-python-server/actions/workflows/ci.yml)

We've built a simple console script that demonstrates how LaunchDarkly's OpenFeature provider works.

## Build instructions

1. Install the project dependencies by running `poetry install`
2. Set the environment variable `LAUNCHDARKLY_SDK_KEY` to your LaunchDarkly SDK key.
3. Set the environment variable `LAUNCHDARKLY_FLAG_KEY` to the LaunchDarkly boolean flag key you wish to evaluate.
4. Run `poetry run python main.py`.

You should see the message `"Feature flag '<flag key>' is <True/False> for this context"`.
