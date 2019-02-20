import collections
from urllib.parse import urlencode
import hashlib, hmac
import base64
import argparse
import sys
import json


def generate_signature(data, merchant_api_key=None):
    od = collections.OrderedDict(sorted(data.items()))
    try:
        pop_signature = od.pop('signature')
    except KeyError:
        print("No signature in data, good.")
    qs = urlencode(od)
    api_key = merchant_api_key
    api_key_binary = api_key.encode("ascii")
    qs_binary = qs.encode("ascii")
    hmac_data = hmac.new(api_key_binary, qs_binary, hashlib.sha512).digest()
    signature_binary = base64.b64encode(hmac_data)
    signature = signature_binary.decode("ascii")
    print("QueryString is: {}".format(qs))
    return signature


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", type=str,
                        help="Merchant API key", default=None)
    args = parser.parse_args()
    content = sys.stdin.read()
    try:
        data = json.loads(content)
    except Exception as e:
        print("Could not parse JSON body")
        sys.exit(1)
    else:
        if args.api_key is None:
            print("Please provide the API Key")
            sys.exit(1)
        else:
            signature = generate_signature(data, merchant_api_key=args.api_key)
            print("Generated signature: {}".format(signature))