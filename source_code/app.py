from flask import Flask , request
from flask_restful import Resource, Api, reqparse




app = Flask(__name__)
api = Api(app)

books = [
    {
        "name":"think like a monk",
        "price":346,
        "type":"paperback"
    }
    
]

class Book(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',type=int, required=True,help="please include price in int type")
    parser.add_argument('type', type=str, required=True, help="please provide type in string ")


    def get(self, name):
        for book in books:
            if book['name'] == name:
                return book, 200 
        return {"message":"book not found"}, 404

    def post(self, name):
       
        for book in books:
            if book['name'] == name:
                return {"message":"{} book already exists.".format(name)}, 400 
        data = Book.parser.parse_args() 
        data["name"] = name
        books.append(data)
        return {"message":"book has been created"}, 201

    def delete(self,name):
        for book in books:
            if book['name'] == name:
                books.remove(book)
                return {"message":"Book has been deleted"}, 200
        return {"message": "book not found"}, 404 

    def put(self,name):
    
        data = Book.parser.parse_args() 
        for book in books:
            if book['name'] == name:
                book.update(data)
                return {"message":"book has been updated"}, 200
        data["name"] = name
        books.append(data)
        return {"message":"book has been created"}, 201

        



class Books(Resource):
    def get(self):
        return {'books':books}
       

api.add_resource(Book, '/book/<string:name>')   #http://127.0.0.1:5000/book/think like a monk     body = {"price":123, "type":"paperback"}
api.add_resource(Books, '/books')   #http://127.0.0.1:5000/books  
app.run(port=5000)



