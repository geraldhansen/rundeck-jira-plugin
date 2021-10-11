#!/usr/bin/env python3
''' The Rundeck JIRA plugin'''

import os

import urllib3
from jira import JIRA

urllib3.disable_warnings()

def get_jira_config():
    '''Read in config from Rundeck'''

    jira_config = {
        'url': None,
        'user': None,
        'pass': None,
        'issue': None,
        'link': None,
        'title': None
    }

    jira_config['issue'] = os.environ.get('RD_CONFIG_JIRATICKETID')
    jira_config['url'] = os.environ.get('RD_CONFIG_JIRAURL')
    jira_config['user'] = os.environ.get('RD_CONFIG_JIRAUSER')
    jira_config['pass'] = os.environ.get('RD_CONFIG_JIRAPASSWORD')
    if os.environ.get('RD_CONFIG_JIRARUNDECKLINK'):
        jira_config['link'] = os.environ.get('RD_CONFIG_JIRARUNDECKLINK')
    else:
        jira_config['link'] = (
            f"{os.environ.get('RD_JOB_SERVERURL')}/project/{os.environ.get('RD_JOB_PROJECT')}/"
            f"execution/show/{os.environ.get('RD_JOB_EXECID')}"
            )
    if os.environ.get('RD_CONFIG_JIRARUNDECKLINKTITLE'):
        jira_config['title'] = os.environ.get('RD_CONFIG_JIRARUNDECKLINKTITLE')
    else:
        jira_config['title'] = (
            f"Rundeck Project {os.environ.get('RD_JOB_PROJECT')} "
            f"{os.environ.get('RD_JOB_NAME')} Execution {os.environ.get('RD_JOB_EXECID')}")

    return jira_config

def add_link_to_issue():
    ''' add an external link to an issue'''

    config = get_jira_config()

    if config['issue']:
        jira = JIRA(options={'server':config['url'], 'verify':False},
                    basic_auth=(config['user'], config['pass']))
        issue = jira.issue(config['issue'])
        jira.add_simple_link(issue, {"url":config['link'],
                                     "title":config['title']})


def main():
    '''Main function'''
    add_link_to_issue()


if __name__ == '__main__':
    main()
