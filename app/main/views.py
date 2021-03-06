from flask import render_template
from . import main
from ..request import get_sources,get_article
from ..models import Sources,Articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources('mysources')
   
    title= "Get the latest news"
    return render_template('index.html', title = title, sources = news_sources)

@main.route('/article/<article_id>')
def article(article_id):

    '''
    View article page function that returns the article details page and its data
    '''
    article = get_article(article_id)
    title = f'{article_id}'

    return render_template('article.html',title = title, myarticle = article, name=article_id)


