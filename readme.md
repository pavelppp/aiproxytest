Prerequisites:
* install serverless framework: https://www.serverless.com/framework/docs/getting-started
* install yq: https://github.com/mikefarah/yq
* install aws cli: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

sls plugin install -n serverless-stack-output

sls plugin install -n serverless-python-requirements

set unique bucket name in serverless.yml in .deploymentBucket.name

aws s3api create-bucket --bucket $(yq .deploymentBucket.name) --region $(yq .provider.region serverless.yml) --create-bucket-configuration LocationConstraint=$(yq .provider.region serverless.yml)
(bucket name must be unique, update name in serverless.yml and repeat if already taken)

sls deploy

chmod +x invoke.sh

./invoke.sh

response: {"key":"value"}
