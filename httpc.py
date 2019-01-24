import argparse


def help_output():
    output = '\nhttpc is a curl-like application but supports HTTP protocol only.\nUsage:\n\thttpc.py command [arguments]\n' + \
           'The commands are:\n\tget\texecutes a HTTP GET request and prints the response.\n\tpost\texecutes a HTTP' + \
           ' POST request and prints the response.\n\thelp\tprints this screen.\n\n' + \
           'Use "httpc help [command]" for more information about a command.'
    return output


def help_get_output():
    output = '\nusage: httpc get [-v] [-h key:value] URL\n\nGet executes a HTTP GET request for a given URL.\n\t-v\t' + \
               '\tPrints the detail of the response such as protocol, status, and headers.\n\t-h key:value\tAssociates ' \
               'headers to HTTP Request with the format "key:value".'
    return output


def help_post_output():
    output = '\nusage: httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL\n\nPost executes a HTTP POST ' \
                'request for a given URL with inline data or from file.\n\t-v\t\tPrints the detail of the response such ' \
                'as protocol, status, and headers.\n\t-h key:value\tAssociates headers to HTTP Request with the format ' \
                '"key:value".\n\t-d string\tAssociates an inline data to the body HTTP POST request.\n\t-f file\t\t' \
                'Associates the content of a file to the body HTTP POST request.\n\nEither [-d] or [-f] can be used ' \
                'but not both.'
    return output


parser = argparse.ArgumentParser(description='httpc is a curl-like application but supports HTTP protocol only.')
parser.add_argument('command', type=str, help=help_output())
parser.add_argument('-gh', '--gethelp', help=help_get_output(), action="store_true")
parser.add_argument('-ph', '--posthelp', help=help_post_output(), action="store_true")
args = parser.parse_args()

if args.command == 'help':
    if args.gethelp:
        print(help_get_output())
    elif args.posthelp:
        print(help_post_output())
    else:
        print(help_output())

elif args.command == 'get':
    print('in get')

elif args.command == 'post':
    print('in post')
