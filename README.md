# greenfield-viewer-cli

greenfield-viewer-cli helps you to use BNB-Greenfield

# Documentation

[Documentation](https://coo-cooing.gitbook.io/greenfield-viewer-cli/)

# Commands

## Display the version of this program

```bash
python gvc.py -v
```

## Display the version of this program

```bash
python gvc.py -v
```

This command will display the version of the program when executed.

You can follow a similar format to document the other command-line arguments:

## List all my buckets

```bash
python gvc.py -hi
```

This command will list all the buckets associated with the program.

## List items. Supported: bucket, sp

```bash
python gvc.py -ls bucket
```

This command will list the available buckets.

## Create a greenfield bucket

```bash
python gvc.py -mkbkt <bucket_name>
```

This command will create a new greenfield bucket with the specified name.

## Remove a greenfield bucket

```bash
python gvc.py -rmbkt <bucket_name>
```

This command will remove the specified greenfield bucket.

## List bucket files

```bash
python gvc.py -show <bucket_name>
```

This command will list the files in the specified bucket.

## Specify a file and add it

```bash
python gvc.py -mkf <file_path>
```

This command will add the specified file to the program.

## Specify a file and delete it

```bash
python gvc.py -rmf <file_path>
```

This command will delete the specified file from the program.

## Create keystore

```bash
python gvc.py -key
```

This command will create a keystore.

# Prerequisite

Python 3.X

# Installation

Clone this repository to your local machine.

```bash
git clone https://github.com/JisongImSorry/greenfield-viewer-cli.git
```

Navigate to the project directory.

```bash
cd greenfield-viewer-cli
```

Install the necessary packages using pip. Please ensure that you are running an appropriate version of Python for these packages.

```bash
pip install -r requirements.txt
```

# Usage

Once you have installed all the necessary packages, you can begin using EZMigrate to facilitate your data transfer needs.

```bash
python main.py
```

# Configuration

Prior to running, it is crucial to set up the correct configuration.

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# License

Please see the LICENSE file for details on our code availability.
