from flask import Flask, render_template,request
from GithubRepoRanking import *
app = Flask(__name__,template_folder='template')

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method =='POST':
        username = request.form['Username']
        repos = getrepo(username)
        repofiles , codes = findfiles(repos)
        scores = complexityFinder(codes)
        repoScores = findResult(repofiles , scores)
        sorted_dict = dict(sorted(repoScores.items(),key=lambda item: item[1] , reverse= True))
        outputRepo = next(iter(sorted_dict))
        outputRepoScore = sorted_dict[outputRepo]
        print(sorted_dict)
        return render_template('output.html',user = username ,resultRepo = outputRepo ,resultRepoScore = outputRepoScore)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)


