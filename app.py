from flask import Flask, render_template, url_for, redirect, request
import pandas as pd

app = Flask(__name__)

# Load CSV and drop unnecessary index column
lko_rest = pd.read_excel("food1.csv.xlsx").drop(columns=["Unnamed: 0"])

# Function to get similar restaurants
def fav(lko_rest1):
    lko_rest1 = lko_rest1.reset_index()
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    count1 = CountVectorizer(stop_words='english')
    count_matrix = count1.fit_transform(lko_rest1['highlights'])

    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

    sim = list(enumerate(cosine_sim2[0]))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:11]
    indi = [i[0] for i in sim]

    final = lko_rest1.copy().iloc[indi[0]]
    final = pd.DataFrame(final).T

    for i in range(1, len(indi)):
        final1 = lko_rest1.copy().iloc[indi[i]]
        final1 = pd.DataFrame(final1).T
        final = pd.concat([final, final1])

    return final


# Main recommendation function
def rest_rec(cost, people=2, min_cost=0, cuisine=[], Locality=[], fav_rest="", lko_rest=lko_rest):
    cost = cost + 200
    x = cost / people
    y = min_cost / people

    # Case-insensitive locality filter
    lko_rest1 = lko_rest[lko_rest['locality'].str.lower() == Locality[0].lower()]

    for i in range(1, len(Locality)):
        lko_rest2 = lko_rest[lko_rest['locality'].str.lower() == Locality[i].lower()]
        lko_rest1 = pd.concat([lko_rest1, lko_rest2])
        lko_rest1.drop_duplicates(subset='name', keep='last', inplace=True)

    lko_rest_locale = lko_rest1.copy()

    # Cost filters
    lko_rest_locale = lko_rest_locale[lko_rest_locale['average_cost_for_one'] <= x]
    lko_rest_locale = lko_rest_locale[lko_rest_locale['average_cost_for_one'] >= y]

    # Case-insensitive cuisine filter
    lko_rest_locale['Start'] = lko_rest_locale['cuisines'].str.lower().str.find(cuisine[0].lower())
    lko_rest_cui = lko_rest_locale[lko_rest_locale['Start'] >= 0]

    for i in range(1, len(cuisine)):
        lko_rest_locale['Start'] = lko_rest_locale['cuisines'].str.lower().str.find(cuisine[i].lower())
        lko_rest_cu = lko_rest_locale[lko_rest_locale['Start'] >= 0]
        lko_rest_cui = pd.concat([lko_rest_cui, lko_rest_cu])
        lko_rest_cui.drop_duplicates(subset='name', keep='last', inplace=True)

    if fav_rest != "":
        favr = lko_rest[lko_rest['name'].str.lower() == fav_rest.lower()].drop_duplicates()
        favr = pd.DataFrame(favr)
        lko_rest3 = pd.concat([favr, lko_rest_cui])
        lko_rest3.drop('Start', axis=1, inplace=True)
        rest_selected = fav(lko_rest3)
    else:
        if lko_rest_cui.empty:
            return pd.DataFrame([{
                "name": "Sorry, no results found",
                "address": "",
                "locality": "",
                "timings": "",
                "aggregate_rating": "",
                "url": "",
                "cuisines": ""
            }])
        lko_rest_cui = lko_rest_cui.sort_values('scope', ascending=False)
        rest_selected = lko_rest_cui.head(10)

    return rest_selected


def calc(max_Price, people, min_Price, cuisine, locality):
    rest_sugg = rest_rec(max_Price, people, min_Price, [cuisine], [locality])
    rest_list1 = rest_sugg.copy().loc[:, ['name', 'address', 'locality', 'timings', 'aggregate_rating', 'url', 'cuisines']]
    rest_list = rest_list1.reset_index(drop=True).T
    ans = rest_list.to_dict()
    res = [value for value in ans.values()]
    return res


@app.route("/")
@app.route("/home")
def home():
    # send all unique localities to dropdown
    localities = sorted(lko_rest['locality'].dropna().unique().tolist())
    return render_template('home.html', localities=localities)


@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        people = int(request.form['people'])
        min_Price = int(request.form['min_Price'])
        max_Price = int(request.form['max_Price'])
        cuisine1 = request.form['cuisine']
        locality1 = request.form['locality']
        res = calc(max_Price, people, min_Price, cuisine1, locality1)
        return render_template('search.html', title='Search', restaurants=res)
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
