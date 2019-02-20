## Signature tool

This tools can be used to calculate signature for REST API requests. The basic usage is very simple: write the body of your request in a file and supply it as STDIN for gen_signature.py.
The --api-key option is the API key value supplied by your provider.

## Signature algorithm

1.	Sort all the key:value pairs of the request based on the key, in alphabetic order
2.	Generate a query string based on the sorted dictionary resulted from step 1
3.	Encode the query string from step 2 in binary format using ASCII encoding
4.	Calculate a HMAC based on the API key and the binary query string from step 3
5.	Encode the resulting HMAC (which is binary) in base64 format
6.	The base64 representation as ASCII is the signature of the request

Check generate_signature function for the actual implementation

## Example usage

```bash

(p3-venv) Alexandrus-MacBook-Pro:signature-tool alexandru.bujor$ cat /tmp/request 
{
    "payout_type": "papara",
    "full_name": "Customer Name",
    "account": "",
    "amount": "100.00",
    "currency": "TRY",
    "customer_email": "",
    "external_payout_id": "X1214323",
    "signature": "NG8OkVT0FU8+9YRnEsZjpYsQpFlBXPZn87p7gKdN6RQIypa+Xkzc9VS8BmO44TR2xgMbteuSz0leDBtiwHojew==",
    "redirect_complete_url": "https://myweb.con/complete.html",
    "redirect_cancel_url": "https://myweb.com/cancel.html"
}
(p3-venv) Alexandrus-MacBook-Pro:signature-tool alexandru.bujor$ python ./gen_signature.py --api-key "13214342" < /tmp/request
QueryString is: account=&amount=100.00&currency=TRY&customer_email=&external_payout_id=X1214323&full_name=Customer+Name&payout_type=papara&redirect_cancel_url=https%3A%2F%2Fmyweb.com%2Fcancel.html&redirect_complete_url=https%3A%2F%2Fmyweb.con%2Fcomplete.html
Generated signature: g7CnllTQda2snSUlPpdUH2iQfqDUaWNF+uWuvqPGjzC9dJcWH38skjjN3bfsZDvdBW7/tgobG613AlwJl+4JrQ==
```

