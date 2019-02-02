import argparse
from sys import exit
import http
from urllib3 import util


def help_output():
    output = '\nhttpc is a curl-like application but supports HTTP protocol only.\nUsage:\n\thttpc.py command ' \
             '[arguments]\nThe commands are:\n\tget\texecutes a HTTP GET request and prints the response.\n\tpost\t' \
             'executes a HTTP POST request and prints the response.\n\thelp\tprints this screen.\n\n' \
             'Use "httpc help [command]" for more information about a command.'
    return output


def help_get_output():
    output = '\nusage: httpc get [-v] [-h key:value] URL\n\nGet executes a HTTP GET request for a given URL.\n\t-v' \
             '\t\tPrints the detail of the response such as protocol, status, and headers.\n\t-h key:value\t' \
             'Associates headers to HTTP Request with the format "key:value".'
    return output


def help_post_output():
    output = '\nusage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL\n\nPost executes a HTTP ' \
             'POST request for a given URL with inline data or from file.\n\t-v\t\tPrints the detail of the ' \
             'response such as protocol, status, and headers.\n\t-h key:value\tAssociates headers to HTTP Request ' \
             'with the format "key:value".\n\t-d string\tAssociates an inline data to the body HTTP POST request.' \
             '\n\t-f file\t\tAssociates the content of a file to the body HTTP POST request.\n\nEither [-d] or [-f] ' \
             'can be used but not both.'
    return output


def help_command():
    if args.arg2 == 'get':
        print(help_get_output())
    elif args.arg2 == 'post':
        print(help_post_output())
    else:
        if not args.arg2:
            print(help_output())
        else:
            print("Error: Unknown second argument. Options are 'get' or 'post' after 'help'")


def get_request(url, v, h):
    """Get executes a HTTP GET request for a given URL."""
    conn = http.client.HTTPConnection(util.parse_url(url).host)

    # Stores the headers received from the command line in a dictionary
    # flat_h = [item for i in h for item in i.split(":")]
    # headers = dict(zip(*[iter(flat_h)] * 2))

    conn.request("GET", url)
    response = conn.getresponse()

    if v:
        print(response.version, response.status, response.reason)
        print(response.headers)
        print(response.read().decode('utf-8'))
    else:
        print(response.read().decode('utf-8'))

    conn.close()


def post_request(url, v, h, d, f):
    """Post executes a HTTP POST request for a given URL with inline data or from
    file."""
    conn = http.client.HTTPConnection(util.parse_url(url).host)

    # Stores the headers received from the command line in a dictionary
    # flat_h = [item for i in h for item in i.split(":")]
    # headers = dict(zip(*[iter(flat_h)] * 2))

    body = None

    if d and not f:
        body = d
    elif not d and f:
        body = f.read()

    conn.request("POST", url, body=body)
    response = conn.getresponse()

    if v:
        print(response.version, response.status, response.reason)
        print(response.headers)
        print(response.read().decode('utf-8'))
    else:
        print(response.read().decode('utf-8'))

    conn.close()


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('command', type=str, help=help_output(), choices=['help', 'get', 'post'])
parser.add_argument('arg2', nargs='?', type=str)
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-h', '--header')
parser.add_argument('-d', '--data')
parser.add_argument('-f', '--file')
args = parser.parse_args()

print(args)

if args.command == 'help':
    help_command()

elif args.command == 'get':
    if args.data or args.file:
        print('Error: -d (--data) or -f (--file) are not accepted arguments for the "get" command.')
        exit()
    elif args.arg2:
        url2 = args.arg2.replace("'", "")
        print(args.header)
        get_request(url2, args.verbose, args.header)
    else:
        print('Error: no URL has been specified. URL is required after the "get"')
        exit()

elif args.command == 'post':
    post_request(args.arg2, args.verbose, args.header, args.data, args.file)
