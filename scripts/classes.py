###############################################################

class Category:
    def __init__(self, name= str, id= int ):
        self.name = name
        self.id = id
        
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    @id.setter
    def id(self, new_id):
        self._id = new_id

class Review:
    def __init__(self, asin= str, data= str, customer= str,
                 rating= int, votes= int, helpful= int):
        self.asin = asin
        self.data = data
        self.customer = customer
        self.rating = rating
        self.votes = votes
        self.helpful = helpful
        
    @property
    def asin(self):
        return self._asin
    
    @property
    def data(self):
        return self._data
    
    @property
    def customer(self):
        return self._customer
 
    @property
    def rating(self):
        return self._rating

    @property
    def votes(self):
        return self._votes
    
    @property
    def helpful(self):
        return self._helpful  
    
    @asin.setter
    def asin(self, new_asin):
        self._asin = new_asin
        
    @data.setter
    def data(self, new_data):
        self._data = new_data

    @customer.setter
    def customer(self, new_customer):
        self._customer = new_customer

    @rating.setter
    def rating(self, new_rating):
        self._rating = new_rating
        
    @votes.setter
    def votes(self, new_votes):
        self._votes = new_votes
        
    @helpful.setter
    def helpful(self, new_helpful):
        self._helpful = new_helpful

class Reviews_product:
    def __init__(self, asin= str, total= int, downloaded= int,
                 avg_rating= float, reviews_vet= Review):
        self.asin = asin
        self.total = total
        self.downloaded = downloaded
        self.avg_rating = avg_rating
        self.reviews_vet = reviews_vet
        
    @property
    def asin(self):
        return self._asin
    
    @property
    def total(self):
        return self._total
    
    @property
    def downloaded(self):
        return self._downloaded
 
    @property
    def avg_rating(self):
        return self._avg_rating

    @property
    def reviews_vet(self):
        return self._reviews_vet
    
    @asin.setter
    def asin(self, new_asin):
        self._asin = new_asin
        
    @total.setter
    def total(self, new_total):
        self._total = new_total
        
    @downloaded.setter
    def downloaded(self, new_downloaded):
        self._downloaded = new_downloaded

    @avg_rating.setter
    def avg_rating(self, new_avg_rating):
        self._avg_rating = new_avg_rating

    @reviews_vet.setter
    def reviews_vet(self, new_reviews_vet):
        self._reviews_vet = new_reviews_vet
    
class Produto:
    def __init__(self, id= int, asin= str,
                 title= str, group= str,
                 salesrank= int, similar= str,
                 categories= Category, reviews = Reviews_product):
        self.id = id
        self.asin = asin
        self.title = title
        self.group = group
        self.salesrank = salesrank
        self.similar = similar
        self.categories = categories
        self.reviews = reviews

    # getter e setter para id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # getter e setter para asin
    @property
    def asin(self):
        return self._asin

    @asin.setter
    def asin(self, value):
        self._asin = value

    # getter e setter para title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    # getter e setter para group
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value

    # getter e setter para salesrank
    @property
    def salesrank(self):
        return self._salesrank

    @salesrank.setter
    def salesrank(self, value):
        self._salesrank = value

    # getter e setter para similar
    @property
    def similar(self):
        return self._similar

    @similar.setter
    def similar(self, value):
        self._similar = value

    # getter e setter para categories
    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = value

    # getter e setter para reviews
    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value