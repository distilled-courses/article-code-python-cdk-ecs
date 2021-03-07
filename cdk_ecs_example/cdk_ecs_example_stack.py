import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
from aws_cdk import core


class CdkEcsExampleStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc = ec2.Vpc(self, "EcsVpc", max_azs=2, nat_gateways=0)
        vpc.add_s3_endpoint('S3Endpoint')
        vpc.add_interface_endpoint('EcrDockerEndpoint', service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER)
        vpc.add_interface_endpoint('EcrEndpoint', service=ec2.InterfaceVpcEndpointAwsService.ECR)
        vpc.add_interface_endpoint('CloudWatchLogsEndpoint', service=ec2.InterfaceVpcEndpointAwsService.CLOUDWATCH_LOGS)
        ecs.Cluster(self, "EcsCluster", vpc=vpc)
