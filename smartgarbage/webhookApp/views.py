from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from webhookApp import helpers

@csrf_exempt
def webhook(request):
    '''Build a request object'''
    request_json = json.loads(request.body)

    # return fulfillment
    fulfillment_text = process_request(request_json)

    # return response
    return JsonResponse(fulfillment_text, safe=False)

def process_request(request):
    '''Primary director of messages received by webhook'''
    query_result = request.get('queryResult')
    # original_detect_intent_request = request.get('originalDetectIntentRequest')
    # data = original_detect_intent_request.get('payload').get('data')
    action = query_result.get('action')
    # intent_name = query_result.get('intent').get('displayName')
    # text_response = query_result.get('fulfillmentText')

    if action == 'action_trash_types':
        return get_parameter_trash_types(query_result)
    if action == 'action_waste_types':
        return get_parameter_waste_types(query_result)

def get_parameter_trash_types(query_result):
    param_trash_types = query_result.get('parameters').get('trash_types')
    helper = helpers.Helpers()
    trash_type = helper.trash_types()

    for type in trash_type:
        if helper.verify_param(type['synonyms'], param_trash_types):
            trash_type_ref = type['value']
            break
        else:
            trash_type_ref = None

    trash_type_ref_format = trash_type_ref.replace("lixeira de ", "") if trash_type_ref is not None else None

    # chamar metodo para acionar lixeira
    #

    return build_message_disposal(trash_type_ref_format)

def get_parameter_waste_types(query_result):
    param_waste_types = query_result.get('parameters').get('waste_types')
    helper = helpers.Helpers()
    waste_type = helper.waste_types()

    for type in waste_type:
        if helper.verify_param(type['synonyms'], param_waste_types):
            waste_type_ref = type['value']
            break
        else:
            waste_type_ref = None

    waste_type_ref_format = waste_type_ref.replace("tipo ", "") if waste_type_ref is not None else None

    # chamar metodo para acionar lixeira
    #

    return build_message_disposal(waste_type_ref_format)

def build_message_disposal(type):
    if type is not None:
        text = "Muito bem. Seu resíduo será descartado na lixeira de {}".format(type.capitalize())
    else:
        text = "Desculpe, não compreendi!"

    return {'fulfillmentText': text}