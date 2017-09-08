# toi

Pronounced "toy" 

Terraform Output Input (toi)

A utility to convert terraform output to json or tfvars for interoperability between HashiCorp tools.

## Description

It's often necessary to chain terraform stacks together where output from one is used as input to another. For example, an AWS VPC terraform stack's output may be needed for an application stack so that it knows what subnets are available for autoscaling. There are many situations where this is useful in a layered architecture. 

toi was created to make this process easy. toi can transform terraform output into key value (tfvars) format or packer format (json).

## Usage

`terraform apply vpc | toi --output terraform &> generated-vpc.tfvars`

## Installation

`./setup.py install`

And then you can:

`toi --help`
