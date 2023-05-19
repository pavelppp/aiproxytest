Prerequisites:
* install serverless framework: https://www.serverless.com/framework/docs/getting-started
* install yq: https://github.com/mikefarah/yq (optional, only required to run invoke.sh)

sls plugin install -n serverless-stack-output

sls plugin install -n serverless-python-requirements

sls deploy

chmod +x invoke.sh

./invoke.sh

response: {"key":"value"}
