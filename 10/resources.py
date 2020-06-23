from flask_restful import Resource
from models import *
from flask import request
from schemas import *
import json
from marshmallow import ValidationError


class AuthorResource(Resource):

    def get(self, author_id):
        author = Author.objects.get(id=author_id)
        posts = Post.read(author=author)
        return json.loads(PostSchema(many=True).dumps(posts))

    def post(self, author_id=None):
        data = json.dumps(request.json)
        try:
            data = AuthorSchema().loads(data)
            author = Author.create(**data)
            res = json.loads(AuthorSchema().dumps(author))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, author_id):
        author = Author.objects.get(id=author_id).update(**request.json)
        return author.to_json()

    def delete(self, author_id):
        Author.delete(author_id)


class PostResource(Resource):

    def get(self, post_id=None):
        res = Post.read(post_id)
        return json.loads(PostSchema().dumps(res))

    def post(self, author_id, tag_id=None):
        author = Author.objects.get(id=author_id)
        if tag_id:
            tag = Tag.read(tag_id)
        else:
            tag = None
        data = json.dumps(request.json)
        try:
            data = PostSchema().loads(data)
            post = Post.create(author, tag, **data)
            res = json.loads(PostSchema().dumps(post))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, post_id):
        post = Post.read(post_id=post_id).update(**request.json)
        return post.to_json()

    def delete(self, post_id):
        post = Post.objects.get(id=post_id)
        author = post.author
        Post.delete(post_id)
        author.posts = len(Post.read(author=author))
        author.save()


class TagResource(Resource):

    def get(self, tag_id):
        tag = Tag.objects.get(id=tag_id)
        posts = Post.read(tag=tag)
        return json.loads(PostSchema(many=True).dumps(posts))

    def post(self):
        data = json.dumps(request.json)
        try:
            data = TagSchema().loads(data)
            tag = Tag.create(**data)
            res = json.loads(TagSchema().dumps(tag))
        except ValidationError as err:
            res = err.messages
        return res

    def put(self, tag_id):
        tag = Tag.read(tag_id=tag_id)
        Tag.update(tag, **request.json)
        return tag.to_json()

    def delete(self, tag_id):
        Tag.delete(tag_id)
