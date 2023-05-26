#!/usr/bin/env python

import argparse
import grfd
import inquirer


def main():
    parser = argparse.ArgumentParser(description='Your CLI Tool Description')

    # Config Operation
    parser.add_argument('-v', '--version', action='store_true', help='Display the version of this program')
    parser.add_argument('-hi', '--hello', action='store_true', help='List all my buckets')

    # Display Operation
    parser.add_argument('-ls', '--list', help='List items. Supported: bucket, sp')
    parser.add_argument('-mkbkt', '--makebucket', help='Create a greenfield bucket')
    parser.add_argument('-rmbkt', '--removebucket', help='Remove a greenfield bucket')
    parser.add_argument('-show', '--showfiles', help='List bucket files')

    # FILE Operation
    parser.add_argument('-u', '--updatefile', help='Add file to bucket')
    parser.add_argument('-rm', '--removefile', help='Remove file to bucket')

    parser.add_argument('-key', '--keystore', action='store_true', help='Create keystore')

    # Add more arguments as needed
    args = parser.parse_args()
    
    # Access the values of the arguments
    if args.makebucket:
        grfd.create_grfd_bucket(args.makebucket)
    if args.removebucket:
        print(grfd.remove_bucket(args.removebucket))
    if args.showfiles:
        print(grfd.display_bucket_items(args.showfiles))
    if args.version:
        print("v0.9.1")
    if args.list:
        if args.list == "bucket":
            print(grfd.list_buckets())
        if args.list == "sp":
            print(grfd.get_service_providers())
    if args.keystore:
        grfd.check_grfd_credential()
    if args.hello:
        print("Hello, world!!")
    if args.updatefile:
        inputbucket = input("bucket : ")
        print(grfd.upload_flean_file(inputbucket, args.updatefile))
    if args.removefile:
        inputbucket = input("bucket : ")
        print(grfd.rem_flean_file(inputbucket, args.removefile))
    
    #gnfd-cmd bucket create gnfd://gnfd-bucket

if __name__ == '__main__':
    main()