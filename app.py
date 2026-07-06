import random
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# ১. আপনার সাইটের প্রধান পেজ বা হোমপেজের রুট
@app.route('/')
def home():
    # এটি সরাসরি ড্যাশবোর্ড (click.html) ওপেন করবে
    return render_template('click.html')


# ২. লাইভ ক্লিক ট্র্যাকার ড্যাশবোর্ডের আসল রুট
@app.route('/ad-budget')
def ad_budget():
    title = request.args.get('title', 'Live Click Tracker')
    link = request.args.get('link', '#')
    return render_template('click.html', title=title, link=link)


# ৩. যদি আপনার ড্যাশবোর্ডের চার্ট বা ম্যাপ জাভাস্ক্রিপ্ট থেকে কোনো লাইভ ডেটা (API) খোঁজে,
# তবে এই রুটটি ব্যাকএন্ড থেকে রিয়েল-টাইম ডেটা জেনারেট করে সাপ্লাই দেবে।
@app.route('/api/live-data')
def live_data():
    sample_data = {
        'total_clicks': random.randint(500, 1500),
        'countries_reached': random.randint(30, 80),
        'status': 'success',
    }
    return jsonify(sample_data)


# অ্যাপ রান করার মেইন কোড (সবার নিচে থাকবে)
if __name__ == '__main__':
    app.run(debug=True)
