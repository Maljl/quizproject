from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   		"name": "SPACE",
	   	"description": "Hur bra kan du din rymd?"
	},
	{
		"quiz_number": 2,
   	   	"name": "ROCKS",
	   	"description": "Vad kan du egentligen om stenar?"
	},
	{
		"quiz_number": 3,
   	    "name": "STARS",
	    "description": "Stjärnor är vackra, men vad kan du om dem?"	},
]

def start(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) -1],
		"quiz_number": quiz_number,
		"quizzes": quizzes,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"quiz": quizzes[int(quiz_number) -1],
		"quiz_number": quiz_number,
		"question_number": question_number,
		"question": "Hur många bultar har ölandsbron?",
		"answer1": "12",
		"answer2": "66 400",
		"answer3": "7 428 000",
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context = {
		"correct": 12,
		"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)
