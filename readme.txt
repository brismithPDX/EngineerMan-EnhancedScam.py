Purpose:
    This was created to expand on and improve the scam.py script used by Engineer-Man on youtube
     at https://www.youtube.com/watch?v=UtNYzv8gLbs

    The original scam.py script made for a awesome 5 minute programing challenge.
        However the code did not provide flexibility and produced passwords and emails easily filtered from
        the defenders data set. (in our context we are the attacker and the scammer is the defender) to resolve
        these issues we enhanced the script to produce scam-enhanced.py which does not have those limitations.

    Scam-enhanced.py provides commandline arguments to run in "youtube example" mode with only a name, email,
        uri, and field information. The script also supports enhanced mode where an additional password list can be
        provided. These enhancements make the data set much more random, harder to filter from actual submissions,
        and is now only vulnerable too IP filtering. A warning about IP filtering defenses and how to over come them
        is also provided in the code output during execution.


Example Use:

    # Run the same attack displayed on youtube but with the enhancements engaged.
    scam-enhanced.py -H "http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php"
        -P "kjauysd6sAJSDhyui2yasd" -U "auid2yjauysd2uasdasdasd" -n "names.json" -e "email-providers.json"
        -l "rockyou_1k.json" --verbose

    # Run the youtube attack with out the enhancements
    scam-enhanced.py -H "http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php"
        -P "kjauysd6sAJSDhyui2yasd" -U "auid2yjauysd2uasdasdasd" -n "names.json" -e "email-providers.json"
        --verbose

Help output Example:
    Usage: python scam-enhanced.py -H <target host URI> -P <target password field>
    -U <target username field> -n <list of names>
    -e <list of email providers> -l <list of passwords to use>
    -v <verbose mode>

    Options:
      -h, --help            show this help message and exit
      -H TARGET_URI, --host=TARGET_URI
                            [required] specify target host URI used for the
                            request
      -P TARGET_PASSWORD_FIELD, --pass=TARGET_PASSWORD_FIELD
                            [required] specify the name of the target password
                            field in the request
      -U TARGET_USERNAME_FIELD, --user=TARGET_USERNAME_FIELD
                            [required] specify the name of the target user name
                            field in the request
      -n NAME_LIST, --name=NAME_LIST
                            specify the .json file containing names for email
                            generation
      -e EMAIL_LIST, --email=EMAIL_LIST
                            specify the .json file containing email provider
                            domains in `"[name].[tld]`" format
      -l PASSWORD_LIST, --list=PASSWORD_LIST
                            specify the .json file containing passwords for use in
                            the attack, (rockyou_1k.json) is best
      -v, --verbose         enable verbose mode


Possible Improvements:
    1) allow for unlimited running mode. in such a mode code execution would continue indefinitely
        continuing to pick names, email providers, and passwords in random order until stopped.

    2) configure multi-threading to not to increase the rate of attack (which may be blocked by an IDS or you local ISP)
        but to instead allow the use of multiple name, email provider, and password lists each distributed to an
        individual thread. This would increase the complexity of sent data making it harder still for the defender to
        filter out the hostile data.

    3) modify the email provider list to include duplicate entries such that the distribution of each provider is
        proportional to the market share occupied by each provider. currently all email providers are chosen
        pseudo-equally which could create an artifact that can be used for filtering by the attacker.