#!/usr/bin/env python3

import argparse
import urllib3
import sys
import json
import os


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser()
parser.add_argument(
    '-s', '--server', help="Artifactory server name that's going to be used", required=True)
parser.add_argument(
    '-u', '--user', help="Artifactory user name", required=True)
parser.add_argument(
    '-p', '--password', help="Artifactory user password", required=True)
parser.add_argument(
    '-a', '--action', help="Choose the action you want to perform", required=True)
args = parser.parse_args()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HTTP = urllib3.PoolManager()


# Creating args.json file with user's arguments
def create_conf(server, user, password):
    setting = {}
    setting["server"] = server
    setting["user"] = user
    setting["password"] = password
    with open('args.json', 'w+') as f:
        json.dump(setting,f)


# Reading user arguments from args.json file
def read_conf(key=False):
    with open("args.json", "r") as f:
        j = json.load(f)
    if key:
        return j[key]
    else:
        return j


def send_api_request(request_method, req_type="GET", data=""):
    j = read_conf()
    ACCESS_HEADER = urllib3.make_headers(
        basic_auth='%s:%s' % (j['user'], j["password"]))
    URL = 'https://%s%s' % (j["server"],
                            ".jfrog.io/artifactory/"+request_method)
    if req_type == "GET":
        headers_dict = ACCESS_HEADER
        response = HTTP.request(req_type, URL, headers=headers_dict, body=data)
    else:
        response = HTTP.request(req_type, URL, headers=ACCESS_HEADER)
    return response


def ping_request():
    create_conf(sys.argv[2], sys.argv[4], sys.argv[6])
    server = read_conf("server")
    request = "api/system/ping"
    response = send_api_request(request)
    if response.data == b'OK':
        print(f"Ping request for server '{server}' was : OK")
    else:
        print("ERROR: Failed to run PING request. Encountered error:\n %s" %
              (response.data.decode('utf-8')))


def version_request():
    create_conf(sys.argv[2], sys.argv[4], sys.argv[6])
    request = "api/system/version"
    response = send_api_request(request)
    if response.data:
        json_data = response.data
        json_object = json.loads(json_data)
        json_formatted_str = json.dumps(json_object["version"], indent=2)
        print("The Artifactory version is: " + json_formatted_str)
    else:
        print("ERROR: Failed to get version. Encountered error:\n %s" %
              (response.data.decode('utf-8')))


def storage_info_request():
    create_conf(sys.argv[2], sys.argv[4], sys.argv[6])
    request = "api/storageinfo"
    response = send_api_request(request)
    if response.data:
        json_data = response.data
        json_object = json.loads(json_data)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
    else:
        print("ERROR: Failed to get storage information. Encountered error:\n %s" %
              (response.data.decode('utf-8')))


def main():
    if not os.path.exists("args.json"):
        print("No configuration file found")
        create_conf()
    if args.action == 'ping':
        ping_request()
    elif args.action == 'version':
        version_request()
    elif args.action == 'storage_info':
        storage_info_request()
    else:
        print("ERROR: This is not working")


if __name__ == "__main__":
    main()
