# -*- coding: utf-8 -*-

from django.http import HttpResponse


class HttpResponseCreated(HttpResponse):
    status_code = 201

class HttpResponseNoContent(HttpResponse):
    status_code = 204

    def __init__(self, content='', mimetype=None, status=None,
            content_type=None):
        return super(HttpResponseNoContent, self).__init__(
            content='',
            mimetype=mimetype,
            status=None,
            content_type=content_type
        )

class HttpResponseSeeOther(HttpResponse):
    status_code = 303

class HttpResponseUnauthorized(HttpResponse):
    status_code = 401

class HttpResponseNotAcceptable(HttpResponse):
    status_code = 406

class HttpResponseConflict(HttpResponse):                                       
    status_code = 409 

class HttpResponseFieldValidationError(HttpResponse):
    status_code = 422

class HttpResponseInternalServerError(HttpResponse):
    status_code = 500

class MultiMessagesException(Exception):
    def __init__(self, messages=[], *args, **kargs):
        super(MultiMessagesException, self).__init__(*args, **kargs)
        self.messages = messages

class Http400MM(MultiMessagesException):
    pass

class Http401MM(MultiMessagesException):
    pass

class Http402MM(MultiMessagesException):
    pass

class Http403MM(MultiMessagesException):
    pass

class Http404MM(MultiMessagesException):
    pass

class Http405MM(MultiMessagesException):
    pass

class Http406MM(MultiMessagesException):
    pass

class Http407MM(MultiMessagesException):
    pass

class Http408MM(MultiMessagesException):
    pass

class Http409MM(MultiMessagesException):
    pass

class Http410MM(MultiMessagesException):
    pass
