import configparser

from behave import *
import requests

config = configparser.ConfigParser()
config.read("Properties.ini")

url = config['caseSearch']['url']

params = {'q': 'caseName%3A'+config['caseSearch']['searchString'], 'sort': config['caseSearch']['sort'],
          'order': config['caseSearch']['order'], 'pageNumber': int(config['caseSearch']['pageNumber'])}

token_val = config['caseSearch']['tokenVal']

headers = {'accept': config['caseSearch']['accept'],
           'Authorization': config['caseSearch']['tokenType'] + ' ' + token_val}


@given(u'URL for API request is available to search case by name')
def step_impl(context):
    context.reqUrl = url
    context.param = params
    context.headers = headers


@when(u'User sends a get request')
def step_impl(context):
    context.getResp = requests.get(context.reqUrl, params=context.param, headers=context.headers)
    assert context.getResp.status_code == int(config['caseSearch']['successCode'])


@then(u'User receives the response with list of cases with {caseText} in case names')
def step_impl(context, caseText):
    context.respJson = context.getResp.json()
    context.caseLen = len(context.respJson['caseSearchResultArray'])
    context.caseList = context.respJson['caseSearchResultArray']
    for i in range(context.caseLen - 1):
        case_name = context.caseList[i]['caseName']
        assert caseText.lower() in case_name.lower()
    print("List of cases retrieved contain {} in the case name".format(caseText))
