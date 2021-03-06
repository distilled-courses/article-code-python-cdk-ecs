#!/usr/bin/env python3

from aws_cdk import core

from cdk_ecs_example.cdk_ecs_example_stack import CdkEcsExampleStack


app = core.App()
CdkEcsExampleStack(app, "cdk-ecs-example")

app.synth()
