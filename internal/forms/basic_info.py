def get_value(text):
    return '' if text==None else text
def get_questions(unique):
    example_username = "{0}{1}".format(unique['firstname'].lower(),unique['lastname'][0].lower())
    return [
        {
            "question" : "What year are you in?",
            "clarification" : "Please do not base this off of number of credits held",
            "align" : "left",
            "name" : "Year",
            "type" : "radio",
            "year": get_value(unique['year']),
            "inputs" : [
                {
                    "value" : "freshman",
                    "description" : "Freshman",
                },{
                    "value" : "sophomore",
                    "description" : "Sophomore"
                },{
                    "value" : "junior",
                    "description" : "Junior"
                },{
                    "value" : "senior",
                    "description" : "Senior"
                },{
                    "value" : "masters",
                    "description" : "Masters student"
                },{
                    "value" : "phd",
                    "description" : "Ph.D. student"
                }
            ]
        },{
            "question" : "What email is best for you?",
            "clarification" : "",
            "align" : "right",
            "name" : "Email",
            "type" : "email",
            "inputs" : [
                {
                    "placeholder" : "{0}@illinois.edu".format(unique['netid'].lower()),
                    "value" : get_value(unique['bestemail']),
                    "maxlength" : 200
                }
            ]
        },{
            "question" : "What's your GitHub account?",
            "clarification" : "GitHub is the industry standard for software collaboration and required for this course. Create a free account at <a href='https://github.com' target=_blank>github.com</a> if you don't have one",
            "align" : "right",
            "name" : "Github",
            "type" : "text",
            "inputs" : [
                {
                    "placeholder" : 'GitHub username (e.g. {0})'.format(example_username),
                    "value" : get_value(unique['github']),
                    "maxlength" : 50
                }
            ]
        },{
            "question" : "What's your Project Euler account?",
            "clarification" : "We need to assess your basic programming abilities. Project Euler allows us to do this. Create a free account at <a href='https://projecteuler.net/register' target=_blank>projecteuler.net</a> if you don't have one.",
            "align" : "left",
            "name" : "Euler",
            "type" : "text",
            "inputs" : [
                {
                    "placeholder" : "Project Euler username (e.g. {0})".format(example_username),
                    "value" : get_value(unique['euler']),
                    "maxlength" : 50
                }
            ]
        },{
            "question" : "What's your cell phone number?",
            "clarification" : "Please include a country code if non-US",
            "align" : "right",
            "name" : "Phone",
            "type" : "tel",
            "inputs" : [
                {
                    "placeholder" : "(217) 265-6847",
                    "value" : get_value(unique['phone']),
                    "maxlength" : 50
                }
            ]
        },{
            "question" : "What experience do you have?",
            "clarification" : "Are you a master marketer, SQL savant, pythonista, mathemagician, or business barbarian? Tell us about it.",
            "align" : "right",
            "name" : "Skills",
            "type" : "textarea",
            "inputs" : [
                {
                    "rows" : 7,
                    "value": get_value(unique['skills'])
                }
            ]
        },{
            "question" : "What are you goals?",
            "clarification" : "What would you like to get out of CS 196? Tell us about it.",
            "name" : "Wants",
            "align" : "left",
            "type" : "textarea",
            "inputs" : [
                {
                    "rows" : 7,
                    "value": get_value(unique['wants'])
                }
            ]
        }
    ]
