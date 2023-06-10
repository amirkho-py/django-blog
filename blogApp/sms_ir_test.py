from sms_ir import SmsIr
from random import randint


# SMS IR CONFIG
sms_ir = SmsIr(
    api_key="8Ca4PBnyrDH6t9mQapjjB8eFsU8z6iBxEg0ExI33uaJl6hnlfyvePAKzSwd7XDkt",
    linenumber=30007732011199
)


# SEND VERIFY CODE
sms_ir.send_verify_code(
    number="9218895185",
    template_id=830439,
    parameters=[
        {
            "name" : "CODE",
            "value": str(randint(1000, 9999)),
        },
    ],
)

