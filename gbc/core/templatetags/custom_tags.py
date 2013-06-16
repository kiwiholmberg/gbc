# encoding: utf-8

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()

@register.filter
@stringfilter
def newsletter_form_sv(value):
    newsletter_form = u'<div class="input-append newsletter-form">\
                <input type="text" id="newsletter-email" placeholder="Email" class="span2" name="email" />\
                <button id="newsletter-signup-btn" type="button" class="btn">Registrera</button>\
              </div>\
              <label class="newsletter-error">Något gick fel. Kontrollera din emailadress och försök igen.</label>\
              <label class="newsletter-signedup">Tack! Du kommer att få ett mail där du måste bekräfta din registrering.</label>\
              <label class="newsletter-already">Din mailadress är redan registrerad.</label>'
    return newsletter(newsletter_form, value)

@register.filter
@stringfilter
def newsletter_form_en(value):
    newsletter_form = u'<div class="input-append newsletter-form">\
                <input type="text" id="newsletter-email" placeholder="Email" class="span2" name="email" />\
                <button id="newsletter-signup-btn" type="button" class="btn">Register</button>\
              </div>\
              <label class="newsletter-error">Something went wrong. Please check your email and try again.</label>\
              <label class="newsletter-signedup">Thank you! You\'ll get an email where you have to confirm your subscription.</label>\
              <label class="newsletter-already">You\'re already signed upp for the newsletter.</label>'
    return newsletter(newsletter_form, value)

def newsletter(val, original):
    trigger_val = 'MAILFORM'
    if trigger_val in original:
        return mark_safe(original.replace(trigger_val, val))
    else:
        return original