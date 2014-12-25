from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotFound
from django.utils import translation
from django.utils.decorators import method_decorator

from django_restful.http import HttpResponseConflict
from django_restful.http import Http400, Http400MM
from django_restful.http import Http404, Http404MM
from django_restful.http import Http409, Http409MM
from django_restful.utils import render_as_json
from django_restful.utils import json_error_document 

from django_restful import settings as rest_settings

class JSONErrorHelpersMixin(View):

    def generate_document(self, messages):
        messages = [unicode(e) for e in messages]
        return json_error_document(messages)

    def bad_request(self, messages=[]):
        document = self.generate_document(messages)
        return HttpResponseBadRequest(
            content=document,
            content_type='application/json'
        )

    def not_found(self, messages=[]):
        document = self.generate_document(messages)
        return HttpResponseNotFound(
            content=document,
            content_type='application/json'
        )

    def conflict(self, messages=[]):
        document = self.generate_document(messages)
        return HttpResponseConflict(
            content=document,
            content_type='application/json'
        )

    def ok(self, doc={}):
        return HttpResponse(
            content=render_as_json(doc),
            content_type='application/json'
        )

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        # Force a language if the settings require it
        if rest_settings.REST_FORCE_LANGUAGE:
            translation.activate(rest_settings.REST_DEFAULT_LANGUAGE)
        # Handling additional HTTP verbs
        for m in self.extend_known_methods():
            if m not in self.additional_http_method_names:
                self.additional_http_method_names.append(m)
        for m in self.additional_http_method_names:
            if m not in self.http_method_names:
                self.http_method_names.append(m)
        # Handling authentication
        response = self.authenticate(request, *args, **kwargs)
        if not response.is_authenticated:
            return self.process_authentication_error(response)
        # Handling authorization
        response = self.authorize(request, *args, **kwargs)
        if not response.is_authorized:
            return self.process_authorization_error(response)
        try:
            # Original dispatch logic continues
            return super(JSONErrorHelpersMixin, self).dispatch(
                request,
                *args,
                **kwargs
            )
        except Http400, e:
            return self.bad_request([e.message])
        except Http400MM, e:
            return self.bad_request(e.messages)
        except Http404, e:
            return self.not_found([e.message])
        except Http404MM, e:
            return self.not_found(e.messages)
        except Http409, e:
            return self.conflict([e.message])
        except Http409MM, e:
            return self.conflict(e.messages)
