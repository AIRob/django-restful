#! -*- coding: utf-8 -*-

from collections import OrderedDict
from django_restful.serializers import RESTfulJSONEncoder
from django_restful import strings


def render_as_json(document, indent=4):
    if type(indent) == int:
        indent = ' ' * indent
    encoder = RESTfulJSONEncoder(indent=indent)
    return encoder.encode(document)


def error_document(error_list=[]):
    document = OrderedDict()
    document['errors'] = error_list
    return document


def json_error_document(error_list=[], indent=4):
    document = error_document(error_list)
    return render_as_json(document, indent)


def errors_from_dictionary(errors, position=0):
    error_list = []
    for field in errors:
        dct = {'field': field + '_' + str(position),
               'msg': unicode(strings.ERROR_INVALID_FIELDS)}
        error_list.append(dct)
    return error_list

def error_list_from_form(form, prefix_with_fields=True):                        
    results = []                                                                
    errors = OrderedDict(form.errors)                                           
    for field, messages in errors.iteritems():                                  
        for message in messages:                                                
            entry = OrderedDict()                                               
            if prefix_with_fields and field != '__all__':                       
                message = '%s: %s' % (field, message)                           
            entry['message'] = unicode(message)                                 
            results.append(entry)                                               
    return results 
