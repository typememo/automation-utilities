#!/usr/bin/env python

import json
import os
import re

import gmail

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# File's path
HOME = os.path.expandvars("$HOME")
CWD = os.path.abspath(".")
TOKEN_FILE = CWD + "/token.pickle"
CREDS_FILE = CWD + "/credentials.json"
MANUSCRIPT_FILE = HOME + \
    "/typememo/blog/content/posts/life/paleo-channel-blogposts/manuscript.md"


def get_blogpost_url(message):
    """Get blogpost url."""
    body = gmail.decode(gmail.get_message_body(message))
    url_list = re.findall("http.*://ch.nicovideo.jp/article/.*", body)
    url = url_list[0].strip("\r")
    return url


def get_blogpost_subject(message):
    """Get blogpost subject."""
    subject = gmail.get_message_subject(message)
    return subject


def is_included(file, str):
    """Flag"""
    with open(file, "r") as file:
        lines = file.readlines()
    for line in lines:
        if (str in line):
            return True
    return False


def add_blogpost(manuscript, subject, url):
    """Add blogpost to manuscript"""
    line_number = 0
    with open(manuscript, "r") as file:
        lines = file.readlines()
    for line in lines:
        if ("## ブロマガ全集" in line):
            lines.insert(line_number + 2, f"- [{subject}]({url})\n")
            with open(manuscript, "w") as file:
                file.writelines(lines)
            print("Add:", subject)
            return 0
        line_number += 1


def main():
    """Update paleo channel blogposts."""

    # Pick files
    token_file = os.path.abspath(TOKEN_FILE)
    creds_file = os.path.abspath(CREDS_FILE)
    manuscript_file = os.path.abspath(MANUSCRIPT_FILE)

    # Authorize Gmail API
    creds = gmail.authorize(SCOPES, token_file, creds_file)

    # Build Gmail API
    service = gmail.build_service(creds)

    # Get messages list
    msgs = gmail.get_messages(service,
                              userid="me",
                              query="from:鈴木祐",
                              )

    # Add blogpost link
    for msg in reversed(msgs):
        msg_ = gmail.get_message(service, msg)
        blogpost_subject = get_blogpost_subject(msg_)
        blogpost_url = get_blogpost_url(msg_)
        if not is_included(manuscript_file, blogpost_url):
            add_blogpost(manuscript_file, blogpost_subject, blogpost_url)
    print("FINISHED: Update paleo channel blogposts.")


# MAIN
if __name__ == '__main__':
    main()
