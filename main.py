from flask import Flask, render_template, request
import prompts
import random as rand

app = Flask(__name__)

@app.route('/')
def index():
    # resave
    # context = 
    # return 'Hello from Flask!'
    return render_template('navForm.html',**({'currentPromptNumber':0,'maxPromptNumber':7}) )

@app.route('/random')
def random_prompt():
    res = []
    res.append(f"<br>Successfully loaded {len(prompts.data)} prompts")
    res.append(f"<br>Here is a random example:<br><br>")
    # res += f"{rand.choice(prompts.data)}"

    #
    # TODO: HW Challenge: Change the code to print out
    # a header with the prompt number and then the 2 prompts
    #
    tuple1,tuple2 = rand.choice(prompts.data)
    p1,_ = tuple1
    p2,__ = tuple2
    
    res.append(f'"{p1}"<br>or<br>"{p2}"')
    
    return "".join(res)

@app.route('/prompt/<int:xx>')
def prompt(xx):
    print(f"this is the promptNumber: {xx}")
    ind = xx + 1

    # TODO: write a function that parses a prompt tuple
    # Into tuple of just the prompt strings
    promptTuple1, promptTuple2 = prompts.data[ind]
    # res = [f"<h2>{xx}</h2>",
    #        f"<p>{promptTuple1[0]}</p>",
    #        f"<p>{promptTuple2[0]}</p>"]
    # return "".join( res )

    return render_template('prompt.html',\
                    **({'currentPromptNumber':xx,\
                        'maxPromptNumber':7,\
                        'prompt1':promptTuple1[0],\
                        'prompt2':promptTuple2[0]}))
    # return "<h2> next prompt </h2>" + promptNumber

@app.route('/prevPrompt')
def prev_prompt():
    return "<h2>Previous Prompt</h2>"

if __name__ == '__main__':
    RUN_APP = False
    if RUN_APP:
        app.run(host='0.0.0.0', port=5000)
    else:
        import prompts
        print(f"{len(prompts.data)} loaded")
