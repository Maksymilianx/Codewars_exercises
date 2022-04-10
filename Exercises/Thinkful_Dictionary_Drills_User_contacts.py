"""
Task: Add None if person has not been assigned a number
and return it in dict
"""


def user_contacts(data):
    # my approach
    # [i.append(None) for i in data if len(i) == 1]
    # return dict(data)

    # another (imo better) approach
    return {
        contact[0]: contact[1] if len(contact) > 1 else None for contact in data  # noqa
    }
