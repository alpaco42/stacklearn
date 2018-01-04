from django.shortcuts import render, reverse
from django.views import generic
from question_creation import models as question_creation_models

class ShortAnswerQuestionCreateView(generic.CreateView):
    """ Class-based view to create short answer questions.
    """
    model = question_creation_models.ShortAnswerQuestion
    fields = ["question", "right_answer"]
    template_name = "question_creation/short_ans_question_create.html"
    #context_object_name

    def get_context_data(self, **kwargs):
        #I didn't mess with this, probably isn't functional rn
    	context_data = super(ShortAnswerQuestionCreateView, self).get_context_data()
    	return context_data
