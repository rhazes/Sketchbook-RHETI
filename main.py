from flask import Flask
import prompts
import random as rand

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

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


if __name__ == '__main__':
    RUN_APP = False
    if RUN_APP:
        app.run(host='0.0.0.0', port=5000)
    else:
        import prompts
        print(f"{len(prompts.data)} loaded")
