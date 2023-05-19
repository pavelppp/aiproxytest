Prerequisites:
* install serverless framework: https://www.serverless.com/framework/docs/getting-started
* install yq: https://github.com/mikefarah/yq (optional, only required to run invoke.sh)
* install aws cli: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

sls plugin install -n serverless-stack-output

sls plugin install -n serverless-python-requirements

aws s3api create-bucket --bucket aiproxytest --region us-east-2 --create-bucket-configuration LocationConstraint=us-east-2

sls deploy

chmod +x invoke.sh

./invoke.sh
OR
<lambda_url>/?key=value

response: {"key":"value"}
