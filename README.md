# Survey
This app lets you create questions for a survey and define the order of the questions. Its just an API.

DESCRIPTION OF MODELS:

Questions Model:

question: saves the question (accepts string as input)

category: relates to 0 or more categories from Category Model (accepts list of strings as input)

question_type: it defines the type of question (accepts 'sub'-subjective question or 'mcq'-multiple choice question)

solution: user's answer for the question

number: this integer field will define the sequence of the questions

Category Model:

name: defines the name of the category

URL DESCRIPTION:

For accessing all the questions and adding a new question:

'localhost:8000/questionbank/question/' - this will show all the questions and order them by them 'number' field. A new question can be added from here.

For accessing individual question and editing/deleting them:

'localhost:8000/questionbank/question/id' - this will show the question with the id in the URL. An existing question can be deleted/edited from here.

The sequence of the questions can only be defined from Django-Admin panel. 2 or more questions cannot have the same sequence number, this error will be only shown when a question is either added/edited from Django Admin panel. When a question is created through the API, the default value of number will be 0.
