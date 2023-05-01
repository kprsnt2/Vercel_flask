from flask import Flask, render_template, request
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    keyword1 = request.form['keyword1']
    keyword2 = request.form['keyword2']
    timeframe = request.form['timeframe']
    
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[keyword1, keyword2], timeframe=timeframe)
    interest_over_time_df = pytrends.interest_over_time()
    chart = interest_over_time_df.drop(columns=['isPartial']).plot().to_html()
    
    return render_template('results.html', chart=chart)

if __name__ == '__main__':
    app.run(debug=True)

