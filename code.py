import argparse
import grfd
import inquirer


def main():
    parser = argparse.ArgumentParser(description='Your CLI Tool Description')
    parser.add_argument('-f', '--file', help='Specify a file')
    parser.add_argument('-key', '--keystore', action='store_true', help='Create keystore')
    parser.add_argument('-v', '--version', action='store_true', help='Display the version of this program')
    parser.add_argument('-ls', '--list', action='store_true', help='List all my buckets')
    parser.add_argument('-sp', '--storageprovider', action='store_true', help='List all storage providers')
    parser.add_argument('-hi', '--hello', action='store_true', help='List all my buckets')
    parser.add_argument('-c', '--create', help='Create something')

    # Add more arguments as needed
    args = parser.parse_args()
    
    # Access the values of the arguments
    if args.file:
        print('File:', args.file)
    if args.version:
        print('v.1.0.3')
    if args.list:
        print(grfd.list_buckets())
    if args.keystore:
        grfd.check_grfd_credential()
    if args.storageprovider:
        print(grfd.get_service_providers())
    if args.hello:
        print("Hello, world!!")
    if args.create:
        if args.create == "bucket":
            questions = [
            inquirer.Text('bucketName',
                            message="Bucket name?",
                        ),
            ]
            answers = inquirer.prompt(questions)
            targetBucketName = answers['bucketName']
            grfd.create_grfd_bucket(targetBucketName)
        else:
            print("Invalid command")
    
    #gnfd-cmd bucket create gnfd://gnfd-bucket

if __name__ == '__main__':
    main()