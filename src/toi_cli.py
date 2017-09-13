#!/usr/bin/env python
import sys
import re
import json
import argparse
import pkg_resources  # part of setuptools

class TOI(object):

    TERRAFORM_OUTPUT_TERM = "Outputs:"

    def terraform_output_to_key_val(data):
      if type(data) is not dict:
        data = terraform_output_to_dict(data)
      output = ""
      for k,v in data.items():
        output += '%s = "%s"\n' % (k, v)
      return output

    def key_val_to_json(data):
      if data is not dict:
        data = terraform_output_to_dict(data)
      return json.dumps(data)

    def terraform_output_to_dict(data):
      outputs = dict()
      index_of_output = next((x for x in range(len(data)) if TERRAFORM_OUTPUT_TERM in data[x]), None)
      data = data[index_of_output+2:]
      for o in data:
        if o != TERRAFORM_OUTPUT_TERM:
            o = re.sub(r'[\x00-\x1F]+|\[0m', '', o)
            kv = o.strip().split("=", 1)
            outputs[kv[0].strip()] = kv[1].strip()
      return outputs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File input (result of terraform show or terraform apply)", type=str)
    parser.add_argument("-o", "--output", help="terraform (tfvars output) or packer (json)", type=str)
    parser.add_argument("-v", "--version", help="Version of toi", action='store_true')

    args = parser.parse_args()
    data = ""
    toi = TOI()

    if args.version:
        version = pkg_resources.require("toi")[0].version
        print(version)
        sys.exit(0)

    if args.file:
        data = os.read(args.file)
    else:
        data = sys.stdin.readlines()

    if 't' in args.output:
        print(toi.terraform_output_to_key_val(data))
    else:
        print(toi.key_val_to_json(data))
