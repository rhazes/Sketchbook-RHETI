from flask import Flask
import prompts
import random as rand

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/random')
def random_prompt():
    res = f"<br>Successfully loaded {len(prompts.data)} prompts"
    res += f"<br>Here is a random example:<br><br>"
    # res += f"{rand.choice(prompts.data)}"

    tuple1,tuple2 = rand.choice(prompts.data)
    p1,_ = tuple1
    p2,__ = tuple2
    
    res += f'"{p1}"<br>or<br>"{p2}"'
    
    return res


if __name__ == '__main__':
    RUN_APP = False
    if RUN_APP:
        app.run(host='0.0.0.0', port=5000)
    else:
        import prompts
        print(f"{len(prompts.data)} loaded")
